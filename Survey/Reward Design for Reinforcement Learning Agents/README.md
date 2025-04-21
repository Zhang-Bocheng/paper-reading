# Reward Design for Reinforcement Learning Agents
[paper link](https://arxiv.org/pdf/2503.21949) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This thesis focuses on the design of reward functions in reinforcement learning. The reward function is the core factor that guides an intelligent body to make optimal decisions, so designing an effective reward function is crucial to accelerate the learning of an intelligent body and avoid unintended consequences.          | Reinforcement Learning (RL)         |

## Methodology

### 1. Abstract
In this paper, three different approaches to reward function design are proposed: **teacher-driven, adaptive explanatory reward design, and meta-learning**. Among them, the teacher-driven approach designs reward signals that can accelerate the convergence of the intelligences to the optimal behavior through the knowledge of the experts; the adaptive interpretive reward design adjusts the reward signals according to the behaviors of the intelligences on the basis of the current policy to ensure consistency with the task goal and optimal progress; and the meta-learning approach allows the intelligences to design their own reward signals online, thus realizing the self-improvement feedback loop.

And, this paper lists some previous research results, including papers presented at conferences such as NeurIPS'21, NeurIPS'22, and AAMAS'24, as well as a number of other projects completed during MPI-SWS. These research results cover a wide range of areas such as inverse RL, interactive teaching algorithms, and collaborative decision making, and provide additional ideas and methods for solving the reward function design problem in RL.

### 2. Method Description 
This paper focuses on the problem of designing reward functions in RL and proposes three different approaches for designing reward functions with different properties: **non-adaptive teacher-driven interpretable reward design (EXPRD), adaptive teacher-driven interpretable reward design (EXPADARD) and exploration-guided reward design (EXPLORS).** Among them, the Exprd framework is an optimization-based framework for designing reward signals with maximum information metrics; the Expadard framework adds consideration of the current strategy to exprd to better adapt to changes in the strategy; and Explors is a fully self-supervised learning method that does not require any domain knowledge.

### 3. Methodological improvements
Compared to traditional reward design methods, these new methods can better meet the needs of real-world applications, such as improved efficiency, enhanced robustness and adaptability. At the same time, these methods also provide some theoretical foundations and practical tools that can provide better support for researchers and developers.

### 4. Issues addressed 
The design of reward functions in RL has always been a challenging problem, because a good reward function not only needs to be interpretable, but also needs to ensure that it maximizes the information metric without introducing problems such as reward hacking. These new methods proposed in this paper can effectively solve these problems and provide more options and possibilities for practical applications.

## Experiments
This paper presents the experimental results of two RL tasks, ROOM based on grid worlds and LINEK based on chained structures. In each task, the authors compared different reward design techniques and evaluated them using the Q-learning method.

**In the ROOM task**, the authors first used a default reward function (RORIG), and then introduced some expert-driven non-adaptive reward design techniques, such as REXPRD to maximize information comprehensibility and RINVAR to maximize information gain. Then, the authors experimented with an adaptive reward design framework, EXPADARD, which can be used based on the current policy to automatically adjusts the reward function. Experimental results show that EXPADARD significantly improves the convergence speed of the learner, especially in the presence of multiple initial strategies.

**In the LINEK task**, the authors similarly used the default reward function (RORIG) and several other reward design techniques, including REXPRD and RINVAR. Experimental results show that REXPRD is more effective than the other techniques because it better balances convergence speed and sparsity.

Overall, the experimental results in this paper show that an adaptive reward design framework can significantly improve the performance of reinforcement learning algorithms, especially in the presence of multiple initial policies. Also, these results provide some guidance on how to choose the best reward design technique.  

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new optimization framework, EXPRD, for designing reward functions that are interpretable and balance informativeness and sparsity.
  2. The framework introduces a new reward information metric that can adaptively optimize the reward function under structured constraints based on the agent's current strategy.
  3. The paper also proposes an expert-driven interpretable and adaptive reward design framework, EXPADARD, which is experimentally validated in two navigation tasks to demonstrate its effectiveness.
 
### 2. Innovative points
  1. A new optimization framework, EXPRD, is proposed for designing reward functions that are interpretable and balance informativeness and sparsity.
  2. A new reward information metric is introduced that can adaptively optimize the reward function under structured constraints based on the agent's current strategy.
  3. An expert-driven interpretable and adaptive reward design framework, EXPADARD, is proposed to share designed reward functions among different learners. 

### 3. Future Works
  1. Further research can be conducted to investigate how the framework can be applied to more complex environments and tasks.
  2. Consideration can be given to combining the framework with other reinforcement learning techniques, such as value iteration, to improve efficiency and performance.
  3. It can be explored how the framework can be extended to multi-intelligence settings for better collaboration and competitive behavior. 
