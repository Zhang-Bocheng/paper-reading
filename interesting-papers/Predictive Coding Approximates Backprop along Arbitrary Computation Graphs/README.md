# Predictive Coding Approximates Backprop along Arbitrary Computation Graphs
[paper link](https://arxiv.org/pdf/2006.04182) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This thesis presents a backpropagation algorithm (backprop) for approximating the backpropagation of errors on arbitrary computational graphs based on a biologically realizable theory of computation, predictive coding.         | Backpropagation Algorithm          |

## Methodology

The method makes use of the concept of automatic differentiation, which allows any differentiable program to be optimized by locally learned rules. The authors use the method to construct predictive coding CNNs, RNNs, and LSTM models that are equivalent to standard ML architectures, and demonstrate performance comparable to standard ML algorithms in challenging ML benchmark tests. This approach offers the potential for the possibility of implementing standard ML algorithms directly into neural circuits and may contribute to the development of fully distributed neuromorphology architectures.

![image](https://github.com/user-attachments/assets/bc7f5f0f-6580-4aa2-949c-5061f524494d)

## Experiments
This paper focuses on the use of predictive coding algorithms to approximate the gradient, and experimentally demonstrates the correctness and effectiveness of the method. Specifically, the authors conducted the following three comparison experiments:

The first experiment **tests the performance of the predictive coding algorithm and the automatic differentiation algorithm on a simple scalar function**. The authors set a target value and computed the gradient of the input values, and the results showed that the predictive coding algorithm was able to quickly converge to the correct numerical gradient and could handle very high learning rates without divergence.

The second experiment was to **apply the predictive coding algorithm to CNNs, RNNs and LSTMs and compare it with the backpropagation algorithm**. The authors tested the performance of these models on datasets such as SVHN, CIFAR10 and CIFAR100 and found that they performed as well as or better than the backpropagation algorithm. In addition, the gradients of the predictive coding algorithms were close to the true numerical gradients.

The third experiment was to **apply the predictive coding algorithms to RNNs and LSTMs**. The authors trained a character-level name categorization task and a next character prediction task on the full Shakespeare set and compared them to a backpropagation algorithm. The results show that the predictive coding algorithm converges equally fast to the correct numerical gradient and can handle deep RNN.  

![image](https://github.com/user-attachments/assets/8d724b6e-f03c-42e7-b5e3-2b3649102e02)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a predictive coding-based backpropagation algorithm that can be used for ML architectures in arbitrary deep computational graphs with fast convergence and high parallelism.
  
  2. The algorithm is closer to the workings of biological neural networks than traditional backpropagation, and thus may be more compatible with the way the brain works.
  
  3. In addition, the algorithm enables backpropagation of any computational graph by using local learning rules, which opens up possibilities for future automatic translation to neuromorphic hardware.

### 2. Innovative points
  1. The predictive coding based backpropagation algorithm proposed in this paper is a new ML framework that allows backpropagation of any computational graph by using local learning rules.
  
  2. The advantages of this algorithm are that it better mimics the way biological neural networks work and has fast convergence and high parallelism. In addition, the algorithm provides a new way to handle the case of different noisy inputs.
     
### 3. Future Works
Since this paper presents generalized theoretical results, it should be relatively easy to extend it to more complex ML architectures such as ResNets, GANs, and Transformers. In addition, the authors believe that the implementation of the algorithm on neuromorphic hardware may improve its efficiency and allow for better handling of continuously varying inputs. 
