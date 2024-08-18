# Supermasks in Superposition
[paper link](https://arxiv.org/pdf/2006.14769) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a model called Supermasks in Superposition (SupSup), which is capable of learning thousands of tasks sequentially without catastrophic forgetting.         |  Neural Network         |

## Methodology

### 1. Abstract
The method uses a randomly initialized, fixed base network and finds a subnetwork (supermask) for each task to achieve good performance. If the task identity is provided at test time, the correct subnetwork can be retrieved with minimal memory usage. If the task identity information is not provided, SupSup can minimize the output entropy by linearly stacking the learned supermasks by inferring tasks based on gradient optimization. The authors find that, in practice, only one gradient step is needed to identify the correct mask, even with 2,500 tasks. 

In addition, the authors show two promising extensions: the SupSup models can be fully trained without providing information about the task identities, since they can detect uncertainty about new data and assign additional supermasks to new training distributions; and the entire growing set of supermasks can be stored in a constant-sized pool by implicitly storing them implicitly as attractors in a fixed-size Hopfield network.

### 2. Method Description 
The SupSup method proposed in this paper is a super mask (supermask) based method for learning thousands of sequential tasks without forgetting previous tasks. The method uses supermasks to learn a sub-network for each task and reassigns new supermasks when needed to handle unknown tasks. Specifically, the SupSup method includes the following steps:

  1. Given the task identity information, train a binary mask (supermask) for fixing the weights to initial values and keeping them constant.
  
  2. For each new task, a new supermask can be randomly initialized or the average of all known supermasks can be used.
  
  3. In the inference phase, the corresponding supermask is computed from the input data and applied to the neural network with fixed weights to obtain the output probability distribution.

![image](https://github.com/user-attachments/assets/9b16c310-6a29-4eba-8eaa-ffc83c527341)

### 3. Methodological improvements
The main advantage of this approach is that instead of storing the full model for each task, only the supermask for each task needs to be stored. In addition, the SupSup method can improve performance by introducing an entropy maximization strategy for the supermasks.

![image](https://github.com/user-attachments/assets/37830f3f-8d2d-4862-9035-8cec67b987af)

### 4. Issues addressed 
The SupSup method mainly solves the problem that traditional classifiers cannot handle a large number of tasks simultaneously. By using super masks, SupSup can learn thousands of sequential tasks without forgetting the previous tasks. This makes SupSup a powerful tool for large-scale multi-task learning.

## Experiments
This paper presents four different experiments to verify the performance of the SupSup algorithm in different scenarios. Specifically, the four experiments are:

Experiment 1: **Task identity information given the training and inference phases (Scenario GG)**. In this experiment, the authors used two datasets, SplitCIFAR100 and SplitImageNet, and two models, ResNet-18 and ResNet-50, to conduct the experiment. The experimental results show that the SupSup algorithm can effectively learn multiple tasks without storing the base model W and can successfully perform task recognition of a single image with the One-Shot algorithm.

Experiment 2: Providing task identity information only during training (Scenarios GNs & GNu). In this experiment, the authors used three datasets, PermutedMNIST, RotatedMNIST and SplitMNIST, and two models, LeNet 300-100 and FC 1024-1024, for the experiment. The experimental results show that the SupSup algorithm can learn thousands of tasks without accessing the task identity information and can successfully perform task recognition on a single image with the One-Shot algorithm.

![image](https://github.com/user-attachments/assets/e906d64a-bacf-4358-9798-dbc79fb42d1e)

Experiment 3: Providing task identity information only at the time of inference (Scenario NNs). In this experiment, the authors used PermutedMNIST, a dataset, and used LeNet 300-100, a model, for the experiment. The experimental results show that the SupSup algorithm can still learn thousands of tasks even without any task identity information.

![image](https://github.com/user-attachments/assets/88a2e148-b5be-49e8-a70d-88d423522900)

Experiment 4: Comparing the performance of different methods. In this experiment, the authors compare the SupSup algorithm with other methods such as PSP, BatchE, Online EWC and SI. The experimental results show that the SupSup algorithm performs well in all situations and has better performance than the other methods.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a flexible and attractive model called “Supermasks in Superposition (SupSup)” for various scenarios in continuous learning.
  
  2. The model exploits the power of sub-networks and gradient-based optimization to infer the identity of unknown tasks and achieve state-of-the-art performance given the task identity.
  
  3. In addition, the model is able to handle thousands of alignments and virtually indistinguishable rotations of the MNIST dataset without task information, providing strong adaptability and generalization capabilities.

### 2. Innovative points
The core idea of the SupSup model is to superimpose a randomly weighted neural network with a binary mask to create sub-networks. When the identity of a task is unknown, SupSup can infer it as a gradient optimization problem to select the correct supermask. This approach can learn multiple tasks without forgetting previous tasks and is flexible and scalable. 

### 3. Future Works
  1. Therefore, future directions for exploration include automatically inferring task identities using more calibrated models and bypassing calibration challenges through optimization objectives such as self-supervised and energy-based models.
  
  2. Further research is also needed to address large scales and to ensure that models do not introduce harmful biases or intentions.
