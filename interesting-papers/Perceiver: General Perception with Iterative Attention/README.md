# Perceiver: General Perception with Iterative Attention
[paper link](https://arxiv.org/pdf/2103.03206) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new perceptual model called Perceiver, which is capable of simultaneously processing many different types of input data (e.g., images, point clouds, audio, etc.) without relying on specific a priori assumptions or domain knowledge.         |  Transformer         |

## Methodology

### 1. Abstract
The model employs a design based on the Transformer architecture and utilizes an asymmetric attention mechanism to progressively compress the input data, thus enabling it to handle very large input sizes. Experimental results show that "Perceiver" exhibits comparable or even better performance than existing specialization models in various classification tasks. In addition, it also shows good competitiveness in other modalities such as AudioSet.

### 2. Method Description 
The paper presents a novel NN architecture called Perceiver for processing data with inputs of arbitrary dimensions. The main components of Perceiver consist of two modules: **the cross-attention module and the Transformer tower**. The cross-attention module maps a high-dimensional input byte array to a low-dimensional hidden layer vector and extracts the information through an iterative application.The Transformer tower uses a highly nonlinear, fully connected layer to process the low-dimensional hidden layer vector, which improves the expressiveness of the model.

![image](https://github.com/user-attachments/assets/b4d0233a-a17d-4bd9-ab2d-af4a740d9fa3)

Problem Solved

  
### 3. Methodological improvements
Perceiver has the following advantages over traditional CNN and self-attention mechanisms:

1. It can handle input data of arbitrary dimensions.

2. Can utilize fewer parameters to achieve better performance than traditional methods.

3. Can reduce computational cost by sharing weights.

4. Higher level features can be extracted incrementally by iteratively applying the cross-attention module.

### 4. Issues addressed 
  1. Perceiver solves the problems of traditional neural networks when dealing with high-dimensional and multimodal inputs, and can be applied to data processing tasks in a variety of fields such as image, audio, and video.
  
  2. Perceiver provides a new way of thinking about how to design a more general and flexible neural network structure to better adapt to various complex data processing scenarios.

 ![image](https://github.com/user-attachments/assets/2a93d1e3-72fe-4171-9a8e-c30db8dedea3)
    
## Experiments
This paper describes the application and performance of the Perceiver model in different domains. Specifically, the authors conducted the following three comparison experiments:

  **Image classification task**: the authors trained the Perceiver model using the ImageNet dataset and compared it with other commonly used models (e.g., ResNet-50). The experimental results show that the Perceiver model performs on ImageNet comparably to, or even slightly better than, models specialized in images.

![image](https://github.com/user-attachments/assets/b94b7ecc-04e6-437f-bbfd-6595e388cf62)

  **Audio event classification task**: The authors trained the Perceiver model using audio signals as input and applied it to the task of classifying audio events in videos. Experimental results show that the Perceiver model performs well in both tasks and can effectively fuse information from multiple modalities.

  **Point cloud classification task**: The authors trained the Perceiver model using the ModelNet40 dataset and applied it to the point cloud classification task. Experimental results show that the Perceiver model also performs well in this task, especially for datasets without a natural grid structure.

 ![image](https://github.com/user-attachments/assets/dd257b53-2659-4298-a608-6351857e8d6d)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a model called Perceiver that can handle any number and type of inputs and achieves excellent performance on multiple datasets.
  
  2. Compared to traditional CNN and Transformer, Perceiver is more flexible and adaptable, and can better cope with different input configurations.
  
  3. In addition, the paper proposes some effective design decisions to mitigate the overfitting problem and provides valuable ideas for further research in the future.
  
### 2. Innovative points
  1. The main contribution of this thesis is to propose a new model architecture, Perceiver, which solves the computational complexity problem in the traditional Transformer model by introducing an attention bottleneck mechanism.
  
  2. The model can adaptively adjust itself according to different types of inputs and location information, thus improving its generalization ability and adaptability.
  
  3. In addition, the paper also proposes some effective technical means to mitigate the overfitting problem, such as using high-fidelity Fourier features.
     
### 3. Future Works
Tn future research, we can explore more optimization strategies and technical tools to further improve the Perceiver model and advance the field of perception.  

