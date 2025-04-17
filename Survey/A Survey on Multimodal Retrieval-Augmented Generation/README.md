# A Survey on Multimodal Retrieval-Augmented Generation
[paper link](https://arxiv.org/pdf/2504.08748) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper presents the current research status and application prospects of multimodal enhancement generation (MRAG) technology.          |  Retrieval-Augmented Generation (RAG)        |

## Methodology

### 1. Abstract
Traditional retrieval augmentation generation (RAG) systems mainly rely on textual data, but are limited by the fact that they can only utilize a single data type, which does not make full use of rich multimedia information. Therefore, the authors propose an MRAG approach that integrates multiple data types (e.g., text, image, and video) into the retrieval and generation process. The approach generates answers containing multiple data types by locating and integrating relevant knowledge from different modalities in the retrieval phase and using multimodal large-scale language models (MLLMs) in the generation phase. 

Experimental results show that MRAGs have higher accuracy and fewer illusions in understanding and answering queries, and perform better than traditional textual modal RAGs. And, the article provides a systematic review of key components and techniques of MRAG, datasets, evaluation methods and metrics, and existing limitations, and suggests future research directions. The article provides a comprehensive understanding and support for constructing and improving MRAGs, and helps to advance the development of multimodal information retrieval and generation.

### 2. Method Description 
This paper focuses on the development of MRAG (Multimodal Retrieval-Augmented Generation) framework and the technical details of its three phases. Among them, MRAG1.0 used pseudo-MRAG to transform multimedia data such as text, images, etc. into modal features and stored them in a vector database, and then completed the query-answer task through the two modules of Retrieval and Generation; MRAG2.0 introduced MLLM (Large Language Model) to directly process multimedia data, and optimized the Retrieval and Generation modules to support multimodal input and output; MRAG 3.0 further extends the system functions, including enhancing the document parsing module, adding the search planning module, modifying the generation module, etc., so that the system can better cope with the needs of different scenarios.

![image](https://github.com/user-attachments/assets/17dee4ba-3f50-453c-bea8-c9eb5ed0193c)

![image](https://github.com/user-attachments/assets/2d807400-dbbd-4d09-9a25-61908eac55e6)

![image](https://github.com/user-attachments/assets/7ab7309a-91e2-4e89-8924-7fdbba0ee43d)

### 3. Methodological improvements
Compared with the traditional unimodal Q&A system, the MRAG framework can handle data in multiple modalities, which improves the intelligence of the system. In addition, MRAG adopts more advanced technological tools, such as MLLM, adaptive search planning, etc., which further improves the performance and effectiveness of the system.

### 4. Issues addressed 
The MRAG framework solves the problem that traditional unimodal Q&A systems are unable to deal with multimodal data, and at the same time, it adopts more advanced technological means to make the system more intelligent and efficient. Therefore, the framework has a wide range of application prospects in the field of natural language processing.

## Experiments
This paper focuses on three different evaluation methods used in MRAG systems, and compares and analyzes them in detail. These evaluation methods include the rule-based evaluation method, the language model-based evaluation method, and the combined coarse and fine-grained evaluation method.

First, the authors provide a brief introduction to the fundamentals of these three evaluation methods. Then, they used a human assessment approach to validate the effectiveness of each evaluation method. Specifically, they used two datasets, one on question answering and the other on generating tasks. For each dataset, they compared the results of the different evaluation methods with the results of human assessment, and calculated the accuracy, recall, and other metrics for each evaluation method.

Finally, the authors summarize the advantages and disadvantages of the three evaluation methods. In general, the language model-based evaluation method has high accuracy, but requires a large amount of computational resources. The rule-based evaluation method, on the other hand, is relatively simple, but may make some errors when dealing with complex problems. The evaluation method combining coarse and fine granularity, on the other hand, can combine the advantages of both methods, but requires more workload for design and implementation.  

## Conclusion

### 1. Advantages of the Thesis
The paper systematically reviews the current state of research and development trends in the field of Multimodal Retrieval Augmented Generation (MRAG) and provides a detailed analysis from four key perspectives: **important components and techniques, datasets, evaluation methods and metrics, and existing limitations**. By providing a structured overview and forward-looking insights, the paper aims to guide researchers in further advancing the development of MRAG, ultimately contributing to the development of more robust and diverse multimodal retrieval augmentation generation.
 
### 2. Innovative points
This thesis presents the concept of multimodal retrieval augmented generation (MRAG), emphasizing the importance of integrating multimodal data (e.g., text, images, and video) into LLMs in order to improve their capabilities. Unlike traditional text-based RAG systems, MRAG addresses the challenge of retrieving and generating information across modalities, thereby improving the accuracy and relevance of responses and reducing the occurrence of illusions. And, the paper explores methods and techniques for effectively handling multimodal data, including key techniques such as multimodal retrieval and multimodal generation. 

### 3. Future Works
Future MRAG research should focus on these problems and propose new solutions. Meanwhile, with the continuous development of AI technology, MRAG will also be applied in more fields, such as healthcare, law, finance, etc., which will further promote the research and development of MRAG. 
