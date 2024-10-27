# FlashTex: Fast Relightable Mesh Texturing with LightControlNet
[paper link](https://arxiv.org/pdf/2402.13251) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a new method, called FlashTex, that allows for rapid automatic texturing of input 3D models and can be controlled by user-supplied text prompts.         | Text-to-Image Model         |

## Methodology

### 1. Abstract
The method allows the model to be correctly rendered and re-illuminated in any lighting environment by separating lighting from surface material/reflectivity. To achieve this, the authors introduce LightControlNet, a new text-to-image model based on the ControlNet architecture that passes the desired lighting to the model as a condition map. Their text-to-texture pipeline is then divided into two phases: the first phase uses LightControlNet to generate a set of visually consistent reference views; the second phase applies a texture optimisation algorithm based on Score Distillation Sampling (SDS) to improve the texture quality and to further separate the surface material from the illumination. This approach is significantly faster compared to previous text-to-texture approaches, while also producing high-quality, relightable textures.

### 2. Method Description 
The paper presents a technique called ‘text-to-texture’ for converting text cues into renderable texture maps. The technique consists of two main phases: **multi-view visual cueing and texture optimisation**. In the first phase, high-quality 2D images are synthesised using the multi-view visual prompting method to capture multiple views of an object. These images are processed through LightControlNet along with the given textual prompts to obtain high-resolution, detail-rich images. In the second stage, texture optimisation is performed using the SDS loss function to ensure that the generated textures are of good quality and consistency and can be adapted to different lighting conditions.

![image](https://github.com/user-attachments/assets/ce3dee0d-34be-4aeb-947d-1f2d67006131)

### 3. Methodological improvements
  1. In the first stage, LightControlNet was used to control the lighting conditions in order to generate object images with the desired shape and lighting effects.
  
  2. Multi-view visual prompting method is used to avoid consistency problems that occur when each reference image is entered independently.

  3. In the second stage, texture optimisation is performed using SDS loss function along with multiresolution hash mesh as 3D texture representation.

### 4. Issues addressed 
  1. How to generate high quality texture maps based on a given text cue;

  2. How to ensure consistency and quality of the generated texture maps under different lighting conditions.

## Experiments
This paper focuses on five experiments using the Objaverse dataset to evaluate text-driven relightable text-based mesh texture generation methods. These experiments include quantitative and qualitative comparisons as well as validation of the importance of each of the main components.

In the experiments, the authors first trained their LightControlNet using the Objaverse dataset and selected approximately 40,000 objects from that dataset as a training set. Then, they used 70 random mesh assets as a test set and collected 22 mesh assets from 3D online games for evaluating their method. In addition, the authors selected existing methods such as Latent-Paint, Text2tex, and TEXTure as baselines and compared them.

For quantitative evaluation, the authors used Frechet Inception Distance (FID) and Kernel Inception Distance (KID) to assess the quality and runtime of each method. The results show that the authors' methods outperform all baselines in terms of quality and runtime.

![image](https://github.com/user-attachments/assets/e04044ed-2465-436d-b5fe-7543455d7479)

In terms of qualitative analysis, the authors show that their method can generate highly detailed textures and can correctly render ambient lighting under different rotations. Compared to other existing methods such as Fantasia3D, the authors' results are not only of higher visual quality, but also enable more successful separation of lighting effects.
![image](https://github.com/user-attachments/assets/ffac4e0e-7399-4cc4-abad-3fb5843fe9a3)

The authors also conducted a user study to further assess texture quality. Participants were asked to assess the realism of the results, their consistency with the input text, and their plausibility when placed under different lighting conditions. The results showed that participants consistently preferred the authors' approach.

Finally, the authors conducted several partial experiments to validate the importance of the various components of their method. For example, when replacing their dilution encoder, performance decreases without significant improvement. When removing the multi-view visual cues for initial generation, the system requires more iterations to produce reasonable results, which can lead to slightly poorer texture quality. Therefore, each component of the authors' approach is important, and they work together to make it possible to generate high-quality relightable text-based mesh textures.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a method for automatically texturing an input 3D model based on user-provided cues. The method uses a lighting-aware 2D diffusion model (LightControl-Net) and an improved optimisation process based on SDS loss.
  
  2. The method significantly improves speed and produces high-fidelity textures compared to previous methods, while separating illumination from surface reflectance/diffuse reflectance. The authors demonstrate the effectiveness of the method through quantitative and qualitative evaluations on the Objaverse dataset.

### 2. Innovative points
  1. The main contribution of the paper is the proposal of an efficient automated texturing technique that automatically generates high-quality 3D model textures based on user-supplied cues and correctly re-illuminates them under different lighting environments.
  
  2. Specifically, the approach introduces LightControl-Net, an illumination-aware text-to-image diffusion model based on the ControlNet architecture, which allows the desired illumination to be applied as a conditional image in the diffusion model.
  
  3. In addition, the paper proposes a new optimisation process that combines multi-view visual cues and SDS sampling techniques to generate re-lightable textures with high quality in two stages.

### 3. Future Works
  1. Although the algorithm proposed in this paper has achieved good results in quantitative and qualitative evaluation, there are still some limitations. For example, baked light may occur in some cases, especially on 3D meshes outside the training data distribution.
  
  2. In addition, the generated material mappings may sometimes not be fully decoupled, making it difficult to interpret properties such as metallicity. Future research could attempt to address these issues and further improve the speed and quality of the algorithm.    
