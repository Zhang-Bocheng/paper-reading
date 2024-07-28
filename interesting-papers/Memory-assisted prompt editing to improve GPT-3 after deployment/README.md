# Memory-assisted prompt editing to improve GPT-3 after deployment
[paper link](https://arxiv.org/pdf/2201.06009) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |This paper describes a memory-assisted cue editing method called MemPrompt, which aims to correct errors that large language models (e.g., GPT-3) may make in understanding user intent through user feedback.          | LLMs         |

## Methodology

### 1. Abstract
The method utilizes a growing memory bank that records how the model has misinterpreted similar questions as well as clarifying feedback from users. This approach can significantly improve model accuracy without retraining and provides a low-cost enhancement tool for large-scale pre-trained language models. The experimental results show that the deployed GPT-3 model can be effectively taught new knowledge and skills using the MemPrompt approach in four tasks, thus improving its accuracy and efficiency.

### 2. Method Description 
This paper presents MemPrompt, which extends the GPT-3 model by adding a task comprehension and a sentence representation to the input, and improves the model's accuracy using a memory table that stores similar questions and feedback information. When the user realizes that the model has misinterpreted their intentions, they can add feedback to the memory table for later reference. 

This approach also introduces a new task: **ethical reasoning**, in which the model needs to provide moral judgments and explain its understanding based on the context. To address these issues, MemPrompt includes two key components: a memory table and a feedback mechanism. The memory table is used to store similar questions and feedback, while the feedback mechanism allows the user to provide feedback on the model's understanding.

![image](https://github.com/user-attachments/assets/c1810735-ca11-4537-9952-1e9e392efb6c)

### 3. Methodological improvements
  1. The main innovation of MemPrompt is its ability to utilize feedback information from the memory table to improve the accuracy of the model.
  
  2. This approach also introduces new tasks, such as ethical reasoning, to test the performance of models in complex situations.
  
  3. In addition, MemPrompt proposes a novel sequence-to-sequence converter (GUD-IR) for converting the input into a better form so that the model can understand the user's intention.

### 4. Issues addressed 
MemPrompt addresses several main problems:

1. The problem of models not being able to understand user input correctly.

2. Lack of an effective feedback mechanism, making it difficult for the user to tell the model which responses are wrong or irrelevant.

3. Lack of new task types applicable to different tasks.

With these improvements, MemPrompt was able to significantly improve the performance of the model and make it more suitable for handling complex tasks.

## Experiments
This paper describes four experiments conducted by the authors on the use of Memory-based Prompt Editing (MemPrompt) in GPT-3 modeling and compares them to two baselines. 
<br>&emsp;(1)The first of these experiments verifies whether MemPrompt improves GPT-3 accuracy in an ethical reasoning task
<br>&emsp;(2)the second tests the effectiveness of MemPrompt in a lexical relations and word confusion task, 
<br>&emsp;(3)the third uses dynamic prefixes to create cues and combines them with MemPrompt, 
<br>&emsp;(4)the fourth explores the effectiveness of whether MemPrompt can work effectively with labeled feedback.

For the first experiment, in an ethical reasoning task, the authors used two evaluation metrics: **accuracy and comprehension accuracy**. The results showed that MemPrompt was able to significantly improve GPT-3 accuracy and comprehension accuracy compared to baseline, especially in the ErtCat and ErtNl tasks. 

![image](https://github.com/user-attachments/assets/4c11b677-a3b9-4596-886a-6f2481fda16c)

![image](https://github.com/user-attachments/assets/26cf6d59-34a3-48b7-b077-107df4cea40e)

For the second experiment, in the lexical relations and word confusion tasks, the authors observed that MemPrompt performed much better than the baseline. In addition, the authors show how performance can be improved by improving the model's comprehension.

For the third experiment, the authors combine the dynamic prefix approach with MemPrompt in an experiment and show that this approach can further improve the model's performance.

Finally, for the fourth experiment, the authors explore whether MemPrompt can work effectively with labeled feedback. The results show that even without the ability to generate comprehension, MemPrompt can still be useful for language and dialect personalization.

![image](https://github.com/user-attachments/assets/8dfc2296-37d8-4497-855f-c240e66a63d0)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a novel approach to enhance the performance of the GPT-3 model, i.e., to improve the model through interaction with and feedback from the user without the need for retraining.

  2. The researchers designed a memory system to store the feedback provided by the user and apply it to new problems to avoid repeating errors.

  3. The paper demonstrates the performance of this approach on four tasks and proves that it can significantly improve the accuracy of the GPT-3 without the need for retraining.
 
### 2. Innovative points
  1. The MemPrompt method proposed in the paper is an interactive feedback-based memory enhancement technique that can effectively improve the performance of large language models such as the GPT-3.
  
  2. The researchers store user-provided feedback in a memory system and use it to dynamically update the prompts to better understand the user's intent.
  
  3. The method also prevents the model from making mistakes again if it encounters similar problems in the future, thus improving the robustness and reliability of the model.

### 3. Future Works
  1. The MemPrompt method proposed in the paper provides an effective way to improve the performance of large language models, which will play an important role in future NLP research.
  
  2. Future research could explore how to further optimize the design of memory systems to improve their efficiency and scalability.
  
  3. In addition, researchers can consider applying the MemPrompt method to other types of models or tasks to verify its generalizability and applicability.
