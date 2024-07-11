# GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
[paper link](https://arxiv.org/pdf/2112.10741) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new method for image synthesis and editing, GLIDE (Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models).         | Diffusion Models          |


## Methodology

### 1. Abstract
   The method uses diffusion models for text-conditioned image synthesis and compares two different guidance strategies: **CLIP guidance and classifier free guidance**. The experimental results show that classifier free guidance is more popular with human evaluators and produces more realistic samples. In addition, the authors found that their model can be used for image filling and robust text-driven image editing.
   
### 2. Method Description 
  The text-conditional diffusion model proposed in this paper is a noise diffusion-based image generation technique that progressively reduces noise by adding Gaussian noise to a given sample and uses a model with differentiable fractional transfer probabilities to predict the posterior distribution at each time step. This approach allows for high-quality text-conditional image generation by training a model to learn how to map text conditions into the image feature space.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/db827401-52d0-48ac-8a2e-b7e4a51c3a4c)

### 3. Methodological improvements
  This paper proposes several improvements to enhance the quality of textual conditional diffusion models:

  1. A structure analogous to a deep neural network is used instead of the traditional Restricted Boltzmann Machine (RBM) structure.
  
  2. An autoregressive module is introduced to enhance the model's memory capability.
  
  3. Multiple hidden layers are added, allowing the model to better capture detailed information in the image.
  
  4. More efficient training algorithms such as Stochastic Gradient Descent (SGD) and Adam optimizer are used.
  
### 4. Issues addressed 
  The main contribution of this paper is to propose a new text-conditional diffusion model which can be used for high-quality text-conditional image generation. In addition, this paper proposes some improvement methods which can further improve the quality and efficiency of the model.
  
## Experiments
  This paper presents experimental results on image generation tasks using CLIP and GLIDE, a generative model for unguided diffusion, and discusses the safety of GLIDE.

In terms of experiments, the authors first compare the effect of two different methods using CLIP and unguided diffusion for zero-sample generation on the MS COCO dataset. By observing the changes in metrics such as FID, Precision/Recall, and Inception Score, it is found that when using CLIP guidance, the model is able to better match the given cue, but at the same time, it may over-rely on the CLIP model and fail to truly understand the meaning of the cue. In contrast, the unguided diffusion approach, while not matching the cues exactly, struck a better balance between quality and variety.

The authors then conduct a number of other comparative experiments, such as comparing GLIDE to existing models such as DALL-E, as well as exploring questions such as whether using CLIP-guided diffusion leads to more violent or discriminatory generation results. Overall, the GLIDE model outperforms other models in a number of ways, and a number of measures have been taken to minimize potential risks in terms of security.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a4c3cdfd-1a5e-4d78-b4c8-be398759d3a1)

## Conclusion
### 1. Advantages of the Thesis
  1. This paper proposes GLIDE to improve the performance of the diffusion model by using CLIP or classifier free guidance to steer the diffusion model towards the textual cues and by refining the model for editing functionality. 
  
  2. The method is capable of rendering a wide range of textual cues in the zero-sample case and also has the capability of iterative improvement to better meet the needs of complex cues.
  
  3. In addition, the method can be used to produce realistic disinformation or Deepfakes, so the authors provide a filtered model for researchers to use.

### 2. Innovative points
  1. In this paper, CLIP guidance and classifier free guidance are used and an experimental comparison reveals that classifier free guidance produces higher quality images.
  
  2. In addition, the authors propose image restoration techniques that enable the model to modify existing images based on natural language cues, further improving the usefulness of the model.
     
### 3. Future Works
  1. The method can also be used to create realistic disinformation or Deepfakes, which needs to draw our attention and take appropriate measures to prevent its misuse.
  
  2. The filtered model provided by the authors also facilitates subsequent research that can help us better understand the workings and limitations of the diffusion model.
