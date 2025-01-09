# AdaFlow: Opportunistic Inference on Asynchronous Mobile Data with Generalized Affinity Control
[paper link](https://arxiv.org/pdf/2410.24028) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a new approach called AdaFlow for non-blocking inference in distributed multimodal systems. This can lead to problems with latency or accuracy degradation due to asynchronous sensor data arrival times on mobile devices.          |  Multimodal        |

## Methodology

### 1. Abstract
Traditional solutions optimise for modal consistency and complementarity, known as modal affinity, but lack a computational way to control this affinity. AdaFlow uses a hierarchical analysis-based normalisation matrix to form structured cross-modal affinities, and employs an attention-mechanism Conditional Generative Adversarial Network (ACGAN) for flexible data interpolation, adapting to a variety of modalities and downstream tasks without without retraining. Experimental results show that AdaFlow significantly reduces inference latency by up to 79.9% and improves accuracy by up to 61.9%, outperforming existing methods.

### 2. Method Description 
This thesis presents AdaFlow, a solution for input asynchrony and heterogeneity in distributed multimodal data fusion systems.AdaFlow consists of two main modules: structured modal affinity modelling and non-blocking asynchronous inference. In the structured modal affinity modelling module, t-SNE-based reduced dimensionality and Gaussian variance are used to compute the similarity between modalities, and the similarity is normalised to an affinity matrix using the Analytic Hierarchy Process (AHP). In the non-blocking asynchronous inference module, an attention mechanism based on Conditional Generative Adversarial Networks (CGAN) is employed for data filling and fusion of asynchronous data streams for real-time and accurate inference.

![image](https://github.com/user-attachments/assets/2356932f-f004-4922-8b22-6ee037449067)

### 3. Methodological improvements
Compared with traditional single-view scenarios, the method is able to effectively deal with multimodal asynchrony and heterogeneity, as well as dynamically adapt to different task requirements. In addition, the method introduces advanced techniques such as AHP and CGAN, which make the establishment of affinity matrices more accurate and efficient, as well as improve the fusion effect of data filling and asynchronous data streams.

### 4. Issues addressed 
The method solves the problem of input asynchrony and heterogeneity in distributed multimodal data fusion systems, enables real-time and accurate reasoning, and can dynamically adapt to different task requirements. In addition, the method improves the accuracy and efficiency of affinity matrix building, as well as the fusion effect of data padding and asynchronous data flow by introducing techniques such as AHP and CGAN. These improvements make AdaFlow an effective multimodal data fusion solution with a wide range of applications.

## Experiments
This paper presents comparative and analytical results on the performance of AdaFlow, a real-time processing system for distributed multimodal data. The authors conducted four experiments for real-world applications and compared them with five synchronous/asynchronous fusion methods. The experimental results show that AdaFlow achieves an optimal balance of maintaining high accuracy with low latency. In addition, the article describes AdaFlow's data-filling performance and generalisation capabilities, and demonstrates the effectiveness of its application in autonomous driving through a case study. 

![image](https://github.com/user-attachments/assets/5211e364-afd8-42c0-9be6-4f2ffd6d1204)

![image](https://github.com/user-attachments/assets/049e3c97-842c-46ab-b7c8-6efc5014a7e1)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents an approach called AdaFlow for processing asynchronous data in distributed mobile environments and achieves significant performance gains on multimodal tasks.
  2. The method solves the problem of asynchronous data by dynamically adapting to multiple inputs and efficiently implementing multimodal fusion, while using AHP to normalise matrix values to accommodate heterogeneity and asynchrony.
  3. The method also introduces Conditional Generative Adversarial Networks (ACGAN) based on the attention mechanism to achieve low-latency, high-precision, and non-blocking inference capabilities for a wide range of input modalities and types without the need for retraining.

### 2. Innovative points
  1. The method proposes the concept of quantitative modal affinity control to accurately assess and control the relationship between different modalities for more effective data fusion.
  2. The method employs an opportunistic inference strategy, where the server performs inference as soon as some of the asynchronous data is available, avoiding the time spent waiting for slow data and reducing the loss of accuracy when excluding such data.
  3. The method also uses a Conditional Generative Adversarial Network (ACGAN) based on an attention mechanism to achieve low-latency, high-accuracy, non-blocking inference capability with high adaptive capacity and flexibility.
     
### 3. Future Works
  1. The method can be further applied to other fields such as smart driving and health monitoring to improve the efficiency and accuracy of the system.
  2. It can be explored how to combine the method with pre-trained models to further improve its performance and generalisation ability.
  3. Extending the method to more modalities and tasks can be considered to better meet the needs of practical applications.  
