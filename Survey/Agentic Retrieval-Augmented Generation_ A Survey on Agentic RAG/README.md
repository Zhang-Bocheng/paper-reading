# Agentic Retrieval-Augmented Generation_ A Survey on Agentic RAG
[paper link](https://arxiv.org/pdf/2501.09136) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper describes how Large Language Models (LLMs) have revolutionised natural language understanding and text generation, but their reliance on static training data limits their responsiveness to dynamic, real-time queries.          | Retrieval-Augmented Generation (RAG)         |

## Methodology

### 1. Abstract
To address the problem, the authors propose the Retrieval Augmented Generation (RAG) approach and further develop the Autonomous AI Agent Embedded Agentic Retrieval Augmented Generation (Agentic RAG). The approach achieves the ability to dynamically manage retrieval strategies, iteratively optimise contextual understanding, and adapt to workflows by embedding autonomous AI agents into the RAG process. The article details the fundamentals and application areas of Agentic RAG, including healthcare, finance, and education. 

In addition, the article explores the challenges of implementing Agentic RAG, such as problems in scaling, ethical decision making and performance optimisation, and provides the framework and tools required to implement Agentic RAG. In conclusion, Agentic RAG is a flexible, scalable and context-aware approach that can play an important role in several application scenarios.

![image](https://github.com/user-attachments/assets/da69727d-be97-4274-a4d8-34837e578e3c)

### 2. Method Description 
The Retrieval-Augmented Generation (RAG) proposed in this paper is an artificial intelligence-based NLP technique that combines the advantages of Large Language Modelling (LLM) and real-time data retrieval. It improves the quality of generated results by dynamically retrieving relevant information and integrating it into the generation process.The architecture of RAG consists of four main components: a coordinator, a router, a parallel processor and an evaluator-optimiser.

The coordinator is responsible for receiving user queries and selecting the appropriate processing strategy based on their type. The router routes queries to specialised processors or knowledge sources such as structured databases, semantic search, web search or recommender systems. Multiple processors can work simultaneously to improve efficiency. Finally, the evaluator-optimiser iteratively adjusts the output using a feedback mechanism to further improve quality.

The RAG system has the following advantages:

  1. The ability to adapt to different types of queries improves response accuracy.
  2. Can effectively utilise various data sources such as structured databases, semantic search, web search, etc.
  3. Highly scalable and flexible, allowing new processors or knowledge sources to be added as required.

![image](https://github.com/user-attachments/assets/b598870e-ddd5-4b62-bcb0-b2e5eac8d552)

### 3. Methodological improvements
In this paper, the authors propose five different system architectures for Agentic RAGs which are Single Agentic RAG, Multi-Agent Agentic RAG, Hierarchical Agentic RAG, Self-Correcting Agentic RAG and Graphically Enhanced Agentic RAG.These system architectures are optimised for different application scenarios such as processing of complex queries, fast response to high load situations, and reduced computational resource consumption.

![image](https://github.com/user-attachments/assets/d243a1a3-e9ab-44ef-b114-43836d993cf8)

![image](https://github.com/user-attachments/assets/026c23c2-3005-4685-890e-056ee3203af1)

![image](https://github.com/user-attachments/assets/542af1b0-2651-4432-9a71-515a83988865)

![image](https://github.com/user-attachments/assets/4eafdaca-5b0d-411e-bf64-4358d59556ac)

### 4. Issues addressed 
The main contribution of this paper is to propose a novel Agentic RAG framework that dynamically selects appropriate knowledge sources and integrates them into the generation process. This enables the system to answer user queries more accurately and also reduces the reliance on static pre-training data. In addition, this paper describes five different Agentic RAG system architectures that are optimised for different application scenarios, thus improving the performance and efficiency of the system.

## Experiments
This paper focuses on the development history of Retrieval-Augmented Generation (RAG) systems as well as the architectural design and application scenarios at different stages. Firstly, the article introduces the basic principles of traditional RAG systems and lists several classic cases to illustrate their applications in different fields. Next, the article discusses the development of Agentic RAG, including the graph-based Agentic RAG and Agentic Document Workflows (ADW), and gives their specific application cases in various domains. Finally, the article also introduces some tools and frameworks related to Agentic RAG, as well as related benchmarks and datasets.

Overall, this article aims to show readers the value and potential of Agentic RAG in real-world applications, and how existing tools and frameworks can be utilised to build efficient and reliable Agentic RAG systems. By presenting different application scenarios and experimental results, this paper can help readers better understand the advantages and limitations of Agentic RAG technology, thus providing guidance and reference for future applications.

![image](https://github.com/user-attachments/assets/6d326c4d-d077-4077-8aac-3a2011aeb9e3)

![image](https://github.com/user-attachments/assets/d3d4b827-1dbd-4822-bbdb-fc00b5a10268)

## Conclusion

### 1. Advantages of the Thesis
  1. The shortcomings of traditional RAG systems are comprehensively sorted out, which provides a reference for subsequent research.
  2. A new Agentic RAG framework is proposed to solve the problems of traditional RAG by introducing autonomous intelligences, which is highly innovative and practical.
  3. The paper elaborates the working principle and implementation of Agentic RAG, which is of great significance for understanding this new framework.

### 2. Innovative points
  1. Autonomous intelligences are introduced, which can better handle complex tasks and multi-step reasoning.
  2. A dynamic decision-making mechanism is adopted, which is able to adjust the strategy in real time according to the contextual information.
  3. Adaptive learning capability is implemented, which can improve its performance in continuous practice.

### 3. Future Works
  1. Continuously optimise the algorithm to improve the computational efficiency and performance performance of Agentic RAG.
  2. Explore more application scenarios, such as natural language Q&A, text summarisation and other fields.
  3. Combine Agentic RAG with other technologies to form more powerful solutions.  
