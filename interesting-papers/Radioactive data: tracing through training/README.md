# Radioactive data: tracing through training
[paper link](https://arxiv.org/pdf/2002.00937) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new technique, radioactive data, for detecting whether specific image datasets are being used to train models.          | Machine Learning          |

## Methodology

### 1. Abstract
The method makes small but imperceptible changes in the dataset, such that any model trained based on these datasets carries a recognizable marking. This labeling is robust to different architectures and optimization methods. By using a standard architecture and training process, in a large-scale benchmark test, the authors demonstrate that they can detect the use of radioactive data with high confidence (p < 10 ^ -4) even if only 1% of the data is radioactive. 

![image](https://github.com/user-attachments/assets/a98ba6cb-3a1f-4dc3-aa10-10c02611ea0c)

### 2. Method Description 
The paper proposes a method for labeling data to detect if the model is trained using radioactive data. The method is divided into three phases: **a labeling phase, a training phase, and a detection phase**. 

<br>&emsp;In the labeling phase, random unit vectors are added to the feature space of the training image to label the data. 
<br>&emsp;In the training phase, labeled or unlabeled data is used to train the classifier. 
<br>&emsp;in the detection phase, the model is checked whether the labeled data is used for training.

![image](https://github.com/user-attachments/assets/5cfbf4b0-a9df-487a-9d24-772f337b59b3)

### 3. Methodological improvements
Unlike traditional watermarking techniques, this method modifies the orientation of the feature vector by changing the pixel values of the image to label the data. In addition, the method also considers data enhancement and proposes two different detection methods, white-box testing and black-box testing.

![image](https://github.com/user-attachments/assets/ad04c27e-cf9b-4fe8-99bf-05b2cbdddda7)

### 4. Issues addressed 
The method addresses the problem of how to detect whether a model has been trained using radioactive data. Since radioactive data can lead to unfair results, this method can help ensure the fairness and reliability of the model. Also, the method can provide similar techniques for labeling data for other fields, such as preventing models from being attacked.

## Experiments
This paper presents an experimental study on adding radiolabeling and detecting its presence in an image classification task. The authors conducted the following comparison experiments:

**Performance comparison of benchmark models**: the Resnet-18 and Resnet-50 models were trained on the ImageNet dataset using the Resnet-18 and Resnet-50 models and metrics such as accuracy and precision of the models were reported.

**Impact of radiolabels**: Radiolabels were inserted by modifying the images in ImageNet, and the models were retrained to analyze the presence of radiolabels in these "contaminated" models. The authors report several performance metrics, including PSNR (Peak Signal-to-Noise Ratio) on the images and p-value and accuracy on the models.

**Contrast to the effectiveness of the backdoor technique**: the backdoor technique is applied to the labeling problem and its effectiveness is observed. The authors found that the backdoor technique activates triggers in the model, but there is no guarantee that data using a specific marker is used to train the model.

**Results under different settings**: the authors analyze the performance of the model under different settings, including different architectures, data augmentation methods, and black-box testing. They also performed a correlation analysis based on class difficulty, verifying that the network relies more on the presence of markers when learning classes with low accuracy.

![image](https://github.com/user-attachments/assets/c175cd2a-6464-4c6b-8bad-dc56a4a480cb)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new method of labeling data, known as radioactive data, which can be used to verify that certain data is being used to train a model and provide statistical assurance.
  
  2. The method achieves labeling by adding small changes to the data that do not have a significant effect on the accuracy of the model, but can be detected by a neural network.
  
  3. The effectiveness and feasibility of the method has been tested on large-scale computer vision tasks, including tasks such as classification and instance segmentation.
  
  4. The method provides a new way of thinking about data tracking in machine learning and has a wide range of applications.
Method Innovation Points

### 2. Innovative points
  1. The method employs a radiolabeling technique that embeds the markers into the data, enabling the model to recognize the data where the markers are used.
  
  2. The method also considers the detectability and invisibility of the markers to ensure that the markers do not negatively affect the performance of the model.
  
  3. The method was also experimented in different settings to demonstrate its effectiveness and robustness.

### 3. Future Works
  1. The method can be applied to a wider range of scenarios in areas such as speech recognition and natural language processing.
  
  2. Further research can be done on how to improve the accuracy and reliability of the markers and how to prevent attackers from countering against the markers.
  
  3. The method can also be used in conjunction with other techniques, such as adversarial training and defense mechanisms, to improve the security and robustness of the model.  
