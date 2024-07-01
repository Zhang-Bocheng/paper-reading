# Axial-DeepLab: Stand-Alone Axial-Attention for Panoptic Segmentation
[paper link](https://arxiv.org/pdf/2003.07853) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a model called Axial-DeepLab for image classification and dense prediction tasks.         | Self-Attention          |

## Methodology

### 1. Abstract
  The model employs a new location-sensitive self-attentive layer that can be used stacked to build more powerful models. Experimental results show that the model performs well on datasets such as ImageNet, COCO, Mapillary Vistas, and Cityscapes, and especially achieves leading results in the Panoptic Segmentation task. Compared with existing self-focused models, the model has higher parameter efficiency and computational efficiency, and is better able to capture long-range contextual information.
  
### 2. Method Description 
  The paper proposes a new attention mechanism, Position-Sensitive Self-Attention (PSSA), and applies it to the task of image classification in CNNs. The method enables attention to capture the relationship between different positions by introducing relative position encoding in queries, keys and values, and is able to handle large-size inputs. Also, the method uses Axial-Attention to further improve computational efficiency and global connectivity.
  
### 3. Key concepts
  _Panoptic segmentation_: A computer vision task that combines the goals of both semantic segmentation and instance segmentation into a unified framework. The aim is to provide a comprehensive understanding of a scene by assigning a class label and an instance ID to every pixel in an image.
  
### 4. Methodological improvements
  The main improvement of the method is the introduction of a PSSA mechanism, which allows the model to better capture long-range dependencies. In addition, the method employs axial attention to further improve computational efficiency and global connectivity. Compared with the traditional self-attention mechanism, the method has better computational efficiency and higher accuracy.
  
### 5. Issues addressed 
  The method mainly solves the problems of high computational complexity and inability to capture long-distance dependencies of the traditional self-attention mechanism when dealing with large-size inputs. By introducing the position-sensitive self-attention mechanism and axial attention, the method is able to significantly reduce the computational complexity while maintaining high accuracy, thus making it suitable for larger datasets and more complex tasks.
  
## Experiments
  This paper focuses on experimental results on Axial-ResNet and Axial-DeepLab on four large datasets: ImageNet, COCO, Mapillary Vistas, and Cityscapes. Specifically, the authors first compare with ResNet-50 using the same training protocol and report results on ImageNet. 

  On ImageNet, the authors report results using position-sensitive self-attention and all-axis self-attention and find that the former is more effective than the latter. In addition, the authors compare performance with different network widths (i.e., different number of channels) and find that in all cases the full-axis self-attention model has the best trade-off between accuracy parameters and computational complexity.

  On COCO, the authors achieved better results than DeeperLab, SSAP and Panoptic-DeepLab using the single-scale Axial-DeepLab-S model. With multi-scale inputs, the authors used a larger number of channels to improve performance and achieve higher accuracy in the test set.

  On Mapillary Vistas, the authors achieved the best results in the tasks of panoptic segmentation, instance segmentation, and semantic segmentation using both single-scale and multi-scale Axial-DeepLab-L models.

  On Cityscapes, the authors achieved the best results in the tasks of panoptic segmentation, instance segmentation, and semantic segmentation using both single-scale and multi-scale Axial-DeepLab models. In addition, the authors conducted ablation studies to demonstrate the importance of PSSA and omniaxial self-attention, and found that the omniaxial self-attention model performed better than the PSSA model in the Cityscapes segmentation task.
  
## Conclusion
### 1. Advantages of the Thesis
  1. The paper proposes a new attention mechanism, axial-attention, which achieves more efficient computation by decomposing two-dimensional attention into two one-dimensional attentions and recovers the ability to model attention for large acceptable ranges. 
  
  2. Also, the paper proposes a pocation-sensitive axial-attention layer, which allows the attention to better utilize the location information without adding too much computational cost.
  
### 2. Innovative points
  1. The main contribution of the paper is the proposal of a new attention mechanism, axial attention, and a position-sensitive axial attention layer. These innovations enable attention to better handle long-distance interactions and also improve computational efficiency.
    
  2. The paper demonstrates the effectiveness of attention by applying it to image classification and segmentation tasks.

### 3. Future Works
  1. Future research could further explore how to combine other techniques to improve the effectiveness of axial attention, such as structured learning or deep reinforcement learning.
  
  2. It could also be investigated how to combine axial attention with other types of attention to achieve better results.
