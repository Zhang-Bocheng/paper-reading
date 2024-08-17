# SpineNet: Learning Scale-Permuted Backbone for Recognition and Localization
[paper link](https://arxiv.org/pdf/1912.05027) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper focuses on the shortcomings of convolutional neural networks in image recognition tasks and proposes SpineNet, a new backbone network architecture.         | Neural Network        |

## Methodology

### 1. Abstract
Conventional CNN perform poorly when dealing with tasks that require simultaneous object detection and localization, so the authors propose an encoder-decoder architecture that solves this problem by applying the decoder to a backbone model designed for classification tasks. However, the authors found that this architecture is unable to produce robust multiscale features because its backbone model decreases layer by layer in a decreasing resolution manner. 

To address this problem, the authors introduced a spine network (SpineNet) with cross-scale connectivity and trained it using neural architecture search techniques. Experimental results show that SpineNet performs better at all scales and uses less computation compared to the ResNet-FPN model. In addition, SpineNet can be used for classification tasks and significant improvements were achieved.

![image](https://github.com/user-attachments/assets/cb701669-98b9-4118-9b94-eb5d86d14d1c)

### 2. Method Description 
The paper presents a NN architecture called SpineNet for visual tasks such as image classification and target detection. The model consists of a **fixed base network** (called a “spine”) and a **learnable scale-crossover network**. The base network consists of a series of convolutional layers with reduced resolution, and each convolutional block can be passed as an input to a different level of the scale-crossover network. The scale-crossover network consists of multiple blocks, each with one feature map level associated with it. The way in which these blocks are connected to each other is determined by the arrangement of scales in the search space and by cross-scale connections. Finally, a range of different models were created to accommodate different computational budgets by gradually converting the model from a base network based on scale reduction to a scale-crossover based network using an incremental approach.

![image](https://github.com/user-attachments/assets/1fc66da0-b8a0-4bfb-8600-ffd6f990459f)

### 3. Methodological improvements
  1. Introduced cross-scale connectivity into the search space in order to improve high-level information while preserving low-level information.
 
  2. Added adjustable block sizes and types to further optimize model performance.
  
  3. Used an incremental approach to build a set of models to accommodate different computational budgets.

![image](https://github.com/user-attachments/assets/d0f180fd-b5fc-4750-a030-a3560675ec12)

### 4. Issues addressed 
The main contribution of the thesis is to propose a new NN architecture, namely SpineNet, which can effectively handle visual tasks such as image classification and target detection. In addition, the thesis proposes a number of improvements to further enhance the model performance and to meet the demands of different computational budgets. Therefore, the paper provides an important reference value for research in the field of computer vision.

## Experiments
The paper focuses on the authors' experimental results using the SpineNet model in object detection and image classification tasks, and compares them with other popular models such as ResNet-FPN. The following is a specific description of each comparison experiment:

**Object Detection Experiment**: the authors tested the SpineNet model on the COCO dataset and compared it to other models such as ResNet-FPN. The experimental results show that the SpineNet model has higher performance and efficiency than other models such as ResNet-FPN.

![image](https://github.com/user-attachments/assets/af112234-b7d2-467c-9dd2-9eddb2f53e17)

**Image classification experiments**: the authors tested the SpineNet model on ImageNet and iNaturalist-2017 datasets and compared it with other models such as ResNet. The experimental results show that the SpineNet model can achieve comparable performance to ResNet with the same setup, but using less computation. 

![image](https://github.com/user-attachments/assets/5c424bbc-03a7-4d02-9fc8-7a20c4b47922)

## Conclusion

### 1. Advantages of the Thesis
  1. In this paper, a new NN architecture design idea, the scale-permuted model, is proposed, and the specific implementation of the model is learned through neural architecture search.
  
  2. On the target detection task, the proposed SpineNet model has a better performance performance compared to the ResNet-50-FPN model, and also improves in terms of computational efficiency.
  
  3. In addition, the authors demonstrated that the SpineNet model can be directly applied to the image classification task with better results.

### 2. Innovative points
  1. This paper proposes the design idea of scale-permuted model, which allows the resolution of the intermediate feature maps to be arbitrarily increased or decreased so as to retain more spatial information.
  
  2. At the same time, the model also introduces cross-scale connectivity, which allows better integration of features at different scales and improves the model's expressive ability.
  
  3. The authors use the neural architecture search technique to automatically learn the best model structure, avoiding the process of manually adjusting the parameters.
     
### 3. Future Works
  1. The scale-permuted model proposed in this paper is a novel NN architecture design idea, which can provide more powerful feature extraction capability for visual tasks.
  
  2. The performance performance of the model can be improved in the future by further optimizing the model structure and training strategy.
In addition, the scale-permuted model can be applied to other visual tasks, such as semantic segmentation, to verify its generality and practicality.   
