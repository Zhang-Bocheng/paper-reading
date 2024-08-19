# TASO: Time and Space Optimization for Memory-Constrained DNN Inference
[paper link](https://arxiv.org/pdf/2005.10709) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a temporal and spatial optimization method called TASO for deep neural network (DNN) inference in memory-constrained situations.          | Deep Neural Network         |

## Methodology

### 1. Abstract
Since large networks often require large amounts of computing resources, the use of CNN models can become very expensive for embedded applications with tight memory and energy budgets, such as mobile devices. To solve this problem, the authors propose a domain-specific optimization method based on integer linear programming (ILP) for selecting the basic operations to implement the convolutional layer and optimizing the trade-off between time and space by minimizing the execution time of the entire network and allocating appropriate workspace. 

The method can be run on any platform that supports the C compiler, and multiple popular ImageNet neural architectures were evaluated on the ARM Cortex-A15, and the results showed an 8x increase in speed, a 2.2x reduction in memory requirements, and a sacrifice of only 15% in inference time compared to a choice based on greedy algorithms. In addition, the optimization method exposes a series of best advantages under different configurations, which can be used for memory and latency trade-offs under arbitrary system constraints.

### 2. Method Description 
This paper proposes an Integer Linear Programming (ILP)-based approach to configure DNNs to achieve optimal inference time and meet memory constraints. Traditional DNNs can be seen as graphs made up of many layers, where convolutional layers take up a lot of execution time and memory. Each convolutional layer can be implemented using one of a set of candidate primitives, each with its own execution time, input and output data conversion costs, and memory requirements.

Previous work has shown that Partitioned Boolean Quadratic Programming (PBQP) effectively minimizes the execution time of CNNs by selecting the optimal primitive for each layer. However, this approach does not take into account memory requirements and does not set a maximum memory budget. This is important for embedded devices with limited memory. Therefore, this paper proposes a new approach that optimizes both memory budget and execution time, which is a more difficult problem.

![image](https://github.com/user-attachments/assets/494773d1-8bd8-491b-9a13-6e56f3caa15d)

Methodological improvements


Problem solved

### 3. Methodological improvements
The ILP model proposed in this paper transforms the DNN configuration problem into a problem of solving the optimal sequence of primitives to meet the given memory and execution time budget. The decision variable is represented as a vector, where each element corresponds to a primitive used in a layer. The objective function includes two metrics: **execution time and memory usage**. Constraints include limits on total execution time and memory budgets. In addition, the cost of data layout transformations is taken into account, which can affect execution time and memory usage.

### 4. Issues addressed 
The ILP method proposed in this paper solves the following problems:

<br>&emsp;How to select the optimal primitive sequence while meeting the memory and execution time budget.
<br>&emsp;How to balance the trade-offs between execution time and memory usage.
<br>&emsp;How to consider the cost of data layout transformation to get more accurate results.

In conclusion, the method proposed in this paper provides an effective solution to the DNN configuration problem, which can help DNN inference tasks in resource-constrained environments such as embedded devices.

## Experiments
In this paper, the method of optimizing the performance and memory footprint of deep learning models using integer linear programming (ILP) is introduced, and verified by experiments. Specifically, the authors implement two different optimization strategies: network-wide performance optimization and interlayer optimization. In the network-wide performance optimization, the authors used ILP to find the optimal convolutional operator selection scheme to meet the given memory budget and execution time constraints. In interlayer optimization, the authors used ILP to determine the optimal combination of convolution operators to use for each layer in order to maximize memory utilization. 

![image](https://github.com/user-attachments/assets/2c7ec13d-78d1-4592-99a4-67b588224d49)

The authors used five popular deep learning models (AlexNet, VGG, GoogLeNet, ResNet, and SqueezeNet) for experiments and Intel Core i5 CPUs as the target devices. Experimental results show that the ILP method proposed by the authors can effectively balance the relationship between performance and memory footprint, and can achieve better performance on various hardware platforms. In addition, the authors compare the effects of the ILP method with other methods such as PBQP and greedy algorithms, and demonstrate the advantages of the ILP method.

![image](https://github.com/user-attachments/assets/519c9233-49b8-451a-bd7f-11da60b811cd)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes an integer linear programming (ILP)-based CNN optimizer that aims to solve the resource constraints faced when running large DL models on mobile and embedded devices.
  
  2. The optimizer is able to select algorithms, implementations, and data layouts based on the needs of each convolutional layer to optimize inference latency and memory footprint.
  
  3. Experimental results show that the optimizer performs better than the greedy algorithm and the solver considering only performance when the inference time and memory usage budget are met.

### 2. Innovative points
The main contribution of this paper is to propose a CNN optimizer based on ILP, and define two optimization strategies: one is to **enhance the performance of the whole network**, and the other is to **optimize layer by layer under memory constraints**. In addition, the optimizer introduces a workspace that reuses data from each layer, making it possible for even the smallest memory size to perform operations on at least one convolutional layer. These innovations provide new ideas and solutions to solve the problem of running large DL models on mobile and embedded devices. 

### 3. Future Works
Future research directions include improving the performance and scalability of optimizers, exploring more optimization strategies and technologies, and applying them to a wider range of application scenarios.    
