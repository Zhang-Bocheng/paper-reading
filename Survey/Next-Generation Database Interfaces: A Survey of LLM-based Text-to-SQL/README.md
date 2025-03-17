# Next-Generation Database Interfaces: A Survey of LLM-based Text-to-SQL
[paper link](https://arxiv.org/pdf/2406.08426) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This dissertation focuses on how to address the challenges in text-to-SQL tasks by translating user questions into SQL statements using natural language understanding techniques.          |  Text-to-SQL        |

## Methodology

### 1. Abstract
While traditional approaches have combined manual engineering and deep neural networks, recent research has used pre-trained language models (PLMs), but as databases and problems become more complex, the effectiveness of PLMs is limited. As a result, researchers have begun to explore the use of large-scale language models (LLMs) to improve the performance of text-to-SQL tasks. This paper provides a comprehensive review of existing text-to-SQL research based on LLMs and presents relevant datasets, evaluation metrics, and recent advances.

![image](https://github.com/user-attachments/assets/6d153989-714e-4658-982d-354506b144d9)

### 2. Method Description 
This paper describes the Text-to-SQL (TTS) task and its challenges, and outlines research advances in the field. The task aims to transform natural language problems into executable SQL queries for data access and analysis. Four different approaches are proposed in the paper: **rule base, deep learning, pre-trained language models (PLMs) and large-scale language models (LLMs)**. Among them, the rule base approach relies on manually written rules and heuristic algorithms to map natural language problems to SQL queries; the deep learning approach uses sequence-to-sequence models or encoder-decoder constructs such as LSTMs and transformers; and the PLMs approach works by fine-tuning pre-trained language models such as BERT and RoBERTa to achieve better results on standard Text-to -SQL datasets for better performance; and LLMs approaches utilize large-scale language models with substantial semantic knowledge, such as the GPT family, for SQL generation.

![image](https://github.com/user-attachments/assets/f3c9e4bf-73f4-429b-bf34-8204f48bea90)

### 3. Methodological improvements
  1. Using Graphical Neural Networks (GNN) to handle complex database relationships;
  2. Integration of database structure information into pre-trained language models to enhance the system's understanding of the database;
  3. Utilizing prompt engineering to guide the application of large-scale language models in SQL generation;
  4. Improving the robustness of models to adapt to contaminated or perturbed data environments;
  5. Developing cross-language Text-to-SQL methods in order to support the needs of users in different languages;
  6. Designing long-context Text-to-SQL datasets to evaluate and improve model performance in complex SQL environments;
  7. Developing domain-specific Text-to-SQL datasets to meet the needs of finance, healthcare, and other domains.

### 4. Issues addressed 
The main goal of Text-to-SQL is to help non-specialists interact with databases easily, thus eliminating the requirement of specialized SQL programming knowledge. This helps in various business scenarios such as business intelligence, customer support, and scientific research by enabling users to retrieve what they need and analyze data more efficiently. However, the task faces many challenges, such as the complexity and ambiguity of natural languages, the understanding and representation of database architectures, and rare and complex SQL operations. 

## Experiments
This paper focuses on two training methods based on large-scale language models (LLMs) in text-to-SQL tasks: unsupervised pretraining and supervised fine-tuning, and compares their respective advantages and disadvantages. Among them, unsupervised pre-training is a method of autoregressive training of models with large-scale data to obtain text generation capabilities, while supervised fine-tuning is a method of tuning models for domain-specific data to improve performance.

For unsupervised pre-training methods, the authors mention CodeLLaMA and StarCoder, two code-specific LLMs, and point out that they can be used to generate code under user instructions. In addition, the authors discuss some text-to-SQL related evaluation metrics such as Component Matching, Exact Matching, Execution Accuracy, and Valid Efficiency Score, and briefly describe the role of these metrics.

![image](https://github.com/user-attachments/assets/2d88064a-0905-4ef6-996e-3410efb31197)

For the supervised fine-tuning approach, the authors mentioned the process of fine-tuning using the collected data and divided it into two phases: the initial phase and the complete phase. In the initial phase, the model is fine-tuned to fit a specific domain, while in the complete phase, the model is further fine-tuned to improve performance. The authors also present some techniques and methods related to supervised fine-tuning, such as augmented architectures, pre-training, and decoder optimization, and discuss how these techniques affect the performance of the model.  

![image](https://github.com/user-attachments/assets/11536ac6-07cb-4fba-91d6-c658429d61b2)
