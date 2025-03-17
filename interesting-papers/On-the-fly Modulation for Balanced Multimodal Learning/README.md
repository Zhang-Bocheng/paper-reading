# On-the-fly Modulation for Balanced Multimodal Learning
[paper link](https://arxiv.org/pdf/2410.11582) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper focuses on the imbalance problem in multimodal learning and proposes two new optimization strategies: the On-the-fly Prediction Modulation (OPM) and the On-the-fly Gradient Modulation (OGM).         | Multimodal Learning         |

## Methodology

### 1. Abstract
The authors point out that the traditional joint training strategy tends to lead to the underestimation or neglect of the information of certain modalities, while the newly proposed optimization strategy can dynamically adjust the weights of each modality during the training process in order to better balance the variability among the modalities. Experimental results show that these simple but effective strategies can significantly improve the performance of multimodal tasks and are applicable to different types of multimodal models.

![image](https://github.com/user-attachments/assets/ceaed047-3655-499c-b86e-0be3c284bdf0)

### 2. Method Description 
The paper proposes two approaches to address the imbalanced learning problem in multimodal learning: On-the-fly prediction modulation (OPM) and On-the-fly gradient modulation (OGM).The OPM approach mitigates the impact of the imbalanced learning by randomly removing modalities that perform better in the training dataset and dynamically adjusting the discard probability of each modality to adapt to changes in model performance. and dynamically adjusts the discard probability of each modality to adapt to changes in model performance.The OGM approach mitigates the imbalance learning problem by adjusting the gradient of the more discriminative modalities, while introducing additional noise to improve the generalization ability of the model.

![image](https://github.com/user-attachments/assets/97c7b9b5-d9b8-486f-a49b-68a8d35592f5)

### 3.  Methodological improvements
The OPM method uses a monotonically increasing function z(x) to control the range of the discard probability, enabling more optimization opportunities for the suppressed modes in the presence of large inter-modal variance.The OGM method recovers the model's generalization ability by introducing stochastic Gaussian noise, which avoids the negative effects due to gradient conditioning.

### 4. Issues addressed 
Both OPM and OGM methods aim to address the problem of unbalanced learning in multimodal learning, i.e., when the amount of data for one or more modalities is small, their learning effectiveness is limited. These two methods improve the performance of the whole model from the prediction and gradient perspectives, respectively, by appropriately conditioning the better-performing modalities so that all modalities can be adequately trained and optimized.

## Experiments
This paper focuses on a solution for the imbalance problem in multimodal learning and verifies its effectiveness through several comparison experiments. Specifically, the following comparison experiments are conducted in this paper:

**Multiple fusion method comparison experiments**: this paper applies the proposed OPM and OGM methods to different fusion methods, including Concatenation, Summation, FiLM, etc., and compares them with the individually trained unimodal model and the multimodal model combined with other tuning methods. The results show that OPM and OGM methods can significantly improve the performance of multimodal models, especially in the case of uneven data sample distribution.

**Experiments in complex cross-modal interaction scenarios**: in this paper, the OPM and OGM methods are applied to a variety of complex cross-modal interaction modules, such as CentralNet, VATT and MMTM, and compared with other tuning methods. The results show that the OPM and OGM methods are not only applicable to simple fusion methods, but also can effectively improve the performance of multimodal models in complex cross-modal interaction scenarios.

**Comparison experiments with other dropout methods**: in this paper, the OPM and OGM methods are compared with other dropout methods, such as GBlending and Greedy, in order to verify their effectiveness in dealing with imbalance problems. The results show that OPM and OGM methods have better performance and efficiency compared to other dropout methods.

![image](https://github.com/user-attachments/assets/361539d3-0fc4-45d0-8c8a-3b6d09db9e0e)

**Experiments on more complex multimodal tasks**: in this paper, OPM and OGM methods are applied to more complex multimodal tasks such as audio-visual event localization and audio-visual question-answering, and compared with other task-oriented methods. The results show that the OPM and OGM methods are able to maintain their effectiveness in these more complex tasks, further demonstrating their effective solutions to the imbalance problem.  

![image](https://github.com/user-attachments/assets/27955b9e-b238-4abe-9b66-d93d299886cb)

## Conclusion

### 1. Advantages of the Thesis
The paper provides an in-depth study on the unbalanced learning problem in multimodal learning and proposes two new conditioning methods, On-the-fly Prediction Modulation (OPM) and On-the-fly Gradient Modulation (OGM), to help weakened modalities get more training. In addition, the authors validate the effectiveness and generalizability of the proposed methods through extensive experiments.

### 2. Innovative points
The main contribution of this paper is that two new conditioning methods are proposed to solve the unbalanced learning problem in multimodal learning. Among them, OPM dynamically controls the features of the dominant modality in the forward propagation phase, while OGM weakens its gradient in the backward propagation phase. Both approaches aim to improve the learning effect of each modality and thus enhance the performance of the whole multimodal model. 

### 3. Future Works
Although the OPM and OGM methods proposed in this paper have achieved significant performance improvements on several tasks, they still need to be further optimized and refined. For example, the issues of how to determine the appropriate tuning parameters and how to combine these methods with other multimodal learning techniques need to be further investigated in practical applications. In addition, for different types of multimodal datasets, it may be necessary to design different conditioning strategies in a targeted manner, which is also one of the directions for future research.   
