# A Distributed Data-Parallel PyTorch Implementation of the Distributed Shampoo Optimizer for Training Neural Networks At-Scale
[paper link](https://arxiv.org/pdf/2309.06497) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes an online and stochastic optimisation algorithm called Shampoo, belonging to the AdaGrad family of methods for training neural networks.          |  Neural Networks        |

## Methodology

### 1. Abstract
The algorithm is implemented by constructing a block diagonal preprocessor and using a rough Kronecker product approximation on each parameter to compute the full matrix AdaGrad. The authors provide a full description of the algorithm as well as their implementation of performance optimisation in PyTorch. Their implementation leverages PyTorch's DTensor data structure to distribute the memory and computation for each parameter and performs the AllGather basic operation at each iteration. This important performance enhancement allows them to perform large-scale deep network training with up to 10% reduction in single-step elapsed time compared to standard diagonal scaling-based adaptive gradient methods. The authors validate their implementation through training experiments on ImageNet ResNet50 and demonstrate the advantages of Shampoo over standard training recipes, requiring very little hyperparameter tuning.

### 2. Method Description 
The Shampoo algorithm proposed in this paper is an optimiser based on a distributed data-parallel PyTorch implementation for training Neural Network models. The algorithm reduces computation and memory footprint by representing the neural network structure using a list of parameters and constructing a block preprocessing matrix. The algorithm also employs an inter-layer learning rate migration strategy to improve convergence speed and performance.

![image](https://github.com/user-attachments/assets/a5e31dff-68b8-4118-8b7e-b8c9ead46250)

Translated with DeepL.com (free version)
### 3. Methodological improvements
  1. **Better convergence and generalisation**: the Shampoo algorithm can effectively reduce the overfitting phenomenon, thus improving the generalisation ability of the model and convergence speed.
  
  2. **Better efficiency and scalability**: Shampoo algorithm can perform efficient computation through distributed data parallelism, thus improving the training efficiency and scalability of the model.
  
  3. **Better adaptability**: Shampoo algorithm can be adaptively adjusted according to different tasks and model characteristics, so as to better meet the actual needs.

### 4. Issues addressed 
  1. When training large deep neural networks, due to the large number of parameters, the traditional gradient descent method is prone to fall into local optimal solutions, resulting in poor model performance.
  
  2. In a distributed environment, the traditional gradient descent method is difficult to perform parallel computation efficiently due to high communication and synchronisation costs.
  
  3. Different tasks and model characteristics require different optimisation strategies, and the traditional gradient descent method cannot flexibly cope with the demands of different scenarios.

## Experiments
This paper describes the authors' performance optimization of the distributed Shampoo optimiser for distributed data-parallel PyTorch implementations and experiments on the ImageNet-1k dataset. Specifically, they compare the distributed Shampoo optimiser with the standard benchmark SGD+Nesterov accelerator through the following three experiments:

For the **experiments with a fixed training budget of 90 epochs**, the authors used an experiment with a fixed training budget of 90 epochs to demonstrate the advantages of the distributed Shampoo optimiser over the standard benchmark SGD+Nesterov accelerator. The experimental results show that the distributed Shampoo optimiser provides better verification accuracy with the same training budget, while reducing the number of iterations and training time. In addition, the distributed Shampoo optimiser reduces the volatility of the validation error, making the model more robust.

![image](https://github.com/user-attachments/assets/7adfb049-bd9c-477a-bf83-6038549d2b0e)

For the **experiments that achieve the target verification accuracy without being limited by the training epoch**, the authors show that the distributed Shampoo optimiser can achieve the same validation accuracy for different numbers of training epochs, thus demonstrating that it has faster convergence and shorter training time. The experimental results show that the distributed Shampoo optimiser is about 1.5 times faster in steps and 1.35 times faster in time than the standard benchmark SGD+Nesterov accelerator.

![image](https://github.com/user-attachments/assets/b636b3bb-b322-49a8-a4e8-1faac14eccf9)

For the **experiments that are sensitive to the learning rate**, the authors investigated the sensitivity of the distributed Shampoo optimiser and the standard benchmark SGD+Nesterov accelerator to different learning rates. The experimental results show that the distributed Shampoo optimiser performs better over the range of learning rates tested, but further research is still needed to improve its robustness to hyperparameter selection.

![image](https://github.com/user-attachments/assets/c7298ebd-6dda-41d3-bdfa-56f6631ccbb3)
 
  
