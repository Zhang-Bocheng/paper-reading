# AMC: AutoML for Model Compression and Acceleration on Mobile Devices
[paper link](https://arxiv.org/pdf/1802.03494) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 |  This paper proposes a new algorithm that can utilize reinforcement learning techniques to provide strategies for model compression         |  Reinforcement Learning        |

## Methodology

### 1. Abstract
  This paper introduces a new approach called AutoML for Model Compression (AMC) that utilizes reinforcement learning techniques to provide strategies for model compression. While traditional model compression techniques require manual design of rules and rules of thumb, this approach, through automation, can perform model compression more efficiently and maintain high accuracy while reducing computational resources. In conclusion, the AMC method proposed in this paper is an effective and automated model compression scheme to improve the performance of neural network models in resource-constrained environments such as mobile devices.
  
### 2. Method Description 
  The paper presents an automated model compression engine called AutoML for Model Compression (AMC). The engine uses reinforcement learning (RL) to search for the effective sparsity of each layer and implements structured pruning through channel compression.AMC aims to automatically find the redundant parts of each layer for the purpose of reducing the number of parameters and computation. They use a continuous action space instead of a discrete action space in order to control the compression rate more precisely. In addition, they used a deep deterministic policy gradient algorithm as a reinforcement learning framework.
  
### 3. Methodological improvements
  Compared to previous studies, AMC introduced the concept of continuous action space, which makes the model compression more fine-grained and accurate. In addition, authers used a deep deterministic policy gradient algorithm to control the compression rate, thus improving the exploration efficiency.
  
### 4. Issues addressed 
  The main goal of this thesis is to improve the accuracy and efficiency of model compression. In traditional methods, the sparsity of each layer needs to be specified manually, which is a time-consuming and difficult task. AMC, on the other hand, can automatically find the optimal sparsity for each layer, resulting in more efficient and accurate model compression.
  
## Experiments
  This paper presents the results of the authors' experiments using RL algorithms for model compression and compares them with other methods. Specifically, the authors conducted experiments on the CIFAR-10 dataset using two different search protocols and compared them to hand-designed rules and neural network architecture search methods. 
  
  On the ImageNet dataset, the authors used **iterative pruning and fine-tuning methods** to improve the performance of the model and compared it to existing channel reduction methods. In addition, the authors performed acceleration experiments on MobileNet and compared it with rule-based methods. 

  On the CIFAR-10 dataset, the authors used the **reward functions Rerr and RParam** for their experiments and compared the results with manually designed rules. The experimental results show that AMC can find the optimal compression strategy more accurately. The experimental results show that AMC can better explore the design space and assign sparsity. 
  
  In MobileNet acceleration experiments, the authors used **verification accuracy** as a reward signal and compared it to rule-based methods. The experimental results show that AMC can achieve higher speed and accuracy. Finally, on the object detection task, the authors used AMC to find the optimal compression strategy and obtained better performance than a hand-designed pruning method.

  Overall, this paper demonstrates that reinforcement learning algorithms can play an important role in model compression and that better performance can be obtained by exploring the design space and optimizing the reward function.
  
## Conclusion
### 1. Advantages of the Thesis
  1. A reinforcement learning-based model compression method is proposed to automatically search the design space and optimize the quality of model compression.

  2. Two novel reward schemes are designed to achieve resource-constrained compression and accuracy-guaranteed compression.

  3. Experiments are conducted on several neural networks and the method is shown to have better performance than hand-designed methods.

  4. An efficient and generalized deep neural network design engine is implemented, which can be applied to hardware resource-constrained scenarios such as mobile devices.
     
### 2. Innovative points
  1. Reinforcement learning techniques are utilized to automatically search the design space, avoiding the time-consuming and inefficient problems associated with manual design.

  2. A continuous compression ratio control strategy is designed to make the compression process more fine and controllable.

  3. Two different compression strategies are proposed for different types of AI applications.
     
### 3. Future Works
  1. Further research could be done on how to extend the method to larger neural networks and how to achieve efficient model compression on a wider range of hardware platforms.

  2. It could be explored how to combine other techniques (e.g., knowledge distillation) to improve the effectiveness of model compression.

  3. Consideration can be given to how distributed learning techniques such as federated learning can be utilized to achieve model compression without sharing raw data.
