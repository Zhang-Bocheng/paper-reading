# DiLightNet: Fine-grained Lighting Control for Diffusion-based Image Generation
[paper link](https://arxiv.org/pdf/2402.11929) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a new approach that allows for fine-grained illumination control in diffusion model-based image generation.          | Diffusion Model         |

## Methodology

### 1. Abstract
Existing diffusion models can generate images under any lighting condition, but lack control over the correlation between image content and illumination. In addition, textual cues lack the expressive power needed to describe detailed lighting settings. In order to provide content creators with fine-grained control over lighting during image generation, the authors added detailed lighting information to the textual cues in the form of radiative cues, i.e., visualisations of scene geometries having a homogeneous baseline material under the target illumination. However, the scene geometry needed to produce the radiative cue is unknown. Therefore, the authors propose a three-stage approach to control illumination during image generation. 

First, an initial image under uncontrolled illumination conditions is generated using a standard pre-trained diffusion model. Next, in the second stage, foreground objects in the generated image are re-synthesised and optimised by passing the target illumination to a refined diffusion model (named DiLightNet) and using radiance cues computed on foreground objects using rough shapes. In order to preserve texture details, the authors multiply the radial cues with the neural encoding of the initial synthesised image before passing it to DiLightNet. Finally, in the third stage, the authors resynthesised the background consistent with the illumination on the foreground objects. The authors validated their lighting-controlled diffusion model under a variety of textual cues and lighting conditions with good results.

### 2. Method Description 
This thesis presents a diffusion model-based image synthesis method for generating images with foreground objects that are consistent with the target illumination, given text cues, target illumination conditions, and shape and texture control seeds. The method is divided into three main stages: provision of temporary image generation, synthesis using radial cues, and background filling.

Firstly, in the first stage, a temporary image unaffected by controlled illumination is generated by feeding text cues and shape/texture control seeds into a pre-trained diffusion model. The goal of this stage is to determine the shape and texture of the foreground objects.

Next, in the second stage, based on the temporary image generated in the previous stage and the target illumination conditions, radiometric cues are computed and multiplied by a neurally encoded version of the temporary image. The result is then passed to DiLightNet along with text cues and shape/texture control seeds to generate an image with foreground objects that are consistent with the target illumination.

Finally, in the third stage, the final image is generated by performing background filling under target illumination conditions.
![image](https://github.com/user-attachments/assets/b8bd2d68-cfa9-4554-a152-e7de1265cb2a)

### 3. Methodological improvements
The method employs a diffusion model for image synthesis by including various shapes, materials, and illumination conditions in the training set so that the model can learn how to generate images that match these conditions. In addition, the method uses radial cues to guide colour changes during the synthesis process, allowing the generated image to better reflect the effects of light interactions under the target lighting conditions.

### 4. Issues addressed 
The method addresses the problem of how to generate images with foreground objects that are consistent with the target illumination, given text cues, target illumination conditions, and shape and texture control seeds. By using a diffusion model and radial cues, the method is able to adaptively adjust the colours to match the target lighting conditions while maintaining the original shape and texture information. This method can be applied to a variety of scenarios, such as virtual reality, game production, and other application areas that require high-quality images.

## Experiments
This paper presents experimental results and comparative experiments with the DiLightNet model. The model was implemented using PyTorch and further optimised using stable diffusion v2.1 as a pre-trained diffusion model. The authors conducted two user studies to measure perceived lighting accuracy and appearance consistency under varying lighting conditions. In addition, the authors conducted several quantitative and qualitative Ablation Studies to better understand the impact of different components on the method.

Firstly, the authors conducted a quantitative evaluation to quantify the error rates of different model variants by selecting high-quality synthetic objects from the Objaverse dataset. The authors compared the difference between passing a preparatory image directly to ControlNet versus multiplying the encoded preparatory image. The authors also compared the effect of different amounts of reflected light cues and whether or not to include a foreground mask on model performance. Finally, the authors also tested the effect of three training data enhancement schemes (colour, material and normal) on model performance.

For the user study, the authors designed three image pairing groups, where each group contained four pairings. The first study was based on the same pairing groups but used different pairings. The second study was of image pairs generated under rotating ambient lighting. The authors used four level rating criteria to measure the similarity of each pairing and calculated an average total score. The results showed that DiLightNet demonstrated good illumination similarity and appearance consistency in all three categories.

![image](https://github.com/user-attachments/assets/ad4b521b-1840-4318-9c51-69c47eef28a7)

## Conclusion

### 1. Advantages of the Thesis
  1. The method controls the illumination effects by using coarse illumination cues as well as an encoder-based diffusion network and matches the generated image to the textual cues and target illumination while preserving the texture information.
  2. In addition, the authors show that their method can work under different types of lighting conditions and conduct extensive experiments to demonstrate its effectiveness.

### 2. Innovative points
  1. The methodological innovation of this paper is that it provides a new way to control the lighting conditions in a diffusion model without the need to explicitly specify the lighting direction or the environment map.
  2. The method utilises established techniques such as depth estimation and foreground mask generators and applies them to generate synthetic images with fine illumination control.
  3. Additionally, the method can generate multiple replicas for better understanding of ambiguous interpretations of material properties.

### 3. Future Works
The methodology of this paper provides many interesting directions for future research. For example, the method can be extended to illumination control of images under a single illumination of a single photograph, or it can be used in combination with other methods to improve the quality of the generated images. In addition, the use of additional material property information could be further explored to enhance the effectiveness of the method.   
