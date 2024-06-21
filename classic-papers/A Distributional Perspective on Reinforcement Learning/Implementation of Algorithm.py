# Key Components:
# Replay Buffer: A buffer to store and sample experience tuples.
# Categorical DQN Network: A neural network that outputs a distribution over returns for each action.
# Projection Step: Projects the target distribution back onto the fixed support.
# Training Function: Computes the loss and performs backpropagation.
# Main Loop: Handles interaction with the environment, stores experiences, and trains the network.

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque
import gym

# Hyperparameters
V_MIN = -10
V_MAX = 10
N_ATOMS = 51
DELTA_Z = (V_MAX - V_MIN) / (N_ATOMS - 1)
GAMMA = 0.99
LR = 1e-4
BATCH_SIZE = 32
BUFFER_SIZE = 10000
TARGET_UPDATE = 1000
EPSILON_DECAY = 0.99
MIN_EPSILON = 0.01

# Initialize environment
env = gym.make('CartPole-v1')

# Replay Buffer
class ReplayBuffer:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)
    
    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)
    
    def __len__(self):
        return len(self.buffer)

# Q-network
class CategoricalDQN(nn.Module):
    def __init__(self, input_dim, output_dim, n_atoms, v_min, v_max):
        super(CategoricalDQN, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.n_atoms = n_atoms
        self.v_min = v_min
        self.v_max = v_max
        self.delta_z = (v_max - v_min) / (n_atoms - 1)
        
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, output_dim * n_atoms)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        x = x.view(-1, self.output_dim, self.n_atoms)
        x = torch.softmax(x, dim=2)
        return x

    def get_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.randint(0, self.output_dim - 1)
        else:
            state = torch.FloatTensor(state).unsqueeze(0)
            with torch.no_grad():
                dist = self.forward(state).data.cpu().numpy()
            z = np.linspace(self.v_min, self.v_max, self.n_atoms)
            q_values = np.sum(dist * z, axis=2)
            return np.argmax(q_values)

# Projection step
def projection(next_dist, rewards, dones, n_atoms, v_min, v_max, delta_z, gamma):
    batch_size = rewards.shape[0]
    proj_dist = np.zeros((batch_size, n_atoms))
    z = np.linspace(v_min, v_max, n_atoms)
    
    for i in range(batch_size):
        if dones[i]:
            Tz = np.clip(rewards[i], v_min, v_max)
            bj = (Tz - v_min) / delta_z
            l, u = np.floor(bj).astype(int), np.ceil(bj).astype(int)
            proj_dist[i, l] += (u - bj)
            proj_dist[i, u] += (bj - l)
        else:
            for j in range(n_atoms):
                Tz = np.clip(rewards[i] + gamma * z[j], v_min, v_max)
                bj = (Tz - v_min) / delta_z
                l, u = np.floor(bj).astype(int), np.ceil(bj).astype(int)
                proj_dist[i, l] += next_dist[i, j] * (u - bj)
                proj_dist[i, u] += next_dist[i, j] * (bj - l)
    
    return proj_dist

# Training function
def train(q_net, target_net, memory, optimizer, batch_size, n_atoms, v_min, v_max, delta_z, gamma):
    if len(memory) < batch_size:
        return
    
    batch = memory.sample(batch_size)
    states, actions, rewards, next_states, dones = zip(*batch)
    
    states = torch.FloatTensor(states)
    actions = torch.LongTensor(actions)
    rewards = np.array(rewards)
    next_states = torch.FloatTensor(next_states)
    dones = np.array(dones)
    
    # Compute projected distribution
    with torch.no_grad():
        next_dist = target_net(next_states).cpu().numpy()
        next_actions = target_net.get_action(next_states, epsilon=0.0)
        next_dist = next_dist[np.arange(batch_size), next_actions, :]
        proj_dist = projection(next_dist, rewards, dones, n_atoms, v_min, v_max, delta_z, gamma)
    
    # Get current distribution
    dist = q_net(states)
    actions = actions.unsqueeze(1).unsqueeze(1).expand(batch_size, 1, n_atoms)
    dist = dist.gather(1, actions).squeeze(1)
    
    proj_dist = torch.FloatTensor(proj_dist)
    loss = -torch.sum(proj_dist * torch.log(dist + 1e-8), dim=1).mean()
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Main loop
def main():
    input_dim = env.observation_space.shape[0]
    output_dim = env.action_space.n

    q_net = CategoricalDQN(input_dim, output_dim, N_ATOMS, V_MIN, V_MAX)
    target_net = CategoricalDQN(input_dim, output_dim, N_ATOMS, V_MIN, V_MAX)
    target_net.load_state_dict(q_net.state_dict())
    target_net.eval()

    optimizer = optim.Adam(q_net.parameters(), lr=LR)
    memory = ReplayBuffer(BUFFER_SIZE)
    
    epsilon = 1.0
    total_steps = 0

    for episode in range(500):
        state = env.reset()
        episode_reward = 0
        
        while True:
            action = q_net.get_action(state, epsilon)
            next_state, reward, done, _ = env.step(action)
            episode_reward += reward

            memory.push(state, action, reward, next_state, done)
            state = next_state

            train(q_net, target_net, memory, optimizer, BATCH_SIZE, N_ATOMS, V_MIN, V_MAX, DELTA_Z, GAMMA)

            if total_steps % TARGET_UPDATE == 0:
                target_net.load_state_dict(q_net.state_dict())
            
            total_steps += 1
            epsilon = max(epsilon * EPSILON_DECAY, MIN_EPSILON)

            if done:
                break

        print(f"Episode: {episode}, Reward: {episode_reward}")

if __name__ == "__main__":
    main()
