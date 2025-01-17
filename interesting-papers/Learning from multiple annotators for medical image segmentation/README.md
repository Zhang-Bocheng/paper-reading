# Learning from multiple annotators for medical image segmentation
[paper link](https://www.sciencedirect.com/science/article/pii/S0031320323001012) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper focuses on a study to learn a multi-annotator label fusion method for medical image segmentation          | Image Segmentation         |

## Methodology

### 1. Abstract
While traditional machine learning algorithms perform poorly when dealing with labels with noise, this study uses two Convolutional Neural Networks (CNNs) to jointly learn the reliability of a single annotator as well as the expert consensus label distribution from observations that contain only noise. The method was validated by creating an MNIST toy segmentation dataset and then demonstrated using three public medical imaging segmentation datasets with both simulated and real-world annotations: ISBI2015 (multiple sclerosis lesions), BraTS (brain tumours) and LIDC-IDRI (lung abnormalities). 

Finally, they also created a real multiple sclerosis lesion dataset (QSMSC) containing manual segmentation from four different annotators (three radiologists with different skill levels and one expert generating expert consensus labels). The results show that the method outperforms competing and relevant benchmark methods in all datasets, especially when the number of annotations is small and varies widely.

### 2. Method Description 
The paper proposes a deep learning-based approach to solve the multi-labelled image segmentation problem. Specifically, they used CNN as the model architecture and proposed a joint probability distribution model to estimate the true label distribution of each pixel. During training, they optimise the model parameters by minimising the cross-entropy loss function and the regularisation term.

![image](https://github.com/user-attachments/assets/feb98000-b815-4f73-b4ef-e01435875932)

### 3. Methodological improvements
To address the noise problem in multi-labelled image segmentation, the paper proposes a new method that uses multiple independent CNN networks to predict the label distribution of each pixel. These label distributions are then combined into a matrix that is used to estimate the true label distribution for each pixel. In addition, they introduced a low-rank approximation technique to reduce the computational and storage requirements.

### 4. Issues addressed 
The main contribution of this paper is to propose an effective method to solve the noise problem in multi-labelled image segmentation. Their approach not only improves segmentation accuracy but also reduces computational cost and storage requirements. This method has important applications in fields such as medical image segmentation.

## Experiments
This paper presents experimental results in a multi-label image segmentation task performed on multiple datasets. The authors compare the effectiveness of their method with several other methods based on label fusion and use multiple evaluation metrics to measure the performance of the model.

First,**in experiments on the MNIST and ISBI2015 datasets**, the authors find that their method performs better than STAPLE in both the dense-label and single-label cases. In addition, they show the difference in performance of different methods with different average Dice values through visualisation.

![image](https://github.com/user-attachments/assets/2698febe-99a0-4600-9404-a4fb5deb0d98)

Second, **in their experiments on the BraTS dataset**, the authors found that their method also performs well in the multi-class segmentation task, outperforming both STAPLE and Spatial STAPLE in both the dense-label and single-label cases. In addition, they show the performance difference between the different methods under different target categories through visualisation.

![image](https://github.com/user-attachments/assets/b2807971-6e33-4ca2-be85-5915d02187ce)

Next, **in experiments on the LIDC-IDRI dataset**, the authors found that their method performs better than STAPLE in the single-label case. In addition, they show the performance difference of different methods under different consensus levels through visualisation.

![image](https://github.com/user-attachments/assets/337b004d-0618-479b-bff1-4a026775d141)

Finally, **in an experiment in a real-life multi-label MS segmentation task**, the authors find that their method performs better than other deep learning methods and the widely used STAPLE and Spatial STAPLE models. In addition, they show the performance difference between the different methods under different annotator capabilities through visualisations.  
![image](https://github.com/user-attachments/assets/d0a2038a-5be1-4c5d-b13b-9de74c579b45)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper propose a novel CNN-based supervised learning segmentation framework that can simultaneously estimate the inter-annotator reliability of multiple annotators as well as the expert consensus label distribution for different medical image segmentation tasks.
  2. The method is very lightweight and can be trained in an end-to-end manner. Experimental results show significant improvements in segmentation accuracy and CM estimation quality compared to traditional label fusion methods, including mean, majority voting and the widely used STAPLE framework and its spatial variants.

### 2. Innovative points
  1. The main contribution of this paper is to propose a novel approach to address the problem of unbalanced datasets in the multi-class image segmentation problem. By integrating two coupled CNNs into an end-to-end supervised segmentation framework, the reliability and expert consensus label distribution of multiple annotators can be jointly estimated in the absence of true labels.
  2. And, this paper explores how metadata can be utilised to improve model performance and suggests potential application scenarios for applying annotation models in downstream tasks.
 
### 3. Future Works
One future direction is  education of less experienced annotators, where estimated spatial features can help them improve their annotation behaviour and thus the quality of their annotations. And, the authors believe it is worth exploring the question of how many training samples are needed at least to achieve reliable performance for each annotator.
