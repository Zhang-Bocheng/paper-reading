# Deep Ensembles: A Loss Landscape Perspective
[paper link](https://arxiv.org/pdf/1912.02757) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |  This paper explores the application of deep ensembles (DEs) to improve the accuracy, uncertainty, and robustness of deep learning models to changes in data distribution.         | Deep Learning          |

## Methodology

### 1. Abstract
  The authors argue that the success of deep integration networks is not only due to their theoretical motivation based on self-sampling, but that there may be other explanations. Compared to deep integration networks, Bayesian neural networks perform poorly in practice, especially if the dataset changes. The authors propose the hypothesis that popular scalable variational Bayesian methods tend to focus on individual patterns, whereas deep integration networks tend to explore different patterns in the function space. By measuring the similarity between functions in the prediction space, the authors find that random initialization can explore completely different patterns, while functions on the optimization trajectory or within the subspace sampled from it tend to deviate significantly in the weight space. Finally, the authors evaluate the relative effectiveness of the integrated approach, the subspace approach, and the integrated subspace approach, and test their hypotheses.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/39d4d7d9-3c3c-48c3-875d-bfaab385e14c)

## Experiments
  This paper presents experiments on the comparison of random initialization and subspace methods in DL. The authors conducted experiments using different architectures and datasets, and the results are analyzed and discussed in detail.

In the experiments, the authors first explored the similarities between random initialization and subspace methods. They computed the similarities in the weights and function spaces on different training trajectories and observed that these similarities increased with training. In addition, they compare the differences between the functions under different initial conditions and find that these functions remain relatively stable throughout the training process.

Next, the authors investigate how multiple solutions can be explored through subspace methods. They used four different subspace sampling methods (Monte Carlo dropout, Gaussian approximation, low-rank Gaussian approximation, and stochastic subspace approximation) to generate new solutions and compared them to the results from random initialization. The results show that these subspace methods can provide more accurate and diverse solutions, but they are still not comparable to independent random initialization.

Finally, the authors compare the effectiveness of the subspace methods with the integrated methods. They compare different variants of each method and find that in some cases the subspace methods provide better accuracy, while in other cases the integrated methods perform better. Overall, the authors concluded that the two methods have complementary strengths, providing a balance between uncertainty and accuracy.

## Conclusion

### 1. Advantages of the Thesis
  This paper experimentally validate that randomly initialized neural networks explore different patterns in the function space, and explain why deep integration models using only random initialization perform well in practice. <br> The authors also propose some interesting research directions, such as delving into the effect of random initialization on the training dynamics and exploring methods that are more diverse than deep integration models.
  
### 2. Innovative points
  1. The main contribution of this paper is to explore the diversity of randomly initialized neural networks in function space and to propose a corresponding experimental approach to test this hypothesis.
  
  2. In addition, the article introduces some common methods for approximating Bayesian neural networks and compares their performance differences with deeply integrated models.

### 3. Future Works
  1. This model can further explore how to use this diversity information to improve the generalization ability and robustness of models.
  
  2.  In addition, these methods can be applied to other types of machine learning problems to expand their applications.
