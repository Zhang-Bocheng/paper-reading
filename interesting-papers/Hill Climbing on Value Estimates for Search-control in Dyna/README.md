# Hill Climbing on Value Estimates for Search-control in Dyna
[paper link](https://arxiv.org/pdf/1906.07791) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper describes a reinforcement learning algorithm called HC-Dyna that uses trajectory search and value estimation to update a policy or value function.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
   The algorithm improves sample efficiency by performing hill-climbing to generate states and actions based on current value estimates and propagating values from high-value regions to low-value regions. The authors also propose a noise-projected natural gradient algorithm for hill-climbing and compare it with Langevin dynamics. The experimental results show that HC-Dyna can obtain significant sample efficiency improvements in four classical domains. In addition, the researchers explore the effects of different sampling distributions on search control and find that hill-climbing from low-value to high-value regions can provide specific benefits.
   
   ![image](https://github.com/user-attachments/assets/45c14e4d-3961-4eb4-b440-3e2e7ea371b2)

### 2. Method Description 
  The algorithm proposed in this paper is an RL algorithm based on DQN (Deep Q-Network) called HC-Dyna. The algorithm uses Hill Climbing method to search for the states in the control queue and update the parameters in the empirical replay buffer. In addition, the algorithm employs a hybrid mini-batch (small batch) approach for training, where one part comes from the SC queue and the other part comes from the ER buffer.
  
### 3. Methodological improvements
  Compared with the traditional DQN algorithm, HC-Dyna algorithm improves the learning efficiency by introducing Hill Climbing method. Meanwhile, the learning problem caused by uneven sample distribution can be mitigated by using hybrid mini-batch to improve the model performance.
  
  ![image](https://github.com/user-attachments/assets/2bcc3a88-1a4d-4022-afea-d18e95abbbc5)

### 4. Issues addressed 
  The HC-Dyna algorithm solves the problems of the traditional DQN algorithm in terms of uneven sample distribution and low learning efficiency, and improves the performance performance of the model.
  
## Experiments
  This paper presents the results of experiments using the HC-Dyna algorithm in four classical domains (GridWorld, MountainCar, CartPole, and Acrobot) and analyzes the effect of different sampling distributions on the learning effect of search control queues. The experiments are divided into two parts, discrete actions and continuous actions.

For discrete actions, the authors compare the **performance of HC-Dyna with the ER and OnPolicy-Dyna algorithms** and show the learning curves of each algorithm for multiple planning steps n. The results are summarized as follows. The experimental results show that HC-Dyna outperforms ER and OnPolicy-Dyna in all cases and more significantly as the number of planning steps increases. 

In addition, the authors observed that HC-Dyna performs better than OnPolicy-Dyna even when the model needs to learn. By visually searching the states in the control queue, it can be observed that HC-Dyna is able to explore more regions, and even in the case of concentrating only on the left half of the ER buffer, HC-Dyna is still able to update the state-value function close to the target region.

For continuous actions, the authors used DDPG as an example and applied HC-Dyna to DDPG. The experimental results show that HC-Dyna is able to significantly improve the learning efficiency of the DDPG and reach better solutions at an early stage. This suggests that the improved search control is particularly suitable for Actor-Critic algorithms that are prone to local minima.

Next, the authors conducted two experiments to explore the **effect of sampling distribution on the learning effectiveness of the search control queue**. The first experiment compares different sampling methods such as HC-Dyna, Gibbs, HC-Dyna-Vstar and Gibbs-Vstar. The experimental results show that HC-Dyna is the optimal sampling method, while Gibbs and Gibbs-Vstar are less effective. 

The second experiment compares the value estimates with the true values and the results of the experiment show that using value estimates instead of true values is more favorable for planning. This suggests that value estimation does have some additional value in the current state.

![image](https://github.com/user-attachments/assets/d3077e0b-48f6-4fd3-8c43-d150efae741c) 

![image](https://github.com/user-attachments/assets/f70d59e2-287c-4ee0-ae86-9e48e5be9f7d)

## Conclusion

### 1. Advantages of the Thesis
  1. The authors propose a noisy natural projected gradient ascent strategy for use during peak search and demonstrate that the use of states from peak search can significantly improve sample efficiency.
  
  2. In addition, the article empirically investigates and validates a number of choices in the algorithm, including the use of natural gradients, the utility of mixing versus ER samples, and the benefits of using estimates for search control.
  
  3. Finally, the article points out that the next research direction is to further explore other criteria for assigning importance, such as encouraging systematic exploration based on more explicit criteria such as error or optimism/uncertainty.

### 2. Innovative points
   1. The methodological innovation of this paper is to propose a new Dyna algorithm based on hill search control that uses value estimation-based hill search control to generate states and experimentally demonstrate its efficiency in several benchmark domains.
   
   2. In addition, the article proposes a noisy natural projection gradient ascent strategy for use in the hill search process and applies it to the algorithm. These innovations provide new ideas and methods for research in the field of deep RL.
      
### 3. Future Works
  1. First, other criteria for assigning importance could be further investigated to encourage systematic exploration;
  
  2. second, the approach could be extended to other types of models, such as RNN models; 
  
  3. finally, the approach could be combined with other techniques, such as meta-learning and adaptive control, to achieve better performance.

