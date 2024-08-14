# Rethinking the Truly Unsupervised Image-to-Image Translation
[paper link](https://arxiv.org/pdf/2006.06500.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper proposes a truly unsupervised image-to-image translation model (TUNIT) that does not require any supervision of pairwise image or domain labeling.         | unsupervised learning          |

## Methodology

### 1. Abstract
TUNIT learns both to separate the image domains and to convert the input image into an estimated domain. Experimental results show that TUNIT performs well on various datasets and is robust to hyperparameter selection. Moreover, TUNIT can be easily extended to semi-supervised learning with a small amount of labeled data.

![image](https://github.com/user-attachments/assets/17b3a63a-623d-4fa3-a0cd-cd0c5ae593b4)

### 2. Method Description 
The paper proposes a framework for unsupervised domain category-based image translation, in which the bootstrap network plays a central role as both an unsupervised domain classifier and a style encoder. The bootstrap network guides the translation process by feeding the style code of the reference image to the generator and its pseudo-domain labels to the discriminator. Using feedback from domain-specific discriminators, the generator can synthesize images of the target domain (e.g., breeds) while respecting the style of the reference image (e.g., fur patterns) and the content of the source image (e.g., poses). Specifically, the method employs technical tools such as contrast loss and Mokko queue, and combines the advantages and disadvantages of different methods to improve model performance.

![image](https://github.com/user-attachments/assets/75b02475-2dd3-4630-87ca-c1ef66eca6c9)

### 3. Methodological improvements
  1. contrast loss is introduced to learn style features, which enables the generator to better preserve the style of the reference image;
  2. contrast loss is applied to the shared embedding, which improves the representation ability of the shared embedding, and thus improves the generalization ability of the model.

### 4. Issues addressed 
The method solves the problems of traditional unsupervised image translation methods, such as the need for a large amount of labeled data and the difficulty of handling samples with complex diversity. Compared with traditional methods, the method does not require a large amount of labeled data and can be applied in a wider range of scenarios. In addition, the method has better generalization ability and robustness, and can cope with various complex image translation tasks.

## Experiments
This paper focuses on the performance of the TUNIT model in image translation tasks, and several comparative experiments are conducted to verify its performance and stability.

  1. the authors comparatively **analyze the components of the TUNIT model**, including the bootstrap network, the new loss function, and so on. By comparing with the existing supervised method FUNIT, it is found that TUNIT has a significant improvement in accuracy, especially in the unlabeled case, which also achieves better results. In addition, TUNIT also has strong generalization ability and maintains good performance with different number of pseudo domains K.

  2. the authors **conducted experiments on semi-supervised learning**, using less labeled data to train the model. The results show that TUNIT can be easily adapted to semi-supervised learning scenarios and performs better relative to other semi-supervised learning methods.

![image](https://github.com/user-attachments/assets/c2b6fda4-521a-4e83-a9a1-be277436cacb)

  3. the authors **apply TUNIT to an image translation task on unlabeled datasets**. The results show that TUNIT can effectively capture the stylistic features between samples and generate high-quality translation results. Meanwhile, TUNIT performs more consistently and reliably compared to other methods.

![image](https://github.com/user-attachments/assets/2ee41697-53bd-4a70-ae62-30cf4feaa359)

## Conclusion

### 1. Advantages of the Thesis
The paper presents TUNIT, a truly unsupervised image translation method, which achieves the goal of image translation without any external information by combining clustering and representation learning to find pseudo-labels and style codes. Experimental results show that TUNIT performs well in both unsupervised and semi-supervised settings and is robust and scalable. In addition, the paper provides a strong baseline for developing more efficient semi-supervised image translation models.
 
### 2. Innovative points
  1. The main contribution of the paper is to propose a novel image translation framework that utilizes a combination of clustering and representation learning for unsupervised image translation.
  
  2. the method combines clustering and contrast loss by introducing a bootstrap network to improve the accuracy of the estimated domain labels and extract better feature representations.
  
  3. The method can be easily extended to semi-supervised settings, which makes it a very promising approach for image translation.
     
### 3. Future Works
  1. in future research, more efficient and lightweight models can be considered to solve these problems.
  
  2. In addition, it is also possible to explore how to apply the method to other areas, such as video conversion.  
