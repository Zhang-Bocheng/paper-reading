# Asynchronous Local-SGD Training for Language Modeling
[paper link](https://arxiv.org/pdf/2401.09135) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper focuses on the use of asynchronous local stochastic gradient descent (Local-SGD) for training language models in distributed optimisation.          |  Stochastic Gradient Descent  (SGD)      |

## Methodology

### 1. Abstract
The authors find that when using a naive implementation, asynchronous Local-SGD requires more iterations to converge, despite updating the global parameters more frequently. To address this issue, the authors propose a novel approach that utilises delayed Nesterov momentum updates and adjusts the local training steps according to the computational speed. Experimental results show that the method matches the performance of synchronised Local-SGD on the C4 dataset and significantly reduces the training time.

### 2. Method Description 
The paper proposes an optimisation strategy based on the asynchronous Local-SGD framework, aiming to solve the pseudo-gradient problem that arises in distributed optimisation. First, they use a data sampling technique to balance the learning progress and assign different learning rates to each device. Second, they devised a delayed update strategy (Delayed Nesterov) to aggregate the pseudo-gradients by applying Nesterov updates to the model parameters at intervals and using buffers between each update to achieve better convergence performance. In addition, they introduce a Dynamic Local Updates strategy (Dynamic Local Updates) that adaptively adjusts the number of training steps according to the speed of different devices to further improve performance.

![image](https://github.com/user-attachments/assets/9462cc36-ee8a-416c-b56a-8538f6cf781b)

### 3. Methodological improvements
The optimisation strategy proposed in this paper is an improvement on the original asynchronous Local-SGD framework. Specifically, they adopt a data sampling technique and a dynamic local update strategy to balance the learning progress and accelerate the convergence speed; at the same time, they introduce a delayed update strategy to solve the pseudo-gradient problem, which enables the model to accumulate information over a longer period of time, and thus better deal with unstable gradient situations.

![image](https://github.com/user-attachments/assets/c7dd1bea-b253-4b7f-b8e2-55a295e0e66c)

### 4. Issues addressed 
This thesis focuses on solving the pseudo-gradient problem that arises in distributed optimisation, i.e., the phenomenon of unstable gradients due to variability between devices and asynchronous operations. To address this problem, they propose a series of optimisation strategies, including data sampling, dynamic local update and delayed update, which effectively improve the convergence performance and stability of the model. These methods are not only applicable to deep learning tasks in large-scale distributed environments, but can also be generalised to related problems in other machine learning areas.

## Experiments
In the first paper, the authors verify the effectiveness of their own improved method DN+DyLU by comparing the effects of baseline algorithms such as asynchronous Local-SGD and synchronous DiLoCo. The experimental results show that DN+DyLU significantly reduces the perplexity and is more efficient than synchronous DiLoCo for different numbers of workers and model sizes. In addition, the authors conduct experiments with varying degrees of worker heterogeneity and find that DN+DyLU outperforms in all cases, while asynchronous DiLoCo suffers from performance fluctuations.

![image](https://github.com/user-attachments/assets/65629c64-5b0d-486f-b9cd-e98b0d75a0eb)

In the second paper, the authors compare the synchronous and asynchronous Local-SGD methods and the Finetuning method for a single worker. The experimental results show that both asynchronous Local-SGD and synchronous Local-SGD are better than the single-worker Finetuning method, especially in the late convergence phase. In addition, the authors conducted experiments with different values of c and k, and found that with a small degree of heterogeneity, a slight increase in momentum has little effect on the results.  

![image](https://github.com/user-attachments/assets/5b5ecdcf-66f7-4cf8-b474-d9d81abf4451)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper systematically explores the feasibility of asynchronous Local-SGD for language model training and proposes a novel method DN+DyLU to address some optimisation challenges in asynchronous Local-SGD.
  2. The authors used experimental data to validate the proposed DN+DyLU method and compared it with existing synchronous Local-SGD methods to demonstrate the effectiveness and superiority of the method.
 
### 2. Innovative points
  1. The DN+DyLU method effectively addresses the optimisation challenges in asynchronous Local-SGD through two techniques, delayed Nesterov momentum update and dynamic local update.
  2. The DN+DyLU method is able to improve the efficiency of asynchronous Local-SGD to approach the performance level of synchronous Local-SGD without sacrificing performance.
  3. The DN+DyLU method is a simple yet effective approach that is easy to implement and applicable to the training of various language models. 

![image](https://github.com/user-attachments/assets/a1373c8d-ecbe-45ff-9d1a-7bc0429ba46d)

### 3. Future Works
  1. Further research can be done to better utilise the advantages of asynchronous Local-SGD, such as improving the utilisation of computational resources and reducing communication costs.
  2. Combining the DN+DyLU method with other optimisation strategies can be explored to obtain better results.
  3. Extending the DN+DyLU method to other types of distributed training tasks, such as image classification and natural language processing, can be considered. 
