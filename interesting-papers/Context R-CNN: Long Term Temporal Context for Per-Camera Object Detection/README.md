# Context R-CNN: Long Term Temporal Context for Per-Camera Object Detection
[paper link](https://arxiv.org/pdf/1912.03538) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a method called Context R-CNN for object detection in surveillance cameras.         |  CNN         |

## Methodology

### 1. Abstract
  Since the sampling frequency of surveillance cameras is usually low, a model that can handle irregular sampling rates is needed. The method utilizes long-term contextual information to improve the object detection performance of the current frame by aggregating features from other frames through an attentional mechanism. The authors conducted experiments in two scenarios: species detection and vehicle detection, and demonstrated that Context R-CNN performs better relative to the baseline model. 
  
### 2. Method Description 
  The Context R-CNN proposed in this paper is a target detection model based on contextual information, which improves the accuracy of target detection by combining the features of the current frame with those of historical frames. Specifically, the model first extracts instance-level features of the current frame using a single-frame detection model and passes them to two attention modules to obtain contextual information. These modules look up the corresponding feature vectors based on the input feature vectors in a memory bank storing the feature vectors of previous frames and return a contextual feature vector associated with the feature vector of the current frame. This context feature vector is then added to the feature vector of the current frame and passed to the second stage of the Faster R-CNN for classification and regression.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/b84f6d90-8fa5-4beb-ab9c-e0ee956b51e1)

### 3. Key concepts
  R-CNN (Region-based Convolutional Neural Network) is a family of computer vision models used for object detection. It addresses the challenge of locating and classifying objects within an image by combining region proposals with CNN features.
  
### 4. Methodological improvements
  1. Compared to traditional target detection models based on spatio-temporal CNN (3D CNN) or recurrent neural networks (RNN), Context R-CNN adopts a simpler and more effective single-frame detection model as the basis and utilizes the information of historical frames by introducing an attention mechanism. This approach not only reduces the computational complexity but also improves the detection performance.

  2. The model proposes two different memory banks: the Long Term Memory Bank and the Short Term Memory. The former is used to store historical frame information over a longer time range, while the latter is used to store historical frame information over a shorter time range. This design allows the model to better adapt to the data distribution in different scenarios.

### 5. Issues addressed 
  Context R-CNN mainly addresses the problems of target detection models based on spatio-temporal CNN or RNN when dealing with low frame rate, irregular data. Since these models need to consider the dependencies between neighboring frames, they usually cannot effectively handle data with low frame rates. Context R-CNN, on the other hand, by introducing an attention mechanism and a hierarchical memory bank, is able to effectively utilize the information of historical frames to improve the accuracy of target detection while guaranteeing a low computational complexity.
  
## Experiments
  This paper focuses on the experimental results of the Context R-CNN model on three different datasets and compares them with other single-frame detection models. Specifically, this paper explores the following four aspects of the experiments:

**Main results**: The authors apply the Context R-CNN model to three datasets, Snapshot Serengeti (SS), Caltech Camera Traps (CCT), and CityCam (CC), and compare it with the single-frame Faster RCNN model. The experimental results show that the Context R-CNN model achieves better performance than the single-frame model on all datasets, with mAP scores improving ranging from 19.5% to 17.9%.

**Experiments with the short-term attention module**: The authors also investigated the effect of the short-term attention module and tried a number of different strategies to utilize the information captured by the camera. The experimental results show that the performance of the model can be further improved by taking into account contextual information within the animal group and by using the S3D video object detection model.

**Experiments with the Long-Term Attention Module**: The authors also explored the effects of the Long-Term Attention Module and experimented with the effects of different time window sizes. The experimental results show that the performance of the model improves as the time window increases. In addition, the model also outperforms short-term attention when only long-term attention is considered.

**Experiments on model parameter tuning**: Finally, the authors also investigated the effect of some hyperparameters of the model on the performance, such as the choice of feature extractor, the number of images stored in the memory, and the way of processing the empty images. The experimental results show that for different datasets, choosing appropriate hyperparameters can significantly improve the performance of the model.

Overall, this paper demonstrates the excellent performance of the Context R-CNN model on multiple datasets and provides some practical suggestions to help users optimize the performance of the model.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new detection model, Context R-CNN, which is able to utilize the contextual information captured by the camera to improve the performance of target detection in static cameras.
  
  2. The model is generalizable in the field of still cameras and can be adapted to data streams with low frame rates and irregular sampling strategies.
  
  3. In addition, the model is able to achieve better performance on long-tailed categories.

### 2. Innovative points
  1. The innovation of the paper's approach is the introduction of the concept of long-term memory banks, which allows the model to learn and use target examples that may be more easily recognized in other cameras over multiple time steps.
  
  2. This non-parametric estimation method (e.g., nearest neighbor) combined with a powerful parametric function (e.g., Faster R-CNN) allows the model to take advantage of unlabeled "neighbor" test examples to improve generalization.
  
### 3. Future Works
  1. Explore how to better store and manage diverse memory banks in the future to optimize accuracy and size and reduce computational and storage overhead during training and inference.
  
  2. Continue to investigate how to apply the method to target detection tasks in dynamic scenes.
