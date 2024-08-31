# Mixup: Beyond Empirical Risk Minimization
[paper link](https://arxiv.org/pdf/1710.09412.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This thesis focuses on the problems that arise during the training process of deep neural networks, such as overfitting and adversarial attacks, and proposes a new learning principle, mixup.         |  Deep Neural Networks         |

## Methodology

### 1. Abstract
by linearly combining and relabelling the training samples, it makes the model more inclined to simple linear behaviours, which improves the model's generalisation ability. Experimental results show that mixup is able to significantly improve the performance of existing NN architectures on ImageNet-2012, CIFAR-10, CIFAR-100, Google commands and UCI datasets. In addition, mixup is able to reduce the effect of label contamination, increase the robustness of adversarial attacks and stabilise the GAN training process.

### 2. Method Description 
In this paper, mixup is proposed as a data augmentation based technique for training DNN models. Unlike traditional data augmentation techniques, mixup uses two random samples and linearly combines these two samples by a random coefficient. This method can effectively improve the generalisation ability of the model and reduce the occurrence of overfitting.

### 3. Methodological improvements
  1. Blending can generate more samples to expand the training set, thus improving the generalisation ability of the model.
  
  2. Mixing can increase the sample diversity while keeping the size of the training set constant, avoiding over-reliance on some specific samples.
  
  3. Mixing can control the weight of new samples by adjusting the random coefficients, making the model focus more on samples that are more difficult to distinguish.
     
### 4. Issues addressed 
This paper addresses the problem of overfitting in DL. By using blending, the sample diversity can be increased without changing the size of the training set, thus improving the generalisation ability of the model and reducing the risk of overfitting. At the same time, blending can also help the model to better understand indistinguishable samples, further improving the performance of the model.

## Experiments
This paper presents the authors' experimental study of the data augmentation method mixup, including classification tasks on the ImageNet-2012, CIFAR-10, and CIFAR-100 datasets, as well as applications to the Google Command dataset, the Speech Recognition dataset, and the Generative Adversarial Network (GAN). The specific experiments are as follows:

Models trained with erm and mixup were compared on ImageNet-2012 and top-1 and top-5 error rates were reported. The results show that the model using mixup performs better in all tests, especially in the case of high volume and long training time.

The performance of pre-trained (CNN) models trained with erm and mixup were compared on the CIFAR-10 and CIFAR-100 datasets. The results show that the model using mixup has better generalisation performance than erm's model.
![image](https://github.com/user-attachments/assets/0755ec46-627e-45d2-b2fe-b341670eb207)

The performance of LeNet and VGG-11 models trained by erm and mixup were compared on the Google Command dataset. The results show that the model with mixup has better generalisation performance than the model with erm.

The performance of erm and mixup-trained models is compared in the ImageNet-2012 classification task under random label noise. The results show that the model using mixup is more difficult to be overfitted than erm's model.
![image](https://github.com/user-attachments/assets/295daf52-dba5-4b51-b0f7-4732ffae2934)

The performance of erm and mixup-trained models was compared under adversarial attacks. The results show that the model using mixup has better robustness than the model using erm.

The performance of erm and mixup trained fully connected neural network models are compared on the UCI dataset. The results show that the model using mixup has better generalisation performance than erm's model.
![image](https://github.com/user-attachments/assets/d2bd6178-353f-4ad5-b454-07b3aa2b301c)

## Conclusion

### 1. Advantages of the Thesis
The paper proposes a simple yet effective data augmentation method, mixup, to improve the generalisation ability of a model by constructing virtual training samples. mixup is an unsupervised data augmentation method that does not require any domain knowledge or a priori information, and is therefore pervasive and scalable. Experimental results show that using mixup on multiple datasets significantly improves model performance and can increase the robustness of the model against attacks. 

In addition, the paper explores the relationship between mixup and existing data enhancement methods, and provides detailed experimental analyses and comparisons. The authors provide rich experimental details and code implementations in the paper to facilitate readers to understand and reproduce the research results.

### 2. Innovative points
  1. The main contribution of the paper is to propose a new data enhancement method, mixup, which is based on the idea of linear interpolation, where two random samples and their labels are weighted and averaged to construct a virtual sample. 
  
  2. This method is not only simple and easy to understand, but also can effectively expand the training dataset without introducing too much computational overhead, thus improving the generalisation ability of the model.
  
  3. Meanwhile, mixup also has some other advantages, such as reducing the risk of overfitting and increasing the robustness of the model.
     
### 3. Future Works
The authors mention that mixup can also be used for regression problems and structured prediction problems, but these applications need more research and experimental validation. Also, whether mixup is applicable to other types of learning tasks (e.g., semi-supervised learning, reinforcement learning, etc.) needs further research. In conclusion, mixup, as a simple but effective method, is expected to play a greater role in future research.  


