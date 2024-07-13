# High-Performance Large-Scale Image Recognition Without Normalization
[paper link](https://arxiv.org/pdf/2102.06171) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores methods for high-accuracy large-scale image recognition without the use of batch normalization.        |  Deep Neural Networks (DNN)         |

## Methodology

### 1. Abstract
   While recent research has successfully trained deep ResNet models without the need for a batch normalization layer, these models typically do not test as accurately as the best batch normalized networks and are often unstable for large learning rates or strong data augmentation. The authors developed an adaptive gradient truncation technique that overcomes these instabilities and designed a significantly improved class of unnormalized ResNet. 
   
   Their smaller model is comparable to EfficientNet-B7's test accuracy on ImageNet, but trains 8.7 times faster and the largest model achieves a new best Top-1 accuracy of 86.5%. In addition, the unnormalized model performed significantly better than the batch normalized model when fine-tuned after large pre-training on ImageNet, with the best model achieving 89.2% accuracy.

![image](https://github.com/user-attachments/assets/14c1d29d-9184-4382-a937-52c1ee398ea9)

### 2. Method Description 
  The paper focuses on methods for training DNN without batch normalization, and proposes the use of adaptive gradient trimming to improve training efficiency. Specifically, they used pre-activated residual blocks and eliminated the effects from normalization by adjusting the activation function, convolutional layer parameters, and so on. In addition, they designed a new algorithm for gradient cropping (AGC), which can train the model stably under large-scale batch processing.

  ![image](https://github.com/user-attachments/assets/9f1ef54f-e186-4a62-a2ae-47399a22da1c)

### 3. Methodological improvements
  Compared with the traditional batch normalization method, this method does not require additional computational overhead and can significantly reduce the training time. Meanwhile, with AGC, the model can be trained more stably under large-scale batch processing, which improves the training effect.
  
### 4. Issues addressed 
  Traditionally, BN is one of the important means to train DNN, but it will increase the computation and lead to longer training time. In contrast, the pre-activated residual block and adaptive gradient trimming method proposed in this paper can achieve efficient training without using BN. This provides a solution for training larger scale DNN.

  ![image](https://github.com/user-attachments/assets/4581316f-43a6-4a20-b300-f1703b1b8253)

## Experiments
  This paper focuses on the results of experiments on the NFNet model on the ImageNet dataset and comparisons with other models. Specifically, the authors conducted the following three comparison experiments:

  1. The performance of different modified NFNet models on the ImageNet dataset is compared, including the effect of using training techniques such as AGC and linear learning rate tuning, and it is shown that the use of stronger data augmentation methods can significantly improve performance.

  2. The performance of the NFNet model and the EfficientNet model on the ImageNet dataset is compared, and it is found that the NFNet model can achieve better performance without using additional data.

  3. In the transfer learning scenario, the authors compare the performance of Batch-Normalized and Normalizer-Free networks and find that removing Batch-Normalized in the pre-training phase improves the final performance.

In the first experiment, the authors used training techniques such as Nesterov's Momentum, AGC, and cosine annealing, and used different data augmentation methods to improve performance. The results of the experiments show that all of these methods can significantly improve the performance of the model, with the use of RandAugment having the best results, increasing the Top-1 accuracy from 84.7% to 86.0%. 

In the second experiment, the authors compared two models, NFNet-F1 and EfficientNet-B7, and NFNet-F1 can achieve higher Top-1 accuracy under the same training time and hardware conditions. 

In the third experiment, the authors compare the performance of the Batch-Normalized network and the Normalizer-Free network on the ImageNet dataset, and find that removing Batch-Normalized in the pre-training phase improves the final performance.

![image](https://github.com/user-attachments/assets/3c266d70-bef1-4df6-bd2b-a6973d90f43a)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new training method that uses an unnormalized network model instead of a batch-normalized model and demonstrates that this method has comparable performance to a batch-normalized model on image recognition tasks.
  
  2. By introducing the Adaptive Gradient Cropping algorithm (AGC), the method is able to train large-scale unnormalized NN stably and with larger batch sizes and stronger data augmentation.
  
  3. The authors design a series of new Unnormalized Residual Networks (NFResNets) models that achieve state-of-the-art best validation accuracy on the ImageNet dataset while training faster than that batch normalized models.

### 2. Innovative points
  1. A new training method is proposed that uses an unnormalized network model instead of a batch normalized model.
  
  2. Introduced the Adaptive Gradient Cropping Algorithm (AGC), which enables the un-normalized neural network to be trained stably and with larger batch sizes and stronger data augmentation.
  
  3. Designed a series of new Unnormalized Residual Networks (NFResNets) models that achieve the latest best validation accuracy on the ImageNet dataset while training faster than state-of-the-art batch normalized models.
     
### 3. Future Works
  1. Unnormalized network models could become a new trend in the field of DL, as they avoid some of the drawbacks of BN and can be trained with larger batch sizes and stronger data augmentation.
  
  2. Future research could explore how to further optimize the design of un-normalized network models to improve their performance and extend their applications.
  
  3. More research may be needed to understand how un-normalized network models work and to determine when it is most appropriate to use such models.
