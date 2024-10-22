# OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement
[paper link](https://arxiv.org/pdf/2402.14658) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an open source code system called OpenCodeInterpreter that aims to address the limitations of current large-scale language models for code generation.          | Large Language Model (LLM)          |

## Methodology

### 1. Abstract
The system integrates code generation, execution, and iterative improvement, and enables dynamic code improvement through the Code-Feedback dataset. Experimental results show that OpenCodeInterpreter performs excellently, achieving similar or even better results than GPT-4 Code Interpreter in benchmark tests such as HumanEval and MBPP. This result fills the gap between open source code generation models and proprietary systems.

### 2. Method Description 
This paper presents a dataset called Code-Feedback, designed to train the OpenCodeInterpreter model. The dataset features diverse and challenging real-world queries, multi-round dialogue structures, and a mix of natural language interpretations and code snippet responses. To meet these needs, the researchers used five different methods to construct the dataset and collected queries from two main sources (the open source dataset and the LeetCode programming challenge).

![image](https://github.com/user-attachments/assets/6014e986-9c52-4a65-81db-ff824ecaa9a9)

### 3. Methodological improvements
  1. The researchers used a very powerful open-source chat model, Qwen-72B-Chat, for the filtering process to ensure that the most challenging instructions were ultimately selected. They also developed a simulator using GPT-3.5 and GPT-4 to mimic real user interactions and introduced simulated human feedback to encourage the model to further optimise the solution.

  2. In addition, the researchers designed an error-correction-focused stage to improve the model's error handling by deliberately generating incorrect code fragments. This approach enabled the model to learn the ability to successfully generate code and identify and correct errors, which significantly improved its problem solving ability and understanding of the debugging process.
     
### 4. Issues addressed 
The dataset addresses multiple challenges faced when training OpenCodeInterpreter models, including how to provide diverse and challenging real-world queries, how to implement a multi-round dialogue structure, and how to merge natural language interpretation and code snippets. By using the above approach, the researchers have successfully created a dataset containing multiple types of questions and richly varied solutions that can be used to train more accurate and efficient code interpretation models

## Experiments
This paper focuses on OpenCodeInterpreter, an open source code generator based on multi-source data, and verifies its performance and effectiveness through several comparison experiments.

Firstly, the authors conducted a single comparison experiment of code generation, comparing OpenCodeInterpreter with leading models such as GPT-3.5/4-Turbo, CodeLlama-Python, Wizard-Coder, Deepseek-Coder, and so on. The experimental results show that OpenCodeInterpreter performs well at different scales, with the OpenCodeInterpreter-DS 33B version achieving the highest score.

Second, the authors conducted several comparative experiments on code generation to examine the performance of OpenCodeInterpreter under iterative feedback. The results of the experiments show that OpenCodeInterpreter outperforms the SOTA benchmark at all scales in the execution feedback scenario and achieves a significant advantage on the 6.7B and 33B models.
![image](https://github.com/user-attachments/assets/5ccb1d9a-0d37-492a-ae8d-b44511f2f390)

In addition, the authors conducted comparative experiments with data sources to explore the impact of high quality single input and diverse feedback mechanisms on OpenCodeInterpreter. The experimental results show that incorporating high-quality single inputs can significantly improve OpenCodeInterpreter's multi-round performance, while diverse feedback mechanisms can also significantly enhance OpenCodeInterpreter's debugging and correction capabilities.
![image](https://github.com/user-attachments/assets/c92ac1d1-0798-401c-a5a5-e5f96f06e7ff)

Finally, the authors present three real-world examples to demonstrate the performance of OpenCodeInterpreter in practical applications. These cases include functions such as computing prime numbers, verifying IPv6 addresses, and identifying the intersection of two lists. Although OpenCodeInterpreter has limitations in some cases, these cases still demonstrate the power and usefulness of OpenCodeInterpreter. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents an open source code system called OpenCodeInterpreter that improves the quality and accuracy of code generation by integrating execution feedback and human feedback. The authors also develop a dataset called Code-Feedback, which contains multiple rounds of interactions between users, code models, and compilers to support iterative improvement of the system.
  
  2. By evaluating OpenCodeInterpreter against widely recognised benchmarks (e.g., HumanEval, MBPP, etc.), OpenCodeInterpreter demonstrates its superior performance in code generation and is comparable to state-of-the-art proprietary systems (e.g., the GPT-4 code interpreter). In addition, the authors released OpenCodeInterpreter as an open source project, making it easier to use and extend.

### 2. Innovative points
  1. OpenCodeInterpreter is unique in its ability to use both execution feedback and human feedback for iterative code generation improvements. Specifically, the system uses compiler diagnostics to correct errors and human insights to optimise code generation.
  
  2. This approach enables OpenCodeInterpreter to produce solutions that are both technically correct and tailored to the user's needs, resulting in significant improvements in overall performance.
  
  3. In addition, the authors developed the Code-Feedback dataset, a large dataset containing multiple rounds of interactions, to train and evaluate OpenCodeInterpreter.
 
### 3. Future Works
Future efforts should focus on further improving and refining OpenCodeInterpreter's methods and techniques to better meet the needs of real-world applications. In addition, as the open source community grows and becomes more popular, OpenCodeInterpreter may become one of the preferred tools used by more developers.    
