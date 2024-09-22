# ITI-GEN: Inclusive Text-to-Image Generation
[paper link](https://arxiv.org/pdf/2309.05569) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores the problem of bias in text-to-image generation models and proposes a new approach called ITI-GEN to address this problem.          | Computer Vision         |

## Methodology

### 1. Abstract
Traditional text-to-image generation models tend to reflect biases in the training data, leading to unequal representation of certain groups. ITI-GEN takes a new approach to inclusive text-to-image generation using existing reference images. The method does not require fine-tuning of existing models and is therefore computationally efficient and easy to implement. Experimental results show that ITI-GEN provides a significant improvement in generating inclusive images relative to current state-of-the-art models.

### 2. Method Description 
The paper proposes a method called ITI-GEN (Image Text Inclusive Generation) for generating images with specified attributes. The method is based on a pre-trained text-to-image generation model G and controls the generated images by learning prompts that contain information about specific attributes. Unlike the traditional discrete language-space based specification approach, ITI-GEN optimises the prompt in continuous embedding space and updates only attribute-specific embeddings, thus enabling plug-and-play applications.

Specifically, ITI-GEN uses the reference image set Drmef to construct a directional consistency loss and a semantic consistency loss for each target attribute Am to bootstrap the learning of prompt. In addition, ITI-GEN uses large-scale multimodal models such as CLIP to connect visual concepts to textual embeddings, avoiding the need to modify text-to-image models.

![image](https://github.com/user-attachments/assets/3a2df9cb-d1f6-429c-9518-9427924b1bf5)

### 3. Methodological improvements
  1. Compared to the traditional discrete language-space based specification, ITI-GEN employs optimisation in a continuous embedding space, which allows for more flexible control over the generated images.
  
  2. At the same time, ITI-GEN updates only attribute-specific embeddings while leaving other embeddings unchanged, which improves computational efficiency.

  3. In addition, ITI-GEN introduces directional consistency loss and semantic consistency loss to bootstrap the learning of the PROMPT for better control of the generated images.

### 4. Issues addressed 
The method solves the problems of traditional discrete language space based specification, such as difficulty in expressing certain complex attributes and susceptibility to quality degradation. By using the optimisation approach in continuous embedding space and introducing directional consistency loss and semantic consistency loss, ITI-GEN can control the generated images more accurately and with high computational efficiency.

## Experiments
This article mainly introduces the author's experiments on image generation under different attributes and scenes using the ITI-GEN method, and compares it with other methods. Specifically, the author conducted the following experiments:

**Single binary attribute experiment**: 40 different reference image sets were constructed on the CelebA dataset, each representing a specific binary attribute and containing an equal number of positive and negative instances. The author used 5 different text prompts to generate 200 images, and the results showed that ITI-GEN performed well in balancing each binary attribute.

![image](https://github.com/user-attachments/assets/2199d2a5-93cf-459b-9bb4-890667c344f0)

**Multiple attribute experiments**: The author further investigated the situation of multiple attributes, including perceived age and skin color. By constructing two challenging settings (perceived gender x age and perceived gender x skin color), the authors demonstrated that ITI-GEN can achieve diversity across all combinations and significantly reduce distribution differences.

![image](https://github.com/user-attachments/assets/42e90d15-832e-44bd-8b19-ce8b9aa38f8b)

![image](https://github.com/user-attachments/assets/62f13039-eeeb-409a-9263-720ea0a30c7a)

**Scene Image Experiment**: In addition to human faces, the author also applies ITI-GEN to another field - scene images. They believe that this inclusive text to image generation is not only applicable to humans, but also to scenes, objects, and even environmental factors. Specifically, they use images from the LHQ dataset as guidance to learn inclusive tokens and generate images with diverse subjective perceptual attributes. For example, in the figure, ITI-GEN can enhance the generated image into multiple color levels, thereby demonstrating its generality for different domain attributes.  

![image](https://github.com/user-attachments/assets/fa3c9ec6-3cd7-46c9-bbe1-0cda2fed3526)

## Conclusion

### 1. Advantages of the Thesis
  1. A new method has been proposed to achieve text to image generation, which improves inclusiveness by utilizing available reference images.
  
  2. The method is simple, compact, universal, and effective, with good results in various applications.
  
  3. It can handle data from multiple attributes and different domains, and can be used for relatively complex prompts beyond the scope of training data.
 
  4. Extensive experimental validation has been conducted in various fields, providing insights into various modeling choices and mechanisms.
  
  5. For some subtle facial features or highly entangled attribute combinations, ITI-GEN does not always provide the best results.

### 2. Innovative points
  1. Using visual guidance to learn separable embedding vectors to represent different attributes of interest.
 
  2. Designed a new training target in the joint embedding space that aligns the direction of the image and the prompt features.
  
  3. Convert visual attribute differences into natural language differences to ensure that the generated images effectively represent all required categories.
 
  4. Compatible with existing text-based image generation models and featuring plug-in functionality.

### 3. Future Works
  1. Further research is needed to better address the issues of subtle facial features or highly entangled attribute combinations.
  
  2. More ways may need to be explored to mitigate the risk of bias or inaccuracy introduced by reference images.
  
  3. Further explore the integration of ITI-GEN with other technologies such as robust control to improve the quality and diversity of generated images.  
