# Reducing Idleness in Financial Cloud Services via Multi-objective Evolutionary Reinforcement Learning based Load Balancer
[paper link](https://arxiv.org/pdf/2305.03463) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper discusses the problem of reducing idle servers in financial cloud services and proposes a multi-objective evolutionary reinforcement learning load balancer solution.          | Reinforcement Learning         |

## Methodology

### 1. Abstract
The solution designs a neural network based scalable policy to route user requests to different number of servers to achieve the desired resilience. Optimising the policy weights through an evolutionary multi-objective training framework not only succeeded in reducing the idle rate by more than 130%, but also slightly improved the original load balancing objective. The applicability of the proposed solution to emerging problems is revealed in extensive simulations using synthetic and real-world data.

### 2. Method Description 
The paper presents a reinforcement learning-based load balancing algorithm for financial data services. Specifically, they use a neural network to learn the relationship between user requests and server resources, and train the neural network through a multi-objective optimisation algorithm to achieve optimal load balancing. 

![image](https://github.com/user-attachments/assets/46e48935-8386-4de1-b7ce-d58d853dda6c)

### 3. Methodological improvements
The reinforcement learning method proposed in this paper is more adaptive and flexible than traditional load balancing methods based on rules or heuristic algorithms. In addition, they adopt a parameter-sharing neural network structure to deal with the dynamically changing number of servers, which makes the method better able to cope with the load balancing problem in cloud computing environments.

### 4. Issues addressed 
The paper addresses the load balancing problem in financial data services, i.e., how to distribute user requests to available servers in order to maximise server resources and reduce server idle time. This is a very important problem because financial data services usually need to handle a large number of concurrent requests and need to guarantee high reliability and low latency. By adopting a reinforcement learning approach, the paper provides an efficient, flexible and scalable solution that can help financial data service providers to better meet their customers' needs.

## Experiments
This paper presents research and experimental results on load balancing algorithms for financial data service scenarios. The authors designed four classical rule-based load balancing algorithms and two reinforcement learning-based routing strategies, and conducted comparative analyses through simulation experiments. 

Specifically, the authors conducted a comprehensive evaluation of the performance of the algorithms in the experiments, including but not limited to: performance under different numbers of user requests, performance under different numbers of servers, and performance of the algorithms under the prediction of user connection time error. In addition, the authors provide an in-depth understanding of the algorithm's decision-making process and optimisation strategy by visualising and analysing the algorithm's learning process. 
![image](https://github.com/user-attachments/assets/a50720b0-1e05-47e9-b619-c115ca5d6e34)

![image](https://github.com/user-attachments/assets/e06c92e1-ff24-455d-b5b1-8adb6ad63cdd)

Among them, for each comparison experiment, the authors give detailed experimental settings and evaluation metrics, and list the corresponding experimental results and conclusions. For example, in Section 5, by comparing the performance of four classical algorithms and two reinforcement learning algorithms under different numbers of user requests, the authors conclude that MERL-LB is able to find the best solution and provide different options. In Section 6, the authors explain how the algorithms balance load and waiting time by visualising and analysing the learning process of the algorithms. In Section 7, the authors apply the proposed algorithm on a real dataset and produce results that outperform other algorithms. 

![image](https://github.com/user-attachments/assets/c1fb8b36-f537-477c-b48b-8367c3b2e7bf)

![image](https://github.com/user-attachments/assets/ba3cdd83-3641-4dc3-b641-a34d72eb9da7)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper provides an in-depth study of the problem of reducing server idle time in financial cloud services and proposes a MERL-LB solution.
  2. The researchers used a reinforcement learning approach to solve the problem and designed a parameter sharing routing strategy for neural networks.
  3. The paper verifies the effectiveness and stability of MERL-LB through extensive experiments and compares it with other algorithms.
  4. The researchers also explored how to apply this method in real-world environments and proposed some future research directions.

### 2. Innovative points
  1. The researchers used user connection duration as a new feature and combined it with traditional load balancing metrics to better address the server idle problem.
  2. Researchers designed a parameter-sharing neural network routing policy that can adapt to different server numbers and request load situations.
  3. The researchers used an evolutionary multi-objective optimisation algorithm to train this policy and proposed an action mask operator to help train the policy stably.

### 3. Future Works
  1. The application of MERL-LB in real-world environments may require additional considerations such as noisy environments and expensive simulation environments.
  2. Further research can be done to balance the two objectives using effective sawtooth patterns and to design new heuristic algorithms.
  3. Similar problems in other fields can be explored and attempts can be made to solve them using similar approaches.
