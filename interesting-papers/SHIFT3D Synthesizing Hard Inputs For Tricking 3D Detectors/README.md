# SHIFT3D: Synthesizing Hard Inputs For Tricking 3D Detectors
[paper link](https://arxiv.org/pdf/2309.05810) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a differentiable pipeline called SHIFT3D for generating structurally sound shapes that are challenging for 3D detectors.          | Computer Vision         |

## Methodology

### 1. Abstract
Downstream 3D detectors are obfuscated by using an SDF representation of the object and using a gradient error signal to smoothly deform the shape or pose of the object. This approach provides interpretable failure modes for modern 3D object detectors and helps to identify potential safety risks before they become critical failures. Experimental results show that the method is capable of generating shapes that are different from the baseline object but semantically recognisable, and can provide insight into unknown vulnerabilities in safety-critical applications such as autonomous driving.

### 2. Method Description 
The paper presents a method called SHIFT3D for generating adversarial object shapes and poses in LiDAR scenes. The method uses a Sign Distance Function (SDF) network to find the shape embedding vector of an object and insert it into a scene with realistic rendering occlusion. The shape and pose parameters of the object are then optimised by minimising the detector score to generate adversarial examples.

Specifically, the method first uses an SDF network to learn the shape of the object and maps the shape embedding vectors to a given pose. Then, the object is inserted into the LiDAR scene at a given pose and which points are occluded based on the SDF function is determined. Finally, the shape and pose parameters are updated by backpropagation until the desired detector score is achieved.

![image](https://github.com/user-attachments/assets/1d3938ee-7b4d-4a72-8503-d8de72149e29)

### 3. Methodological improvements
Unlike traditional point cloud-based attacks, SHIFT3D does not require direct manipulation of 3D points, but generates adversarial examples by making small changes to the shape and pose of objects. This approach makes the generated examples more natural and resistant to some of the defence techniques against point cloud attacks. And, the method takes into account some physical constraints, such as not overlapping with other objects and contacting with the ground, which improves the quality and realism of the generated examples.

### 4. Issues addressed 
The method addresses the problem of generating adversarial object shapes and poses in LiDAR scenes. It can generate more natural and challenging examples, while also avoiding some of the problems faced by traditional attack methods, such as not being able to produce realistic occlusion effects or being easily detected as an attack. Thus, the method can improve the effectiveness of adversarial training and enhance the robustness of the model.

## Experiments
This paper focuses on a method called SHIFT3D used by the authors to generate adversarial samples and experimentally validated on the Waymo Open Dataset (WOD). The method generates effective adversarial samples that make the performance of the detector degrade while maintaining the physical reality of the object. The authors experimentally demonstrate the effectiveness and robustness of SHIFT3D and also show that this approach is potentially useful for improving detection models.

![image](https://github.com/user-attachments/assets/33410477-8790-4128-9c7a-d783021d6efb)

Specifically, the authors first describe the datasets and models they used, including PointPillars and SST models trained using LiDAR point cloud data and 3D bounding box annotations from the Waymo Open Dataset (WOD), and DeepSDF models used to generate benchmark objects. The authors then detail their experimental setup, including inserting benchmark objects into randomly selected WOD scenes and recording detection results under different conditions. Then, the authors provide a detailed analysis and discussion of the experimental results, including the evaluation metrics and scores of the generated adversarial samples in terms of their effectiveness, robustness and transferability. Finally, the authors also explore the feasibility of using SHIFT3D-generated objects to improve the robustness of the model and present the experimental results.

![image](https://github.com/user-attachments/assets/630c34a1-b904-4b49-8ad9-a2cfbabed024)

![image](https://github.com/user-attachments/assets/38b5bda9-313e-44eb-8296-97f53271ddc5)

Overall, the main contribution of this paper is to propose an effective method to generate adversarial samples and demonstrate its feasibility and effectiveness in practical applications. In addition, the authors show some interesting results, such as some similarities between the adversarial shapes output by Shift3D and real vehicles in natural scenes, which provide new ideas to improve the detection model.  

## Conclusion

### 1. Advantages of the Thesis
This paper presents an approach called SHIFT3D that provides prior insights by generating challenging natural examples to detect failure modes in 3D vision systems. The method can effectively obfuscate 3D detectors in self-driving vehicles and can be robust and transferable across different scenarios. In addition, the method provides multiple advantages, such as exploring new parts of the input distribution and explaining which shape changes cause the most difficulties.

### 2. Innovative points
The main innovation of the method is the use of generative models to synthesise challenging 3D objects and apply gradient perturbations on these objects to confuse downstream models. Unlike traditional adversarial attack methods, this method creates 3D objects with observable variations that reflect meaningful challenges. Moreover, the method can combine pose and shape deformations of the objects while ensuring that the generated objects look naturally realistic.

### 3. Future Works
The method can be applied to other fields such as medical image processing and robot navigation. Therefore, future research should focus on improving this method and extending it to a wider range of applications. 
