# Constrained Multi-objective Optimization with Deep Reinforcement Learning Assisted Operator Selection
[paper link](https://arxiv.org/pdf/2402.12381) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | The aim of this paper is to address the problem of selecting appropriate evolutionary operators in multi-objective constrained optimisation problems.           | Reinforcement Learning         |

## Methodology

### 1. Abstract
The authors propose an online evolutionary operator selection framework based on deep reinforcement learning and embed it into four popular multi-objective evolutionary algorithms for evaluation. Experimental results show that the method significantly improves the performance of these algorithms and the resulting algorithms are better adapted with respect to nine state-of-the-art multi-objective evolutionary algorithms.

### 2. Method Description 
In this paper, the authors propose an adaptive operation selection method based on Deep Reinforcement Learning (DRL) for solving Constrained Multi-Objective Optimisation Problems (CMOP). The main idea of the method is to use a deep neural network to evaluate the effects of different operation choices on the evolutionary process and dynamically select the best operation based on these effects. 

![image](https://github.com/user-attachments/assets/6e2624df-c8d9-4e54-844c-b6240b28dee1)

Specifically, the method represents the state at each moment of the evolutionary process as a vector containing information about the evolutionary state in three aspects: convergence, diversity and feasibility. Then, a deep neural network is trained to predict the value of the reward that each operation may bring in a given state. Finally, in each iteration, the operation with the maximum expected reward is selected as the next action based on the current state and the prediction of the deep neural network.

### 3. Methodological improvements
  1. The ability to handle constrained multi-objective optimisation problems, whereas traditional methods can usually only handle unconstrained single- or multi-objective optimisation problems.
  2. The deep neural network-based model is able to better capture the effect of operation selection on the evolutionary process, thus improving the accuracy of operation selection.
  3. Due to the use of deep neural networks, the method can handle more complex decision spaces, including both continuous and discrete variables.

### 4. Issues addressed 
  This paper proposes an adaptive operation selection method based on deep reinforcement learning, which is capable of dynamically selecting the optimal operation under the premise of guaranteeing feasibility, thus improving the performance of the optimisation algorithm. The method is applicable to various types of CMOPs, including combinations of continuous and discrete variables. Therefore, the method has a wide range of applications.

## Experiments
I. Experimental setting: In their experiments, the authors chose four challenging CMOP benchmark test suites to test their approach and classified these benchmarks into four categories. They embedded four different C MMO algorithms (CCMO, MOEA / D-DAE, EMCMO, and PPS) and used DRL-assisted selection of operators to compare with these four algorithms. In addition, they analysed the algorithm parameters and investigated the effectiveness of using two performance metrics to assess the population state.

![image](https://github.com/user-attachments/assets/0b9f29db-677b-4176-a5cf-86896e117399)

II. DQL-assisted OS experiments: in this part of the experiments, the authors compare the effectiveness of the CCMO and EMCMO algorithms using DQL-assisted selection operators with other fixed and random operator selection algorithms. The results show that DRLOS-CCMO and DRLOS-EMCMO significantly outperform the other methods, performing better on CFs and DAS-CMOPs, and worse on DOCs and LIR-CMOPs. Overall, the DQL-assisted selection operator improves the performance of these C MMO algorithms.

III. Comparative Research Experiment: In this part of the experiments, the authors compared the DRLOS-EMCMO algorithm with nine state-of-the-art C MMO algorithms in order to study the performance of these algorithms. The results show that DRLOS-EMCMO outperforms other C MMO algorithms on these challenging CMOPs. However, it performs poorly in some cases, e.g., on problems requiring specific operators, or when some constraint relaxation techniques are required, such as ε-constraints or penalty functions in ShiP-A.

![image](https://github.com/user-attachments/assets/9611fc45-5466-4316-92a4-f4282aa32dec)

IV. Parameter Analysis Experiments: In this part of the experiments, the authors test the effect of parameters such as EP size and batch size on the training DQL by varying them, and test the effect of greedy thresholds on their robustness. The results show that these parameters have little effect on the performance of all benchmark problems. The authors then varied the settings of important parameters, including learning rate decay, learning rate, number of iterations, and number of nodes in each hidden layer, to test the effects of these parameter settings on DRLOS-EMCMO. The results show that different parameter settings have little or no significant effect on DRLOS-EMCMO.

![image](https://github.com/user-attachments/assets/9a3873b8-8935-4889-a833-c6dc99f2443d)

Finally, the authors also conducted a metrics-based experiment comparing the impact of using simple and complex evaluations on the performance of the algorithms. The results show that for CCMO and EMCMO, the use of simple evaluation performs better when dealing with DSA-CMOP1-3 and DOCs, while the use of the HV and Spacing metrics provides more accurate results when evaluating DAS-CMOP4-9 with a higher degree of GA operator preference. For MOEA / D-DAE and PPS, on the other hand, there are no significant differences.
  
## Conclusion

### 1. Advantages of the Thesis
  1. An adaptive operation selection method based on deep reinforcement learning is proposed to efficiently solve the optimisation problem in CMOPs.
  2. Using a DQL model to train the operation selection policy and embedding it into any existing CMEGO can achieve good performance on different types of CMOPs.
  3. Comparative experiments show that the method works better with specific types of operations and is highly scalable and robust.
 
### 2. Innovative points
  1. Using deep reinforcement learning technique, the operation selection policy is embedded into CMEGO, which improves the efficiency and accuracy of the algorithm.
  2. When dealing with specific types of operations, the method can automatically adjust the operation selection strategy according to the actual situation, avoiding the need for human intervention. 

### 3. Future Works
  1. Further research can be done to improve the learning speed and accuracy of the DQL model in order to find the optimal solution faster.
  2. Combining other advanced learning methods (e.g. deep reinforcement learning) with traditional evolutionary algorithms can be considered for better performance.
  3. More types of CMOPs can be explored to validate the applicability and effectiveness of the method.
