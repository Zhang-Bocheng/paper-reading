# DeepRAG: Thinking to Retrieval Step by Step for Large Language Models
[paper link](https://arxiv.org/pdf/2502.01142) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper presents a framework called DeepRAG for optimizing language models based on retrieval-enhanced reasoning (RAG).          |  Retrieval-augmented Generation(RAG)        |

## Methodology

### 1. Abstract
Large language models (LLMs) are prone to factual illusions in the reasoning process due to temporal, accuracy and coverage issues. Also, combining inference with RAG faces problems such as ineffective task decomposition and redundant retrieval, which may introduce noise and degrade response quality. Therefore, DeepRAG achieves strategic and adaptive retrieval by modeling RAG as a Markov Decision Process (MDP), and by iteratively decomposing the query and dynamically deciding whether to retrieve external knowledge or rely on parametric reasoning at each step.

![image](https://github.com/user-attachments/assets/49573d71-647f-4df8-a416-5498042571da)

### 2. Method Description 
The paper presents Deep-RAG, a Markov Decision Process (MDP)-based retrieval-enhanced generation model for multi-round question and answer problems in natural language reasoning tasks. The model decomposes the question into multiple subqueries and decides the answer generation strategy by choosing whether to use external knowledge in each subquery. Specifically, the model maintains a partial solution in each state that includes the input question, known information, and an intermediate answer. If it chooses to continue, it generates the next subquery and moves to the next state; otherwise, the model generates the final answer and stops. At each state, the model also considers whether it needs to obtain information from external sources to generate a more accurate answer.
![image](https://github.com/user-attachments/assets/8c92f56a-f56d-49bc-a4cb-045bef9c06ca)

### 3. Methodological improvements
Deep-RAG introduces techniques such as binary tree search and imitation learning to improve the performance of the model compared to traditional single decoder generation models. Specifically, the model utilizes binary tree search to construct different retrieval paths in order to select the best answer generation strategy in each subquery. And, the model employs imitation learning techniques to train the model by synthesizing optimal reasoning processes so that it can better understand when internal knowledge should be used instead of external knowledge.

### 4. Issues addressed 
The model can handle these problems efficiently because it is able to select the best answer generation strategies in each subquery and can dynamically adjust these strategies as needed. Besides, the model avoids over-reliance on external knowledge, which improves the reliability and robustness of the model. Thus, Deep-RAG is a very useful tool to help researchers better understand and solve multi-round question and answer problems in natural language reasoning tasks.

## Experiments
This paper focuses on the performance of the DeepRAG model in different question and answer tasks, and conducts several sets of comparison experiments to verify its superior performance and reliability. Specifically, the comparison experiments in this paper include the following:

**Model comparison experiments:** the performance of DeepRAG in different Q&A tasks is evaluated by comparing it with CoT, CoT*, CoT-Retrieve, CoT-Retrieve*, IterDRAG, UAR, FLARE, TAARE, and AutoRAG methods, and it is concluded that DeepRAG has better performance and more reliable reasoning ability is concluded.
![image](https://github.com/user-attachments/assets/b9b42797-5e00-4c5f-80c0-1b8f08f7c884)

**Data analysis experiments:** questions in the dataset are analyzed to explore how DeepRAG performs on different types of questions and how knowledge boundaries can be effectively identified and utilized.
![image](https://github.com/user-attachments/assets/9d7023a9-a275-40f8-8483-8a9b77d846d0)

**System efficiency experiments:** by comparing the average number of retrieval times and accuracy rates, the advantages of DeepRAG in efficient retrieval are verified.

**Experimental results analysis:** by analyzing the F1 score, accuracy rate, balanced accuracy and Matthews correlation coefficient, DeepRAG is further proved to have better performance on different types of problems.  

![image](https://github.com/user-attachments/assets/3342ba25-6f9c-4181-b79f-48ae7a3a79db)

## Conclusion

### 1. Advantages of the Thesis
The framework introduces two key components: retrieval narratives and atomic decisions by modeling the retrieval process as a Markov Decision Process (MDP) to achieve a smarter, adaptive retrieval process. Experimental results show that DeepRAG significantly outperforms existing methods on multiple open-domain Q&A datasets, improving answer accuracy and retrieval efficiency.

### 2. Innovative points
The main innovation of DeepRAG is its approach of combining a RAG model with a Markov decision process. Specifically, it employs a binary tree search method to explore the impact of atomic decisions on the inference results, and learns by synthesizing the data into a language model to capture the pattern of “subquery generation-atomic decisions-intermediate answers”. In addition, the authors designed a chain calibration method to further improve the model's understanding of its own knowledge boundaries, allowing it to dynamically determine when retrieval is required. 

### 3. Future Works
Future research could consider extending DeepRAG to more application scenarios, such as natural language dialog systems or tasks such as text summarization. And, further research could be conducted on how to optimize the retrieval process in order to better balance the retrieval requirements with the model's own knowledge boundaries.    
