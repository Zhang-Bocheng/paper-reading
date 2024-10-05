# VLOGGER: Multimodal Diffusion for Embodied Avatar Synthesis
[paper link](https://arxiv.org/pdf/2403.08764) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a method called ‘VLOGGER’ that generates high-quality human videos from a single input image and easily controls the video length with advanced human face and body representations          | Diffusion Model         |

## Methodology

### 1. Abstract
Unlike previous work, the method does not need to be trained for each individual and does not rely on face detection and cropping, while taking into account a wide range of scenarios (e.g., visible torsos or diverse subject identities) that are critical for correctly synthesising humans in communication. In addition, the authors created a new and diverse large-scale dataset, MENTOR, for training and validating the main technical contributions. Experimental results show that ‘VLOGGER’ outperforms existing methods in three public benchmark tests, making significant progress in terms of image quality, identity retention and temporal consistency. Finally, the authors demonstrate the application of VLOGGER to video editing and personalisation.

### 2. Method Description 
The paper presents a framework called VLOGGER for generating high-quality, realistic videos for human-machine interaction. The framework consists of two phases: **audio-driven motion generation and generation of realistic human videos**. In the first phase, Network M generates intermediate body movement controls based on input speech and uses these controls to predict facial expressions and 3D poses. Then, in the second phase, the predicted body controls are converted into corresponding frames using a conditional image-to-image translation model to generate realistic videos.

![image](https://github.com/user-attachments/assets/5fdecba8-ae2a-477a-8fd5-fe0e81e2040d)

### 3. Methodological improvements
Compared to the traditional diffusion model, the model proposed in this paper introduces a parametric representation of the 3D mannequin, allowing the model to better capture the details of the face and body movements. In addition, the model employs a temporally continuous image rendering technique to ensure better smoothness and continuity in the generated video.

### 4. Issues addressed 
The method proposed in this paper can effectively address problems in natural speech synthesis, such as lack of fluency and realism. By combining 3D human body models and temporally continuous image rendering techniques, the method can generate more realistic and natural videos, thus improving the quality and efficiency of human-computer interaction. The method can also be applied to virtual reality and augmented reality to provide a more immersive experience for users.

## Experiments
This paper focuses on presenting the VLOGGER model for the audio-driven video generation task and verifying its performance and advantages through comparison experiments with several baseline approaches. Specifically, the authors conduct the following comparison experiments:

**Ablation Study**: the authors show the impact of different design choices on model performance, including the use or non-use of time loss functions, prediction residuals, etc. And, the authors compare the impact of different 2D control methods on the quality of image reconstruction, including a keypoint-based approach, a dense representation, and the authors' proposed control method that combines a dense representation with a reference partial view.

![image](https://github.com/user-attachments/assets/c46e8920-315c-4868-937a-ddd0ecb1181b)

**Quantitative Results**: The authors compare VLOGGER with multiple other baseline methods on the HDTF and TalkingHead-1KH datasets, evaluating the performance of the models in terms of photo-realism, lip-synchronisation, diversity, identity preservation and temporal consistency. The results show that VLOGGER achieves the best performance on several metrics, especially on expression diversity and photo authenticity.

![image](https://github.com/user-attachments/assets/39036a25-b320-417c-bf2e-8b10ff715673)

**Qualitative Results**: The authors demonstrate the generation results of the VLOGGER model, including the generated video frames, the differences between multiple videos, and the edited video results. These results show that VLOGGER is capable of generating more diverse expressions and gestures and has good editing capabilities.

![image](https://github.com/user-attachments/assets/ffa5cf78-4570-4d17-b1c9-9513204bd2ce)

## Conclusion

### 1. Advantages of the Thesis
The method is a temporal extension of the control diffusion model, using 3D face head and body pose representations as the underlying framework, while introducing a large and diverse dataset and validating its performance on multiple other datasets, demonstrating its superiority in the task of talking avatar generation and its robustness across different axes of diversity. In addition, the study explores the potential of VLOGGER for downstream applications such as video editing and personalisation.

### 2. Innovative points
  1. VLOGGER is a novel approach to automatically generate human video compositions, including face and body, which requires solving a number of complex problems such as data acquisition, representation of natural expressions, synchronisation of audio with expression, occlusion, and whole-body motion.
  
  2. The method employs a two-step approach: firstly, body movements and facial expressions are predicted by generating a diffusion network, based on the input audio signal; secondly, a novel architecture based on the nearest-image diffusion model is proposed, which provides control in both the temporal and spatial domains.
  
  3. In addition, the approach takes into account all aspects of human communication, including gestures, gaze, blinks, and postures, resulting in more realistic and diverse motion representations.
     
### 3. Future Works
With the development of technology, VLOGGER is expected to be widely used in various fields in the future, such as content creation, entertainment, and gaming. In addition, the method can be further improved to enhance the quality and diversity of generated videos and explore more application scenarios.    
