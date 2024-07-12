# Gradient Descent Provably Optimizes Over-parameterized Neural Networks
[paper link](https://arxiv.org/pdf/1810.02054) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper explores a puzzle for the success of neural networks: randomly initialized first-order methods such as gradient descent can achieve zero training loss with nonconvex and nonsmooth objective functions.         | Neural Networks          |


## Methodology
  By analyzing a NN activated by a two-layer fully-connected ReLU, the authors show that stochastically initialized gradient descent can converge to a globally optimal solution at a linear rate of convergence as long as the number of hidden nodes is sufficiently large and there are no two inputs in parallel. 
  
  The analysis relies on the observation that over-parameterization and stochastic initialization jointly restrict each weight vector to be close to its initial value in all iterations, and uses properties similar to strong convexity to show that gradient descent converges to the global optimal solution at a global linear rate. These insights may also be useful for analyzing depth models and other first-order methods.
  
## Experiments
  This paper presents analysis and research on nonconvex optimization problems. 
  
  In the first part, the authors provide an overview of previous research, including the use of landscape analysis methods to determine whether NN have good geometric properties and the use of algorithmic dynamics to directly analyze gradient descent. However, none of these methods can explain why randomly initialized gradient descent can find a global minimum. 
  
  Therefore, in Part II, the authors propose a new theoretical framework, continuous time analysis, to demonstrate that randomly initialized gradient descent can achieve zero training error over infinite training time. 

  Specifically, the authors consider two-layer fully connected NN with ReLU activation functions and demonstrate their convergence rate by assuming that the input data are not parallel.

  ![image](https://github.com/user-attachments/assets/cabfabfd-aa0b-48c4-867f-6903bd56c5c9)

## Conclusion
   Finally, the authors point out that the framework can be further improved by more advanced concentration analysis. Overall, this paper provides a new theoretical framework to explain why stochastically initialized gradient descent can find a global minimum and provides insights for future research.

