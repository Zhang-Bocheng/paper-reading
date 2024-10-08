# CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model
[paper link](https://arxiv.org/pdf/2403.05034) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a high-fidelity single image to 3D model generation method called Convolutional Reconstruction Model (CRM).          |convolutional neural networks (CNN)          |

## Methodology

### 1. Abstract
While traditional autoregressive model-based 3D generation methods are slow and ineffective, the CRM employs convolutional neural networks for pixel-level alignment and bandwidth optimisation, thereby improving generation speed while maintaining high quality. The method also utilises Flexicubes as a geometric representation, enabling direct end-to-end optimisation. Experimental results show that the CRM is able to generate high-quality textured meshes in just 10 seconds without any test-time optimisation.

### 2. Method Description 
This study proposes a 3D reconstruction method based on convolutional neural networks that uses a multi-view diffusion model to generate six orthogonal images and coordinate mapping charts (CCMs), which are then reduced to a 3D mesh with texture by a convolutional reconstruction model (CRM). Specifically, they used a three-plane representation to achieve high-resolution 3D results, and introduced some enhancement techniques during training to improve quality and robustness.

![image](https://github.com/user-attachments/assets/99930399-8e04-4ddf-80c8-ef6b2a439a45)

### 3. Methodological improvements
The method mainly improves the way of initialising the multi-view diffusion model and the techniques used in the training process. Firstly, they use ImageDream model as the initialisation model instead of training from scratch; secondly, they introduce techniques such as zero signal-to-noise ratio training, random scaling and contour enhancement to improve the quality and robustness of the model.

### 4. Issues addressed 
The method solves the problem of unpredictable geometry in traditional 3D reconstruction methods and also improves the accuracy and stability of the model. In addition, the method employs a flexible cube representation and a deep learning model to achieve high-quality 3D reconstruction.

## Experiments
This paper focuses on a single-image-based 3D texture mesh generation method and verifies the effectiveness of the method through several comparative experiments. Specifically, the following four comparison experiments are conducted in this paper:

**Comparison with previous work**: in this paper, the results of previous work such as Wonder3d, Sync-Dreamer, Magic123, One-2-3-45 and OpenLRM are used for comparison to verify its performance in terms of geometric quality and texture quality. The results show that the method in this paper outperforms all the baselines in terms of both geometric and texture quality.

**Comparison with Other Models**: In this paper, the method of this paper is compared with other models such as LGM and LRM to verify its performance in terms of geometric quality and texture quality. The results show that the method in this paper outperforms all the baselines in terms of geometric quality and texture quality.
![image](https://github.com/user-attachments/assets/169da91e-8fd1-47ce-913c-17e0ccd23ac5)

**The importance of input CCM**: In this paper, the effect of input CCM on model performance is investigated. The results show that when CCM is not provided, the geometry of the model output, although reasonable, is not as good as in the case where CCM is provided.
![image](https://github.com/user-attachments/assets/870e0754-03ac-4415-b57a-41995b370726)

**Effect of multi-view diffusion design**: this paper also examines the effect of multi-view diffusion model design on the effectiveness of new viewpoint synthesis. The results show that the zero SNR trick and random scaling are beneficial, while contour enhancement does not significantly improve the quantitative metrics, but it makes the model more robust.  

![image](https://github.com/user-attachments/assets/0023791e-470a-4bde-85bd-ea6eca12eec1)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a novel convolutional reconstruction model (CRM) for generating high-quality 3D models from a single image. The proposed method utilizes the spatial relationship between input images and the output triplane, resulting in improved textured meshes with significantly less training costs compared to previous transformer-based methods.
  
  2. The model operates on an end-to-end training basis, directly outputting textured meshes. The study demonstrates the effectiveness of the CRM in producing detailed textured meshes within 10 seconds.

### 2. Innovative points
  1. The authors propose a new CRM architecture that combines a convolutional encoder-decoder network with a transformer-based decoder. This architecture allows for more efficient processing of the input image and better utilization of the spatial relationships between the input images and the output triplane.
  
  2. Additionally, the use of a transformer-based decoder enables the incorporation of textual information into the 3D reconstruction process, allowing for more accurate and detailed reconstructions.
 
### 3. Future Works
  1. While the proposed CRM shows promising results in terms of speed and accuracy, further research could focus on improving the quality of the reconstructed textures and incorporating additional features such as lighting and shading.
  
  2. Additionally, exploring ways to incorporate user feedback during the reconstruction process could lead to even more accurate and personalized reconstructions.    
