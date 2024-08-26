# Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks
[paper link](https://arxiv.org/pdf/2402.13144.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper presents an unpaired image translation method that learns to convert an input image in one domain to an output image in the target domain.         | adversarial generative network (GAN)          |

## Methodology

### 1. Abstract
The authors propose a learning method using an adversarial loss function and a cyclic consistency loss function to ensure the accuracy of the mapping relationships. Experimental results show that the method achieves excellent performance on several tasks, including style shifting, object deformation, seasonal conversion, and photo enhancement.

![image](https://github.com/user-attachments/assets/fc0b190e-85fc-48c0-850e-d1b0c8fc2d0d)

### 2. Method Description 
The cross-domain image transformation method proposed in this paper uses an adversarial generative network (GAN) and cyclic consistency loss to learn the mapping functions of two domains. Specifically, the method consists of two mapping functions, G and F, which map the source domain X to the target domain Y and map the target domain Y back to the source domain X. At the same time, two adversarial discriminators, DX and DY, are introduced to distinguish between real and generated samples. The ultimate goal is to learn these two mapping functions by minimising the difference between the generated samples and the real samples as well as keeping the consistency of the mapping functions.

![image](https://github.com/user-attachments/assets/c3344e08-6a37-4de8-a8ee-c94f090a02c7)

### 3. Methodological improvements
Compared to traditional image transformation methods, the method in this paper uses an GAN and cyclic consistency loss to learn the mapping functions, which makes the generated images more realistic and able to satisfy the correspondence between the source and target domains. In addition, the method employs instance normalisation techniques to improve the model performance.

### 4. Issues addressed 
The method in this paper can effectively solve the problem of cross-domain image conversion, i.e., converting an image from one domain to an image in another domain. This is of great significance for many practical applications, such as style migration in natural scenes and conversion between different modalities in medical image processing. Compared with traditional image conversion methods, the method in this paper has higher accuracy and better generalisation ability.

## Experiments
This paper focuses on the authors' experiments using their own method (CycleGAN) in comparison with several baseline methods, and analyses and interprets their results. Specifically, the authors used the following methods in their experiments:

  1. For the translation task on the paired dataset, the authors used a ‘real vs. fake’ perceptual study to assess the realism of the model-generated images, and used FCN scores to assess the comprehensibility of the model-generated images. In addition, the authors used standard semantic segmentation metrics to evaluate the model's performance on the tag-to-photo task.

![image](https://github.com/user-attachments/assets/1a43ade0-25bd-49d0-b015-cf624c2c2515)

  2. In the absence of paired data, the authors conducted a ‘real vs. fake’ perceptual study using Amazon Mechanical Turk (AMT) to assess the authenticity of the model-generated images. The authors also used FCN scores to assess the comprehensibility of the model-generated images.

![image](https://github.com/user-attachments/assets/d2bab662-6f2c-4479-b964-034ebf0b0894)

  3. For different loss functions, the authors conducted experiments and compared their performance.

![image](https://github.com/user-attachments/assets/846e87bb-fb00-4bae-9f83-3b5f6739e0c4)

By comparing these experiments, the authors came up with the following conclusions:

  1. The authors' method produces higher quality translation results compared to other baseline methods.

  2. The authors' method requires the use of both GAN loss and cyclic consistency loss to obtain the best results.

  3. In the absence of paired data, the authors' method can still achieve the image translation task to some extent.
 

