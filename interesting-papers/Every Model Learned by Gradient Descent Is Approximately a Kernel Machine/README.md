# Every Model Learned by Gradient Descent Is Approximately a Kernel Machine
[paper link](https://arxiv.org/pdf/2012.00152) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper explores the relationship between gradient descent algorithms and kernel methods in deep learning.           | Machine Learning          |

## Methodology

  The authors show that deep networks trained by standard gradient descent algorithms can actually be approximated as kernel function-based machine learning models, which directly memorize data and make predictions using a similarity function (i.e., a kernel). This finding enhances the interpretability of deep network weights and reveals that they are actually superimpositions of training examples. In addition, the paper mentions the concept of neural tensor kernels, which incorporate knowledge of the objective function into the kernel and helps to better understand the learning process of deep networks.

   ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/43da1795-53b0-4c0b-bf84-8bceb8b25312)

## Experiments
  This paper focuses on the authors' comparative experiments to explore the issue of interpretability of DL models and to propose a new method, Path Kernels, for analyzing and explaining the behavior of DL models. Specifically, the authors conducted the following two comparative experiments:

The first experiment compares the effects of using a traditional feature engineering-based approach and using the Path Kernels method to classify the same dataset. The authors conducted experiments on the MNIST handwritten digits dataset, and the results show that using the Path Kernels method yields better classification results and better explains the behavior of the model.

The second experiment compares the effect of regression on the same dataset using a traditional feature engineering based approach and using the Path Kernels method. The authors conducted experiments on the Boston Housing dataset and showed that using the Path Kernels method gives better regression results and can better explain the behavior of the model.

For both experiments, the authors used the mean square error (MSE) as an evaluation metric and compared the performance of the two methods. The results show that using the Path Kernels method can improve the performance of the model to some extent and can better explain the behavior of the model.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new perspective on deep learning models, i.e., as path-kernel machines, and explores the implications of this perspective for interpretability and scalability.
 
  2. The paper demonstrates experimentally that deep networks and kernel machines are different in mathematical expression but very similar in actual performance, which provides new ideas for deep learning research.
  
  3. The paper also proposes the use of path kernels to construct more flexible kernel functions, which can improve the performance of the model by applying existing knowledge directly to the kernel function.
     
### 2. Innovative points
  1. The paper presents the idea that DNNs are path kernel machines, which is a fresh perspective on how deep learning models work.
  
  2. The paper proposes ways to build more flexible kernel functions using path kernels, which can directly utilize existing knowledge to improve the performance of the model.
  
  3. The paper also explores how the idea of path kernels can be applied to other areas of machine learning, such as probabilistic models and non-convex optimization problems.
     
### 3. Future Works
  1. The ideas and methods presented in the paper provide a new direction for deep learning research that can further explore the nature and workings of deep learning models.
  
  2. Research can continue to investigate how path kernels can be used to build more flexible and efficient kernel functions, and how they can be applied to a wider range of machine learning tasks.
  
  3. It is also possible to explore how the idea of path kernels can be combined with other machine learning techniques, such as reinforcement learning and transfer learning, to achieve better performance and results.
