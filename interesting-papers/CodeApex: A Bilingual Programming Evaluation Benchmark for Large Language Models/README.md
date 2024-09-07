# CodeApex: A Bilingual Programming Evaluation Benchmark for Large Language Models
[paper link](https://arxiv.org/pdf/2309.01940) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes CodeApex, a new programming competence assessment benchmark designed to evaluate the performance of Large Language Models (LLMs) in programming understanding, code generation, and code fixing.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The benchmark consists of multiple-choice questions testing the LLM's ability to perform conceptual understanding, common-sense reasoning, and multi-step reasoning, and assesses the LLM's ability to complete C++ functions by providing descriptions and prototypes, as well as having the LLM fix erroneous code segments in the real world with different error messages. The authors used 12 widely used LLMs for the evaluation, including both general-purpose and specialised models. 

The results showed that GPT-4 demonstrated the best programming ability, achieving about 69%, 54% and 66% accuracy on the three tasks, respectively. There is still a lot of room for improvement in programming for LMMs compared to human performance. The authors hope that CodeApex can be used as a reference for evaluating the programming ability of LMMs to further promote their development and growth.

### 2. Method Description 
The paper describes several approaches for code understanding, generation and annotation. Among them, encoder-based approaches use NNs to transform source code into graphical structures or fixed-length vector representations to capture structural information about the code and enhance the accuracy of programming understanding. Meanwhile, Transformer architectures have been introduced, with models such as CodeT5 and CodeBERT, which can map natural language and code into a shared vector space and utilise attentional mechanisms to capture the semantic relationships between them. There are also models for specific programming tasks such as code annotation generation and API documentation generation.

In terms of code generation, code generation has also received a lot of attention due to the emergence of large-scale language models (LLMs). These models are typically pre-trained with large-scale text datasets to learn rich language representations. General-purpose LLMs (e.g., GPT and Llama) have some code generation capabilities. Some LLMs specifically designed for programming tasks aim to improve their coding performance. A common approach to code generation is to use existing large-scale language models for fine-tuning. 

In this approach, pre-trained language models are used as initial models and further trained on specific code generation datasets. For example, models such as Codex, PaLMCoder, and CodeGeeX2 are further trained on large public code datasets based on models such as GPT-3, PaLM, and ChatGLM2, demonstrating better programming understanding and generation capabilities. With the development of instruction fine-tuning techniques, a range of models (e.g., WizardCoder, Code Llama-Instruct, and PanguCoder) demonstrate powerful multilingual code generation and debugging capabilities. Another popular approach is hint engineering, which involves designing suitable hints or guidance statements to guide the model through specific code generation tasks. 

By providing insightful input, models can generate more accurate and expected code output. For example, CodeGen transforms natural language problems into code generation tasks and improves generation with appropriate hint engineering techniques.DocPrompting, on the other hand, uses keyword search to integrate information from the codebase to guide the performance of LLMs in code generation tasks.

![image](https://github.com/user-attachments/assets/50b27194-24fc-4f00-b7b4-4be5f1f22ea3)

### 3. Methodological improvements
In contrast to traditional rule- or template-based approaches, these encoder- and LLMs-based approaches do not require complex rules or templates to be manually written, but instead automatically infer the correct way to generate code by learning from a large amount of source code and associated annotations. This makes these methods more flexible and adaptable to handle a wide range of different types of programming tasks.

### 4. Issues addressed 
These problems include, but are not limited to: programming understanding, code generation, code annotation generation, API documentation generation, multilingual code generation and debugging. By using these methods, researchers can better understand source code, automatically generate high-quality code, and generate detailed code comments and API documentation. In addition, these methods can help developers find and fix bugs faster, thus improving the efficiency and quality of software development.

## Experiments
This paper presents a detailed description of the three tasks of the CodeApex benchmark test: programming comprehension, code generation, and code fixing. 
<br>&emsp;In the programming comprehension task, the authors used 250 multiple-choice questions to examine the model's ability to understand the programming language, divided into three categories of questions: conceptual understanding, commonsense reasoning, and multi-step reasoning. 
<br>&emsp;In the code generation task, the authors provide basic practice questions that allow the model to generate code that conforms to the test cases by entering natural language descriptions of the problems and sample inputs and outputs. 
<br>&emsp;Finally, in the code fixing task, the authors chose incorrect codes and standard answers from the assignments submitted by the students and let the model modify them. For each task, the authors designed different prompting strategies and evaluation metrics, such as accuracy and pass rate. 

In addition, the authors present 12 large pre-trained models with different parameter settings for comparing their performance on these tasks. Overall, this paper provides researchers with a comprehensive benchmarking framework that can be used to evaluate the performance of large language models in the programming domain. 

![image](https://github.com/user-attachments/assets/9de27ded-1431-417b-8db9-552674d5822f)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents CodeApex, a comprehensive benchmark designed to evaluate the programming capabilities of LLMs. The authors conduct extensive experiments using various methods such as prompting, chains of thought, and answer-only to assess the LLM's performance in multiple categories of multiple-choice questions. 

  2. The paper contributes to the understanding of the current state of LLMs' programming abilities and provides insights into their strengths and weaknesses. The results suggest that while LLMs have made significant progress in recent years, they still have a long way to go before reaching human-level performance in programming tasks.

### 2. Innovative points
 1. The authors employ a combination of methods to assess the LLM's programming capabilities. They design a set of benchmarks that cover multiple categories of multiple-choice questions, including syntax, semantics, and logic. They also evaluate the LLM's ability to generate code and correct errors in existing code. 

  2. The authors also explore different prompting strategies, such as answer-only and chain-of-thought, to see how they affect the LLM's performance. This approach allows them to identify which prompting techniques work best for specific tasks and helps guide future research in this area.

### 3. Future Works
  1. The paper highlights several areas where future research can focus on improving the LLM's programming capabilities. One key area is the development of more sophisticated prompting techniques that can help the LLM better understand the problem at hand. 

  2. Additionally, the authors suggest exploring other programming paradigms beyond imperative and functional programming, such as object-oriented programming, to broaden the scope of the evaluation.
  
  3. Finally, the authors encourage further exploration of the ethical implications of using LLMs for programming tasks, particularly when it comes to the potential for bias and unintended consequences.  
