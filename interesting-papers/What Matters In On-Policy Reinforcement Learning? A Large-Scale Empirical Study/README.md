# What Matters In On-Policy Reinforcement Learning? A Large-Scale Empirical Study
[paper link](https://arxiv.org/pdf/2006.05990) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | The aim of this paper is to explore how online policy training can be performed in reinforcement learning and to analyse some of the key factors in the training process in a large-scale experiment.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
The authors implemented more than 50 different design decisions to build an online policy training framework in a unified way for training more than 250,000 agents in five successively controlled environments of varying complexity. Through these experiments, they provide practical advice and insights on online policy training to help people better understand the design and implementation of reinforcement learning algorithms.

### 2. Method Description 
This paper focuses on the selection of different hyperparameters to optimise algorithm performance in continuous control reinforcement learning. The authors propose a unified RL algorithm and configure it with several optional choices, including loss function, neural network architecture, gradient clipping and so on. At the same time, in order to avoid problems such as slow training progress or failure to converge due to random sampling, the authors used group experiments, in which each experiment combines relevant choice items, randomly samples these combinations, and uses a set of default baseline configurations as the basis for other settings. Finally, the authors assessed the significance and effectiveness of each selection term by calculating its distribution in the top 5% best models and the 95th percentile of conditions.

### 3. Methodological improvements
The algorithm design presented in this paper is highly flexible and extensible, allowing new choice items to be easily added and maintaining a uniform configuration approach. In addition, the reliability and accuracy of the experiments are improved by means of group experiments, which avoid misleading results that may result from the adjustment of a single choice item.

### 4. Issues addressed 
The research in this paper addresses the problem of how to select different hyperparameters to optimise the performance of the algorithm in continuous control RL. By designing a unified RL algorithm and configuring it with multiple optional choices, the authors were able to gain a more comprehensive understanding of the impact of different choices and provide some suggestions on how to select hyperparameters. In addition, by means of group experiments, the authors have addressed the problem of misleading results that can result from the adjustment of a single choice term, improving the reliability and accuracy of the experiments.

## Experiments
This paper describes hyperparametric search experiments on the PPO algorithm in five environments and provides an analysis of the design and results of each experiment. Specifically, these experiments include:

**Policy Losses experiment**: in this experiment, the authors compare different policy loss functions, including AWR, PG, PPO, RPA, and V-MPO. The results show that PPO performs best, followed by V-MPO and RPA.
![image](https://github.com/user-attachments/assets/d40adf48-8058-4b2c-bf84-9ce4adc82978)

**Network Architectures experiment**: this experiment compares different network architecture choices, including the use of clip or tanh as the output activation function and the choice of separated or shared MLP. The results show that the shared MLP performs best, while using clip as the output activation function works better than tanh.
![image](https://github.com/user-attachments/assets/10facc48-ca57-4c97-9806-7d2d7488d1c8)

**Normalisation and Clipping Experiment**: In this experiment, the authors compared different input normalisation and gradient clipping methods. The results show that using the mean value as input normalisation works best, while using a larger value of gradient clipping improves performance.
![image](https://github.com/user-attachments/assets/466b17dc-1dec-42f2-9da9-d7b39eea637b)

**Advantage Estimation (AE) Experiment**: this experiment compares different advantage estimation methods, including value function based methods and policy based methods. The results show that using GAE and V-Trace as an advantage estimator performs best.
![image](https://github.com/user-attachments/assets/322b2095-c41b-4f51-ad9d-177948e8eb13)

**Training Setup Experiment**: In this experiment, the authors compared different training setups, including iteration size, batch mode, and optimiser selection. The results show that the best performance was achieved using a fixed trajectory batch mode and the Adam optimiser.
![image](https://github.com/user-attachments/assets/1bfaefcc-41ec-443b-b42b-b19283847cb1)

**Time experiment**: this experiment compares different time factors, including discount factor and frame skip rate. The results show that smaller discount factors and higher frame skip rates improve performance.
![image](https://github.com/user-attachments/assets/b3297d12-08ec-453a-bb72-989be90d88d8)

**Optimizers Experiment**: In this experiment, the authors compare different optimisers, including Adam and RMSProp, and the results show that the best performance is achieved using the Adam optimiser.
![image](https://github.com/user-attachments/assets/535b1b05-fb42-44eb-9601-3e3fae847651)

**Regularizers experiment**: finally, the authors compared different regularisation methods including constraints, penalties and entropy regularisation. The results show that using the penalty term as a regularisation method performs best. 
![image](https://github.com/user-attachments/assets/0d0150ed-8105-4ceb-a2ba-3ed236202c8f)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper examines the importance of a range of high-level and low-level choices that need to be made when designing and implementing policy-based learning algorithms, and provides practical advice.
  
  2. Using over 250,000 experiments, the authors evaluate the impact of different choices in five continuously controlled environments.
  
  3. In addition, the paper provides a unified implementation of the on-policy algorithm with more than 50 choices. These contributions provide important insights for understanding performance improvement in deep reinforcement learning.

### 2. Innovative points
  1. The main contribution of this paper is to explore the importance of the range of high-level and low-level choices that need to be made when designing and implementing policy-based learning algorithms, and to provide practical advice through an in-depth study of over 250,000 experiments.
  
  2. The authors use a unified implementation of the on-policy algorithm that contains more than 50 choices, which allows researchers to better understand the impact of low-level decisions on the performance of high-level algorithms.
  
  3. In addition, the authors found some surprising results, such as that initialising the network so that the initial action distribution has a zero mean, a low standard deviation and is independent of observations can significantly improve training speed.
     
### 3. Future Works
Future research can further explore the impact of other low-level design choices on performance and try to propose better solutions to address these issues. In addition, the methods in this paper can be applied to a wider range of environments and tasks to verify their generalisability and practicality. 
