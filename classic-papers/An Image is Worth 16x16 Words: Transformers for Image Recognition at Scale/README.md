# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
[paper link](https://arxiv.org/pdf/2010.11929) 
| Year | Introduction  | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 |  This paper explores the possibility of applying the Transformer architecture to computer vision tasks.        | Transformer          |

## Methodology

### 1. Abstract
Traditional Convolutional Neural Networks perform well in image recognition, but they require a lot of
computational resources and time for training. The authors propose Vision Transformer (ViT), which 
directly divides an image into blocks of pixels and inputs them as sequences into a pure Transformer 
model for processing. Experimental results show that ViT achieves comparable or even better 
performance than the current best convolutional neural networks on benchmark datasets such as 
ImageNet, CIFAR-100, etc., while requiring significantly less computational resources. 
This research result brings new ideas and methods to the field of image recognition.

### 2. Method Description 
  In this paper, a model called Vision Transformer (ViT) is proposed to handle image classification 
tasks. The model employs a Transformer structure and cuts the input 2D image into a series of 2D 
patches, which are then converted into vector representations and used as input sequences to the 
Transformer. A linear projection layer is applied to each patch to map it into a fixed size vector 
space. Next, position encoding is added to the vector representation of each patch to preserve their 
relative position information in the original image. Finally, features are extracted and the 
classification task is accomplished by a multi-head self-attention mechanism and a fully connected 
network layer.

### 3.  Methodological improvements
Compared to traditional convolutional neural networks (CNNs), ViT has the following advantages:

1. Stronger translational invariance: due to the use of a global self-attention mechanism, ViT can better
   capture the global information in an image, which improves the translational invariance of the model.

2. Fewer parameters: ViT has a smaller number of parameters compared to traditional CNNs, which makes it
   easier to train and enables faster convergence.

3. Better generalization ability: Since ViT does not depend on a specific image local structure, it can
   better adapt to various types of image datasets and shows better generalization ability in tasks such
   as small sample learning.

### 4. Issues addressed 
  The ViT model proposed in this paper solves some problems of traditional CNN models, such as the need 
to manually design filters and the need for a large amount of computational resources. At the same time, 
ViT also provides a new idea of how to utilize the self-attention mechanism to deal with the image 
classification task, which is also instructive for future research.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/fd5c0a36-725e-41cb-bb30-ef16dc0b0deb)

## Experiments
  This paper focuses on comparative experiments using Vision Transformer (ViT) and ResNet in an image 
classification task, and explores the impact of pre-training data size on model performance as well as 
computational efficiency comparisons between the different models. Specifically, the authors conducted the 
following comparison experiments:

1. Comparing the performance of ViT and ResNet on benchmark datasets such as ImageNet. The authors used
   three different model sizes and input resolutions to compare their performances, and the results show
   that the ViT model is able to achieve better performance, especially on larger datasets, with the same
   pre-training time and computational resources.

2. Comparing the effect of different pre-training data sizes on model performance. By pre-training the ViT
   model on datasets of different sizes and comparing its performance on the ImageNet dataset, the authors
   found that the performance of the model improves as the size of the pre-training data increases.

3. Comparing the computational efficiency of different models. The authors compared the computational
   efficiency of multiple models, including the pure Transformer model, ResNet and Hybrid model, etc.
   The results show that the ViT model is able to achieve higher performance with the same computational
   resources compared to the ResNet model.

  Overall, the experimental results in this paper show that the ViT model outperforms the traditional 
ResNet model in image classification tasks, and its performance can be further improved by appropriate 
pre-training data size adjustment. In addition, the authors explore the computational efficiency comparison 
between different models, which provides a reference for practical applications.

## Conclusion
### 1. Advantages of the Thesis
  The paper proposes a new image recognition method, Vision Transformer (ViT), which directly applies the
Transformer model in natural language processing to the image recognition task and achieves excellent 
results. Compared with traditional convolutional neural networks, 

1. ViT has higher scalability and less computational cost,
  
2. while it can achieve better performance after pre-training on large-scale datasets.
   
3. the paper explores the method of self-supervised learning and demonstrates its effectiveness for
   improving model performance.

### 2. Innovative points
  The main contribution of the paper is the proposal of ViT, a new approach to image recognition that avoids
the introduction of a priori knowledge specific to the field of computer vision by treating images as 
sequences and processing them using the standard Transformer encoder. Also, the paper explores the approach 
of self-supervised learning, demonstrating its effectiveness for improving model performance.

### 3. Future Works
  Although ViT has achieved excellent performance in several image recognition tasks, there are still some 
challenges to overcome. For example, 

1. how to apply ViT to other computer vision tasks, such as target detection and segmentation;
   
2. how to further optimize the self-supervised learning approach to improve the model performance;

3. how to further scale up ViT for better performance. 

These research directions will be the focus of future research.
