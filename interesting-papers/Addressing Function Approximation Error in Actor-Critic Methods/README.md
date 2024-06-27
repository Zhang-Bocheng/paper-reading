# Addressing Function Approximation Error in Actor-Critic Methods
[paper link](https://arxiv.org/pdf/1802.09477) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 |  This paper explores the problem of function approximation errors in reinforcement learning(RL) and proposes new mechanisms for Actor-Critic methods to minimize their effects.        |  Reinforcement Learning         |

## Methodology

### 1. Abstract
  The algorithm proposed in this paper is based on Double Q-learning and limits the overestimation by taking the minimum between two critics. The authors also mention the link between the target network and the overestimation bias and suggest delaying the policy update to reduce the error at each update and further improve the performance. Experimental results show that the method outperforms existing techniques on the OpenAI Gym task performing best in all test environments.
  
### 2. Method Description 
  The paper presents a RL algorithm called TD3 (Twin Delayed Deep Deterministic policy gradient Clipped Double Q-learning) for continuous control problems. It is based on the Actor-Critic framework and stabilizes the learning process by using a target network, while using Clipped Double Q-learning to reduce overestimation bias.
  
### 3. Key concepts
  _Clipped Double Q-learning_: An enhancement to the Double Q-learning algorithm, designed to address the overestimation bias in Q-value estimation in reinforcement learning. This method improves upon traditional Q-learning by using two separate Q-networks and a clipping mechanism to produce more accurate Q-value estimates.
  
### 4. Methodological improvements
  1. Used a target network: TD3 introduces a stable target for policy updating, i.e., a target network, to avoid instability that occurs during policy updating.

  2. Uses Clipped Double Q-learning: To address the problem of over-estimation bias, TD3 employs the Clipped Double Q-learning algorithm, which limits the difference between two value functions to a certain range, thus reducing the effect of over-estimation.
     
### 5. Issues addressed 
  1. Stable learning process: Due to the use of a target network, TD3 is able to perform policy updates more stably, avoiding instability and oscillations.

  2. Reducing overestimation bias: by using the Clipped Double Q-learning algorithm, TD3 can effectively reduce overestimation bias and improve the learning effect.

  In conclusion, the TD3 algorithm is an effective RL algorithm for continuous control problems, which is able to stably carry out policy update and effectively reduce overestimation bias by using technical means such as target network and Clipped Double Q-learning, thus improving the learning efficiency.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/c057efb2-e78b-451f-893f-4412aed63c87)

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/96b65b05-48bd-4587-a0ae-2b9720d82993)

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/ee16b605-0231-4280-b791-06d13725b4cb)

## Experiments
  This paper focuses on the performance of the Deep RL based TD3 on the MuJoCo continuous control task, with comparisons with existing algorithms and Ablation studies of different components.

First, in the experimental part, the authors used the MuJoCo continuous control task under the OpenAI Gym interface as an evaluation criterion and employed the DDPG algorithm as a benchmark method. The authors used a two-layer fully-connected neural network as the value function and action output, and trained it using the Adam optimizer. The authors used a pure exploration strategy, followed by exploration using a strategy that adds Gaussian noise. Each task was run for one million time steps and performance was evaluated every five thousand times.

Second, in the comparison experiments, the authors compared the TD3 algorithm with existing algorithms such as DDPG, PPO, ACKTR, TRPO, SAC, etc. and came up with the result that the TD3 algorithm outperforms the other algorithms in all tasks. In addition, the authors conducted an Ablation study to analyze the impact of components such as shear double Q learning, delayed policy updating, and target policy smoothing on the performance of the algorithms. The results show that the contribution of these components varies from task to task, but the combination can significantly improve the algorithm performance.

In summary, this paper experimentally demonstrates the excellent performance of the TD3 algorithm on the MuJoCo continuous control task and analyzes the role of its components in depth. This is of great significance for further improving the deep reinforcement learning algorithm.

## Conclusion
### 1. Advantages of the Thesis
  1. The paper provides an in-depth study of the overfitting problem in the actor-critic algorithm in continuous control and proposes a solution.

  2. The authors experimentally validate the effectiveness of the proposed solution and outperform the best existing algorithms on several tasks.

  3. The methodological innovations of the paper include a double-Q learning variant designed for continuous action spaces, the application of target networks, and delayed policy updates.

  4. The paper also explores the relationship between noise and overfitting and proposes a SARSA-style regularization technique to further reduce variance.

### 2. Innovative points
  1. The authors propose a new dual-Q learning variant that employs two independently trained commentators to avoid maximizing bias and uses a clipping operation to limit possible overestimation.

  2. The target network is shown to be one of the key factors in reducing error accumulation.

  3. Delayed strategy updating is a novel technique that ensures that the value function converges before updating the strategy, thus reducing the volatility associated with strategy updating.

  4. The SARSA style regularization technique allows updating the action estimates in a similar state, which further reduces the variance.

### 3. Future Works
  1.The authors believe that future research should continue to explore how to better deal with the overfitting problem under continuous action space.

  2. More research and improvements are needed for other issues in the field of deep RL, such as sample efficiency, exploration and generalization capabilities.
