# Recent Advance in 3D Object and Scene Generation: A Survey
[paper link](https://arxiv.org/pdf/2504.11734) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper reviews recent advances in static 3D object and scene generation in recent years and establishes a comprehensive technical framework through systematic classification.          | Scene Generation         |

## Methodology

### 1. Abstract
The article first introduces the mainstream 3D object representation methods, and then delves into data-driven supervised learning methods and deep generative model-based object generation techniques. For scene generation, the article focuses on three dominant paradigms: layout-guided combinatorial synthesis, 2D a priori-based scene generation and rule-driven modelling. Finally, the article critically analyses persistent challenges in 3D generation and suggests directions for future research. The survey aims to provide readers with a structured understanding of current state-of-the-art 3D generation techniques, while inspiring researchers to explore more in this area.

![image](https://github.com/user-attachments/assets/0c1c90a0-f78d-4513-8f49-8900fe8da153)

### 2. Method Description 
This paper mainly introduces the development status and research progress of 3D object and scene generation techniques. Among them, for 3D representations, the paper elaborates on three methods, namely explicit, implicit and hybrid, and lists specific application cases respectively. In addition, the article also discusses the application of both data-driven and generative model-based approaches in 3D object generation, including the use of pre-trained models such as CLIP to enhance the generation effect under zero-sample conditions.

![image](https://github.com/user-attachments/assets/5152289f-dfb7-4953-bc72-bcd1780dd320)

### 3. Methodological improvements
Compared with traditional 2D image generation techniques, 3D object and scene generation faces more challenges, such as complex geometric structures and high-dimensional data processing. Therefore, to address these issues, researchers have proposed many new methods and techniques, such as using deep learning models for end-to-end 3D object generation, combining multiple 3D representations to improve the generation quality, and so on.

### 4. Issues addressed 
The research on 3D object and scene generation technology can be applied to the fields of virtual reality and game development to provide users with more realistic and rich interactive experiences. Meanwhile, the technology can also be used in medical image processing, architectural design, etc., which has a wide range of application prospects.

![image](https://github.com/user-attachments/assets/966caa48-1300-427b-86df-1472e6c8f5c7)

## Experiments
This paper presents an exploration of evaluation metrics and potential research directions in the field of 3D generation. Firstly, the authors discuss objective and subjective evaluation methods and mention some commonly used metrics, such as PSNR, SSIM, LPIPS, Chamfer Distance, Intersection over Union and so on. However, these metrics do not fully reflect the quality and diversity of 3D content, so a multidimensional evaluation framework is needed to simultaneously consider aspects such as geometric accuracy, physical realism, and semantic consistency.

Next, the authors propose several potential research directions. The first one is about the research on controllability. Currently, automated generation tools are still difficult to satisfy users' requirements for geometric details and appearance features, while rule-based procedural modelling, although having good controllability, the complexity of designing the rule system and algorithmic implementations also increases the technical threshold. Therefore, extracting scene features using linguistic and visual models to support reverse procedural modelling is a promising research direction. Next is research on physical feasibility, which can improve the physical plausibility of generated objects by combining physical constraints and generative models. Finally, there is research on infinitely scalable scenes, which needs to address the challenges of storage and transmission requirements as well as structural and texture consistency. 

![image](https://github.com/user-attachments/assets/2ea662d6-462d-47cf-ae8f-ee63159fea16)

## Conclusion

### 1. Advantages of the Thesis
  1. The article systematically reviews, classifies and summarises research on 3D object and scene generation. The authors propose different methods for 3D object generation, including rule-based, physical simulation-based, and graphical model-based methods.
  2. The article details text-to-3D scene generation methods, including diffusion process-based, neural network-based, and other methods.
  3. The article discusses the challenges in the current research and suggests possible future research directions.

### 2. Innovative points
  1. The main contribution of the article is a comprehensive overview of the field of 3D object and scene generation, covering a wide range of methods and techniques.
  2. The article provides a clear categorisation and summary, enabling the reader to better understand the differences, strengths and weaknesses between the different approaches.
  3. For text-to-3D scene generation, the article also introduces some new approaches, such as diffusion process-based and neural network-based approaches, which have high potential for practical applications.

### 3. Future Works
Future research could explore more efficient and accurate algorithms to improve the quality and speed of the generated results. It is also possible to combine 3D object and scene generation with other fields, such as virtual reality and augmented reality, to realise more application scenarios. In addition, new techniques such as deep learning can be considered to improve existing methods to further enhance the quality and diversity of the generated results.  
