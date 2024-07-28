# Mastering Atari with Discrete World Models
[paper link](https://arxiv.org/pdf/2010.02193) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a reinforcement learning agent called DreamerV2 that is able to learn behavior by prediction in the compact hidden space of a robust world model that uses a discrete representation and is trained separately from the strategy.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
This approach successfully solved 55 tasks in the Atari game benchmark, achieving human-level performance. Using the same computational budget and time, DreamerV2 achieves higher frame rates compared to existing single-GPU agents and outperforms the final performance of top single-GPU agents such as IQN and Rainbow. In addition, DreamerV2 can be applied to tasks with continuous motion, such as accurate world modeling of complex humanoid robots and solving standing and walking problems with pixel-only input.

![image](https://github.com/user-attachments/assets/e015a777-cf6d-4e8f-b806-3e74f313e4e5)

### 2. Method Description 
This paper proposes a model-based RL algorithm called DreamerV2. The algorithm predicts future behaviors by using a world model and learns long-term dependencies in the model. Specifically, DreamerV2 consists of three main components: **a world model, an actor, and a value function**. The world model is used to predict future state sequences and extract information from them to guide behavioral choices. The actor is a randomized strategy network that selects actions based on the current state. The value function is used to evaluate the value of each state and help the actor optimize its strategy.

![image](https://github.com/user-attachments/assets/516a1249-5174-414d-9fd2-39a5b841b748)

### 3. Methodological improvements
  1. The main improvement in DreamerV2 compared to DreamerV1 is the replacement of the Gaussian Latent variable with a Categorical Latent variable, and this makes the model more robust and allows for better utilization of the available information.
  
  2. In addition, DreamerV2 introduces the KL balancing technique in order to better train the world model and avoid overfitting.

### 4. Issues addressed 
DreamerV2 aims to solve the problem of long-term dependency in RL. By using a world model, DreamerV2 can learn long-term dependencies in a simulated environment and perform these behaviors in a real environment. This approach has already yielded good results on Atari games and continuous control tasks.

## Experiments
This paper focuses on the performance of DreamerV2 in Atari benchmarks and a comparison with four model-independent algorithms. The experiments include a comparison of game performance under four types of aggregation methods and single-task settings, as well as a detailed analysis of the role of each component in DreamerV2.

First, the article describes four different aggregation methods: _Gamer Median, Gamer Mean, Record Mean, and Clipped Record Mean_. by comparing these methods, the authors found that using Clipped Record Mean provides a better measure of the overall performance of the algorithms.

Next, the article compares DreamerV2 to four other model-independent algorithms, including _IQN, Rainbow, C51, and DQN_.The results show that DreamerV2 outperforms the other algorithms under all four aggregation methods and achieves the greatest advantage under Record Mean.

In addition, the article conducts an extensive Ablation Study to explore the role of various components in DreamerV2. Among them, the use of discrete latent variables and KL balancing significantly improves performance, while stopping the reward gradient even further improves performance on certain tasks. 

Finally, the article also compares DreamerV2 with some recent RL algorithms, including MuZero and SimPLe. The results show that DreamerV2 and SimPLe build complete models of the environment by utilizing the learning signals from the image inputs, while MuZero learns its models through value gradients specific to each task. However, the Monte Carlo tree search used by MuZero adds complexity and is difficult to parallelize, and thus has some limitations compared to DreamerV2.

![image](https://github.com/user-attachments/assets/d24ee2bc-3816-4b49-969c-790ba6135d78)

![image](https://github.com/user-attachments/assets/df5e8ce0-14b3-4467-aaf5-9c802073c50b)

## Conclusion

### 1. Advantages of the Thesis
1. In contrast to traditional model-based approaches, DreamerV2 does not need to explicitly model the state transfer probabilities of the environment, but instead uses a trained world model for prediction and planning.

2. In addition, the authors have made improvements to the original Dreamer, including the use of discretized hidden spaces and KL balancing terms, to further improve performance.

### 2. Innovative points
1. Compared to traditional model-based approaches, DreamerV2 does not need to explicitly model the state transfer probabilities of the environment, but instead uses the trained world model for prediction and planning.

2. This approach not only reduces modeling complexity, but also allows for better handling of high-dimensional inputs in continuous control tasks.

3. In addition, the authors have made improvements to the original Dreamer, the use of discretized hidden space reduces error accumulation and improves memory efficiency, while the KL balancing term helps the model to better learn the hidden space distribution, thus improving the performance performance.
   
### 3. Future Works
1. The algorithms could be applied in a multi-intelligent body environment or extended to more complex physical robot control tasks.

2.  In addition, other RL algorithms can be attempted to be combined with the world model for better performance.
