# UltrAvatar: A Realistic Animatable 3D Avatar Diffusion Model with Authenticity Guided Textures
[paper link](https://arxiv.org/pdf/2401.11078) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a novel 3D avatar generation method called UltrAvatar, which enables more realistic animated 3D avatar generation by enhancing the quality of geometric fidelity and physically based rendering textures.          |  Diffusion Model        |

## Methodology

### 1. Abstract
 The method uses a denoising diffusion model compared to existing methods and proposes a fidelity-based texture diffusion model for generating more diverse 3D avatars.

### 2. Method Description 
The paper presents a framework for generating high-quality 3D avatars based on a diffusion model. Firstly, a noiseless view I is generated using a diffusion model by inputting a facial image or textual cue, and a DCE model is used to extract the separated colour of the face in addition to the effect of lighting. Then, this separated colour is used to train an AGT-DM model to generate high-quality PBR textures including normal mapping, highlight mapping, roughness mapping, and so on. Finally, the FLAME model is used to generate 3D avatars and combine them with PBR textures.

![image](https://github.com/user-attachments/assets/b056001e-cace-4a85-a607-972c7df7d658)

### 3. Methodological improvements
**Removing the effect of lighting using a DCE model: **traditional 3D avatar generation methods are usually affected by lighting, which leads to a degradation of the quality of the generated avatar. Instead, the method introduces a DCE model to remove lighting effects, thus improving the quality of the avatar.

**Generate high-quality PBR textures using AGT-DM models:** Traditional 3D avatar generation methods usually only generate low-resolution textures that lack detail. This method, however, uses the AGT-DM model to generate high-quality PBR textures, including normal mapping, highlight mapping, roughness mapping, etc., which makes the generated avatar more realistic.

### 4. Issues addressed 
**How to improve the quality of 3D avatars:** traditional 3D avatar generation methods usually only produce low-resolution avatars with a lack of details. This method can generate high quality 3D avatars by using DCE models and AGT-DM models.

**How to eliminate the effect of lighting:** Traditional 3D avatar generation methods are usually affected by lighting, resulting in a degradation of the quality of the generated avatar. The method introduces a DCE model to eliminate the effect of lighting, thus improving the quality of the avatar.

## Experiments
This paper conducts several comparative experiments to validate the effectiveness of their proposed AGT-DM approach. Specifically, they compare AGT-DM with five other state-of-the-art text-to-avatar generation models and two image-to-avatar generation models. These models include Latent3d, CLIPMatrix, Text2Mesh, CLIPFace, DreamFace, FlameTex, and PanoHead. In the experiments, the authors used several evaluation metrics to measure the performance of each model, including FID, LPIPS, SSIM, MS-SSIM, ECCV, and NLPCC. Below are the details of each comparison experiment:

**Text-to-avatar generation model comparison experiment**
In this experiment, the authors use several evaluation metrics such as FID, LPIPS, SSIM, MS-SSIM, ECCV, and NLPCC to compare the performance of AGT-DM with five other state-of-the-art text-to-avatar generation models. The results show that AGT-DM exhibits the best performance in most of the metrics, especially in generating faces with high quality details and realism. This proves that AGT-DM is a very effective text-to-avatar generation method.

![image](https://github.com/user-attachments/assets/f33fe754-68e8-4841-9555-b350c4380848)

**Comparison Experiment of Image to Avatar Generation Models**
In this experiment, the authors used several evaluation metrics such as FID, LPIPS, SSIM, MS-SSIM, ECCV and NLPCC to compare the performance of AGT-DM with two other state-of-the-art image-to-avatar generation models. The results show that AGT-DM exhibits the best performance in most of the metrics, especially in generating faces with high quality details and realism. This further proves that AGT-DM is a very effective method for avatar generation. 

![image](https://github.com/user-attachments/assets/e5af7af0-0d69-4436-bba4-f88813276da1)

## Conclusion

### 1. Advantages of the Thesis
The core of the method is based on the design of a Deep Convolutional Encoder (DCE) model designed to eliminate unwanted illumination effects in the source image and guide the texture generation model with light and edge signals to preserve the PBR details of the avatar. The method generates realistic 3D avatars with higher quality and fidelity in the case of either textual cues or single images compared to current state-of-the-art methods.
 
### 2. Innovative points
The main innovation of this thesis is the use of a Deep Convolutional Encoder (DCE) model and a Neural Radiation Field (NeRF) based technique, while an Adaptive Light Topology Mapping (AGT-DM) technique is introduced to enhance the robustness and diversity of the model. In addition, the method employs GPT-4V(vision) for automatic performance evaluation, which improves the reliability and practicality of the model. 

### 3. Future Works
This thesis provides a new research direction in the field of 3D avatar generation, which can be further explored to apply the method to other fields, such as virtual reality and game development. In addition, attempts can also be made to combine the method with other technologies, such as motion capture, speech recognition, etc., so as to achieve a more natural and intelligent human-computer interaction experience.  
