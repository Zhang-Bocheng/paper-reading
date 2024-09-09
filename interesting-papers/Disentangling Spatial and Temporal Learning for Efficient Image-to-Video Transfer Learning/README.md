# Disentangling Spatial and Temporal Learning for Efficient Image-to-Video Transfer Learning
[paper link](https://arxiv.org/pdf/2309.07911) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |This paper introduces a new method called DiST for solving spatio-temporal modeling problems in video recognition.           |  Computer Vision |

## Methodology

### 1. Abstract
Traditional speech-image models perform well in understanding spatial content, but still fall short when dealing with video. To address this problem, the authors propose a dual-encoder architecture in which the pre-trained base model acts as a spatial encoder while the introduced lightweight network acts as a temporal encoder. In addition, an integration branch is inserted to fuse spatio-temporal information. This approach avoids back-propagation of large-scale pre-training parameters and is therefore very efficient. Experimental results show that DiST performs better in five benchmark tests compared to the best existing methods and still scales well after pre-training on large-scale datasets.

![image](https://github.com/user-attachments/assets/31fa64a9-cadb-4567-9e87-c9355d2d0915)

### 2. Method Description 
The paper proposes a model called DiST (Disentangled Spatiotemporal Modeling) for video understanding tasks. The model consists of three main components: **a spatial encoder, a temporal encoder and an integrated branch**. Among them, the spatial encoder is a powerful CLIP pre-trained visual Transformer that extracts robust spatial semantics between sparse frames; the temporal encoder is a lightweight spatio-temporal network with low channel capacity and the ability to capture temporal patterns specific to video comprehension; and the integration branch connects the spatial and temporal encoders to achieve a unified spatio-temporal representation through interactive learning.

![image](https://github.com/user-attachments/assets/0c5f1129-10f3-4353-a254-2a1d6bb8c86c)

### 3. Methodological improvements
DiST employs a more efficient training approach compared to traditional video understanding models, as it utilizes a powerful CLIP pre-training model to provide spatio-temporal feature extraction capabilities, thus reducing the number of spatio-temporal feature extractors that need to be manually designed. In addition, DiST uses some new designs to further improve the performance, such as the use of deep residual blocks to enhance the spatio-temporal feature extraction capability and the introduction of a spatio-temporal interaction module in the integration branch to better fuse spatio-temporal information.

### 4. Issues addressed 
The main contribution of this thesis is to propose an efficient and scalable video understanding model that can handle video sequences of different lengths and is capable of video classification with zero samples. The model has been tested on two popular video understanding datasets and achieves comparable or even better results than the best existing models. This shows that DiST is a very promising method for video understanding and can play an important role in practical applications.

## Experiments
This paper focuses on DiST, a video action recognition method proposed by the authors, and conducts several comparison experiments to verify its performance and efficiency. Specifically, the comparison experiments in this paper include the following:

**Ablation Study Based on Different Modules (AB Experiment)**: this experiment explores the effect of different components of DiST on performance by trying different design options. The results show that adding more frames improves accuracy, larger channel widths allow for better fusion of spatio-temporal information, and a lighter weight encoder better captures video-specific motion patterns.

**Zero Sample Learning Experiment**: This experiment uses a pre-trained model for a zero sample learning task and shows that DiST performs better than existing methods on all datasets.
![image](https://github.com/user-attachments/assets/a29b5f09-f10a-46ed-bb5b-15549aaf4119)

**Bayesian Inference Experiment**: This experiment compares the performance of DiST with other Bayesian inference-based methods and shows that DiST achieves better results in most cases.

**Other methods comparison experiment**: this experiment compares DiST with other existing methods, including X-CLIP with full fine-tuning and freezing features, ST-Adapter, and other methods. The results show that DiST performs well on various datasets, especially on datasets with more spatio-temporal information.

![image](https://github.com/user-attachments/assets/25bf1348-8c14-496b-8657-523497b37950)

## Conclusion

### 1. Advantages of the Thesis
  1. The framework employs a dual-encoder architecture that includes a frozen but heavyweight spatial encoder and a lightweight learning temporal encoder.
  
  2. An integrated branch then fuses spatial and temporal information into a unified spatio-temporal representation for video understanding. Experimental results validate DiST's scalability in terms of model size and data scale.
  
  3. In addition, DiST is able to utilize large-scale video datasets for pre-training and performs better than fully fine-tuned methods.

### 2. Innovative points
  1. The main contribution of this paper is the proposal of a new image-to-video transfer learning framework, DiST. compared to existing video understanding methods based on pre-trained models, DiST improves its performance by separating spatial and temporal modeling.
  
  2. Specifically, DiST uses parallel concatenation to avoid the inefficiency of backpropagation through pre-trained parameters, while introducing an encoder specifically designed to extract temporal information from the input video, thus enhancing the temporal modeling capability.
  
  3. Finally, in order to simultaneously utilize the spatial semantics from the dual-encoder structure and the temporal information extracted from the spatio-temporal encoder, DiST introduces an integration branch to fuse these two features.

### 3. Future Works
In the future, it can further explore how to optimize the architecture of DiST to better adapt to different video understanding tasks. For example, its performance can be improved by adjusting the number of network layers in the spatio-temporal encoder or adding more attention mechanisms. In addition, combining DiST with other techniques, such as reinforcement learning or migration learning, can be considered to further improve its performance.
