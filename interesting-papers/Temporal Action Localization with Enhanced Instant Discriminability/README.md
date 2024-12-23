![image](https://github.com/user-attachments/assets/74497ce5-dc1e-4e18-bb23-e4c382c021fc)# Temporal Action Localization with Enhanced Instant Discriminability
[paper link](https://arxiv.org/pdf/2309.05590) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a one-stage framework called TriDet for solving the problem of unclear action boundaries in videos.           | Transformer         |

## Methodology

### 1. Abstract
The framework includes a triangular header to model the action boundaries and uses a scalable granularity perception layer to mitigate the instantaneous discriminability problem in transformer-based approaches. In addition, the paper leverages the powerful representation capabilities of pre-trained large-scale models to further improve the immediate discriminability of video backdrops, and designs a separated feature pyramid network to provide rich spatial contextual information. Experimental results show that TriDet performs well on several TAD datasets, including the multi-labelled TAD dataset.

### 2. Method Description 
The paper proposes a spatio-temporal feature fusion method based on a single-stage detector to solve the accuracy problem in action recognition. Specifically, they use two different types of backbone networks: **temporal-level backbone and spatial-level backbone**, and utilise two corresponding feature pyramids. for temporal-level backbone, they employ the pre-trained VideoMAEv2 model, while for the spatial-level backbone, they used the pre-trained DINOv2 model. Then, they fused the feature pyramid of these two backbones and introduced a new SGP layer for capturing multi-granularity motion information. Finally, they designed a boundary-directed Trident-head for accurate boundary localisation.

### 3. Methodological improvements
Compared to traditional methods based on pairwise interactions, this approach avoids the problems of high computational complexity and low accuracy. Meanwhile, by introducing a spatial-level backbone and SGP layer, it can better handle the information of long distance and the relationship between multiple moments. In addition, they proposed a boundary-orientated Trident-head that can locate the action boundary more accurately.

### 4. Issues addressed 
The method mainly addresses the problem of accuracy in action recognition. Traditional methods tend to consider only the global information and ignore the detailed information of each moment, resulting in the inability to accurately locate the action boundary. This method, on the other hand, is able to better handle multi-granularity action information and the relationship between multiple moments, thus improving the accuracy of action recognition.

## Experiments
This paper focuses on TriDet, a novel approach in the field of Multi-Task Action Detection (MTAD), which is experimented and analysed in several aspects. Specifically, this paper conducts comparative experiments in the following aspects:

**Comparing performance on different datasets**: the superior performance of TriDet is demonstrated on two publicly available datasets (THUMOS14 and HACS) in comparison with other state-of-the-art methods.

![image](https://github.com/user-attachments/assets/02b2d1f2-47e6-4d8c-998e-fe1f2fe9c0a0)

**Comparing the performance of different models**: TriDet's superiority over other models is demonstrated by comparing it with TriDet using three different pre-trained models (I3D, SlowFast and VideoMAEv2), tested on three datasets.

![image](https://github.com/user-attachments/assets/d1e4cf91-3435-49cb-aa46-de9db78ce5a8)

**Comparing the effect of different components:** the importance of the SGP layer and Trident-head for improving detection performance is demonstrated by replacing them with other methods, respectively.

![image](https://github.com/user-attachments/assets/a8ca2a47-5fec-4cb5-8f2b-92afede4d276)

**Comparing the effects of different architectures:** by comparing different types of convolutional neural network structures, it is demonstrated that improvements to Trident-head can further improve detection performance.

![image](https://github.com/user-attachments/assets/81e9747a-bcec-4f64-aa84-68a4d861def4)

**Comparing the effects of different fusion strategies:** by comparing different types of fusion strategies, it is demonstrated that delayed fusion can better preserve spatial-level contextual information and thus improve the prediction ability of the detection head.

![image](https://github.com/user-attachments/assets/cadb0627-4752-4859-8c7a-994e8c92d2c9)

**Error analysis:** by analysing the error types and features, the strengths and weaknesses of TriDet are revealed, providing guidance for further optimisation.

## Conclusion

### 1. Advantages of the Thesis
  1. A new framework, TriDet, is proposed that addresses the problems in existing TAD tasks by introducing a three-stage feature extraction network and an adaptive learning rate adjustment strategy.
  2. TriDet uses an objective function specific to action boundaries and designs the training strategy accordingly, which improves the performance of the model.
  3. TriDet has been extensively experimentally validated on multiple datasets and achieves results comparable to or better than current state-of-the-art methods.
 
### 2. Innovative points
  1. TriDet proposes a new framework that extends existing CNN architectures to handle video sequences and incorporates a new mechanism based on relative position coding.
  2. TriDet also introduces a new objective function to better capture action boundaries and employs an adaptive learning rate adjustment strategy to optimise the training process.
  3. The design ideas of TriDet are inspiring and can provide a reference for research in other related fields.

### 3. Future Works
  1. It is possible to further explore how to apply TriDet to more complex scenarios, such as multi-object tracking.
  2. It can try to combine TriDet with other techniques, such as reinforcement learning, to improve its performance.
  3. The objective function and training strategy of TriDet can be continued to be improved to make it more suitable for practical application scenarios. 
