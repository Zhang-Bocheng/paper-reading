# Gradients are Not All You Need
[paper link](https://arxiv.org/pdf/2111.05803) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper discusses the limitations of differentiable programming techniques that are widely used in the field of machine learning and proposes a failure model based on chaos theory.         | Machine Learning          |

## Methodology

### 1. Abstract
  By analyzing the spectral characteristics of the Jacobi matrix of the system, the authors provide judgment criteria that practitioners can refer to in order to avoid such failures when using differentiable optimization algorithms. The results of this paper contribute to a better understanding of the scope and limitations of the application of microprogrammable techniques and provide some insights for future research.
  
  ![image](https://github.com/user-attachments/assets/3f932ddd-d98e-4166-9081-b352f70340d6)

### 2. Method Description 
  One such approach utilizes the Fokker-Planck equation for climate modeling. Other approaches utilize the Fluctuation-Dissipation theorem with different assumptions.Gutiérrez and Lucarini treat the state-space distribution evolution as a Markov chain, which allows to compute the gradient.Chandramoorthy and Wang proposed another approach to compute the time-averaged gradient that involves averaging multiple samples over a finite time horizon.

### 3. Methodological improvements
  Each of these methods proposed by the researchers involves working with the distribution of the system's states rather than using samples. This allows the researchers to better understand the dynamic behavior of the system and compute more accurate gradient values. And they proposed new methods for calculating time-averaged gradients, which are based on averaging over multiple samples and have better convergence rates.
  
### 4. Issues addressed 
  The method proposed by the researchers can help solve some of the problems that arise when calculating the gradient of a system, such as how to deal with the distribution of system states and how to calculate the time-averaged gradient. These problems are usually complex and require the use of some advanced mathematical tools and techniques to solve them. These methods proposed by the researchers provide some useful ideas and tools to solve these problems.
  
## Experiments
  This paper focuses on several optimization methods commonly used in model training and conducts comparative experiments to evaluate their performance. The following is a detailed description of each comparison experiment:

**Comparison experiment between gradient descent method and adaptive learning rate algorithm**
This experiment evaluates the effectiveness of the gradient descent method and the adaptive learning rate algorithm by comparing them in training a simple NN. The experimental results show that the adaptive learning rate algorithm is able to converge to the optimal solution faster and has better generalization ability.

**Experiment comparing stochastic gradient descent with regularization and Adam's algorithm**
This experiment is evaluated by comparing the effectiveness of Stochastic Gradient Descent (SGD) with L2 regularization and Adam's algorithm in training a complex NN. The experimental results show that the Adam algorithm outperforms the SGD method with regularization in terms of convergence speed and generalization ability.

**Experiment comparing the backpropagation algorithm and Newton's method**
This experiment is evaluated by comparing the effectiveness of the backpropagation algorithm and Newton's method in training a DNN. The experimental results show that Newton's method is more effective than the backpropagation algorithm.

**Experiment comparing dynamic programming algorithm and Monte Carlo tree search algorithm**
This experiment is evaluated by comparing the effectiveness of the dynamic programming algorithm and the Monte Carlo tree search algorithm when solving problems in board games. The experimental results show that the Monte Carlo tree search algorithm is more advantageous than the dynamic programming algorithm, especially when facing complex decision-making problems.

![image](https://github.com/user-attachments/assets/b0b606d0-ef2c-4b0b-9506-33052e91f8f5)

![image](https://github.com/user-attachments/assets/4f0730dd-b6cc-42e2-9ee2-85efb1afea04)

## Conclusion

### 1. Advantages of the Thesis
  This paper provides an in-depth study on the application of automatic differentiation in iterative dynamical systems and points out the problems involved. The article lists the instabilities and explosions that occur in several real-world application scenarios and proposes corresponding solutions. Also, the authors discuss the problems faced by different types of ML tasks and give corresponding solution ideas.
  
### 2. Innovative points
 In this paper, a new perspective is proposed to understand the stability problem of iterative dynamical systems and its validity is verified experimentally. The authors point out that for some specific tasks, the explosion phenomenon can be avoided by controlling the initial state or adjusting the network structure. This approach is different from traditional optimization strategies and can provide new ideas for research in related fields.
 
### 3. Future Works
It is still a challenge to better control the explosion phenomenon when dealing with complex nonlinear models. Therefore, future research directions can be pursued in the following areas: 

1. to further investigate the stability and instability of iterative dynamical systems;

2. to explore more effective control strategies;

3. to apply the method to a wider range of scenarios in order to improve the accuracy and reliability of the automatic differentiation.
