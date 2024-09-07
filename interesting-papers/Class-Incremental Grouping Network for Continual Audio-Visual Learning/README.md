# Class-Incremental Grouping Network for Continual Audio-Visual Learning
[paper link](https://arxiv.org/pdf/2309.05281) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores the problem of continuous learning on non-static data, especially for audio and visual modalities.          | Transfer Learning         |

## Methodology

### 1. Abstract
The authors propose a new network structure, the Class Incremental Grouping Network (CIGN), that learns category-level semantic features and uses learnable audio and visual class tokens and audio and visual groupings for continuous aggregation. In addition, CIGN uses category token distillation and continuous grouping to prevent forgetting parameters learned in previous tasks, thus improving the model's ability to capture discriminative audio and visual categories. Experimental results show that CIGN achieves state-of-the-art incremental learning performance for audio and visual categories in the VGGSound-Instruments, VGGSound-100, and VGG-Sound Sources benchmarks.

### 2. Method Description 
In this paper, a new Class-Incremental Grouping Network (CIGN) is proposed for implementing audio-visual continuous learning. The network is mainly composed of two modules: **audio-visual class tokens distillation** (Audio-Visual Class Tokens Distillation) and **audio-visual continuous grouping** (Audio-Visual Continual Grouping). In the Audio-Visual Class Tokens Distillation module, previous class tokens are constrained to have the same distribution of class tokens as in the current task by introducing learnable audio-visual incremental class tokens, and audio and visual features are connected to class token embeddings using a self-attentive transformer. In the audio-visual continuous grouping module, audio-visual incremental category markers and aggregated features are used as inputs using a set of combinatorial blocks to generate category-aware incremental embeddings.

![image](https://github.com/user-attachments/assets/8a1ac794-91f4-43b6-8829-20f7a09b1cd2)

### 3. Methodological improvements
  1. The introduction of learnable audio-visual incremental category labelling allows the model to better learn the distinction between old and new categories.
  
  2. More accurate audio-visual matching is achieved by using a self-attention transformer and a global similarity vector to compute the similarity between audio-visual features.
  
  3. Simultaneous optimisation of audio-visual category probabilities using cross-entropy loss and KL scatter loss further improves the performance of the model.
Problem Solved.

### 4. Issues addressed 
The CIGN method proposed in this paper addresses the problems in incremental audio-visual category learning, i.e., how to efficiently handle cross-modal associations of audio-visual information and how to prevent old category markers from being forgotten. By introducing learnable audio-visual incremental category labelling and using an audio-visual continuous grouping module, CIGN is able to achieve incremental audio-visual class learning by learning new categories while maintaining old category labelling. Experimental results show that CIGN exhibits better performance on multiple datasets relative to other methods.

## Experiments
This paper focuses on the authors' novel audio visual learning framework, CIGN, and validates its effectiveness by comparing it with other continuous learning methods. Specifically, the authors conducted the following comparison experiments:

On the VGGSound-Instruments dataset, CIGN is compared with eight other continuous learning methods, including EWC, LwF, iCaRL, IL2M, BiC, POD-Net, SSIL and L2P. The experimental results show that CIGN achieves the best results in all three category incremental settings (audio, visual and audio-visual), outperforming current state-of-the-art methods such as dual cueing and L2P.

![image](https://github.com/user-attachments/assets/87374323-2727-434d-810c-a60b2ceb6e25)

On the VGGSound-100 and VGGSound Source datasets, the authors further compare the effectiveness of CIGN with other continuous learning methods. The experimental results show that CIGN also performs significantly better than existing methods on these datasets.

![image](https://github.com/user-attachments/assets/aa967a13-628b-4207-a533-ecd43ba33c6b)

AB experiments were conducted to explore the impact of introducing the Audio Visual Class Token Distillation and Audio Visual Continuous Grouping modules on performance. The experimental results show that both modules significantly improve the classification accuracy and reduce the forgetting rate.

The ability of CIGN to support a flexible number of incremental tasks is further validated. The authors used CIGN for continuous training on the VGGSound-100 dataset for 10 tasks, and the results show that CIGN is still able to achieve competitive results.

![image](https://github.com/user-attachments/assets/a46c219f-71a0-47f3-8c4b-0a63c740b0c0)

Finally, the authors demonstrate the quality of the category-aware audio visual representation learned by CIGN. Visualisation by t-SNE reveals that the audio visual embeddings extracted by CIGN are compact within categories and separated between categories, whereas the other methods suffer from mixing. 

## Conclusion

### 1. Advantages of the Thesis
CIGN utilises learnable audio-visual category tokens and audio-visual groupings to continuously aggregate category-aware features, and introduces category token distillation and continuous grouping to mitigate the effect of forgetting parameters on previous tasks, thereby capturing more discriminative audio-visual categories. 

### 2. Innovative points
  1. The main contribution of CIGN, a novel class incremental learning network, is the proposed method of audio-visual category token distillation and continuous grouping to alleviate the cross-modal forgetting problem. 
  
  2. CIGN uses learnable audio-visual category tokens to continuously aggregate category-aware features and group different categories together via audio-visual grouping to better capture cross-modal category information.
  
  3. In addition, CIGN introduces category token distillation and continuous grouping techniques to avoid forgetting important parameters from previous tasks, thus improving the generalisation ability of the model.

### 3. Future Works
Future directions for improvement may include increasing the number of learnable category tokens to support the task of open-set audio-visual classification without additional training. Since data bias may cause the model to fail to predict certain rare but important audio-visual categories, these issues need to be further addressed to enable CIGN to be more useful in real-world applications.  
