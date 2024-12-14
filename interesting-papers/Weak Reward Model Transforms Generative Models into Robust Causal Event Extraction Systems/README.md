# Weak Reward Model Transforms Generative Models into Robust Causal Event Extraction Systems
[paper link](https://arxiv.org/pdf/2406.18245) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the challenges posed by boundary ambiguity in causal event extraction tasks and proposes weakly supervised methods to train reinforcement learning models to improve model performance.          |  Reinforcement Learning        |

## Methodology

### 1. Abstract
The authors use an evaluation model to approximate human evaluation and experimentally validate it with multiple datasets. They also propose a weakly-supervised to strongly-supervised approach that can use partially labelled data to train the evaluation model and still be able to train a high-performance RL model. Overall, this work provides a novel solution to the causal event extraction task.

### 2. Method Description 
This paper proposes a new causal event extraction method that exploits the powerful generalisation capabilities of generative models (e.g. T5, GPT-3.5 and GPT-4). Traditional approaches are mainly based on single cause-and-effect scenarios and usually only consider simple causal relationships. However, generative models can not only learn from IE training data through fine-tuning, but can also rely on contextual examples or instructions alone to extract information in small or zero sample situations. Furthermore, this paper describes how human feedback in reinforcement learning can be used to improve the quality of causal event extraction.

![image](https://github.com/user-attachments/assets/9eaa5af5-9741-44fa-944f-e8ac78314a93)
 
### 3. Methodological improvements
This paper proposes two improvements: one is to use human feedback in reinforcement learning to guide the learning process of the generative model; the other is to use the generalisation ability of the generative model to extract causal events in small or zero sample situations.

### 4. Issues addressed 
  1. The limitation of single cause and effect scenarios: traditional causal event extraction methods mainly target single cause and effect scenarios and only consider simple causal relationships.

  2. The problem of inconsistency between automatic assessment metrics and human evaluations: traditional automatic assessment metrics (e.g., exact match and F1 scores) do not accurately reflect human evaluations, and thus need to develop their own assessment models to better correspond to human evaluations.
     
## Experiments
This paper focuses on experiments using a reinforcement learning framework and human feedback to improve the performance of generative models in a causal event extraction task. The experiment is divided into the following sections:

**Data collection and platform building:** the authors build a platform to collect human evaluations of generative model outputs and generate test data using two different generative models (FLAN-T5 and GPT-3.5).

**Human Feedback Collection:** The authors used the collected human feedback to train an evaluation model that determines whether the generative model output is a valid extraction result. The authors also developed some guidelines to ensure the consistency of human feedback.

![image](https://github.com/user-attachments/assets/82dc6bd4-cce7-4351-bc45-5d50dd1115a7)

![image](https://github.com/user-attachments/assets/3951f0b9-f6e4-4082-9aa4-e8a8a4fa48a4)

**Comparision Experiments:** the authors used three causal event extraction datasets (FCR, FinCausal, and SCITE) and divided them into a training set, a validation set, and a test set. The authors compared the following methods:

Evaluation using automatic scoring metrics (e.g., precision, recall, F1 score, etc.);
  1. Using a weakly supervised learning approach where the evaluation model is trained with a small sample size of labelled data;
  2. Using a fully supervised learning approach, where evaluation models are trained with large amounts of labelled data;
  3. Using human experts for evaluation.

![image](https://github.com/user-attachments/assets/f76b2f40-7cb2-49c2-a751-008e33a2c7e9)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a reinforcement learning-based approach for the evaluation problem in causal event extraction tasks, and experimentally verify its effectiveness.
  2. The authors first collected human evaluation data and used them to train an evaluator (reward model), which was then combined with the PPO algorithm and used to optimise the causal event extraction model.
  3. And, the article proposes a weakly-supervised to strongly-supervised learning framework to further improve the efficiency of data utilisation.

### 2. Innovative points
  1. While traditional evaluation methods are usually based on the exact match or on the subjective judgement of human experts, this paper guides the generative model to produce outputs that are more in line with human evaluation results by constructing a reward model.
  2. Meanwhile, this paper also proposes a weakly supervised to strongly supervised learning framework, which makes it possible to learn effectively even for data that lacks labelling. 

### 3. Future Works
In future research, consideration could be given to exploring how to better handle tasks of different types and sizes, and trying to use more automatic evaluation metrics to replace some or all of the human evaluations.    
