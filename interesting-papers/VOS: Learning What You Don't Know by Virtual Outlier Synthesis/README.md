# VOS: Learning What You Don't Know by Virtual Outlier Synthesis
[paper link](https://arxiv.org/pdf/2202.01197) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new framework called VOS for detecting unknown data (i.e., out-of-distribution data) in neural networks.         |   Neural Networks        |

## Methodology

### 1. Abstract
While traditional detection methods require model regularisation using real datasets, VOS is trained by adaptively synthesising virtual outliers and estimating class-conditional distributions in the feature space. In addition, the paper introduces a new unknown-aware training target to contrastingly shape the uncertainty space between known data and synthetic outliers. Experimental results show that VOS achieves good performance on both object detection and image classification models, reducing the FPR95 by up to 9.36% over the previous best method.

### 2. Method Description 
This paper proposes an unknown data synthesis framework called Virtual Outlier Synthesis (VOS) for model regularisation and OOB detection. The framework consists of three main components: **virtual outlier synthesis, effective model regularisation using virtual outliers, and performing OOB detection at inference time**.

&emsp;First, virtual outliers are synthesised in the feature space. This is achieved by estimating class-conditional Gaussian distributions, using the penultimate layer of the neural network as the embedding representation, and maintaining class-conditional queues for each class to estimate parameters online. 
<br>&emsp;The virtual outliers are then sampled from within the likelihood subregion of the class-conditional distribution and their categorical outputs are computed. 
<br>&emsp;Finally, the classification outputs of the virtual outliers are used to train the model along with the real ID samples so that the model produces low OOB scores and has high outlier scores.

![image](https://github.com/user-attachments/assets/9210e080-bcec-4381-a104-ca803de5a90c)

### 3. Methodological improvements
Compared to traditional generative models such as GAN, VOS uses a simpler and more effective class-conditional distribution in the feature space to synthesise virtual outliers. In addition, VOS introduces a new training objective of model regularisation using virtual outliers, which improves the generalisation ability of the model.

### 4. Issues addressed 
The VOS framework proposed in this paper solves the problem of the model's inability to handle unknown data by synthesising virtual outliers for model regularisation, enabling the model to perform better on unknown data. At the same time, the framework also enables OOB detection at extrapolation time, improving the security and robustness of the model.

## Experiments
This paper focuses on the effectiveness of the Virtual Outlier Synthesis (VOS) method for object detection and image classification tasks, and compares it with existing methods. Specifically, the authors conducted the following two experiments:

I. Experiments under the object detection task

In this task, the authors used datasets such as PASCAL VOC1 and Berkeley DeepDrive as ID training data and datasets such as COCO and OpenImages as OOD datasets. The authors used the Detectron2 library and two different neural network architectures, ResNet-50 and RegNetX-4.0GF, for their experiments and used two metrics, FPR95 and AUROC, to evaluate the performance of the models. 
![image](https://github.com/user-attachments/assets/de8bc799-4954-4a88-a683-fbfedcc63539)

The results show that VOS performs better in recognising OOD samples compared to other competing methods such as maximum softmax probability, energy score, Mahalanobis distance, etc., while maintaining a high mAP value.

II.Experiments under image classification task

In this task, the authors used the CIFAR-10 dataset as ID training data, experimented with different types of neural networks such as WideResNet-40 and DenseNet-101, and used the cross-entropy loss function instead of the previous object detection loss function. The authors used six different OOD datasets for testing and used accuracy to evaluate the performance of the model. The results show that VOS performs well in recognising OOD samples while maintaining a high test accuracy. 
![image](https://github.com/user-attachments/assets/64b081ed-1da2-4db3-b63e-5745cb07d964)

## Conclusion

### 1. Advantages of the Thesis
  1. Suitable for object detection and classification tasks.
  
  2. Outliers can be synthesised adaptively without the need to collect or clean data manually.
  
  3. Synthesised outliers can estimate compact decision boundaries rather than using outliers that are too simple or difficult to separate.

### 2. Innovative points
  1. A novel unknown sample learning framework, VOS, is proposed to optimise both ID task and OOD detection performance.
  
  2. Virtual anomaly synthesis is achieved by estimating class-conditional distributions and sampling outliers from low-likelihood regions.
  
  3. A novel unknown sample training objective is proposed to shape the uncertainty surface between ID data and synthetic outliers in a contrastive manner.

### 3. Future Works
  1. Explore more effective outlier synthesis methods to improve the robustness and generalisation of models.
  
  2. Investigate how to extend VOS to other types of deep learning models in areas such as natural language processing and recommender systems.

  3. Explore how to incorporate other techniques, such as adversarial training and meta-learning, to further improve the performance and robustness of the model.  
