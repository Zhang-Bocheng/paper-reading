# A Robust Integrated Multi-Strategy Bus Control System via Deep Reinforcement Learning
[paper link](https://arxiv.org/pdf/2308.08179) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a deep reinforcement learning-based multi-policy fusion approach for solving the problem of inefficient bus operations on signalised urban corridors.          | Deep Reinforcement Learning         |

## Methodology

### 1. Abstract
The method utilises connectivity and self-driving vehicle technologies to combine real-time information with traffic conditions and achieves effective management of multiple traffic conditions and passenger demand by integrating elements of physical information, equilibrium and consensus concepts from control theory, and reward functions. The experimental results show that the method exhibits excellent results under different factors and provides new ideas for improving the service quality and user experience of urban public transport.

### 2. Method Description 
This paper proposes a distributed DRL-based multi-strategy fusion control algorithm to solve the transit congestion problem by integrating multiple control strategies. The method is based on a physical information-driven deep reinforcement learning model that combines data sources such as real-time traffic flow, signal status, and historical passenger demand, which are used as inputs to develop an optimal scheduling plan. 

![image](https://github.com/user-attachments/assets/1948fe13-7674-461c-90a2-8b9085ee082a)

### 3. Methodological improvements
  1. Compared with traditional control strategies, the multi-strategy fusion control algorithm proposed in this paper can better cope with complex traffic environments and changing demand situations.
  2. And, the method adopts a distributed architecture, which allows multiple intelligences to work together to optimise the efficiency of bus operation.
  3. In terms of concrete implementation, the method also introduces a physical information-driven deep reinforcement learning model to improve the accuracy and robustness of decision-making.

![image](https://github.com/user-attachments/assets/64b66269-3404-44ff-8d8a-1fad2aaa2cda)

### 4. Issues addressed 
The multi-strategy fusion control algorithm proposed in this paper mainly solves the congestion problem arising in public transport systems. By comprehensively analysing data sources such as real-time traffic flow, signal status, and historical passenger demand, the method is able to develop a more reasonable scheduling plan, thus improving the operational efficiency and on-time rate of buses. 

## Experiments
This paper focuses on a bus control system based on deep reinforcement learning, and evaluates and compares it through numerical experiments. Specifically, the authors designed four experiments to evaluate the performance of the system:

**General performance comparison experiment:** the system was compared with no control, schedule strategy and arrival time strategy, and the results showed that the system performs well in reducing the congestion problem of buses.

**Control experiments under different traffic conditions:** different traffic conditions were simulated by setting different traffic costs, and the results show that the system maintains a good performance under different traffic conditions.

![image](https://github.com/user-attachments/assets/0d0ab4bd-dd47-4a01-acea-e0051379f36f)

**Single control force experiment:** the effects of using speed control, signal priority control and stopping control alone are tested separately, and the results show that each of the three strategies has its own advantages and disadvantages, but the combination can solve the problem better.

**Sensitivity Analysis Experiment:** The performance of each strategy under high traffic volume is investigated by further analysing the single control force experiment, and the results show that each of the three strategies has a limited range of control and needs to be used in combination to achieve the best results. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a multi-strategy bus control method based on distributed DRL, which is able to integrate bus arrival time accuracy, headway spacing regularity and multi-intelligent body system consistency, and capture uncertainty in the process of handling uncertainty.
  2. Besides, this paper constructs a real DRL environment based on historical data and real-time traffic information, and designs a distributed control framework to achieve the fusion of multiple control variables.
  3. Finally, through a series of numerical experiments, it is demonstrated that the proposed control method is advantageous in maintaining the regularity of scheduling time and headway spacing, and is able to work cooperatively under different congestion levels, proving that it is unaffected by fluctuations in traffic conditions.

### 2. Innovative points
  1. The method employs historical data and real-time traffic information to construct a real DRL environment, and utilises a distributed control framework to achieve the fusion of multiple control variables.
  2. And, the method introduces the DPPO algorithm to update the control strategy and considers the influence of external factors such as traffic volume and signals. 

### 3. Future Works
  1. There is a need to develop a bus control model that can handle multiple bus routes in order to adapt to more complex traffic situations.
  2. More accurate passenger demand model needs to be developed that takes into account factors such as the number of boarding and alighting passengers as well as vehicle capacity.
  3. Some deep learning algorithms can also be applied to predict bus arrival times to further develop active bus control strategies.
In conclusion, future research should continue to focus on the uncertainty problem of bus systems and seek better solutions.   
