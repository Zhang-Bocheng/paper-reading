# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
[paper link](https://arxiv.org/pdf/2201.11903) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores how the ability of large language models to perform complex reasoning can be significantly improved by generating a series of intermediate reasoning steps (i.e., “thought chains”)          | Prompting Engineering         |

## Methodology

### 1. Abstract
The authors use a simple method, the “thought chain cue”, which allows a sufficiently large language model (LLMs) to naturally exhibit this reasoning ability by providing only a few examples as a guide. Experimental results show that when tested on three large language models, the Chain of Thought Cue significantly improves performance on arithmetic, general knowledge, and symbolic reasoning tasks, and the results are highly significant.

![image](https://github.com/user-attachments/assets/554beaeb-1c7c-4141-9873-a337394b6e9a)

### 2. Method Description 
The paper proposes a method called “chain-of-thought prompting”, which aims to enable language models to generate a series of reasoning steps to solve problems and arrive at a final answer. The method accomplishes this by providing examples of chain-of-thought in training data and applying it to tasks such as mathematical problems, common-sense reasoning, and symbolic manipulation.

### 3. Methodological improvements
Instead of training a separate model for each task, the chain-of-thought prompting approach uses a large-scale language model for a small number of samples of prompts, allowing knowledge and parameters to be shared across multiple tasks, as compared to traditional task-specific fine-tuning-based approaches. In addition, the approach provides interpretability and debugging capabilities, allowing for a better understanding of the model's behavior and errors.

![image](https://github.com/user-attachments/assets/242a7e89-984c-4dc7-9765-9d4e2229ff95)

### 4. Issues addressed 
The method addresses an important current problem in the field of NLP: **how to make language models more reasoning and interpretable**. By introducing the concept of chain thinking, the method enables the model to decompose complex problems and solve them step by step, while also explaining its reasoning process. This not only helps to improve the performance of the model, but also helps to increase understanding and trust in the model's behavior.

## Experiments
This paper focuses on the performance of chain-of-thought prompting for mathematical and common-sense reasoning tasks in language models of different sizes, and explores the relationship between its performance and model size, as well as its ability to adapt to diversity. The experimental results show that chain-of-thought prompting can significantly improve the performance of language models on these tasks as the model size increases. 

![image](https://github.com/user-attachments/assets/f7f53cac-312e-48d4-900d-b5c673c80b06)

Besides, the paper investigates different variants of chained thinking prompts and their effects, and explains the success of chained thinking prompts by analyzing the types of errors. And, it also demonstrates the application of the chain-thinking cue to symbolic reasoning tasks, proving that it not only helps language models solve difficult problems, but also promotes length generalization. 

![image](https://github.com/user-attachments/assets/17e89f59-b44b-4c0d-b8eb-7a1f8ca47f85)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a simple and widely applicable method, chain-of-thought prompting, for enhancing the reasoning ability of LLMs.
  2. It is experimentally demonstrated that chain-of-thought prompting can significantly improve the performance of LLMs on tasks such as arithmetic, commonsense, and symbolic reasoning, and has stronger generalization ability and smaller data requirements than traditional prompting methods.
  3. The findings suggest that chained thought prompts are an effective tool to extend the range of capabilities of LLMs and further stimulate research directions in solving complex problems using NLP techniques.
 
### 2. Innovative points
  1. Chained Thinking Prompts, a new prompting approach, is proposed to guide the model through the reasoning task by generating a series of intermediate natural language reasoning steps.
  2. In the experiments, Chained Thinking Prompts were applied to many different types of reasoning tasks and achieved excellent performance.
  3. Compared with traditional prompting methods, chained thought prompting does not require a large amount of training data and complex NN structures, and thus is more flexible and easier to implement. 

### 3. Future Works
  1. As language models continue to grow in size, chained thought prompts may become a more general and effective method for enhancing the inference of models.
  2. Further research could explore how chained thought prompts can be applied to other types of tasks such as text categorization, question and answer systems, etc.
  3. Consideration could be given to using chained thought prompts in conjunction with other techniques, such as meta-learning, transfer learning, etc., to further improve the performance and efficiency of the model.   
