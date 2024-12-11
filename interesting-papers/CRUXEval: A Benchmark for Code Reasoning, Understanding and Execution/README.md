# CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution
[paper link](https://arxiv.org/pdf/2401.03065) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a benchmark for evaluating code reasoning, understanding, and execution called CRUXEval, and provides a general scheme for generating it.          | Code Generation         |

## Methodology

### 1. Abstract
The authors used 800 Python functions (each 3 to 13 lines of code in length), each with an input-output pair, so that two natural tasks can be performed: input prediction and output prediction. The authors then evaluate 20 code models on the benchmark and find that many of the models that recently scored high on HumanEval do not perform well on the benchmark. Finally, the authors show that simple CoT and fine-tuning methods can improve performance on this benchmark, but are still far from solving the problem. The best setup is GPT-4 combined with Chain Thinking (CoT), achieving pass rates of 75% and 81%. In comparison, Code Llama 34B had pass rates of 50% and 46%, highlighting the gap between open and closed source models.

### 2. Method Description 
The paper presents a dataset called CRUXEval for evaluating the performance of models in Python code generation tasks. The dataset contains 800 different functions and their input-output pairs, divided into two tasks: **an output prediction task and an input prediction task**. The goal of the output prediction task is to predict the output obtained after executing the function; while the goal of the input prediction task is to find an input such that the output obtained after executing the function is the same as the given output. For both tasks, a correctness metric based on the execution result is used.

![image](https://github.com/user-attachments/assets/9478ae45-9c45-4ceb-9d17-5adb03760cf6)

### 3. Methodological improvements
To generate the dataset, the authors used the Code Llama 34B model to generate all candidate functions and inputs. Specifically, they allowed the model to generate Python functions that used specific functions from the Python standard library by providing a number of hint statements, and also provided two samples with different difficulty levels to increase the diversity of the generated samples. In total, 102,000 functions and 489,306 input-output pairs were generated.

To ensure that the generated samples were of high quality and reasonable, the authors designed a series of filters to screen out tasks that were unreasonable or difficult to complete. These filters included requirements for compile time, run time, and best-effort removal of other undesirable code.

### 4. Issues addressed 
The method addresses the issue of how to construct a dataset that can be used to evaluate the performance of models in Python code generation tasks. In addition, the method takes into account the quality and noise of the dataset, which improves the reliability and accuracy of the assessment.

## Experiments
Firstly, the authors evaluated multiple models using CRUXEval and compared the results with those of HumanEval. The results show that after fine-tuning and optimisation of the dataset, some models based on GPT-3.5 and GPT-4 perform significantly better than others on HumanEval, but not as well as base models such as Code Llama on CRUXEval. This suggests that training more powerful code generation models by extracting knowledge from GPT may not necessarily improve their execution.

![image](https://github.com/user-attachments/assets/f6687937-bf92-4e9e-bafd-616e408644c1)

Secondly, the authors also conducted experiments on the relationship between input prediction and output prediction. The results show that there is some correlation between these two tasks, but this correlation is not very strong. In addition, for different models, their performance on different tasks varied, demonstrating that the ability of a model does not only depend on its size, but is also related to its specific design.

![image](https://github.com/user-attachments/assets/14aa2beb-7949-4043-b1c4-010258e1600e)

Next, the authors conducted a study on the Chain of Thought (CoT) prompting method. The results show that CoT can significantly improve the performance of some models, especially the GPT-4; however, in some cases, CoT can reduce the performance of the model, and therefore needs to be used with caution.

![image](https://github.com/user-attachments/assets/1e08e843-fa3f-4523-888b-52dabb56f4c3)

Finally, the authors also performed some preliminary fine-tuning experiments to understand the effect of simple fine-tuning schemes on CRUXEval performance. The results show that even with a simple fine-tuning scheme, the performance of the model cannot reach the expected level, which suggests that CRUXEval has a difficult task and requires a more complex fine-tuning strategy to achieve better results. 

![image](https://github.com/user-attachments/assets/4e5be015-4666-4fe3-9df5-d6ef6deabdc6)

## Conclusion

### 1. Advantages of the Thesis
  1. The benchmark uses simple but representative Python functions as test data and aims to evaluate the performance of code generation models in terms of input prediction and output prediction.
  2. In addition, the article provides detailed experimental results and analyses, providing researchers with a comprehensive understanding of the performance of current code generation models.

### 2. Innovative points
  1. The main contribution of this paper is to propose a new code understanding evaluation benchmark, CRUXEval, and to design a series of experiments to evaluate the performance of different types of code generation models on this task.
  2. In addition, the authors provide detailed analyses and explanations of the experimental results, thus helping readers to better understand the strengths and weaknesses of these models.

### 3. Future Works
  1. In future research, more tasks can be considered to be added to CRUXEval, such as testing execution complexity, programme debugging capabilities, etc.
  2. Moreover, tests using more complex programming languages or more realistic code snippets can be tried to further improve the usefulness of the benchmark.
  3. Also, some new technical tools, such as co-training and self-repairing, can be explored to improve the performance of code generation models. 
