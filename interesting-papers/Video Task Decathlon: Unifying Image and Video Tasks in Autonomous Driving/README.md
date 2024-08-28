# Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving
[paper link](https://arxiv.org/pdf/2309.04422) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper introduces a new challenge, Video Task Decathlon (VTD), which aims to explore the problem of building a unified model to solve multiple heterogeneous visual tasks in autonomous driving.         |  Computer Vision         |

## Methodology

### 1. Abstract
The authors designed the VTDNet network architecture and used a training scheme called Curriculum training, Pseudo-labeling, and Fine-tuning (CPF) to successfully train the VTDNet and achieve significant performance improvements. This research provides a promising new direction for exploring the unification of perceptual tasks in autonomous driving.
![image](https://github.com/user-attachments/assets/a75c4494-ae97-4f25-9510-f75d6e4ff7f6)

### 2. Method Description 
This paper proposes a new video task challenge, Video Task Decathlon (VTD), which aims to study diverse 2D video tasks in the field of autonomous driving and to design models that can handle all 2D tasks. VTD contains ten tasks: image labelling, object detection, attitude estimation, drivable region segmentation, lane detection, semantic segmentation, instance segmentation, optical flow estimation, and multiple object tracking (MOT) and multiple object segmentation (MOTS). These tasks represent the spatial scope in the field of autonomous driving. 

The challenge is constructed based on the large real-world BDD100K video dataset, which contains annotations for a variety of vision tasks.The BDD100K consists of 100,000 driving video sequences, each approximately 40 seconds long. Tracking tasks are annotated at 5 frames/second. These tasks were annotated in three separate image sets, all of which were subsets of the original 100,000 videos. However, only a portion of the tasks in each image set were labelled. This complicates the optimisation because different tasks have different data scales and each image is only partially annotated.
![image](https://github.com/user-attachments/assets/a5f2932b-3a21-4d19-8ab3-3b3c2451b3c1)

### 3. Methodological improvements
The VTD challenge presented in this paper aims to facilitate research in multi-task learning by evaluating the performance of different models through the combination of multiple tasks. Compared with the traditional single-task challenge, the VTD provides a more comprehensive test environment that can better simulate autonomous driving applications in real scenarios. In addition, this paper proposes a proxy evaluation method for the optical flow estimation task so that the task can be evaluated without optical flow labelling.

### 4. Issues addressed 
The VTD challenge proposed in this paper addresses the research problem of multi-task learning in the field of autonomous driving. While traditional single-task challenges cannot fully reflect the reality of autonomous driving applications, VTD provides a more comprehensive test environment to better evaluate the performance of different models on multiple tasks. In addition, this paper proposes a proxy evaluation method for the optical flow estimation task so that the task can be evaluated without optical flow labelling. These improvements can help to advance the development of autonomous driving technologies and improve their reliability.

## Experiments
This paper presents a study of a multi-task learning method for Video Task Dataset (VTD) with multiple labels, and conducts several comparison experiments to verify the effectiveness of the method. The following are the specific comparison experiments:

  1. **Comparing single-task and multi-task baselines**: two baseline models were used, one single-task model and the other multi-task model. By comparing the performance of these models on VTD, it can be concluded that training all tasks jointly is better than training each task individually, but a special training strategy is required to overcome the optimisation challenges and achieve better performance.

![image](https://github.com/user-attachments/assets/d70c94d0-2caf-4fa2-bd10-b1986f699acc)

  2. **Comparing different baseline models**: the authors used two different baseline models, based on ResNet-50 and Swin Transformer. The results show that Swin Transformer performs better in both the models and hence it is recommended to use Swin Transformer as the base network.

  3. **Comparison with other multitasking models**: the authors also compared with other multitasking models, including Mask2Former and others. The results show that while some models perform well on some tasks, they perform poorly on others due to issues such as task interference and under-labelling.

![image](https://github.com/user-attachments/assets/c3b8df09-60ec-4f99-9695-a98e52a22075)

  4. **Analysis of model components**: the authors conducted several experiments to evaluate the impact of different components on model performance, including feature interaction blocks, training protocols, etc. The results show that adding feature interaction blocks significantly improves the performance of segmentation and localisation tasks, while using more complex training protocols can further improve performance.

  5. Loss weights and evaluation metrics: the authors also investigate the performance variation of the model under different loss weight configurations and propose adjustable task loss weights to meet the needs of different application scenarios. In addition, they use a custom multi-task evaluation metric, VTDA, to measure the overall performance of the model.

![image](https://github.com/user-attachments/assets/4f7f9dc3-66bc-46fa-9112-c133f5f4130a)

## Conclusion

### 1. Advantages of the Thesis
  1. A new Video Task Decathlon (VTB) challenge is proposed to promote multi-task learning in the field of autonomous driving.

  2. Several representative image and video tasks are designed and the efficiency of the single-task model is enhanced by exploring the performance difference between the single-task model and the multi-task model.
  
  3. A new multi-task model, VTDNet, combining feature interaction blocks and our CPF training protocol is proposed to significantly improve the performance of the single-task model.

### 2. Innovative points
  1. The concept of multi-task learning is introduced to improve the learning of a single task by sharing the underlying feature extractor.
  
  2. A VGG network was utilised as a feature extractor to be used in multi-task learning.
  
  3. Combined the feature interaction block and CPF training protocol to further improve the effectiveness of multi-task learning.

### 3. Future Works
  1. The method can be applied to other domains such as NLP.
  
  2. The model structure can be further optimised to make it more efficient and accurate.
  
  3. More advanced deep learning techniques, such as the self-attention mechanism, can be tried to further improve the effect of multi-task learning.  
