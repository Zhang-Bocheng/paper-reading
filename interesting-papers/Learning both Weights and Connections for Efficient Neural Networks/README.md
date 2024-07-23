# Learning both Weights and Connections for Efficient Neural Networks
[paper link](https://arxiv.org/pdf/1506.02626) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2015 | This paper describes a new approach to neural networks that can reduce the space required for storage and computation by an order of magnitude without compromising their accuracy.           | Neural Networks         |

## Methodology

### 1. Abstract
Conventional neural networks have their architecture determined before training, so it is not possible to improve the architecture through training. The method accomplishes this by learning important connections and pruning redundant ones. Experimental results show that on the ImageNet dataset, the method reduces the number of AlexNet parameters by a factor of 9 and the number of VGG-16 parameters by a factor of 13 without loss of accuracy.

### 2. Method Description 
The paper proposes a new network pruning method, which is divided into three main steps: firstly, the importance of connections is learned through normal training; secondly, the dense network is converted into a sparse network by removing low-weight connections according to a threshold; and finally, the remaining sparse connections are re-trained to learn the final weights. 

![image](https://github.com/user-attachments/assets/319cae8b-f52a-4a91-8e3c-4bda8a29dbdd)

In these steps, choosing the correct regularization and adjusting the dropout ratio are crucial to improve the pruning results. In addition, retaining the weights from the original training phase during retraining reduces the computational effort and avoids the gradient vanishing problem. Finally, pruning iteratively can further improve the pruning rate.

### 3. Methodological improvements
The main improvement of this method is the use of iterative pruning to find the optimal number of connections. Meanwhile, the gradient vanishing problem can be effectively prevented by retaining the weights from the original training stage and retraining only the FC or CONV layers. In addition, a neuron-specific pruning method is proposed, which can significantly improve the pruning rate without loss of accuracy.

### 4. Issues addressed 
The method solves some problems of traditional pruning methods, such as excessive computational cost and difficulty in recovering pruning errors. By iteratively pruning and retaining the weights from the original training phase, the method can effectively reduce the computational cost and avoid the gradient vanishing problem. In addition, the pruning rate can be significantly improved by the neuron-specific pruning method. 

## Experiments
  This paper presents four sets of experiments aimed at exploring the effects of network pruning on different DL models. Specifically, the authors used the Caffe framework to prune LeNet-300-100 and LeNet-5, and to prune AlexNet and VGG-16. The experimental results show that pruning can significantly reduce network parameters and computation while maintaining accuracy.

The first set of experiments is **the pruning of LeNet-300-100 and LeNet-5 on the MNIST dataset**. The experimental results show that the error rate of LeNet-300-100 is reduced from 1.6% to 1.8% after pruning, while the error rate of LeNet-5 is reduced from 0.8% to 0.9%. In addition, pruning reduces the number of network parameters by a factor of 12 and the amount of computation by a factor of 6.

The second set of experiments is **the pruning of AlexNet on the ImageNet dataset**. The experimental results show that pruning reduces the number of parameters of AlexNet by about 90% and the amount of computation by about 3 times, but the accuracy is not affected.

The third set of experiments is also **the pruning of VGG-16 on the ImageNet dataset**. The experimental results show that the number of parameters of VGG-16 is reduced by about 93% after pruning, the amount of computation is reduced by about 7.5 times, and both of the two largest fully connected layers can be pruned to less than 4% of the original.

![image](https://github.com/user-attachments/assets/25c40aaa-ab69-430f-80ee-e64f1b86f372)

![image](https://github.com/user-attachments/assets/e3798c54-b627-4d54-a1f3-8370e31515f8)

## Conclusion

### 1. Advantages of the Thesis
  This paper proposes a new NN parameter reduction method that improves energy efficiency and storage space by learning which connections are important, then pruning away unimportant connections and retraining the remaining sparse network without compromising accuracy. 
  
  In addition, this paper details various details and techniques used during the experiments, including how to select thresholds, how to store sparse matrices, and how to use techniques such as L1 and L2 regularization to improve accuracy and performance. These techniques are also informative for other research on model compression and acceleration.

  ![image](https://github.com/user-attachments/assets/6c9431d3-03a8-4bc4-b0cf-c950a8991747)

### 2. Innovative points
 1. The method borrows from the mammalian brain by learning the importance of the connections, then pruning away the unimportant ones, and finally retraining the remaining sparse network. 
 
 2. This approach not only reduces the number of connections, but also improves energy efficiency and storage space without compromising accuracy.
 
 3.In addition, the authors also propose the technique of iterative pruning, which can further reduce the number of connections while maintaining accuracy, which is very useful for practical applications.

### 3. Future Works
How to reduce the model size and computational effort while maintaining accuracy has become an important research direction. The pruning method proposed in this paper provides an effective way to solve this problem. Future research can be carried out in the following aspects: 

(1) exploring more efficient pruning algorithms; 

(2) combining other model compression techniques, such as quantization and low-rank decomposition, in order to obtain better results; 

(3) investigating how to maintain the interpretability and stability of the model during the pruning process.
