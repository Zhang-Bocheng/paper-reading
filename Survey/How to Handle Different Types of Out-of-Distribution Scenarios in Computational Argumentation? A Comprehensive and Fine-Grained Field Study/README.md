# How to Handle Different Types of Out-of-Distribution Scenarios in Computational Argumentation? A Comprehensive and Fine-Grained Field Study
[paper link](https://arxiv.org/pdf/2309.08316) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the performance of pre-trained language models in dealing with different types of out-of-distribution scenarios and focuses on some of the challenges in the field of computational argumentation.           |  LLMs        |

## Methodology

### 1. Abstract
Data scarcity due to complex annotation schemes and high costs make it difficult to cover a wide range of text sources and topics. To address this problem, the paper systematically evaluates the capabilities of pre-trained language models for three common out-of-distribution scenarios: topic shifting, domain shifting, and language shifting. The results of the study show that the effectiveness of the learning method varies across different out-of-distribution scenarios. 

For example, in the case of domain shifting, cue-based fine-tuning is more effective than context-based learning; while in the case of topic shifting, the opposite is true. These findings provide guidance for solving extra-distributive problems in the domain of computational argumentation, while also highlighting the potential of base-scale language models to address these challenges.

![image](https://github.com/user-attachments/assets/fb8f1353-8b94-4bb8-acb9-e01752c7e55d)

## Experiments
This paper focuses on the performance of large pre-trained models for NLP tasks in the face of different types of distributional biases, and explores the impact of different learning methods and parameter tuning strategies on model performance through a series of comparative experiments. Specifically, this paper compares the following aspects:

  1. **Model selection and task classification**: this paper selects 11 tasks including text classification, sentiment analysis, stance recognition, etc., and uses several pre-trained models including BERT, RoBERTa, DeBERTa-v3, etc. as the base models.

  2. **Types of distributional biases**: this paper classifies distributional biases into three types, namely topic, domain and language, and explores the performance differences of models under different types by conducting experiments on different types of distributional biases.

  3. **Comparison of Learning Methods**: This paper compares the traditional Fine-tuning method with the Prompt-based Fine-tuning method and the Contextual Learning method, and explores the performance differences of these methods under different types of distributional offsets.

  4. **Comparison of parameter tuning strategies**: this paper compares the effects of various parameter tuning strategies, such as LoRA-based, P-Tuning and Prompt-Tuning, as well as the effects of their application on larger-scale models.
     
![image](https://github.com/user-attachments/assets/349b1572-9eb9-4722-aee7-98f16276c9ae)

From the comprehensive experimental results, this paper draws the following conclusions:

  1. There are significant differences in the performance of different pre-trained models in the face of different types of distributional biases, with DeBERTa-v3 having better performance compared to other models.

  2. The Prompt-based Fine-tuning method is able to cope with different types of distributional offsets better than the traditional Fine-tuning method and is less prone to overfitting than the traditional Fine-tuning method.

  3. Context learning methods can achieve better results than Prompt-based Fine-tuning in some cases, but perform less well than Prompt-based Fine-tuning in most cases.

  4. Parameter tuning strategies such as LoRA can improve the performance of the model to a certain extent, but their effectiveness may be limited as the model size increases.

![image](https://github.com/user-attachments/assets/48f4260f-cbe0-43d3-a835-dd3fa15b7db4)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper systematically assesses different types of OOD scenarios in CA and provides detailed experimental results and analyses.
  
  2. An assessment framework with 11 CA tasks covering three types of OOD scenarios is proposed to provide practitioners with guidance to address these challenges.
  
  3. The experiments show that different learning paradigms can effectively manage OOD situations in CA in different OOD scenarios.
  
  4. The paper highlights the key role of OOD heterogeneity in addressing the generalisation challenges of CA tasks and provides directions for future research.

### 2. Innovative points
  1. A comprehensive evaluation framework is proposed to determine the performance of models in different types of OOD scenarios.
  
  2. Multiple learning paradigms and language models (LMs) of different sizes were used to evaluate model performance in different types of OOD scenarios.
  
  3. The training of the models was optimised by training a portion of the base-sized LMs using LoRA in order to improve their stability and obtain a performance comparable to that of full volume tuning.

### 3. Future Works
  1. The importance of studying OOD scenarios will become more prominent when facing increasingly complex natural language processing tasks.
  
  2. Further research on the impact of various factors, such as computational efficiency, task complexity, and data contamination, may be needed.
  
  3. More advanced learning paradigms, such as meta-learning or adaptive learning, can be explored to better cope with various types of OOD scenarios.   
