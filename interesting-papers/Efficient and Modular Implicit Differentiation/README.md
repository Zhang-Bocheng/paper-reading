# Efficient and Modular Implicit Differentiation
[paper link](https://arxiv.org/pdf/2105.15183) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new method called automatic implicit differentiation (AID) for solving the derivation problem in optimization problems.         | Mathematical Foundation         |

## Methodology
  The method allows for efficient implicit differentiation by combining user-defined functions with automatic differentiation techniques, and is scalable and flexible. The authors demonstrate the effectiveness of this method in applications such as multilevel optimization and molecular dynamics analysis.
  
## Experiments
  This paper describes the application of automatic implicit differentiation (implicit differentiation) to ML and demonstrates the advantages and applicability of the method through several experiments. The main experiments include:

  1. Hyperparametric optimization problems are solved using automatic implicit differentiation by combining gradient descent fixed points with backpropagation;
  
  2. For the dataset distillation problem, solving the training model using automatic implicit differentiation;
  
  3. For the molecular dynamics simulation problem, the energy function was solved using automatic implicit differentiation.

     ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/6b523f1d-1b96-4d16-818f-58e5b7eb2c5c)

In these experiments, the authors used different optimization algorithms to solve these problems, such as gradient descent and projected gradient method. By comparing the results of different algorithms, the authors demonstrate that automatic implicit differentiation can improve computational efficiency and reduce errors.

## Conclusion

### 1. Advantages of the Thesis
 1. This paper presents an approach to automatic implicit differentiation that allows the user to express optimality conditions for optimization problems directly in Python and can be applied to a large number of optimality conditions.
 
 2. This approach avoids the problem of reimplementing the algorithm and using an autodiff system, and also allows the use of existing state-of-the-art software to improve efficiency.
 
 3. In addition, the approach lowers the technical barrier to using implicit differentiation, making it easier for users to use implicit differentiation by abstracting low-level details through seamless JAX integration.

### 2. Innovative points
  The main contribution of this paper is to present a generalized framework for adding implicit differentiation to any existing solver. The user only needs to define a mapping function F to capture the optimality conditions of the problem, and then use the implicit function theorem and autodiff to automatically differentiate the solution of the problem. This approach not only saves time but also reduces the effort of manual derivation.
  
### 3. Future Works
  1. Future research directions include further extending the method to support more types of optimization problems, as well as using it in conjunction with other optimization techniques, such as evolutionary algorithms.
  
  2. In addition, the method needs to be investigated in greater depth to deal with multi-objective optimization problems.

