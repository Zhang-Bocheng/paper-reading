# QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning
[paper link](https://arxiv.org/pdf/1803.11485) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 |This paper describes a new method called QMIX for training decentralized strategies in multi-intelligent agent reinforcement learning.           |  Reinforcement Learning         |

## Methodology

### 1. Abstract
In many real-world situations, a group of agents must coordinate their behavior and act in a decentralized manner. However, in a simulation or laboratory setting, agents can be trained by centralized learning where global state information is available and communication constraints are lifted. Learning joint action values using additional state information is an attractive way to leverage centralized learning, but the optimal strategy for extracting decentralized strategies from it is not known.

QMIX is a novel value-based method for training decentralized strategies in a centralized end-to-end style. QMIX uses a network to estimate joint action values as a complex nonlinear combination of per-agent values under locally observed conditions. The structure enforces monotonicity of joint action values over agent values, which allows for the derivation of joint action value maximization in off-policy learning and ensures consistency between centralized and decentralized strategies. 

![image](https://github.com/user-attachments/assets/25f70b6f-0307-4b4f-abab-f19697ccae42)

### 2. Method Description 
The paper proposes four different multi-intelligent body reinforcement learning methods: **deep Q learning, recursive Q learning, independent Q learning and value decomposition network (VDN)**. Among them, VDN is a new method that combines the value functions of all the intelligences into a global value function and calculates the contribution value of each intelligence by its individual value function. This method is more effective than others in some cases.

![image](https://github.com/user-attachments/assets/efb9e7bd-51f4-4bf5-896b-92a2ce9acd7a)
 
### 3. Methodological improvements
VDN can better handle problems in non-stationary environments than traditional independent Q-learning methods. It can calculate the contribution value of each intelligence by its individual value function, which makes the behavior of each intelligence more coherent. In addition, the method can use recurrent neural networks to handle problems in partially observable environments.

### 4. Issues addressed 
The paper mainly addresses some problems in multi-intelligence RL, such as how to deal with problems in non-stationary environments and how to deal with problems in partially observable environments. Also, the paper provides a new method, VDN, for solving these problems.

## Experiments
This paper focuses on the authors' experiments in the StarCraft II game and conducts several comparison experiments to evaluate the performance of different reinforcement learning algorithms. Specifically, the authors used the following three comparison experiments:

Q-Mix is compared to Q-Mix without supernetwork (i.e., without conditioning) and VDN to assess the impact of supernetwork on hybrid networks. Results show that Q-Mix performs better on maps with more complexity, while VDN performs better on simpler maps.

Q-Mix is compared to a linearly mixed VDN to assess the importance of nonlinear mixing. The results show that Q-Mix performs better on maps with more complexity, while the linearly mixed VDN performs better on simpler maps.

Q-Mix is compared to a state-independent value function decomposition method to assess the impact of state information on hybrid networks. The results show that Q-Mix performs better on maps with more complexity, while the state-independent value function decomposition method performs better on simpler maps. 

![image](https://github.com/user-attachments/assets/00ead23d-efae-4537-b10b-740fd6591f38)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new deep RL method, QMIX, capable of learning decentralized policies in the presence of centrally trained centralized policies and efficiently exploiting additional state information.
  
  2. QMIX allows the learning of rich joint action value functions that can be decomposed into action value functions for each agent. This is achieved by imposing monotonicity constraints on the hybrid network.
  
  3. Experimental results from the thesis show that QMIX outperforms other value-based multi-intelligence approaches, including methods that use less complex factorization of joint state-value functions as well as independent Q-learning, in the task of decentralized unit micromanagement in StarCraft II.

### 2. Innovative points
  1. QMIX is a deep RL method that can learn decentralized policies in the context of centrally trained centralized policies and efficiently use additional state information.
  
  2. The key to QMIX is the need only to ensure that the global argmax operation produces the same result as a set of individual argmax operations, without the need to fully factorize the VDN.
  
  3. QMIX enforces monotonicity constraints by restricting the hybrid network to have positive weights, allowing for the representation of more complex centralized action value functions and easy extraction of decentralized strategies.

  ![image](https://github.com/user-attachments/assets/8a5031a4-cc75-4c9d-a685-f43b23a28a6c)
 
### 3. Future Works
  1. In future research, the authors plan to conduct more experiments comparing the performance of the methods on tasks with a larger number and higher diversity of units.
  
  2. The longer term goal is to combine QMIX with other coordinated exploration schemes to handle the case of many learning agents.  
