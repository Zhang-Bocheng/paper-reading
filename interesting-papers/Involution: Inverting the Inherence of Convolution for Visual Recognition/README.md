# Involution: Inverting the Inherence of Convolution for Visual Recognition
[paper link](https://arxiv.org/pdf/2103.06255) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper proposes a new neural network atomic operation, "involution", which rethinks the intrinsic principles of convolution in visual tasks by inverting the design principles of standard convolution, which are spatial-independent and channel-specific.         |  Neural Network         |

## Methodology

### 1. Abstract
 The approach includes self-attention operations as complex instances and can be used to build a new generation of NN models to improve the performance of common tasks such as image classification, target detection and segmentation. Experimental results show that the involution-based model achieves better performance on several benchmark test datasets such as ImageNet classification, COCO detection and segmentation, and Cityscapes segmentation, as well as a significant reduction in computational cost compared to a convolutional baseline model using ResNet-50. 
 
### 2. Method Description 
This paper proposes an alternative to convolution called "involution" for efficiently handling the information interaction problem in DNNs. Unlike the traditional convolution operation, involution generates a set of location-specific convolution kernels in the image space by sharing meta-weights, thus realizing the global perception of the input feature map. Specifically, involution first unfolds the input feature map into a matrix and generates a set of involution convolution kernels through a series of linear transformations and nonlinear activation functions, and then applies these convolution kernels to the original feature map to obtain the final output feature map.

![image](https://github.com/user-attachments/assets/b363ea34-9357-4dbb-97a0-435c1acb94d5)

### 3. Methodological improvements
  Compared with the traditional convolution operation, involution has the following advantages:

  1. **Higher computational efficiency**: since involution requires only one matrix multiplication operation, its computational speed is faster than the traditional convolution operation.
  
  2. **Better generalization ability**: involution can be adapted to different task requirements by adjusting the number and size of involution convolution kernels, which improves the generalization ability of the model.
  
  3. **Stronger translation invariance**: Since the involution convolution kernels are shared, stronger translation invariance can be achieved, making the model more robust to positional changes in the image.
     
### 4. Issues addressed 
  1. The INVOLUTION method proposed in this paper mainly solves the information interaction problem that exists in DNNs. Although the traditional convolution operation can effectively extract local features, it is difficult to capture the global information. In contrast, involution generates a set of location-specific convolution kernels in the image space by sharing meta-weights, thus realizing the global perception of the input feature map.
  
  2. This not only improves the performance of the model, but also reduces the number of parameters and the risk of overfitting. Meanwhile, involution also has the advantages of higher computational efficiency, better generalization ability and stronger translation invariance, which provides a new idea and method for the field of DL.
     
## Experiments
  This paper focuses on the performance of the RedNet model based on CNN on tasks such as image classification, object detection and instance segmentation, semantic segmentation, etc., and several comparative experiments are conducted to verify the effectiveness of the model.

First, on the task of image classification, the authors compare RedNet with improved models such as ResNet and SAN, and the results show that RedNet is able to achieve higher accuracy with the same parameter storage and computational resources. In addition, the authors show the advantages of RedNet in terms of inference time.

Secondly, for the object detection and instance segmentation tasks, the authors used representative models such as RetinaNet and Faster R-CNN and modified different components (e.g., FPN, head) to apply the INVOLUTION operation. The results show that using RedNet as the backbones significantly improves the performance while reducing the parameters and computational cost. In addition, further application of involution to task-specific heads can also achieve better results.

Finally, for the semantic segmentation task, the authors used frameworks such as Seman-tic FPN and UPerNet and trained the Cityscapes dataset by fine-tuning. The results show that using RedNet as a backbone can significantly improve the average IoU score and better results can be obtained by further introducing the involution operation.

![image](https://github.com/user-attachments/assets/a4b5ea36-6db1-4da9-9f41-4dc22b90db21)

![image](https://github.com/user-attachments/assets/92508c9c-1e49-43b4-98eb-6d8e36cf764f)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new convolution operation, involution, which achieves more efficient visual representation learning by reversing the design principles of convolution and generalizing the self-attention formulation.
  
  2. The authors conduct experiments on several standard visual benchmark tests and compare them with traditional convolutional models and models based on self-attention, and the results show that involution can significantly improve performance and reduce computational cost.
  
  3. In addition, the authors provide a detailed ablation analysis of the method, demonstrating that its core contribution lies in the effectiveness of spatial modeling and the efficiency of its architectural design.
     
### 2. Innovative points
  1. Compared with traditional convolutional models, involution can better handle local feature variations and also reduce the amount of computation and number of parameters.
  
  2. In addition, the authors applied involution to several visual tasks, including image classification, target detection, instance segmentation, and semantic segmentation, demonstrating its broad applicability.

### 3. Future Works
  1. the authors hope to further explore the application scope of involution and combine it with other state-of-the-art NN architectures to obtain better performance and higher efficiency.
  
  2. In addition, the authors also plan to introduce involution into the field of automatic NN search to extend its search space and improve the search efficiency.
  
  3. In conclusion, the involution proposed in this paper is a very promising approach that is expected to play an important role in future research.

