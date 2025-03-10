# A Multi-Stage Adaptive Feature Fusion Neural Network for Multimodal Gait Recognition
[paper link](https://arxiv.org/pdf/2312.14410) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a multi-stage adaptive feature fusion neural network (MSAFF) approach for multimodal gait recognition.          |  Fusion Model        |

## Methodology

### 1. Abstract
While most of the existing gait recognition algorithms are unimodal, the method performs multiple multimodal fusions during the feature extraction process by considering the complementary advantages between different modal data and proposes an Adaptive Feature Fusion Module (AFFM) to take into account the semantic correlation between the contour and the skeleton. In addition, a multiscale spatio-temporal feature extractor (MSSTFE) is proposed in order to fully learn the spatial temporal correlation information.

![image](https://github.com/user-attachments/assets/1906b7e9-1266-4c50-a457-a93acb140aaf)

### 2. Method Description 
This thesis proposes a gait recognition network based on multimodal fusion for recognising human posture features during walking. The network uses the following three steps:

  1. **Multimodal feature extraction**: human skeleton data and contour data are taken as inputs respectively, and local and global spatial features are extracted by convolutional neural network and graph convolutional network.
  2. **Multi-scale spatio-temporal feature extraction**: the local and global spatial features extracted in the first step are subjected to multi-scale and multi-temporal dimensions, and the information interaction between different scales is realised through the self-attention mechanism.
  3. **Multi-modal fusion and dimensionality reduction**: multi-modal fusion of features extracted in the second step with different scales and time dimensions, and reduction of feature dimensions through dimensionality reduction operation to obtain the final gait representation.
![image](https://github.com/user-attachments/assets/36b73285-1b64-4c8a-b455-716cf2fc4621)

### 3. Methodological improvements
The multimodal fusion strategy proposed in this thesis can make full use of two different data sources to improve the accuracy of gait recognition. Also, the network employs a self-attention mechanism to capture the relationship between different scales, which further improves the performance of the model.
![image](https://github.com/user-attachments/assets/0fbf1a1e-d6b2-4e5f-be7a-117be9f5e9d3)

### 4. Issues addressed 
This thesis addresses the problem of under-utilisation of multimodal data in the field of gait recognition and proposes an efficient and accurate multimodal gait recognition network. The network can provide strong support for security monitoring, intelligent access control and other fields in practical applications.

## Experiments
This paper focuses on a gait recognition method based on multimodal feature fusion and conducts comparative experiments on three publicly available datasets. Specifically, three datasets, CASIA-B, Gait3D and GREW, are used as the experimental objects in this paper, and the effectiveness and superiority of the method are verified by comparing with other gait recognition algorithms.

**In the experiments on CASIA-B dataset**, the method proposed in this paper (MASFF) is compared with several existing gait recognition algorithms, including GaitSet, GaitPart, GaitGL, CSTL and TransGait. Experimental results show that MASFF achieves better performance in all conditions, especially in complex environments. 

For example, the accuracy under the condition of wearing a coat is 22.9% higher than other algorithms, and the accuracy under the condition of walking with a backpack is 14.6% higher than other algorithms. These results suggest that MASFF is able to extract more robust gait features, leading to more effective gait recognition.
![image](https://github.com/user-attachments/assets/ce07850c-91d3-415f-800d-a9eb4bf25314)

**In experiments on the Gait3D dataset**, this paper applies the network to a gait recognition task in a field environment and compares it with other model-based and multimodal algorithms. The experimental results show that the network proposed in this paper has the best recognition accuracy on this dataset, which is significantly higher than the two model-based algorithms and comparable to the multimodal algorithm SMPLgait. This further demonstrates the effectiveness and superiority of the method in the field environment.

![image](https://github.com/user-attachments/assets/82273d59-d371-4c06-80f7-a69a01c58cfa)

**In the experiments on the GREW dataset**, this paper tests more pedestrians to verify the generalisation ability and robustness of the method in practical applications. The experimental results show that the network proposed in this paper also performs well on this dataset with a Rank-1 accuracy of 57.40%, which exceeds other algorithms by about 10%. 

![image](https://github.com/user-attachments/assets/01034e5b-1a75-42e8-971b-485e6ef6dbce)

In addition, the authors found an interesting phenomenon that algorithms using only pose information performed poorly in terms of accuracy in the field environment, while when fusing pose and contour information, pose once again made a significant contribution to the complete gait representation. This phenomenon suggests that more modalities can provide a more complete gait representation.  

## Conclusion

### 1. Advantages of the Thesis
The paper proposes a multi-stage feature fusion strategy and an adaptive modal fusion module to exploit the complementary advantages of contours or skeletons, designs a multi-scale spatio-temporal feature extractor capable of extracting spatio-temporally correlated features at different spatial scales, and proposes a feature dimensionality pooling method to reduce dimensionality in the representation, which improves the recognition accuracy.

### 2. Innovative points
  1. The main contributions of this thesis are the proposal of a multi-stage feature fusion strategy and an adaptive modal fusion module to take full advantage of contours and skeletons, as well as the design of an efficient spatio-temporal feature extractor capable of extracting spatio-temporal correlation features at different spatial scales.
  2. In addition, a feature dimension pooling method is proposed to reduce the dimensionality in the representation, which improves the recognition accuracy.

### 3. Future Works
  1. Further research can be conducted to investigate how to integrate the data from other modalities into the model to improve the recognition accuracy.
  2. In addition, more effective feature extraction methods and model structures can be explored to better solve the gait recognition problem.   
