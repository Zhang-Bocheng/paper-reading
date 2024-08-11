# Reinforcement Learning with Deep Energy-Based Policies
[paper link](https://arxiv.org/pdf/1702.08165) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2017 |This paper presents a new reinforcement learning method that can be used for continuous state and action space learning and is able to learn energy-based policies with high expressive power.          | Reinforcement Learning          |

## Methodology

### 1. Abstract
The method is applied to the learning of maximum entropy policies, yielding a new algorithm called soft Q-learning, which represents the optimal policy through a Boltzmann distribution. To achieve this, the authors used approximate Stein variational gradient descent to train a random sampling network to approximate samples from this distribution. Experimental results show that this approach improves exploration efficiency and allows for skill transfer between tasks. Furthermore, the authors explore the connection between this method and the actor-critic approach, arguing that the latter can be viewed as a process of performing approximate inference on the corresponding energy model.

### 2. Method Description 
This paper proposes Soft Q-Learning, a maximum entropy based policy learning algorithm in continuous action space. The algorithm achieves policy learning by alternately collecting new experiences and updating the soft Q-function and sampling network parameters. New experiences are stored in a replay memory buffer D and the parameters are updated from this buffer using randomized small batches of data. The optimizer uses the ADAM optimizer and the empirically estimated gradient V̂. 

![image](https://github.com/user-attachments/assets/97b3eb83-60fb-4b8d-920e-6faf1e7533c1)

### 3. Methodological improvements
  1. Compared to traditional deep Q learning, the soft Q learning algorithm proposed in this paper employs a maximum entropy strategy, which results in smoother and better generalization of the learned policies.
  
  2. In addition, the algorithm introduces a delayed target value version, which can effectively alleviate the overfitting problem in target Q estimation.

### 4. Issues addressed 
  1. The method proposed in this paper mainly addresses the problem of maximum entropy policy learning in continuous action space.
  
  2.  Traditional deep Q learning methods are usually only applicable to discrete action spaces, while the soft Q learning algorithm proposed in this paper can effectively handle the policy learning task under continuous action spaces.
  
  3.  Meanwhile, the algorithm also has good generalization ability and stability, and can achieve good results in practical applications.
 
## Experiments
This paper describes the authors' use of the soft Q learning algorithm in a continuous control task and compares it with the DDPG algorithm. The experiment consists of three parts:

  1. It is verified in a simple multi-objective environment whether the soft Q learning algorithm is able to accurately sample from an energy-based strategy and whether it can successfully learn the full algorithm representing multimodal behavior.

For the first experiment, the authors designed a simple "multi-target" environment in which the agent is a two-dimensional mass trying to reach one of four symmetrically located targets. The reward is defined as a mixed Gaussian distribution, where the mean is located at the target position. The optimal policy is to choose a goal arbitrarily, while the optimal maximum entropy policy should be able to randomly choose all four goals. The resulting policy correctly selects one of the four targets and is able to learn diverse trajectories across all four targets. In contrast, the policy trained using the DDPG algorithm selects one target randomly.

![image](https://github.com/user-attachments/assets/15cdbf62-9a52-4715-9e81-e3f983064fed)

  2. A simulated continuous control environment is constructed to investigate how a maximum entropy strategy can be utilized to aid exploration. These environments need to track multiple modes to successfully accomplish the task.

For the second experiment, the authors constructed a number of simulated continuous control environments in which tracking multiple patterns is important for success. It used a swimming snake simulator that received speed along the x-axis as a reward for swimming both forward and backward. Once the swimmer swims far enough, he or she crosses a "finish line" and receives a larger reward. Thus, the optimal learning strategy is to explore in both directions until the additional benefit of the reward is discovered, and then focus on swimming forward. The results show that our method is able to recover this strategy by tracking both patterns simultaneously until the finish line is discovered. In contrast, the method using the DDPG algorithm selects a less favorable pattern.

![image](https://github.com/user-attachments/assets/4cdf920e-1aac-40fa-848e-13533731619d)

The second experiment was a more complex task involving a series of equally good options that remained so until a sparse reward target was discovered. In this task, a three-dimensional quadrupedal robot needs to find a path to a goal location. The reward function is a Gaussian distribution centered on the goal. The agent can choose either an upper or lower pathway, which look the same at first, but the upper pathway is blocked by a wall. As in the swimming snake experiment, the optimal strategy requires exploring in both directions and choosing the better one. The results show that our method successfully completes the task faster than the DDPG algorithm.

![image](https://github.com/user-attachments/assets/49ce9d84-d2a3-4fe2-8129-bb7637b558ae)

  3. Explore how pre-trained maximum entropy strategies can be used to accelerate learning of complex tasks. In this section, the authors use a variant of the quadrupedal robot task for demonstration purposes.

For the third experiment, the authors show how a pre-trained maximum entropy policy can be used to accelerate learning of complex tasks. In this section, the authors used a variant of the quadrupedal robot task for their demonstration. The pre-training phase involved learning to move in an arbitrary direction with a reward equal to the speed of the center mass. The resulting policy moves the agent rapidly in a randomly chosen direction. This pre-training is similar to recent work such as modulated controllers and hierarchical models, but does not require any task-specific goal generators or rewards. Test environments included hallway environments, U-shaped mazes, etc., which were used to fine-tune the running strategies to fit specific tasks. The results show that the pre-trained strategies can explore the space extensively and in all directions, which provides a good initialization for subsequent tasks.  

## Conclusion

### 1. Advantages of the Thesis
This thesis presents an energy model-based RL algorithm for training energy models of arbitrary multimodal strategies by using soft-valued functions and Stein variational gradient descent (SVGD), and combines it with Q-learning and actor-critic algorithms.

  1. It is able to handle complex multimodal behaviors, and initial strategies can be obtained through pre-training.
  
  2. Multiple modes in a high-dimensional state space can be explored efficiently and can be switched between them.
  
  3. Due to the use of an energy model, the policies can be represented as arbitrary distributions and can therefore be adapted to a variety of different tasks and environments.

![image](https://github.com/user-attachments/assets/111536f5-28fb-4173-9b78-71aa912fbd52)

### 2. Innovative points
  1. The ability to handle complex multimodal behavior and the ability to obtain an initial policy through pre-training.
  
  2. The ability to efficiently explore multiple modes in a high-dimensional state space and to switch between them.
  
  3. Due to the use of an energy model   


