# EmerDiff: Emerging Pixel-level Semantic Knowledge in Diffusion Models
[paper link](https://arxiv.org/pdf/2401.11739) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the application of diffusion models to semantic segmentation tasks and presents a new method called EmerDiff.          |  Diffusion Models        |

## Methodology

### 1. Abstract
The method utilises the semantic knowledge extracted by Stable Diffusion (SD) and is able to generate highly accurate pixel-level semantic segmentation maps without additional training. By exploiting the generation process of SD, the authors make connections between image pixels and the spatial locations of low-dimensional feature maps and use these connections to construct high-resolution segmentation maps. Experimental results show that the resulting segmentation maps are able to depict the detailed parts of the image well, demonstrating the existence of highly accurate pixel-level semantic knowledge in the diffusion model.

### 2. Method Description 
This study uses a pre-trained diffusion model to generate fine-grained segmentation maps. A low-resolution segmentation mask is first generated by applying the k-means algorithm on a low-dimensional feature map. Each pixel is then mapped to the most relevant low-resolution mask to construct a high-resolution segmentation mask. In order to find the semantic correspondence between image pixels and masks, the researchers exploited the ability of the diffusion model to generate high-resolution images and applied it to process contextual information on the spatial dimensions of the low-resolution feature maps.

![image](https://github.com/user-attachments/assets/a45849bf-f563-4062-9dc2-c3caeb9ac47b)
 
### 3. Methodological improvements
The researchers chose a particular architecture, Stable Diffusion (SD), which has a lower dimension and higher performance when using the diffusion model. They also used the U-Net structure from the Attention Mechanism and focused on 16x16 resolution block of modules as these contain rich semantic information. In addition, they used the modulation technique of cross-attention layers in processing low-resolution feature maps in order to better capture the semantic links between image pixels and masks.

![image](https://github.com/user-attachments/assets/9d6e20fc-6f82-48d5-95dd-0a511def7759)

### 4. Issues addressed 
The method addresses the problem of how to generate fine-grained segmentation maps using pre-trained diffusion models. By utilising the diffusion model's ability to generate high-resolution images, as well as targeting semantic information to specific blocks of modules, the researchers successfully achieved this goal. This approach can provide more accurate and fine-grained segmentation results for computer vision tasks, thereby improving the effectiveness of related applications.

## Experiments
This paper focuses on the use of diffusion models to generate high-quality semantic segmentation masks, and conducts several comparative experiments to verify their performance and effectiveness.

Firstly, in the experiments, the authors compare their method with traditional semantic segmentation methods. On a standard semantic segmentation dataset, the authors used the traditional evaluation protocol where pixels must be classified as the same number of concepts as the number of categories in the dataset in order to match concepts to categories in the dataset via Hungarian matching. The results show that although this method produces clear and accurate segmentation masks, it performs poorly when dealing with datasets with a large number of categories. In addition, the authors modified this method to allow access to annotations and create concept embeddings to further improve performance. The results show that this method performs better than other self-supervised learning methods based on text-image pairs.

![image](https://github.com/user-attachments/assets/59c34665-366f-486d-8991-6b01dbe7144b)

Secondly, the authors compared their method with a diffusion model based approach. They used SD (Stable Diffusion) as a benchmark, which is a recently proposed self-supervised learning method based on the diffusion model. The results show that their method produces more accurate and clearer segmentation masks than SD.

![image](https://github.com/user-attachments/assets/3ead1d7d-4d77-4c9d-9a83-44340f0eb895)

Finally, the authors also compare their method with other self-supervised learning methods based on text-image pairs. These methods include CLIP, TCL and CLIPpy. The results show that their method produces better performance than these methods. 

![image](https://github.com/user-attachments/assets/b24489c9-e4db-4109-a5e1-e728b04f2e0a)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes an unsupervised image segmenter based on a pre-trained diffusion model that can generate fine-grained pixel-level semantic segmentation maps using only the semantic knowledge extracted from the diffusion model. The method is extensively experimentally validated on multiple scene-centred datasets with surprising results, demonstrating the presence of highly accurate pixel-level semantic knowledge in the diffusion model.

### 2. Innovative points
  1. The main contribution of this paper is to propose an unsupervised image segmenter based on the diffusion model, which does not require any additional knowledge or annotation information to generate fine pixel-level semantic segmentation maps.
  
  2. The authors first cluster low-dimensional feature mappings into several semantic categories by applying the k-means algorithm, and then construct a high-resolution semantic segmentation map based on the correspondence between these semantic categories and high-resolution pixels.
  
  3. The advantage of this approach is that it is simple and efficient, and at the same time, it can make full use of the semantic knowledge in the diffusion model, thus improving the quality of the segmentation results.

### 3. Future Works
Considering our generated pseudo-masks as part of a weakly supervised framework may be a promising direction. In addition, although the method in this paper is built on Stable Diffusion, the basic idea can be applied to various generative models, which is one of the future research directions.   
