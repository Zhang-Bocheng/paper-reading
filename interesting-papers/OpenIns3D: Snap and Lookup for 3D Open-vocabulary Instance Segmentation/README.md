# OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation
[paper link](https://arxiv.org/pdf/2309.00616) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |This paper introduces a new open-vocabulary scene understanding framework based on 3D point clouds, OpenIns3D, which adopts a "Mask-Snap-Lookup" scheme           | LLMs         |

## Methodology

### 1. Abstract
The " Mask" module learns a class-independent 3D point cloud mask proposal, "Snap" module generates multi-scale synthetic scene images and extracts interesting objects using a 2D visual language model, "Lookup" module generates a multi-scale synthetic scene image in "Snap" module, "Lookup" module generates a multi-scale synthetic scene image in "Snap" module and extracts interesting objects using a 2D visual language model. The "Lookup" module searches through the results of "Snap" and assigns category names to the proposed masks.

This approach is simple yet effective, achieving state-of-the-art performance on indoor and outdoor datasets for a variety of 3D open-vocabulary tasks, including recognition, target detection, and instance segmentation. In addition, OpenIns3D can easily switch between different 2D detectors without retraining. When integrated with a powerful 2D open world model, it achieves excellent results for scene understanding tasks. Finally, when combined with the use of LLM-driven 2D models, OpenIns3D demonstrates the power to process complex textual queries that require sophisticated reasoning and real-world knowledge.

![image](https://github.com/user-attachments/assets/9f1b3215-c9b5-45b7-a7ee-2ba96c0b258e)

### 2. Key Concept
_Vision-Language Model_: A type of artificial intelligence model that combines both visual understanding and NLP capabilities. These models aim to bridge the gap between vision and language modalities, enabling machines to comprehend and generate descriptions of visual content.

## Experiments
This paper focuses on the experimental design and result analysis of the OpenIns3D model. In the experiments, the authors conducted multifaceted comparative experiments for the open vocabulary recognition task on 3D point cloud data and came up with the following conclusions:

  1. For the zero-sample classification task, OpenIns3D's Synap and Lookup methods outperform all other methods on ScanNetv2, including the latest language-aligned large-scale 3D base models.

![image](https://github.com/user-attachments/assets/ccd965a7-0572-499d-ad29-26026869a0f9)

  2. In the 3D Open Vocabulary Instance Segmentation task, OpenIns3D achieves significant improvements on both S3DIS and ScanNetv2 compared to PLA and its successor work, RegionPLC and Lowis3D.

![image](https://github.com/user-attachments/assets/4af713cd-ad4b-46e2-8f15-fc2277d282b2)

  3. On STPLS3D, OpenIns3D has better performance than the baseline model.

  4. OpenIns3D also achieved good results in the 3D open vocabulary object detection task.
     
![image](https://github.com/user-attachments/assets/b246cec0-9931-47d3-aa7d-b688ab116252)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new 3D open-vocabulary scene understanding pipeline, Mask-Snap-Lookup (M-S-L), which converts scene-level information into queryable image representations by generating realistic masks in the 3D domain and using 2D image rendering techniques, and then using 2D visual language model to query these images for accurate 3D object recognition results.
  
  2. This approach does not require input 2D images, so it can be better adapted to different types of scenes and can easily evolve with 2D models without retraining. In addition, the authors have conducted extensive experimental evaluations, including comparisons with other state-of-the-art 3D object detectors and segmenters, as well as Ablation studies for different datasets. 

### 2. Innovative points
The main contribution of this paper is to propose a new 3D open vocabulary scene understanding pipeline, Mask-Snap-Lookup (M-S-L). This pipeline employs a variety of techniques and strategies to achieve the task of 3D object recognition and segmentation, including: <br>&emsp;methods for generating realistic masks in the 3D domain; 
<br>&emsp;the use of 2D image rendering techniques to convert scene-level information into queryable image representations; 
<br>&emsp;and the use of a 2D visual language model to query these images to obtain accurate 3D object recognition results. 

### 3. Future Works
  1. reconstruction inaccuracies may occur when dealing with small objects, which may affect its performance in certain application scenarios.
  
  2.  In addition, there are some other techniques and strategies that can be used to improve the performance and efficiency of OpenIns3D, such as more efficient mask generation algorithms, better 2D image rendering techniques, and more powerful 2D visual language models. 
