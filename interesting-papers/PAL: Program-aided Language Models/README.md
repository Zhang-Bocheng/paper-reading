# PAL: Program-aided Language Models
[paper link](https://arxiv.org/pdf/1709.04109) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This thesis focuses on the performance of large-scale language models (LLMs) in mathematical, symbolic and algorithmic reasoning tasks and proposes a new approach called Program-Aided Language models (PAL).         | Large-scale Language Models (LLMs)         |

## Methodology

### 1. Abstract
The approach uses LLMs to read natural language problems and generate programs as an intermediate reasoning step, but delegates the solution part to the interpreter for processing. Experimental results show that using LLM to generate code and reasoning with the Python interpreter has higher accuracy than larger models across 13 natural language reasoning tasks. For example, PAL implemented using CODEX achieves better results in the GSM8K benchmark test, outperforming PaLM-540B using chainthinking, improving top-1 accuracy by an absolute 15%.

### 2. Method Description 
This paper proposes the Program-aided Language Model (PAL), a new NLP model that presents the thought process between problem and solution in an alternating form that includes both natural language and programming language statements. The model uses an interpreter to execute program code and does not provide the final answer. The language model is allowed to generate predictions containing intermediate steps and their corresponding programme statements.

![image](https://github.com/user-attachments/assets/2bbd293b-572d-49dd-a1c5-5ca37604f016)

### 3. Methodological improvements
In contrast to traditional chain-of-thought reasoning-based approaches, the PAL model, by combining natural language problem solving steps with corresponding procedural statements, enables the model to learn to generate a procedure that provides an answer to the test question, rather than relying on the language model to correctly compute the answer. And, the article mentions the importance of keeping the generated code relevant to the problem entity through meaningful variable names.

### 4. Issues addressed 
By combining natural language problem solving steps with corresponding program statements, the model can improve the reasoning power and accuracy of the model. Besides, the paper explores how to write meaningful variable names and how to relate procedural statements to problem entities, which further improves the model's performance.

## Experiments
This paper describes the authors' experimental study of three directions of reasoning tasks, including mathematical problems, symbolic reasoning, and algorithmic problems, and compares the effectiveness of different prompting methods. Specifically, they used direct hinting, chain-thinking hinting, and our hinting approach to solve these problems, and tested them on multiple benchmark datasets. 

Their results show that using our hinting approach significantly improves the performance of the model, especially when dealing with large numbers. In addition, they explored a number of factors related to the cueing method, such as the strength of the model, the capabilities of natural language models, and the importance of variable names.
![image](https://github.com/user-attachments/assets/2ec84e29-bdd4-4875-97c6-3be5ccf1d029)

![image](https://github.com/user-attachments/assets/2feb6c14-a474-4ea3-8e89-68b91f6a3303)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a new natural language reasoning method, the procedural assisted language model (PAL), which avoids the potential for incorrect answers that can arise in existing methods such as chain thinking by decomposing natural language problems into procedural steps and solving the problems in real test examples using the Python interpreter. 
 
### 2. Innovative points
Unlike existing chain-thinking approaches based on large-scale pre-trained language models, the PAL method proposed in this paper divides the problem-solving process into two stages: 
1. The natural language problem is transformed into procedural steps by the language model;
2. These steps are passed to the Python interpreter to obtain the final answer. This approach effectively solves the problems existing in existing methods, such as performance degradation when dealing with complex arithmetic or large numbers.
 
### 3. Future Works
In the future, it can be further explored how to integrate more symbolic reasoning techniques into PAL to improve its reasoning capability and applicability. And, it can be investigated how symbolic reasoning can be integrated with knowledge from other domains to achieve a more comprehensive and intelligent AI system.  
