# A Physics-Informed Machine Learning Framework for Safe and Optimal Control of Autonomous Systems
[paper link](https://arxiv.org/pdf/2502.11057) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper presents a physically informed machine learning framework for autonomous system security and optimal control.           |  Physics-Informed Machine Learning        |

## Methodology

### 1. Abstract
Safety and performance may be competing goals, which makes their co-optimisation difficult. Learning-based approaches, such as Constrained Reinforcement Learning (CRL), can achieve robust performance, but the lack of formal safety guarantees limits their use in critical settings as safety is enforced as a soft constraint. In contrast, formal methods, such as Hamilton-Jacobi (HJ) reachability analysis and Control Barrier Functions (CBFs), provide tight guarantees but typically ignore performance, leading to overly conservative controllers. To bridge this gap, the paper formalises the co-optimisation of safety and performance as an optimal control problem with state constraints, encoding the performance objective in a cost function and treating the safety requirements as state constraints. 

The results show that the obtained value function satisfies the Hamilton-Jacobi-Bellman (HJB) equation, which we efficiently approximate via a novel physically-informed machine learning framework. Furthermore, a calibration prediction-based validation strategy is introduced to quantify the learning error and recover a high-confidence secure value function as well as probabilistic error bounds for performance degradation. 

### 2. Method Description 
This thesis presents a machine learning based approach to optimise the safety performance of a nonlinear system. First, the behaviour of the system is modelled as a state-control input dynamic equation and a cost function is defined to measure the performance of the system. Then, an auxiliary value function is used to represent the optimal strategy for minimising the cost in a given state and encoded as a neural network. Finally, the safety and performance of the strategies are verified through a predictive model-based approach, and the value function is adjusted to obtain a better strategy based on the results.

![image](https://github.com/user-attachments/assets/60ee9ff4-9018-4ff1-903b-970e8cd3be13)

### 3. Methodological improvements
Compared to traditional numerical methods, this approach offers better scalability and efficiency, especially in high-dimensional systems. In addition, it provides an efficient way to deal with non-convex, non-smooth and non-linear problems.

### 4. Issues addressed 
The method can be used to optimise various types of nonlinear systems, including robots and self-driving cars. It can improve the safety, reliability and performance of systems and help designers better understand and control the behaviour of complex systems.

## Experiments
This paper presents three different experiments to validate the effectiveness of its proposed synergistic optimisation approach for performance and security. In each experiment, comparisons are made with several baselines and the results are evaluated using two metrics (cumulative cost and safety rate).

The first experiment is **a 2D autonomous ship navigation problem** in which a ship must avoid two circular obstacles and reach an island. In this experiment, the authors' method is able to successfully approach the target and remain safe, whereas the other methods do not guarantee safety or performance.

The second experiment was **an experiment in which an acceleration-driven pursuer vehicle tracked a mobile evader while avoiding five circular obstacles**. This experiment is more complex than the first, but the authors' approach still manages to balance safety and performance in a high-dimensional environment.

The third experiment is **a multi-intelligent body navigation problem** in which five agents need to avoid collisions and reach their respective goals. This experiment is the most complex, but the authors' approach is still able to balance safety and performance in a high-dimensional system.
![image](https://github.com/user-attachments/assets/1b065b08-dd3e-4e02-87dc-b644e3923d20)

## Conclusion

### 1. Advantages of the Thesis
The approach does this by modelling the problem as a state-constrained optimal control problem and using the Epigraph method to compute security-aware policies, while incorporating adaptive security verification techniques to ensure high-confidence security guarantees while maintaining optimal performance. And, the authors conduct several case studies to demonstrate the effectiveness and scalability of the methodology in high-dimensional systems.

### 2. Innovative points
The approach uses the Epigraph method to compute security-aware policies while incorporating adaptive security verification techniques to ensure high-confidence security guarantees while maintaining optimal performance. This approach is innovative and can be applied to various types of autonomous systems.
 
### 3. Future Works
  1. In future work, the authors plan to explore how to quickly adapt learned strategies based on new information (e.g., system dynamics, environmental or security constraints).
  2. In addition, they will apply the method to other high-dimensional autonomous systems as well as to systems with unknown dynamics. This will further extend the application of the method and help to solve more practical problems. 
