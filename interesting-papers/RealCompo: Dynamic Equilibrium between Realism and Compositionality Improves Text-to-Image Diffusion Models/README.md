# RealCompo: Dynamic Equilibrium between Realism and Compositionality Improves Text-to-Image Diffusion Models
[paper link](https://arxiv.org/pdf/2402.12908) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces RealCompo, a new text-to-image generation framework that aims to leverage the strengths of both text-to-image models and spatially-aware image diffusion models to improve the realism and combinability of generated images.          |   Diffusion Models       |

## Methodology

### 1. Abstract
 By introducing an intuitive and novel balancer that dynamically balances the strengths of the two models during the denoising process, it allows any model to be used seamlessly without additional training. Experimental results show that RealCompo consistently outperforms state-of-the-art text-to-image models and spatially-aware image diffusion models for multi-object combinatorial generation, and maintains satisfaction with the realism and combinatoriality of the generated images. In addition, RealCompo can be easily extended to various spatially-aware image diffusion models and stylised diffusion models.

### 2. Method Description 
The RealCompo method proposed in this paper aims to achieve a dynamic balance between realism and combinatoriality in the image generation process. The method is mainly applied to layout-based text-to-image (L2I) models by designing a novel balancer to adjust the prediction noise between two different models and updating the coefficients based on the feedback of the cross-attention map to maintain the localisation capability while injecting realistic information. In addition, the method can be extended to other text-to-image diffusion models based on spatially-aware conditions, such as the keypoint-to-image (K2I) model and the segmentation-to-image (S2I) model.

![image](https://github.com/user-attachments/assets/df527cc8-1df2-43fe-af37-ca86bfc41637)

### 3. Methodological improvements
The main innovation of the RealCompo method compared to previous methods is the use of a loss function to measure the degree of match between the cross-attention map and the layout, and using this as a basis for updating the weighting coefficients of the prediction noise. This method is not only stable and reliable, but also effective in improving the quality and diversity of the generated images.

### 4. Issues addressed 
The RealCompo method proposed in this paper addresses the problem of how to achieve a dynamic balance between realism and combinatoriality in the image generation process. By designing a novel balancer and combining it with the feedback mechanism of the loss function, the method is able to enhance the diversity and aesthetic value of the generated images while ensuring their quality. Meanwhile, the method can be extended to other text-to-image diffusion models based on spatially-aware conditions, which has a wide range of application prospects.

## Experiments
This paper focuses on four experiments of the RealCompo framework, including the Experimental Setup, Benchmarking and Main Results, Extended Application, and Ablation Study. In the experiments, the authors used several T2I and L2I models and compared them to evaluate the performance in terms of Compositionality and Realism.

First, in the experimental setup section, the authors chose different T2I and L2I models as backbone and used tools such as ViT-B-32 and LAION aesthetic predictor to calculate assessment metrics such as CLIP score and aesthetic score. A user study was also designed to assess the practical performance of the various methods.

Next, in the benchmarking and main results section, the authors compare RealCompo with the best current T2I and L2I models and draw the following conclusions:
![image](https://github.com/user-attachments/assets/eb40abb4-9d64-49a5-b85b-fc6d5406da59)

&emsp;RealCompo achieves state-of-the-art performance on all seven tasks, with significant advantages especially in spatial and numerical aspects;
<br>&emsp;RealCompo enhances image realism and aesthetic quality with dynamic balancers, while maintaining a high degree of combinability;
<br>&emsp;RealCompo achieves excellent user ratings, especially in terms of realism and combinatorial capabilities.

Then, in the Extended Applications section, the authors further explore RealCompo's application scenarios, including more spatially-aware conditions and stylised generation. Specifically, the authors found that RealCompo can be applied to a wide range of spatial-awareness conditions, such as layout, keypoints, and segmentation mapping, and enables powerful combinatorial generation. In addition, the authors try to apply RealCompo to different pre-trained stylised T2I models and draw the following conclusions:
<br>&emsp;RealCompo is able to inherit the style of T2I models perfectly and enables powerful combinatorial generation with help;
<br>&emsp;RealCompo preserves styles better than the current outstanding stylised models and also achieves better combinatorial capabilities.

Finally, in the Ablation Study section, the authors explore the importance of dynamic balancers and the effects of combining them with other models. Specifically, the authors found that when the dynamic balancer was not used, the generated images could not be aligned with the layout, resulting in reduced combinability and controllability. And when combining RealCompo with other models, it allowed for seamless model switching and more satisfying results.  

![image](https://github.com/user-attachments/assets/742990bc-842f-4530-9e60-2e01d9ce845c)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents RealCompo, a new training-free and transferred-friendly text-to-image generation framework that enhances combinatorial text-to-image generation by dynamically balancing the advantages of verisimilitude and combinatoriality.

  2. The authors design a novel balancer that dynamically combines prediction noise from T2I models and spatially-aware (e.g., layout, keypoints, segmentation mapping) image diffusion models.

  3. RealCompo is flexible enough to be generalised to balance various (stylised) T2I models and spatially-aware image diffusion models, and enables high-quality combinatorial stylised generation. It provides a new research perspective on combinatorial image generation.

### 2. Innovative points
  1. RealCompo uses pre-trained conditional statement-based image diffusion models and autoregressive generation models to generate images.

  2. RealCompo uses LLMs to generate scene layouts from textual cues, and then uses an innovative balancer to dynamically combine pre-trained T2I models and spatially-aware image diffusion models.

  3. RealCompo provides a flexible way to adjust the style of the T2I models to enable style-specific combinatorial generation.

### 3. Future Works
  1. RealCompo has achieved significant performance gains in generating multiple objects and complex relationships, but there is still room for improvement.

  2. In future work, the authors will continue to improve the framework, using a more robust backbone and extending it to more realistic applications.  
