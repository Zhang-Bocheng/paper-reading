# Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
[paper link](https://arxiv.org/pdf/2312.08935) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a mathematical problem solving process reward model called ‘MATH-SHEPHERD’, which assigns a reward score to each step and is trained using automatically constructed process-supervised data, avoiding the reliance on human annotations.          | Large Language Model (LLMs)         |

## Methodology

### 1. Abstract
Experimental results show that the use of ‘MATH-SHEPHERD’ can significantly improve the performance of various open source language models in both validation and reinforcement scenarios. Among them, ‘MATH-SHEPHERD’ in combination with ‘MISTRAL-7B’ can improve the accuracy from 77.9% to 84.1%, and further enhance it to 89.1%; and the accuracy on ‘MATH’ is also improved from 28.6% to 33.0%, and can reach 43.5%. Therefore, automatic process supervision has great potential for the development of future language models.

![image](https://github.com/user-attachments/assets/a1cec49b-92d1-4d5f-952d-29f8ab00a5a0)

### 2. Method Description 
The paper proposes two mathematical problem reward models (Reward Models): **the Operation Result Model (ORM) and the Process Step Model (PRM)**. In this case, the ORM gives a single real value as a score based on the problem and the solution result; while the PRM assigns a score to each solution step and is trained using a cross-entropy loss function. In addition, the paper proposes an automatic process annotation framework to alleviate the high cost of manual annotation in PRM.

![image](https://github.com/user-attachments/assets/865b9bbe-6de3-4e78-84cd-156708fdaf5e)

### 3. Methodological improvements
The thesis improves the training efficiency by introducing an automatic process annotation framework to reduce the manual labelling cost. Meanwhile, by comparing the effects of ORM and PRM, it is found that PRM can provide more detailed and reliable feedback information, but there is no automated method to build high-quality PRM training datasets.

### 4. Issues addressed 
  1. How to evaluate the performance of mathematical problem solving;
  2. How to improve the accuracy and reliability of mathematical problem solving.

## Experiments
This paper presents the experimental results of four sets of experiments conducted by the authors using two widely used mathematical reasoning datasets (GSM8K and MATH). 

The first set of experiments **compares the effectiveness of validation methods**, including self-consistent voting, self-consistent validation models, and reward model validation. The results show that using mathematical reasoning supervised learning as a validator significantly improves the accuracy of the generated models. 

![image](https://github.com/user-attachments/assets/1c155def-4fa6-47ab-ac70-fdb4a1c98800)

The second set of experiments **compared the effects of reinforcement learning strategies**, including self-consistent validation-based methods, rejection of sampling fine-tuning, and mathematical reasoning supervised learning-based methods. The results show that the mathematical inference supervised learning based approach can significantly improve the model performance.

![image](https://github.com/user-attachments/assets/e2f07207-f3a4-4834-baf0-a6c3bc68b0d8)

A third set of experiments **combines reinforcement learning and validation and finds that they are complementary**. 

![image](https://github.com/user-attachments/assets/31c223b0-2898-4eff-84bf-770fe5bb33ef)

The fourth set of experiments **analysed the effect of different numbers of candidate solutions**, the quality of the automatic process annotations, the effect of pre-training the base model, and the effect of the amount of data. 

![image](https://github.com/user-attachments/assets/ea6051aa-5fd3-465d-afdb-021fe3e163f7)

Finally, the authors also tested the performance of MATH-SHEPHERD on out-of-distribution performance and compared it to other methods.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a method for automatically constructing process-supervised datasets for mathematical reasoning tasks without the need for manual labelling, which solves the problem of the traditional manual labelling approach that is costly and difficult to access.
  2. Meanwhile, the method determines the labels by automatically evaluating the quality of intermediate steps, achieving high-quality dataset construction. Experimental results show that the method achieves good results in both validation and reinforcement learning scenarios and significantly improves the performance of open source models.

### 2. Innovative points
  1. The method proposed in this paper for automatic construction of process-supervised datasets is based on the idea of Monte Carlo Tree Search algorithm, which uses known answers to decode multiple subsequent inference paths and compares their correctness to determine labels.
  2. This method not only avoids the traditional manual labelling, but also adaptively adjusts the difficulty of the labels according to the difficulty of the questions, which improves the quality of the dataset. In addition, the method is scalable and pervasive, applicable to various types of mathematical reasoning tasks. 

### 3. Future Works
Future research directions include further optimising the quality of the dataset, exploring more application scenarios, and combining with other technical means (e.g., migration learning) to improve the model performance. At the same time, in-depth research is needed to better utilise automated process-supervised datasets to train smarter and more efficient mathematical inference models.   
