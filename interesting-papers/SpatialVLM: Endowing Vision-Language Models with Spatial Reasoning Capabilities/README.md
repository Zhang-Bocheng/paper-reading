# SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities
[paper link](https://arxiv.org/pdf/2401.12168) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new approach called Spatial-VLM, which enables visual language models to better understand and answer scene-related questions by giving them spatial reasoning capabilities.           | Large Language Models         |

## Methodology

### 1. Abstract
In the experiments, the researchers used two different models: a traditional visual language model (VLM) and a Spatial-VLM with a spatial reasoning module added.The results show a significant improvement in the performance of the model with the addition of the spatial reasoning module compared to the traditional model. For example, when determining whether the robot can pass the path between the sofa and the table, Spatial-VLM can give the answer more accurately. 

In addition, Spatial-VLM can answer questions about distances based on information about object positions in images. These results show that incorporating spatial reasoning capabilities into a visual language model can improve its scene understanding and accuracy.

### 2. Method Description 
The paper proposes an approach called SpatialVLM (Spatial Visual Language Model), which aims to endow visual language models with spatial reasoning capabilities. The method first extracts object-centred contexts in images using a series of computer vision models and generates large-scale spatial VQA datasets through a templating approach. These datasets are then used to train SpatialVLMs to learn direct spatial reasoning capabilities, and finally higher-order commonsense reasoning is combined with them to achieve chained-thinking spatial reasoning.

![image](https://github.com/user-attachments/assets/e92c2437-2940-4428-9c28-8eab687a0424)

Specifically, the method includes the following steps:
  1. Filtering data suitable for synthetic spatial reasoning quizzes using a CLIP classifier.
  2. Extracting object-centred information using a series of expert models such as region proposal, region description and semantic segmentation modules.
  3. Lifting the 2D image context to a 3D point cloud context to give the notion of depth or height.
  4. For cases where there are multiple similar categories of objects, user-configurable object-centred description methods such as FlexCap are used to avoid fixed and coarse object categories and to remove ambiguities in expression.
  5. A large and diverse Spatial Reasoning quiz dataset is generated using a large number of question templates and answer templates.
  6. Use this dataset to train the SpatialVLM model for direct spatial reasoning.
  7. Combine this with higher-order common-sense reasoning to achieve chain-thinking spatial reasoning.
  
### 3. Methodological improvements
The method mainly improves the traditional visual language model in spatial reasoning by introducing multiple computer vision models and templating methods to generate a large-scale and diverse spatial reasoning Q&A dataset, so as to improve the performance of the model on spatial reasoning tasks.

### 4. Issues addressed 
The approach addresses the shortcomings of traditional visual language models on spatial reasoning tasks and improves the performance of the models when dealing with tasks that require spatial reasoning. At the same time, by incorporating higher-order commonsense reasoning, it achieves chained-thinking spatial reasoning, which further expands the application scope of the model.

## Experiments
This paper focuses on several comparative experiments for visual language models (VLMs). First, the authors create a new benchmark test for evaluating the performance of VLMs in spatial reasoning and compare it with several existing VLMs. The results show that by using the generated data to train the VLM, its spatial reasoning ability can be significantly improved. Second, the authors investigated the effect of adding more data about spatial problems on the VLM. They found that on other tasks, adding spatial data does not degrade the general performance of the VLM, but instead slightly improves its performance. 
![image](https://github.com/user-attachments/assets/15e4e624-7903-4c89-8f8c-a163dc57201c)

In addition, the authors investigate whether pre-trained visual transformer (ViT) encoders are sufficient to perform spatial reasoning and find that in some cases, freezing a ViT may not perform as well as unfreezing a ViT. Finally, the authors explore how VLM can learn generalised spatial common sense from large amounts of noisy data and show the potential of VLM for applications in robotics, e.g., as a reward annotator and chain-thinking spatial reasoning tool. 
![image](https://github.com/user-attachments/assets/f778db1e-be4c-44cf-8555-6593776a7417)

## Conclusion

### 1. Advantages of the Thesis
  1. The method learns 3D spatial relationships on massive real-world images, which enables the model to understand the positional and directional relationships between objects, and thus enables more complex visual reasoning tasks. 

  2. The advantage of this method is that it does not require any manually labelled data, but rather makes use of a large number of real-world images on the Internet to train the model, making it highly scalable and pervasive.
 
### 2. Innovative points
  1. The main innovation of this paper is that it proposes a new method to construct a large-scale 3D scene atlas and apply it to visual reasoning tasks. Specifically, the method uses a large-scale real-world image dataset to train models to learn 3D spatial relationships between objects.
  
  2. In addition, the method introduces some novel techniques, such as adaptive template design and multi-scale feature fusion, to improve the performance and robustness of the model.

### 3. Future Works
Future research can further explore how to apply the method to more visual reasoning tasks, such as robot navigation, autonomous driving, and other fields. Meanwhile, it can also consider how to combine other techniques, such as deep reinforcement learning, to further improve the performance and intelligence of the model.  
