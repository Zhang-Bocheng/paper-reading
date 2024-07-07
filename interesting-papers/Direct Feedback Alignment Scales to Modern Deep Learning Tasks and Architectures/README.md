# Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures
[paper link](https://arxiv.org/pdf/2006.12878.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores the problems with backpropagation algorithms commonly used in deep learning and proposes direct feedback alignment (DFA) as an alternative.         |  Deep Learning         |

## Methodology

### 1. Abstract
  Unlike traditional backpropagation, DFA does not require weight passing and therefore can parallelize the training process more efficiently. The authors demonstrate the applicability of DFA in modern DL tasks and architectures by applying it to a variety of domains such as neural image synthesis, recommender systems, geometry learning, and NLP. While the gap between DFA and backpropagation is large in some complex architectures, such as Transformer, the authors argue that this requires a rethinking of common practices for large and complex architectures. In conclusion, this paper provides new ideas and approaches for deep learning.
  
### 2. Method Description 
  The paper proposes two methods to optimize weight updates in NN: backpropagation (BP) and the fast gradient descent algorithm (DFA). In BP, the error vector is backpropagated to compute the contribution of each neuron and the weights are updated based on their impact on the cost function. Whereas, in DFA, the weights are updated by replacing the weights with the topmost derivatives of a stochastically projected loss function, thus avoiding the synaptic asymmetry problem.
  
### 3. Key concepts
  _Backpropagation algorithm_: A supervised learning technique used for training artificial NN. It is essential for adjusting the weights of the network to minimize the error between the predicted output and the actual output. Backpropagation stands for "backward propagation of errors," reflecting the process of propagating the error gradient backward through the network to update the weights.
  
### 4. Methodological improvements
  Compared with traditional BP, DFA achieves faster weight updates by using random matrices and can reduce training time. In addition, DFA can be applied to more complex NN structures such as CNN and RNN.
  
### 5. Issues addressed 
  The training process of NN usually requires a lot of time and computational resources. DFA can improve the training efficiency of NN as it accelerates the weight update and reduces the training time by using random matrices. In addition, DFA can also deal with synaptic asymmetry, which helps to improve the performance of NN.
  
## Experiments
  This paper presents the performance of deep backpropagation (DFA) in different application scenarios and compares it with traditional backpropagation algorithms. The experiment consists of three parts:

In the **neuroradiometric field synthesis task**, a neuroradiometric field (NeRF) network is used to generate high-quality 3D scene rendering images. The experimental results show that the NeRF model trained using DFA has better performance in complex scenes, approaching or even exceeding the model trained using the traditional BP algorithm.

In the **recommender system task**, several different ML methods, such as DeepFM and DCN, are used to improve the accuracy of click-through rate prediction. The experimental results show that the model trained using DFA can achieve a comparable level of performance to the BP algorithm and is better able to handle large-scale datasets.

In the **geometry learning task**, Graph Convolutional Neural Network (GCNN) was used to process complex non-Euclidean graph-structured data. Experimental results show that the GCNN model trained using DFA can achieve good performance without using weight transfer and can be applied to different graph convolution operations and attention mechanisms.

## Conclusion

### 1. Advantages of the Thesis
  1. This study is the first experimental validation of DFA as an effective training method for a wide range of challenging tasks and NN architectures.
  
  2. The study broadens the scope of DFA applications and provides new insights into alternative training techniques to BP.
  
  3. The study considers current deep learning trends as well as attractive technical mechanisms (e.g., graph convolution and attention) and demonstrates the potential impact of each application.
     
### 2. Innovative points
  1. DFA is able to parallelize the backpropagation process and place individual operations at the core of the training process, thus promising to reduce the power consumption of the training chip by an order of magnitude.
  
  2. The use of DFA reduces the dependence on upstream layers, making parallelization easier.
  
  3. DFA does not require weight transfer, which makes it more compatible with bioheuristics.

### 3. Future Works
  1. Further research should continue to demonstrate the use of DFAs in novel areas as they are discovered requiring new perspectives.

  2. More knowledge is needed on how to train models and the behavior of the models after training to better understand the impact of DFAs.
  
  3. Alternative training methods for DFAs need to be cross-checked in order to safely scale DFAs and respond to demand.
  
  4. Biologically inspired methods are a more important research direction, but their long-term impact is difficult to estimate. Therefore, the possibilities of these approaches need to be further explored.

