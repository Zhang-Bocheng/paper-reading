# Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention
[paper link](https://arxiv.org/pdf/2006.16236) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper describes a new method that accelerates the processing of long sequences by transforming the self-attention operation into the form of a linear inner product and reducing its complexity from O(N^2) to O(N) using the union law of matrix multiplication.         | Transformer          |

## Methodology

### 1. Abstract
The method is called ‘linear transformer’, which is related to recurrent neural networks (CNN). Experimental results show that the linear transformer is 4000 times faster than a conventional transformer in predicting very long sequences, and has comparable performance to a conventional transformer. This work provides an effective new idea for solving the long sequence processing problem.

### 2. Method Description 
This thesis presents a new linear transformer model for processing sequential data. While the traditional softmax attention mechanism has high computational complexity and memory requirements, the linearised attention mechanism significantly reduces these costs and allows for greater efficiency in training and inference.

![image](https://github.com/user-attachments/assets/c003b1f5-f0f0-4ff7-af6e-d4dbef12c8b3)

### 3. Methodological improvements
The main contribution of this thesis is the proposal of a linearised attention mechanism that converts traditional softmax attention into a linear form by using a specific feature mapping function. This linearised attention mechanism results in a significant reduction in both computational complexity and memory requirements. In addition, the paper introduces a causal masking technique to ensure that only previous inputs are considered during inference, which further improves inference speed.

### 4. Issues addressed 
The linear transformer model proposed in this thesis solves the problems of high computational complexity and high memory requirements of the traditional softmax attention mechanism, while maintaining high accuracy and performance. This makes the model suitable for processing large-scale sequence data and enables higher efficiency in training and inference.

## Experiments
This paper focuses on the results of the authors' experiments using the Linear Transformer in two real-world applications and compares them with the standard softmax attention and Reformer accelerators. The experiments consisted of four parts:

<br>&emsp;Experiment 1: Performance analysis of Linearised Attention, which examines the convergence, memory requirements and computation time of Linearised Attention by replicating the task;
<br>&emsp;Experiment 2: MNIST image generation task, comparing the performance of the linear transformer with softmax and Reformer in terms of image generation speed and quality;
![image](https://github.com/user-attachments/assets/6bba3311-8429-4181-b236-46fa310b012b)

<br>&emsp;Experiment 3: CIFAR-10 image generation task to further demonstrate the advantages of linear transformers;
![image](https://github.com/user-attachments/assets/a91c061a-88f0-4451-953c-ec02abe796b3)

<br>&emsp;Experiment 4: automatic speech recognition task, comparing the performance of linear transformers with LSTM and Reformer. 

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new model, the Linear Transformer, which significantly reduces the memory and computational costs of the original transformer model and is able to handle longer sequence lengths.
  
  2. The model achieves linear complexity in terms of time and memory by using the associatable nature of matrix multiplication to compute self-attention weights.
  
  3. In addition, the model can be used with causal masks, maintaining its linear asymptotic complexity.
  
  4. Finally, expressing the transformer model in the form of a RNN allows for faster inference on autoregressive tasks.

  5. This research has important implications for the study of storing and retrieving information, as well as exploring methods for linear attention selection feature mapping, such as approximating a radial basis function kernel using stochastic Fourier features in order to pre-train the softmax attention model.

### 2. Innovative points
  1. The main contribution of this thesis is the proposal of a linear transformer model, which allows for linear complexity by using the associatable nature of matrix multiplication to compute self-attention weights.
  
  2. In addition, the model can be used with causal masks to maintain its linear asymptotic complexity. This correlation reveals the link between the transformer model and the RNN, allowing for faster autoregressive inference.
     
### 3. Future Works
Future research directions include how to optimise linear attention selection feature mapping and how to apply it to other natural language processing tasks. It is also possible to explore how to combine linear transformer models with other models for better performance and efficiency. 
