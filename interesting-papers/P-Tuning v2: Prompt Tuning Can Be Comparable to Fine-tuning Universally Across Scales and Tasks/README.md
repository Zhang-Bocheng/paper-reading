# P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks
[paper link](https://arxiv.org/pdf/2110.07602) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper presents a novel approach called “P-Tuning v2” for optimizing the performance of pre-trained models in natural language understanding (NLU) tasks.          |  Pre-trained Language Models (PLMs)        |

## Methodology

### 1. Abstract
The approach significantly reduces the amount of storage and memory usage required for each task by tuning successive cues without having to fine-tune the entire model. Although previous studies have shown that cue tuning is not as effective on normal-sized pretrained models, the authors find that properly optimized cue tuning can be universally effective across a wide range of model sizes and NLU tasks. Compared to fine-tuning, P-Tuning v2 requires only 0.1%-3% parameter tuning and performs quite well.

### 2. Method Description 
This paper proposes a new deep cue tuning (P-tuning v2) approach to address the limitations of cue tuning on different scales and tasks. Compared to traditional continuous cue tuning, P-tuning v2 adds cues in different layers and uses more tunable parameters to improve performance. And, P-tuning v2 provides optimization and implementation details including reparameterization, cue length, multi-task learning, and classification headers.

![image](https://github.com/user-attachments/assets/469bb701-5dd8-4341-b8f4-c5d58f0c5c40)

### 3. Methodological improvements
  1. Added multiple layers of cues to make model prediction more straightforward.
  2. Increased the number of tunable parameters, improving the model's capabilities.
  3. Provided some optimization and implementation details such as reparameterization, cue length, multi-task learning, and classification headers.

### 4. Issues addressed 
The P-tuning v2 method proposed in this paper addresses the limitations of cue tuning on different scales and tasks. Specifically, the method can be adapted to larger scale models and can achieve better performance on different natural language understanding (NLU) tasks. What is more, P-tuning v2 provides some optimization and implementation details that can help users better apply the method.

## Experiments
This paper focuses on the effectiveness of P-tuning v2 on different pre-trained models and natural language understanding tasks, and compares it with fine-tuning. Specifically, the authors conducted the following three comparison experiments:

**Performance of P-tuning v2 on pre-trained models of different sizes**: the authors used multiple tasks from the SuperGLUE dataset to test the effectiveness of P-tuning v2 and compared it with Lester et al. (2021) and fine-tuning. The results show that P-tuning v2 performs comparably or even better than fine-tuning on smaller scale models, while on larger scale models, P-tuning v2 gradually approaches fine-tuning, but only requires 0.1% of the task-specific parameters.

![image](https://github.com/user-attachments/assets/c63ea9db-413c-4335-be52-500e37320e93)

**Performance of P-tuning v2 on different tasks**: the authors tested the effectiveness of P-tuning v2 using several sequence annotation tasks (e.g., named entity recognition, extractive Q&A, and semantic role annotation) and compared it to P-tuning and Lester et al. (2021). The results show that P-tuning v2 performs comparably to fine-tuning on all tasks, while P-tuning and Lester et al. (2021) perform poorly on some tasks.

![image](https://github.com/user-attachments/assets/9141b2bc-d10d-4b16-9e3b-29e07ae77aed)

**The role of different components in P-tuning v2**: The authors compare two key components in P-tuning v2, the continuous cue and the classifier, and analyze their impact. The results show that using continuous cues instead of a classifier improves performance, while adding continuous cues to deeper layers improves performance further.  

## Conclusion

### 1. Advantages of the Thesis
Compared to the traditional cueing approach, P-tuning v2 tunes only continuous cues and improves performance by increasing the capacity of continuous cues. Experimental results show that P-tuning v2 outperforms the cueing approach on a variety of hard sequence labeling tasks, as well as being more parametrically efficient.

### 2. Innovative points
The main contribution of this paper is the discovery that P-tuning v2 can compete with fine-tuning methods on a variety of model sizes and NLU tasks. The core of the method is the use of continuous cues instead of discrete cues, tuning only the continuous cues and applying them to pre-trained models at each layer. And, the authors provide some key optimizations and implementation details to ensure that the performance of P-tuning v2 is comparable to fine-tuning methods. 

### 3. Future Works
Future research can explore how to further improve the performance of P-tuning v2 and try to extend it to other areas such as image processing. It could also be investigated how P-tuning v2 can be combined with other techniques, such as adaptive learning rate and dynamic learning rate decay, to further improve the performance.    
