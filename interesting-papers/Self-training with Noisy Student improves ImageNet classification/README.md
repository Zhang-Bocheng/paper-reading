# Self-training with Noisy Student improves ImageNet classification
[paper link](https://arxiv.org/pdf/1911.04252) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper describes a semi-supervised learning method called “noisy student training” that works effectively even with large amounts of labeled data.          | Semi-supervised Learning          |


## Methodology

### 1. Abstract
The method extends the idea of self-training and distillation by using equal or larger student models and adding noise (e.g., dropout, random depth, and RandAugment data augmentation) to the students during the learning process. At ImageNet, the authors first trained an EfficientNet model as a teacher using labeled images and used it to generate pseudo-labels for 300 million unlabeled images. Then, they train a larger EfficientNet model as a student model using images with a combination of labels and pseudo-labels. Finally, the students were iteratively trained as new teachers. 

The experimental results show that Noisy Student Training achieves 88.4% Top-1 accuracy on ImageNet, which is 2.0% higher than the state-of-the-art model that requires 350 million weakly labeled Instagram images. In addition, it improves ImageNet-A Top-1 accuracy on Robustness Test Sets, and reduces ImageNet-C average fault error rate and ImageNet-P average flip rate.

![image](https://github.com/user-attachments/assets/966fd7b0-c0da-4dc5-aad7-60d39753b699)

### 2. Method Description 
The paper presents a semi-supervised learning method called Noisy Student Training. The input consists of labeled and unlabeled images and uses the labeled images to train a teacher model, which is then used to generate pseudo-labels for the unlabeled images. The pseudo-labels can be soft or hard distributed. Next, a student model is trained that minimizes the total loss from combining the cross-entropy loss on both labeled and unlabeled images. Finally, iterative training is performed by regenerating new pseudo-labels and training a new student model with the student as the teacher. This method is an improvement on methods such as self-training and distillation.

![image](https://github.com/user-attachments/assets/fc9f2931-7dea-421f-b27f-0001b5a11069)

### 3. Methodological improvements
  1. The main improvements to the method are the addition of noise to the student model and the use of a student model that is equal to or larger than the teacher model.
  
  2. This makes the method different from knowledge distillation, where 1) noise is usually not used and 2) a smaller student model than the teacher's model is often used to speed up the process.
  
  3. One can think of the method as a knowledge extension where we want the student model to be better than the teacher model and therefore give the student model sufficient capacity and learning opportunities in difficult environments.
     
### 4. Issues addressed 
The method addresses the problem in semi-supervised learning of how to utilize large amounts of unlabeled data to improve model performance. By adding noise to the student model, the method is able to force the student model to ensure predictive consistency, thus enhancing the invariance of the decision function. In addition, data filtering and balancing techniques help to improve model performance. The method also has the advantage of scalability and adaptability as it can be used across a variety of datasets and tasks.

## Experiments
This paper focuses on the experimental results of model training using the Noisy Student Training method on the ImageNet dataset and compares it with other related methods. Specifically, the authors first introduce the experimental details and data sources, and then show the accuracy on ImageNet and the performance on other test sets. Finally, the authors also provide a detailed analysis and summary of the Noisy Student Training method.

![image](https://github.com/user-attachments/assets/b526a1a1-d0ff-4f58-817e-572b85f63f95)

In terms of experiments, the authors first used the Noisy Student Training method to train the EfficientNet-L2 model and compared it with other methods such as ResNeXt-101WSL. The results show that using the Noisy Student Training method can significantly improve the accuracy of the model, which is about 2.9 percentage points higher than ResNeXt-101WSL. In addition, the authors investigated the effects of different parameter settings and iterative training for the Noisy Student Training method and drew relevant conclusions.

![image](https://github.com/user-attachments/assets/ca9f27fe-664f-403e-b28b-3481066c7c28)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new semi-supervised learning method, Noisy Student Training, which uses unlabeled data to improve the accuracy and robustness of image recognition models.
  
  2. Compared with traditional weakly supervised learning methods, Noisy Student Training does not require a large amount of weakly labeled data, but instead utilizes a large-scale unlabeled dataset and promotes the learning ability of the student model by adding noise.
  
  3.  Experimental results show that Noisy Student Training can significantly improve the classification accuracy of EfficientNet on ImageNet with better robustness.
  
### 2. Innovative points
Noisy Student Training is a semi-supervised learning-based method whose main innovation is the introduction of noise to promote the learning ability of the student model. Specifically, the method improves the generalization ability and robustness of the model by introducing noise into the input data and the model itself, enabling the student model to better adapt to different data distributions.

### 3. Future Works
Future research directions include how to further optimize the Noisy Student Training algorithm to improve its performance and how to extend it to other types of data, such as text, speech, and so on. In addition, it is also possible to explore how to combine other techniques, such as transfer learning and adaptive learning, to further enhance the effectiveness of Noisy Student Training.  
