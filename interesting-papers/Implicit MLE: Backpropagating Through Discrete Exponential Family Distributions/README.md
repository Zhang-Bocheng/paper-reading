# Implicit MLE: Backpropagating Through Discrete Exponential Family Distributions
[paper link](https://arxiv.org/pdf/2106.01798) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper describes a learning framework called Implicit Maximum Likelihood Estimation (I-MLE) for end-to-end learning by combining discrete probability distributions and microscopic neural network components.         |           |

## Methodology

### 1. Abstract
   The method does not require smooth relaxation, only the computation of the most probable state, and can be applied to a wide range of situations. The paper also introduces a class of noisy distributions for approximating marginal distributions obtained through perturbation and maximum likelihood estimation (MLE). Experimental results show that I-MLE exhibits competitive or even better performance than existing methods that rely on problem-specific relaxations on multiple datasets.
   
### 2. Method Description 
  The method avoids the complex reparameterization process and exponential suboptimization problem by constructing an objective distribution instead of the standard point estimation method and using sample gradients instead of function gradient computation. Specifically, the method first maps the input data to a discrete probability distribution and then uses the gradient estimator in the I-MLE framework to compute the gradient of the loss function with respect to the network parameters.
  
### 3. Methodological improvements
  Compared with traditional point estimation methods, the I-MLE framework has the following advantages:

  1. It can handle arbitrary forms of target distributions, including complex high-dimensional, sparse or discrete distributions.
  
  2. Reparameterization techniques can be effectively used to avoid exponential suboptimization problems.
  
  3. Simple Monte Carlo sampling methods can be used to approximate the gradient without explicitly computing the probability density function (PDF) of the target distribution.
     
### 4. Issues addressed 
  1. The I-MLE framework proposed in this paper can be applied in the training of various DLg models, especially those that need to deal with complex distributions or have highly nonlinear structures.
  
  2. By using the I-MLE framework these models can be trained more efficiently and better performance can be achieved.
  
  3. In addition, this paper also provides some new ideas and methods for solving some special DL problems, such as how to design appropriate target distributions when facing ILP problems with constraints.
     
## Experiments
  This paper describes several experiments conducted by the authors to compare the performance of different methods and strategies in different scenarios. Specifically, the experiments are divided into three parts:

The first part analyzes and compares the performance of using different methods (including Score function and Straight-through Estimator) on solving a simple Toy Problem and draws some conclusions.

The second part is an experiment under a Latent Variable Setting, where both hv and fu are NN and the optimal structure is not available during training. In this setting, the authors compare different approaches and draw conclusions.

The third part is about how to optimize the black-box combinatorial optimization problem by gradient descent. The authors propose a new approach that uses the objective distribution instead of directly computing the derivative of the objective function. 

![image](https://github.com/user-attachments/assets/91c178ed-e7b2-4e50-9128-15bb999032b4)

A more detailed description of each experiment follows:

**Synthetic Experiments**
This experiment was designed to test the performance of the Score Function and Straight-through Estimator on a Toy Problem. The authors used a tractable 5-subset distribution to simulate a real-world scenario and compared the results of the three methods. The results show that the Straight-through Estimator converges to a better solution faster than the Score Function, but SoG achieves the final result better than Gumbel.

**Learning to Explain**
This experiment was designed to investigate how to learn a distribution that best explains a given aspect score. The authors used the BEERADVOCATE dataset and compared the effects of different approaches. The results show that the method using I-MLE predicts subset accuracy more accurately than other methods.

**Discrete Variational Auto-Encoder**
This experiment was conducted to compare the effectiveness of different noise sampling strategies in solving a Discrete k-subset Variational Auto-Encoder. The authors used a Latent Variable Setting and compared the effects of different approaches. The results show that using SoG-distributed noise achieves the final result better than Gumbel.

**Differentiating through Combinatorial Solvers**
This experiment was conducted to compare the effectiveness of different approaches to solving a Combinatorial Solver. The authors used a randomly generated map dataset and compared the effectiveness of different methods. The results show that the method using I-MLE predicts the shortest path more accurately than the other methods.

![image](https://github.com/user-attachments/assets/94d63fde-6ca5-4c54-b719-20e704481f28)

## Conclusion

### 1. Advantages of the Thesis
  1. The Implicit Maximum Likelihood Estimation (I-MLE) can be applied to learn mixture models and performs well when dealing with discrete probability distributions and discrete combinatorial optimization problems.
  
  2. Compared to traditional relaxation-based problem-specific smoothing methods, I-MLE has wider applicability and better performance performance.
  
  3. In addition, the method does not require access to constraints or the design of specialized relaxation methods, making it more feasible and scalable for large state spaces.

### 2. Innovative points
  1. The main contribution of the paper is the proposal of the I-MLE framework, which approximates the gradient of a discretely distributed parameter by computing the target distribution q at each update step.
  
  2. The maximum likelihood gradient is approximated using q as the empirical distribution in the backpropagation process. The advantage of this method is that it only requires the ability to compute the most likely state without the need for faithful samples or probabilistic inference.
  
  3. In addition, the paper proposes two families of target distributions and one family of noise distributions for Gumbel-max (perturb-and-MAP) sampling.
  
  4. Finally, I-MLE reduces to explicit maximum likelihood learning when used in some recently studied learning settings involving combinatorial optimization solvers.
     
### 3. Future Works
  The findings of this thesis have a wide range of applications that could lead to effective integration between symbolic reasoning and neural networks in many domains. Future work includes developing adaptive strategies for adapting to τ and λ, exploring potential target distributions when VzL is unavailable, and testing and integrating I-MLE into several challenging application areas.

