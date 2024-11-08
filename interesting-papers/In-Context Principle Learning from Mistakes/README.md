# In-Context Principle Learning from Mistakes
[paper link](https://arxiv.org/pdf/2402.05403) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a new Learning Principles (LEAP) approach to language model (LLM)-based learning         | Large Language Model (LLM)         |

## Methodology

### 1. Abstract
This method improves the performance of LLMs on downstream tasks by learning a number of errors in the input-output pairs and allowing the model to reflect on and learn the task-specific principles behind these errors, thereby improving LLM performance on downstream tasks. The authors conducted experiments using a variety of benchmark test datasets and demonstrated that LEAP achieves better results than the standard sample less cueing approach on a variety of tasks. Furthermore, LEAP does not require additional input or examples to achieve this improvement.

### 2. Method Description 
This paper proposes a method called LEAP (Learning Principles from Mistakes), which aims to improve the accuracy of a model by learning general principles for avoiding potential errors in downstream tasks. The method consists of the following steps:

  1. Generate a small number of examples P={(xi, yi)}ki=1 for a given task.
  2. For each input-output pair (xi, yi), generate a diverse set of solutions using a zero-sample approach and compare them with the original answers yi to determine which are wrong.
  3. The incorrect answers are provided to the language model along with the original question so that it can automatically generate natural language explanations to form the set of low-level principles LLOW-LEVEL.
  4. Use the language model to condense the low-level principles into approximately 5 key points to form the high-level principles set LHIGH-LEVEL.
  5. Finally, these principles were added to the standard prompts for answering examples not seen in the test set.

![image](https://github.com/user-attachments/assets/c1435de4-2135-429a-be34-7e37539e48dd)
 
### 3. Methodological improvements
  1. The main innovation of the LEAP methodology is that it exploits the self-assessment capabilities of the language model, allowing it to identify and extract the errors it may make when dealing with a particular task, and to generate generic principles based on these errors. This enables the model to reason and answer questions more accurately in future responses.
  2. In addition, LEAP uses a zero-sample approach to generating solutions, which means that it can generate new solutions without any additional data, further improving the model's ability to generalise.

### 4. Issues addressed 
  1. **Errors that may occur when the model is dealing with a specific task:** the LEAP method utilises the self-assessment capabilities of the language model, enabling it to identify and extract errors that may occur when it is dealing with a specific task and generate generalised principles based on these errors.

  2. **Data scarcity:** the LEAP method uses a zero-sample approach to generating solutions, which means that it can generate new solutions without any additional data, thus further improving the model's ability to generalise.

  3. **Enhanced Reasoning Ability **and Accuracy of Models: By learning general principles for models to avoid potential errors in downstream tasks, the LEAP approach enhances the reasoning ability and accuracy of models, thus making them better able to cope with a variety of complex scenarios.

## Experiments
This paper describes the authors' evaluation of a variety of reasoning tasks using the LEAP method and compares it to the standard Few-shot prompting with COT (Few-shot prompting with COT) method. The experiments included a variety of domains including textual reasoning, mathematical reasoning, and Big-Bench Hard. The experimental results show that the LEAP method performs better than the standard method in most cases, improving the accuracy of the model.

Specifically, the LEAP method can improve the accuracy by 7.5% in HotpotQA, 7.5% in DROP, and 7.5% in both MATH and GSM8K. In addition, the LEAP method is interpretable and can help users understand how the model makes decisions. Overall, the LEAP method is an effective augmented learning strategy that can improve model performance in a variety of inference tasks. 

![image](https://github.com/user-attachments/assets/8c11464b-92e0-4e7f-ba13-849abd259814)

![image](https://github.com/user-attachments/assets/1bbbd7e3-fbb8-400a-8cdd-9df52ce2ba9a)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new Learning Principles (LEAP) approach that allows pre-trained Language Models (LLMs) to better adapt to a given few examples by deliberately making mistakes and avoiding similar ones.
  2. The method does not require more input data, but only the same amount of labelled data as the standard few-sample cue setting.
  3. The method can be used on a wide range of reasoning tasks, including mathematical reasoning, multi-hop quizzes, and textual reasoning.
  4. Experimental results show that the method achieves significant improvements on several powerful LLMs such as GPT-3.5-turbo, GPT-4, GPT-4-turbo, and Gemini Pro.

### 2. Innovative points
  1. The methodology enables the model to learn from its mistakes and avoid similar mistakes by allowing it to deliberately make mistakes and reflect on those mistakes.
  2. The method divides the learning process into three phases: generating a zero-sample Chain-of-Thought response of errors, generating explicit principles, and providing the model with a given input-output example and the principles that have been learnt, thus improving the model's performance.
  3. The method utilises the concept underlying human learning, i.e., learning by making mistakes, not just learning the correct answer or feedback. 

### 3. Future Works
  1. The approach can be further extended to other domains such as natural language generation and dialogue systems.
  2. It could be explored how to incorporate other techniques, such as meta-learning and reinforcement learning, to further improve the performance of the model.
  3. The method can also be applied to other types of machine learning problems such as image classification and speech recognition.    
