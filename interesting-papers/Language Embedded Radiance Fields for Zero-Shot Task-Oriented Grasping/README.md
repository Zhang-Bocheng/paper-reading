# Language Embedded Radiance Fields for Zero-Shot Task-Oriented Grasping
[paper link](https://arxiv.org/pdf/2309.07970) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |This paper presents a new method called LERF-TOGO (Language Embedded Radiance Fields for Task-Oriented Grasping of Objects) for task-oriented grasping of objects in the zero-sample case.          |  LLMs |

## Methodology

### 1. Abstract
The method utilizes a visual language model and Neural Radiance Field (NERF) technology to output the grasping distribution on objects via natural language queries. Specifically, the method first reconstructs the NERF in the scene and quantizes the CLIP embedding into a multi-scale 3D linguistic field, then extracts a 3D object mask of the object using the DINO feature extractor, and queries the NERF based on the mask conditions to obtain the semantic distributions for selecting the correct grasping location. The experimental results show that Lerf-toGo successfully selects the correct portion of the grasping points on 31 different physical objects with a percentage of 81% and a success rate of 69%.

### 2. Method Description 
The Lerf-to-go method proposed in this paper aims to solve the problem of a robot grasping a specified object on a planar surface. The method determines the optimal grasping position by converting a natural language query into a 3D point cloud and calculating the correlation between each point and the target object using a LERF model. Specifically, the Lerf-to-go method consists of the following steps:

  1. Reconstruct the scene using the LERF model and generate a 3D correlation map.

  2. Generate a 3D object mask based on a natural language query for recognizing the target object.

  3. Generate a 3D part correlation map using conditional LERF queries to further localize the target part to be crawled.

  4. Generate multiple parallel gripper grasping scenarios using the GraspNet algorithm and rank the grasping scenarios based on LERF correlation and geometric quality scores.

![image](https://github.com/user-attachments/assets/bb5c115a-0d3f-40bc-a21c-3ef6b051a831)

### 3. Methodological improvements
Traditional methods based on region proposal or fine-tuning detector have some problems, such as the inability to effectively decompose some components of complex objects and the loss of language comprehension. The Lerf-to-go method, on the other hand, avoids these problems by mapping natural language queries directly into 3D space. In addition, the method introduces conditional LERF queries and non-great suppression techniques to improve the success rate of crawling.

### 4. Issues addressed 
The Lerf-to-go method mainly solves the problem of robots grasping specified objects on planar surfaces. Specifically, it can help the robot find the target object quickly and accurately and determine the optimal grasping position, thus realizing efficient and reliable robot operation.

## Experiments
This paper focuses on several experiments conducted by the authors using the Lerf-to-go algorithm and compares them with other algorithms. The following is a detailed description of each experiment:

**Part-Oriented Grasping Experiment**: This experiment was designed to evaluate the performance of the Lerf-to-go algorithm in grasping different objects and parts. The authors selected 31 different objects and 49 parts with a total of 31 objects as test objects. For each object, the authors used a natural language description to select an object query and provided a part query to determine where the robot should grab it. If successful, then the robot would be able to correctly pick up the correct object and lift it off the table to a height of at least 10 centimeters, with the object remaining in the gripper jaws at all times. The experimental results show that the Lerf-to-go algorithm performs well in task completion with a success rate of 69% and selects the correct object and part 82% of the time.

**Task-Oriented Grasping Experiment**: This experiment was designed to evaluate the ability of the Lerf-to-go algorithm to generate task-relevant parts in conjunction with a Large Language Model (LLM). The authors used ChatGPT to generate automated prompts for tasks and objects as well as parts, and used a few sample prompts to select the correct combination of objects and parts using the LLM. Experimental results show that the method recognizes the correct combination of objects and parts with a 92% success rate.

**Integration with an LLM Planner Experiment**: This experiment aims to evaluate the performance of the Lerf-to-go algorithm when integrated with an LLM planner. The authors define a set of robot manipulation instructions (e.g., grasping, pressing, twisting, etc.) and use the LLM to provide the correct instructions to accomplish a given task. The experimental results show that the method can select the correct robot manipulation instructions for a given task with a 92% success rate.

**ConceptFusion Comparison Experiment**: This experiment was designed to evaluate the performance difference between the Lerf-to-go algorithm and the ConceptFusion algorithm, which is a multimodal point cloud based method that fuses RGBD images and extracted features to produce a high quality point cloud. The authors provide depth maps so that ConceptFusion can generate the same high quality point clouds as Lerf-to-go. Experimental results show that the Lerf-to-go algorithm performs better at selecting the correct objects and parts, with a 43% success rate.

**Semantic Abstraction Comparison Experiment**: This experiment is designed to evaluate the performance difference between the Lerf-to-go algorithm and Semantic Abstraction, a single RGBD image-based method that outputs relevant heat maps based on textual queries. The authors provided single images including all object parts to fairly represent both methods. The experimental results show that the Lerf-to-go algorithm performs better in selecting the correct objects and parts with a success rate of 80%.

**OWL-ViT Comparison Experiment**: This experiment aims to evaluate the performance difference between the Lerf-to-go algorithm and the OWL-ViT algorithm, an open vocabulary detector that outputs segmentation mappings based on RGB images and textual cues. The authors provided single images including all object parts to fairly represent both methods. Experimental results show that the Lerf-to-go algorithm performs better in selecting the correct objects and parts with a success rate of 85%.

## Conclusion

### 1. Advantages of the Thesis
  1. This research proposes a new method, Lerf-ToGo, for task-oriented object grasping in a zero-sample manner by using a large visual language model.
  
  2. Lerf-ToGo is based on the previous work Language Embedded Radiance Fields (LERF) and improves upon it by enhancing the spatial grouping capability of LERF to support hierarchical object part queries.
  
  3. Experimental results show that Lerf-ToGo successfully grasps the correct object under natural language guidance and can specify the object part as 81%, and achieves a success rate of 69% when performing task-oriented grasping on a physical robot.

### 2. Innovative points
  1. Lerf-ToGo proposes a DINO eigenfield-based approach to predict 3D object masks to address the lack of spatial grouping in LERF.
  
  2. Lerf-ToGo also designed a conditional LERF query method that restricts the object subpart query to object masks only, taking advantage of the multi-scale nature of LERF to isolate specific regions in the object.
  
  3. Lerf-ToGo uses GraspNet to generate crawls and re-rank them based on geometric and semantic distributions.

### 3. Future Works
  1. The paper mentions that future efforts will focus on adding additional regularization and optimizing LERF training to reduce computation time.
  
  2. Also, support for hierarchically structured groups of objects is needed to handle the case of multiple connected foreground objects.
  
  3. The paper also mentions some limitations and directions for future work, such as evaluating for more tasks and supporting more complex expressions (e.g., “the cup next to the vase”).
