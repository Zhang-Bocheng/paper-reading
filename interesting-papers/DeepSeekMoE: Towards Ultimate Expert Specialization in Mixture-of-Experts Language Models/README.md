# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
[paper link](https://arxiv.org/pdf/2401.06066) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a language model architecture called DeepSeekMoE that aims to achieve expert specialisation in order to cope with the computational cost of large-scale language models.          |  Large-scale Language Models        |

## Methodology

### 1. Abstract
The architecture employs two strategies: subdividing experts into mN and activating mK of them; and using Ks experts as shared experts in order to capture common knowledge and reduce redundancy among routing experts. Experimental results show that DeepSeekMoE using 2B parameters has comparable performance to GShard 2.9B with 1.5 times the number of expert parameters and computation. Furthermore, when DeepSeekMoE is scaled up to 16B parameters, its performance approaches that of a dense model with the same number of total parameters as it, and with 145B parameters, DeepSeekMoE shows a significant advantage, requiring only about 28.5% of the computational effort to reach the performance level of DeepSeek 67B.

![image](https://github.com/user-attachments/assets/bc82484e-5041-47b3-a47e-ed05839fc910)

### 2. Method Description 
This paper presents a hybrid model architecture called DeepSeekMoE for implementing expert specialisation in the Transformer language model. The approach improves expert specialisation through two main strategies: **fine-grained expert segmentation and shared expert isolation**. In particular, fine-grained expert segmentation splits each standard FFN into smaller experts and increases the number of activated experts to keep the same computational cost. Shared expert isolation, on the other hand, specifically assigns some experts to capture and integrate common knowledge, thus reducing parameter redundancy among other routing experts and making the model more specialised.

![image](https://github.com/user-attachments/assets/11c0fbb8-31cd-4b50-a4ce-13a9924e2043)

### 3. Methodological improvements
Compared to the traditional Mixture-of-Experts (MoE) architecture, DeepSeekMoE employs two new strategies, fine-grained expert segmentation and shared expert isolation, to improve the efficiency and accuracy of the model. In addition, to prevent routing crashes and balance loads, DeepSeekMoE introduces expert-level balancing loss and device-level balancing loss.

### 4. Issues addressed 
DeepSeekMoE aims to solve the problems existing in traditional MoE architectures, such as route collapse and parameter redundancy. With two strategies, fine-grained expert segmentation and shared expert isolation, DeepSeekMoE is able to better utilise different types of experts and improve model accuracy and efficiency. Meanwhile, by introducing expert-level balancing loss and device-level balancing loss, DeepSeekMoE can also effectively avoid problems such as routing collapse and balancing load.

## Experiments
This article focuses on the validation and analysis experiments of the DeepSeekMoE model and compares them with other models. Specifically, the article includes the following comparison experiments:

**Validation experiments:** the DeepSeekMoE was validated using several tasks such as Pile, HellaSwag, PIQA, ARC, RACE-high and RACE-middle, and compared with other MoE models such as Dense, Hash Layer, Switch Transformer and GShard . The results show that DeepSeekMoE outperforms other models on all tasks, proving its effectiveness in large-scale pre-training.

![image](https://github.com/user-attachments/assets/03ef0767-d85c-479a-aed4-dfc89c48d069)

**Ablation Study:** The effectiveness of DeepSeekMoE is further validated by adjusting hyperparameters such as shared expert isolation strategy, fine-grained expert segmentation strategy and routing parameter ratio. The results show that all these strategies can improve the model performance, especially the shared expert isolation strategy can better utilise the knowledge.

![image](https://github.com/user-attachments/assets/bee7cf94-076f-4e47-8f90-29cae1872234)

**Analysis on Expert Specialisation:** by analysing different types of experts in DeepSeekMoE, it is demonstrated that it has higher flexibility and accuracy. For example, DeepSeekMoE has lower redundancy than GShard and shared experts capture more basic knowledge.

![image](https://github.com/user-attachments/assets/12a646dc-df0d-4f87-92ce-e3c10209bfbe)

**Scaling up to DeepSeekMoE 16B:** Scaling up DeepSeekMoE to a larger scale (16B parameter) and comparing it to LLaMA2. The results show that DeepSeekMoE only needs about 40% of the total computation of LLaMA2 to achieve better performance. 

![image](https://github.com/user-attachments/assets/dd6d12aa-3f1a-4aeb-875e-a5e3d3aeb0ef)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a novel hybrid model architecture called DeepSeekMoE, which aims to maximise the degree of expert specialisation. With fine-grained expert segmentation and shared expert isolation strategies, DeepSeekMoE significantly outperforms existing hybrid model architectures in terms of expert specialisation and performance.
  
  2. The authors validate the advantages of DeepSeekMoE starting with a smaller scale 2B parameter and demonstrate that it has an upper bound performance close to that of dense models. In addition, the authors provide detailed experimental results and analyses to support their claims and demonstrate the scalability and adaptability of DeepSeekMoE.
  
### 2. Innovative points
  1. DeepSeekMoE employs two main strategies: fine-grained expert segmentation and shared expert isolation. Fine-grained expert segmentation allows for more precise decomposition and learning of knowledge, thus increasing the specialisation of each expert.
  
  2. The shared expert isolation strategy, on the other hand, treats some experts as shared experts in order to capture and merge common knowledge across different contexts, thus reducing redundancy among other routing experts, enhancing parameter efficiency and ensuring that each routing expert focuses on different aspects.

### 3. Future Works
Future research can further explore the potential of DeepSeekMoE and apply it to various NLP tasks. It can also try to combine other techniques to further improve the performance and efficiency of DeepSeekMoE.
