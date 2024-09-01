# AniPortraitGAN: Animatable 3D Portrait Generation from 2D Image Collections
[paper link](https://arxiv.org/pdf/2309.02186) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper proposes a novel GAN model called AniPortraitGAN for generating animated portrait images with controllable facial expressions, head poses and shoulder movements.         |  GAN        |

## Methodology

### 1. Abstract
The model is based on generating a radial manifold representation equipped with learnable facial and head-and-shoulder deformations, while dual-camera rendering and an adversarial learning scheme are used to improve the quality of the generated images. In addition, a pose deformation processing network is developed to generate reasonable deformations for challenging regions such as long hair. Experimental results show that the method is capable of generating diverse and high-quality 3D portrait images with good control over different attributes when trained using unstructured 2D images.

### 2. Method Description 
The paper presents a human avatar generation method based on neural radiation field representation and dual camera discriminator. 
<br>&emsp;Firstly, face attributes and viewpoints are controlled by inputting multiple latent codes and mapped to the final output image. 
<br>&emsp;Second, the human avatar is mapped onto a predefined 3D model using neural radiation field representation and inverse deformation techniques to achieve high-resolution, multi-viewpoint consistent and detail-rich generation results. 
<br>&emsp;Finally, the generation quality is improved by the design of a dual-camera discriminator that provides more direct supervision of the signals at different viewpoints.

![image](https://github.com/user-attachments/assets/cdc3df1e-df30-4016-937d-9633a4d9d41c)

### 3. Methodological improvements
Compared with the traditional GAN method, this method adopts neural radiation field representation and inverse deformation techniques to generate higher quality, multi-viewpoint consistent and detail-rich avatars. Meanwhile, the design of dual camera discriminator is introduced to provide more direct supervised signals and improve the generation quality.

### 4. Issues addressed 
This method solves the problems of traditional GAN methods in generating high-quality, multi-viewpoint consistent and detail-rich human avatars, and provides an effective method for generating avatars with realism and detail.

## Experiments
This paper focuses on a study conducted on the SHHQ-HS dataset to generate animated head-and-shoulder portraits, and comparison experiments with three other state-of-the-art 3D-aware GAN models (EG3D, GRAM-HD and AniFaceGAN). The details of each comparison experiment are described below:

**Generated Results Comparison Experiments**: this paper shows some generated head-and-shoulder portraits obtained by training using the authors' method, which are diverse and of high quality, with control over camera viewpoint, facial expression, head rotation and shoulder pose. An example of attribute control is also shown, which demonstrates that the authors' method allows for consistent attribute control across different identities. 
![image](https://github.com/user-attachments/assets/b9e405c6-6c7f-481d-97b5-5a9deeaafe9c)

**Comparison Experoment**: In this paper, the authors' approach is compared to three state-of-the-art 3D-aware GAN models (EG3D, GRAM-HD and AniFaceGAN). The authors quantitatively evaluated the FID and KID metrics on both full-face images and face regions. The results show that the authors' method scores comparable to EG3D and GRAM-HD on the face region and slightly lower on the full-face image. 

Although EG3D had the lowest scores, the authors found that it often generated flat geometries, leading to visual parallelism errors. Visually, the authors' method is comparable to EG3D and GRAM-HD in terms of image quality, with portraits having the correct geometry, as shown in Figure 4. In addition, this paper compares the results of AniFaceGAN and the authors‘ method, and it is clear that the authors’ method can generate and control larger regions.

**Ablation Study Experiments**: In this paper, Ablation Study experiments are conducted on the effectiveness of the algorithm design. 
Firstly, the authors verified the efficiency by quantitatively evaluating the generation quality at 128x128 resolution and calculated the FID and KID metrics between 5K generated and real images. The results show that the use of Dwhole (whole body discriminator) alone is clearly insufficient because of its low FID and KID scores on the human face. Combining Dwhole and Dface (face discriminator) significantly improves the quality of the face, but the quality of the whole portrait will be worse than using only Dwhole. The authors' method has low FID and KID scores on both the full portrait image and the face region. 

Second, to validate the effectiveness of the dual-camera rendering and adversarial learning scheme, the authors trained a variant that does not use a separate face camera for training. For this variant, the authors localised faces in the rendered head-and-shoulders portrait image and applied a face discriminator after cropping and alignment. The results show that the authors' method outperforms this method based on an image cropping strategy in terms of face quality, but with a slightly reduced FID on the full-face image. 

Finally, the authors removed the pose deformation processing CNN Dp, and it was found that the quality of the full-face image decreased. The specific experimental results and conclusions are shown in Table 2 and Figure 6.
![image](https://github.com/user-attachments/assets/690b4aa5-40ad-44f6-b946-2f58058e6d5c)

**Talk Video Generation Experiment**: this paper further tests the performance of the authors' trained model on the task of generating talk portrait videos. The authors selected some talking videos from the 300-VW dataset and tracked the estimation results of 3DMM expression and SMPL head-and-shoulder pose using the SMPL head-and-shoulder pose estimation method and the 3DMM expression estimation method. The authors then transfer the tracking results to the generated personas to obtain virtual talking videos. The article shows typical examples and provides complementary videos of continuous animation. 

## Conclusion

### 1. Advantages of the Thesis
  1. The method is the first of its kind to focus on generating movable face and shoulder regions for applications such as video conferencing and virtual presenters in real-world scenarios.
  
  2. In addition, the method employs dual-camera rendering and an adversarial learning scheme to improve the quality of face generation, and proposes a pose deformation processing module to achieve smoother and more realistic pose-driven deformation effects.

### 2. Innovative points
  1. firstly, it is a completely new task that has not been solved by other methods before;
  
  2. secondly, to address the problem of face quality, the authors adopt a dual-camera rendering and an adversarial learning scheme to improve the quality of face generation;
  
  3. And, in order to solve the problem of the unnatural deformation of long hair under SMPL guidance, the authors propose a pose deformation processing module to achieve smoother and more realistic pose-driven deformation effects.

### 3. Future Works
  1. The method may produce artefacts of human poses and expressions that are not present in the training data distribution, and there are problems with the inner mouth region with poor visual quality.
  
  2. Additionally, the method lacks the ability to control other attributes such as eye gaze and ambient illumination. Therefore, in future research, the authors plan to further explore and address these issues in order to make the method more complete and practical.
