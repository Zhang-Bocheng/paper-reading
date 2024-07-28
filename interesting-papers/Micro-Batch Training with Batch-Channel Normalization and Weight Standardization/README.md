# Micro-Batch Training with Batch-Channel Normalization and Weight
[paper link](https://arxiv.org/pdf/1903.10520v2.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new tiny batch training method that aims to address the problem that deep neural networks can only be trained with very little data under memory constraints.         |  Deep Neural Networks         |

## Methodology

### 1. Abstract
The authors propose two new methods: **weight normalization and batch-channel normalization**, which can introduce the success factors of batch normalization (BN) into tiny batch training. Experimental results show that these two methods significantly improve the effectiveness of tiny batch training and can even match or exceed the performance of large batch training. This approach is useful for many computer vision tasks such as object detection, semantic segmentation, etc.

![image](https://github.com/user-attachments/assets/9f20986a-a300-4ed8-b150-8ede499a9adf)

### 2. Method Description 
The paper proposes a method called Weight Standardization (WS) for accelerating the training of DNNs. WS normalizes the weights by adding a standardization operation after the convolutional layers, making the gradient more predictable and reducing the smoothness of the loss function, thus improving training speed and performance.

Specifically, WS represents the original weights W as a new weight W', where W' is reparameterized based on the input of the first convolutional layer. Then, W' is normalized using the standard deviation and mean to make the gradient easier to predict. Finally, these new weights W' are used to update the model parameters.

![image](https://github.com/user-attachments/assets/b31bc113-4d44-4fe8-a861-75de59ca6fcc)

### 3. Key concepts
_Batch Normalization (BN)_: A technique used in NNs to improve the training speed and stability of DL models. It addresses the problem of internal covariate shift, which refers to the change in the distribution of network activations as the parameters of the preceding layers change during training.

### 4. Methodological improvements
  1. Compared to the traditional Batch Normalization (BN), WS does not need to compute additional statistical information, and therefore can complete the normalization operation faster.
  
  2. In addition, WS can better handle nonlinear activation functions because it does not change the direction of the gradient.

![image](https://github.com/user-attachments/assets/c0afed8e-b161-4183-85c0-7c9cdf5aa2a3)

### 5. Issues addressed 
The paper addresses two main problems in deep neural network training: 

1. eliminating the vanishing problem and avoiding overfitting.

2. By using WS, the gradient explosion or vanishing phenomenon during training can be reduced, and the generalization ability of the model can also be improved.

## Experiments
This paper focuses on the authors' experimental results in the areas of image classification, object detection and instance segmentation, and provides a comparative analysis of different regularization methods. Specifically, the authors used the ResNet model, fine-tuned on the ImageNet dataset, and compared the effects of different regularization methods such as Layer Normalization, Instance Normalization, Group Normalization and Batch Normalization. 

In addition, the authors conducted experiments for Batch-Channel Normalization and compared it with Switchable Normalization and Dynamic Normalization. Finally, the authors also conducted experiments for Object Detection and Instance Segmentation on the COCO dataset and compared the results with other methods. From these experiments, the authors conclude that Batch-Channel Normalization can significantly improve the model performance. 

![image](https://github.com/user-attachments/assets/7273840f-8fc4-4121-835a-e21631fc38c0)

![image](https://github.com/user-attachments/assets/46b9349a-455f-4f96-9239-15b965abd2a6)

## Conclusion

### 1. Advantages of the Thesis
In this paper, two new normalization methods, Weight Standardization (WS) and Batch-Channel Normalization (BCN), are proposed and theoretically analyzed and experimentally validated.

WS reduces the magnitude of the gradient by normalizing the weights in the convolutional layers, which makes the loss function smoother, while BCN avoids the problem of eliminating the singularity between channels by estimating the activation value and using it as the reference value for normalization.

The experimental results show that WS and BCN can significantly improve the performance in tiny batch training, even comparable to large batch training. In addition, BCN can further improve the generalization ability of the model.

![image](https://github.com/user-attachments/assets/336ccf73-02f4-4c5c-917a-b4416af5f751)
 
### 2. Innovative points
The WS and BCN proposed in this paper are based on the improvement and extension of the existing normalization methods and have the following innovative points:

  1. WS applies the normalization operation directly on the weights instead of the activation values, thus avoiding the problem of eliminating the singularity between channels;
  
  2. BCN introduces the method of estimating activation values, which avoids the problem of overfitting that may result from using real activation values;
  
  3. BCN also employs a residual connection-based design, which further improves the performance of the model.

### 3. Future Works
  1. In future research, it is possible to consider how to further optimize these methods to achieve better performance and efficiency.
  
  2. Meanwhile, other types of normalization methods, such as those based on the attention mechanism, can also be explored to expand the research direction in this field. 

