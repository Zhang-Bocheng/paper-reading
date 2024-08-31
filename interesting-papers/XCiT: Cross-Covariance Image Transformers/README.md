# XCiT: Cross-Covariance Image Transformers
[paper link](https://arxiv.org/pdf/2106.09681) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new image processing method, Cross-Covariance Attention (XCA), which is based on a self-attention mechanism and has linear complexity to efficiently process high-resolution images.         |  Transformer & Computer Vision       |

## Methodology

### 1. Abstract
The authors also propose a cross-covariance image transformer called ‘XCiT’, which combines the accuracy of traditional transformers with the scalability of convolutional neural networks, and achieves excellent performance in several vision benchmarks, including self-supervised image classification on ImageNet-1k, target detection and instance segmentation on COCO, and language segmentation on ADE20k. segmentation, and semantic segmentation for ADE20k, among other tasks. This research provides new ideas and tools for the field of computer vision.

### 2. Method Description 
This paper proposes the Cross-Covariance Image Transformer (XCiT) model, which uses the self-attention mechanism and improves on the traditional transformer with the cross-covariance attention operation (XCA). Specifically, the XCiT model divides the image into multiple local regions and extracts the feature vectors of each region by a convolution operation. These feature vectors are then fed into the self-attention layer to capture the dependencies between different regions. In addition, XCiT introduces a cross-covariance attention operation, which computes the correlation between two feature vectors to better capture the dependencies between them. Finally, the XCiT model also includes a number of fully connected and pooled layers to further improve performance.

![image](https://github.com/user-attachments/assets/7dafb32d-be0f-403e-aac0-8ccdcc1472a5)

### 3. Methodological improvements
The main improvement of the XCiT model is the introduction of the cross-covariance attention operation (XCA), which improves the performance of the model without increasing the computational cost. Compared with the traditional self-attention mechanism, XCA can capture the correlation between feature vectors more accurately, which improves the generalisation ability of the model. In addition, XCiT employs a local region partitioning strategy, which enables the model to better handle the detailed information in the image.

![image](https://github.com/user-attachments/assets/d811dd42-8b6b-478b-a3ee-519867d6bad3)

### 4. Issues addressed 
The XCiT model mainly solves some of the problems that exist in the traditional transformer model when processing image data. For example, when processing large images, the traditional transformer model may run out of memory; and when processing small-size images, the traditional transformer model may not be able to capture the detail information in the image. XCiT model can better handle these problems by introducing the local region partitioning strategy and the cross-covariance attention operation, which can improve the model's performance.

## Experiments
This paper focuses on the performance of using the XCiT model on several computer vision tasks, and several sets of comparative experiments are conducted to analyse its performance and effectiveness. Specifically, this paper includes the following three parts:

The first part is the image classification experiments, where the authors trained and tested the XCiT model using the ImageNet-1k dataset and compared it with other CNN and transformer neural networks. The results show that the performance of the XCiT model improves with increasing depth and width, and the performance can be further improved by using both hard distillation and convolutional teachers. And the XCiT model can achieve better accuracy with higher FLOPS budget and has good robustness to different image resolutions and sizes.

![image](https://github.com/user-attachments/assets/56f91caf-faed-4af4-a950-554cf5a6765f)

In the second part, object detection and instance segmentation experiments, the authors apply the XCiT model to the object detection and instance segmentation tasks in the COCO dataset and compare it with traditional convolutional neural networks and other transformer-based models. The results show that the XCiT model outperforms the traditional convolutional neural network in all model sizes and also exhibits better performance relative to other transformer-based models.

![image](https://github.com/user-attachments/assets/a1c0615d-d258-44f9-a367-583c492a4354)

The third part is the semantic segmentation experiments, where the authors apply the XCiT model to a semantic segmentation task on the ADE20K dataset and compare it with other common models. The results show that the XCiT model shows better performance than other models in both Semantic FPN and UperNet methods, especially on smaller models. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a novel self-attention model called XCiT, which is computed using feature dimensions rather than square matrices, avoids expensive quadratic operations, and has good generality and scalability.
  
  2. The authors validate the effectiveness and superior performance of XCiT through experiments on a variety of computer vision tasks, including image classification, object detection, instance segmentation, and semantic segmentation.
  
  3. In addition, XCiT can be used as a powerful backbone network for unsupervised learning.

### 2. Innovative points
  1. The main innovation of XCiT is its use of feature dimensions rather than square matrices for computation, which greatly reduces the amount of computation. Specifically, XCiT maps the input features into a smaller dimensional space and then performs the self-attention computation within this space.
  
  2. This approach not only reduces the amount of computation, but also improves the generalisation ability and efficiency of the model. In addition, XCiT employs residual linkage and convolutional design to improve the stability and accuracy of the model.

### 3. Future Works
The performance of the model can be further improved by increasing the number of layers or changing the number of feature dimensions. In addition, XCiT can be applied to other fields, such as NLP and speech recognition. Therefore, XCiT is a very promising research direction that deserves further in-depth research and application.  
