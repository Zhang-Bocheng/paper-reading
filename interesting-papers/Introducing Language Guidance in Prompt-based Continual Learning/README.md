# Introducing Language Guidance in Prompt-based Continual Learning
[paper link](https://arxiv.org/pdf/2308.15827) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a method called ‘Language Guidance for Prompt-based Continual Learning’ to address the catastrophic forgetting problem in continuous learning.          |          |

## Methodology

### 1. Abstract
The method uses a pre-trained language encoder to map categories in different tasks into the same embedding space, and introduces language guidance at the level of cue pools and visual encoder output features. Experimental results show that the method performs better than existing cue-based continuous learning methods and does not require additional learning parameters.

### 2. Method Description 
This thesis proposes a continuous learning method based on cue learning that aims to achieve continuous learning of a task by utilising pre-trained models and cues. Specifically, the method uses a pre-trained image feature extractor and a pre-trained linguistic feature extractor and applies them to visual and linguistic input data, respectively. In each new task, the method uses learnable cues from a pool of cues to guide the model in learning new task knowledge, rather than retraining the entire model or storing data from previous tasks. In addition, the method introduces linguistic guidance to further mitigate the forgetting problem.

![image](https://github.com/user-attachments/assets/b1b5ccaf-a03f-4134-b015-f750d522c4f4)

### 3. . Methodological improvements
Compared to traditional continuous learning methods, the method does not need to store data from previous tasks, thus providing better scalability and efficiency. In addition, the method can dynamically add prompts as needed to accommodate different task requirements. Also, the method introduces linguistic guidance to help the model better understand and categorise different classes of objects.

### 4. Issues addressed 
The method solves many of the problems that exist in traditional continuous learning methods, such as storing large amounts of data, high computational costs, and the tendency to forget old tasks. In addition, the method improves the generalisation ability and accuracy of the model, allowing it to better cope with unknown tasks and scenarios.

## Experiments
This paper focuses on the performance of the model LGCL (Language Guided Continual Learning) using language guidance in a continuous learning task and compares it with some existing methods. Specifically, the authors conducted the following experiments:

On two datasets (Split ImageNet-R and Split CIFAR-100), the performance differences between LGCL and two regularisation-based methods (Learning to Prompt and Dual Prompt) and a memory-based architecture (L2P) were compared. The results show that LGCL significantly outperforms these methods, improving both in terms of average accuracy and forgetfulness.

![image](https://github.com/user-attachments/assets/f89b1670-d9dc-49b4-9b42-a034b84bb9a0)

Ablation experiments were conducted for different components in LGCL, including task-level language loss, category-level language loss, and the effect of using both simultaneously. The results show that each component in LGCL improves the performance of the model, and using both modules together further improves the performance of the model.

![image](https://github.com/user-attachments/assets/8e92d47e-8487-4a80-b902-fdd9baefbf72)

The performance improvement of LGCL for each task was analysed and compared to the model without LGCL. The results show that LGCL reduces the rate of model performance degradation at each stage, thus mitigating the catastrophic forgetting problem.

![image](https://github.com/user-attachments/assets/2253cb1f-1e04-4366-87bf-263c71f6ac90)

Selective Ablation experiments with Text Transformer were conducted to verify whether LGCL is robust to text encoder selection. The results show that LGCL achieves good results with different text encoders.

![image](https://github.com/user-attachments/assets/3f27a04c-a56d-47f7-95a6-ff55f936cc30)

Finally, Ablation experiments with Prompt Pool design are conducted to verify whether the design of Prompt Pool affects the performance of LGCL. The results show that better performance can be obtained by using a learnable Prompt Pool. 

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a new perspective that introduces linguistic guidance in prompt-based continual learning to mitigate the forgetting problem. The approach mitigates forgetting and improves performance by mapping task labels with varying task distributions into the same linguistic space, enabling the model to learn to map features into this shared linguistic representation. Furthermore, the method requires no additional learning parameters or memory requirements, achieving state-of-the-art performance on two challenging continuous learning benchmarks.
  
### 2. Innovative points
The main innovation of the method is the introduction of the concept of language guidance, which guides the model through the learning process by guiding it at two levels: **the task level and the category level**. At the task level, the authors propose task-level linguistic guidance by motivating the model to map the keys in its learnable cue pool to a shared linguistic representation of all categories. At the category level, the authors encourage the model to match the output features of the visual encoder to its corresponding category-level linguistic representation. These innovative approaches not only improve the performance of the model, but also do not require any additional learning parameters or memory requirements.

### 3. Future Works
The method provides a novel solution for prompt-based continual learning, but there are still some issues that require further research. For example, how to better select shared language representations and how to balance the trade-off between forgetting and new knowledge between different tasks. These issues may be addressed in future research to further improve the effectiveness of continuous learning.
