# VideoElevator: Elevating Video Generation Quality with Versatile Text-to-Image Diffusion Models
[paper link](https://arxiv.org/pdf/2403.05438) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method called VideoElevator that aims to improve the quality and performance of text-to-video diffusion models (T2V).          |      Diffusion Model    |

## Methodology

### 1. Abstract
While the traditional T2V method has deficiencies in frame quality and text alignment, VideoElevator takes advantage of the text-to-image diffusion model (T2I) to achieve higher quality and more personalised video synthesis results by decomposing each sampling step into two parts, namely, spatio-temporal motion fine-tuning and spatial quality enhancement. Experimental results show that VideoElevator not only significantly improves the T2V baseline performance of the underlying T2I, but also enables more stylised and personalised video synthesis.

![image](https://github.com/user-attachments/assets/cd67d25e-1914-4989-b3d4-b67e77ecda7d)

### 2. Method Description 
Specifically, VideoElevator divides the sampling process into two parts: **time domain motion correction and airspace quality enhancement**. In time-domain motion correction, a low-pass filter LPFF is first used to reduce high-frequency flicker in the video, and a priori knowledge of T2V generation is used to generate a video with natural motion. Then, more detailed motion is achieved by iterating the T2V denoising process N times. Finally, the motion integrity of the inverted time-domain motion-corrected video is maintained during the process of inverting the motion-corrected video to the noise distribution. In airspace quality enhancement, the quality of the video is improved by inflating the T2I to share the content and adding high quality details directly.

![image](https://github.com/user-attachments/assets/4d089047-49e2-4ea5-aa42-2306b276893a)

### 3. Methodological improvements
The main improvement of VideoElevator over the traditional T2I and T2V models is the introduction of the two steps of time-domain motion correction and air-domain quality enhancement. Time-domain motion correction reduces high-frequency flickering and enhances motion continuity in the video, while air-domain quality enhancement directly adds high-quality details to the video to improve the overall quality of the video.

### 4. Issues addressed 
VideoElevator solves the problem that traditional T2I and T2V models cannot satisfy both spatial and temporal consistency and high quality details. By introducing the two steps of temporal motion correction and spatial quality enhancement, VideoElevator can add high-quality details to the video while ensuring temporal and spatial consistency, thus significantly improving the effect of T2V.

## Experiments
This paper focuses on VideoElevator, an enhancement method for text-to-video diffusion models, and its performance is validated and analysed through several comparative experiments.

First, the authors compare VideoElevator quantitatively and qualitatively on two benchmark datasets, VBench and VideoCreation. On the quantitative side, the authors used five metrics to evaluate the quality of the composite video, including frame consistency, cue consistency, frame quality, aesthetic score, and domain similarity. The results show that VideoElevator significantly improves the aesthetic score and frame quality and exhibits better performance in all metrics compared to the base text-to-video model. In addition, the authors provide visual comparative results showing how VideoElevator improves the visual quality and text consistency of the generated videos.

![image](https://github.com/user-attachments/assets/93262dd8-9c56-4de4-8d2d-3b617873ad2f)

Second, the authors conducted additional experiments to validate the effectiveness of VideoElevator. One of the experiments was to apply VideoElevator to the Personalised Stable Diffusion XL (SDXL) model and compare it with other models. The results show that VideoElevator is able to better inherit the stylistic features of the SDXL model and performs better in terms of text alignment and frame quality.

![image](https://github.com/user-attachments/assets/b01ed2a0-d231-464b-b49e-1b34ff7b4f44)

In addition, the authors conducted experiments on the tuning of hyperparameters such as low-pass filters and inverse projection strategies to further optimise the performance of VideoElevator. The results show that proper low-pass filtering reduces high-frequency flickering in the video, while the DDIM inverse projection strategy results in more continuous timeline slices.

 ![image](https://github.com/user-attachments/assets/68f867af-1d4f-420f-9256-a359ead36121)

## Conclusion

### 1. Advantages of the Thesis
The method achieves this by decomposing each sampling step into two components: temporal motion optimisation and spatial quality enhancement. Spatio-temporal motion optimisation uses a low-pass filter to reduce flicker and SDEdit to add fine-grained motion; spatial quality enhancement adds more realistic detail directly using an inflated T2I model. Experimental results show that this approach significantly improves the performance of the T2V baseline, including higher frame quality and better style consistency.

### 2. Innovative points
The authors propose two novel components: spatio-temporal motion optimisation and spatial quality enhancement to achieve this goal. Spatiotemporal motion optimisation improves temporal consistency and natural motion by encapsulating T2V and preserving as much motion information as possible through a DDIM inversion process. Spatial quality enhancement, on the other hand, utilises an inflated T2I model to directly convert noisy codes to less noisy codes. In addition, the method supports interactions between various T2Vs and T2Is as long as they share clean latent variable distributions.

### 3. Future Works
  1. The method proposed in this paper has great potential to improve T2V generation, but there are still some limitations that need to be addressed. For example, the method is only applicable to trained T2I models, so more research is needed to develop unsupervised or weakly supervised learning methods.
  
  2. In addition, the method needs to further explore how to deal with complex scenes and backgrounds in videos, and how to make smooth transitions between different styles. 
