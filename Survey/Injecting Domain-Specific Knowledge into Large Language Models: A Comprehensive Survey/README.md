# Injecting Domain-Specific Knowledge into Large Language Models: A Comprehensive Survey
[paper link](https://arxiv.org/pdf/2502.10708) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper focuses on how domain-specific knowledge can be injected into Large Language Models (LLMs) to improve the effectiveness of their application in specific domains.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The authors propose four key approaches: dynamic knowledge injection, static knowledge embedding, modularity adapters, and cueing optimization, and discuss the advantages and disadvantages of each approach as well as their impact on flexibility, scalability, and efficiency. In addition, the article compares the differences between domain-specific LLMs and general-purpose LLMs and summarizes some commonly used benchmark datasets.

![image](https://github.com/user-attachments/assets/3219a460-91ca-4e7b-a3ba-3b4f9b0d603f)

### 2. Method Description 
This paper presents four open source frameworks belonging to different knowledge injection methods: **KnowGPT, StructTuning, K-Adapter, and SelfLift**.These frameworks all aim to improve the performance of pre-trained models on relevant tasks by injecting domain-specific knowledge.

**KnowGPT** is a dynamic knowledge injection method that utilizes reinforcement learning to extract highly relevant subgraphs from the knowledge graph, represent them as triples and convert them into natural language cues. These cues can be interpreted and used by language models through multiple templates. This approach significantly reduces the cost of API calls to LLMs while improving their performance in domain-specific tasks.

**StructTuning** is a structure-aware approach for embedding domain knowledge into pre-trained models. It employs a two-stage strategy: structure-aware continuous pre-training encodes knowledge into model parameters, while structure-aware supervised fine-tuning optimizes understanding through structured QA tasks. The framework shows significant performance gains on knowledge-driven tasks such as relational categorization and Q&A, and strikes a balance between generality and efficiency.

**K-Adapter** stores knowledge in adapter modules. The core approach is to freeze the original model parameters and assign each type of knowledge to a separate and task-specific adapter. These adapters are inserted as independent modules into the middle layer of the model to generate enhanced representations of specific knowledge. This design effectively mitigates the catastrophic forgetting problem by preventing newly injected knowledge from overwriting the model's original knowledge.

**SelfLift** uses an iterative retrieval augmentation generator to create an infinite pool of memories and uses a memory selector to choose an output as a memory for subsequent generation rounds. This is an excellent example of cued optimization, in which the model's outputs are dynamically optimized and reused to improve its overall performance and coherence.

![image](https://github.com/user-attachments/assets/7cfa1d0c-7757-4ee4-ace0-289808c50259)

### 3.  Methodological improvements
The main point of improvement in these frameworks is their ability to inject domain-specific knowledge into pre-trained models, thereby improving their performance on relevant tasks. Compared to traditional rule-based or hand-annotated approaches, these frameworks are more flexible and scalable as they can automatically learn knowledge from a large number of data sources.

In addition, these frameworks employ different techniques for knowledge injection, including dynamic knowledge injection, structure-aware embedding, adapter design, and cue optimization. The choice of these techniques depends on the specific application scenario and requirements.

### 4. Issues addressed 
  1. **How to inject domain-specific knowledge into pre-trained models so that the models can perform better on relevant tasks.** Traditional approaches are usually rule-based or manually annotated, but this approach requires a lot of manual work and is difficult to adapt to new application scenarios. These frameworks learn knowledge from data sources in an automated way, allowing models to be better adapted to new tasks and environments.

  2. **How to avoid the newly injected knowledge overwriting the model's original knowledge, leading to catastrophic forgetting.** These issues are critical in many applications, such as the fields of natural language processing, computer vision, and intelligent dialog. These frameworks employ different techniques to mitigate these problems, thus ensuring that the model can maintain good performance in the long run.

## Experiments
This paper focuses on the research progress and challenges of language modeling (LLM) for different domains, and experimentally compares the performance differences between generic and domain-specific LLMs as well as the impact of knowledge injection on LLMs.

  1. **The article summarizes commonly used datasets or benchmark tests in each domain and observes that there are significant differences in the richness of data resources in each domain**. The biomedical domain has numerous high-quality datasets, such as PubMed, Pub-MedQA, and BioASQ, which support Q&A and clinical summarization tasks. In contrast, the materials science and chemistry domains have more limited resources, while datasets such as USPTO and Enzymes focus on chemical reactions. Datasets from other domains are scattered across mental health, education, etc. This suggests the need to tailor LLM for specific domains, while emphasizing the need for extensive collation of benchmarking in unrepresented domains.

![image](https://github.com/user-attachments/assets/5b483b0a-8ed4-4834-a1ce-cd33445c8b29)

  2. **The article discusses a comparison between domain-specific LLMs and generic domain LLMs, using the biomedical domain as an example to determine whether a specific knowledge injection process is needed**. The results show that closed-source LLM is currently the most effective model, but open-source LLM should also be emphasized. In this domain, domain-specific LLMs typically perform better than generalized domain models. For example, on the MedQA dataset, PMC LLaMA-13B outperforms LLaMA2-70B by more than 10 points. This suggests that domain-specific LLMs are important for achieving superior performance on specialized tasks. While generalized domain models can provide robust results, incorporating domain-specific knowledge can allow them to achieve significant improvements, especially in open source initiatives.

## Conclusion

### 1. Advantages of the Thesis
  1. A systematic review of the application and development of knowledge injection techniques in large-scale language modeling is presented.
  2. Knowledge injection methods are categorized, and the characteristics, advantages and disadvantages of each method are described in detail.
  3. The applications of knowledge injection techniques in various domains are summarized, and relevant benchmark datasets and tool resources are provided.
  4. Directions and challenges for future research are presented, providing guidance for the development of the field.

### 2. Innovative points
  1. Knowledge injection techniques are innovatively categorized into four methods: dynamic knowledge injection, static knowledge embedding, adapters and cue optimization, and the working principle and application scenarios of each method are described in detail.
  2. Emphasizes the importance of knowledge injection techniques for solving domain-specific problems, and demonstrates their superior performance through specific cases.
  3. The applications of knowledge injection techniques in different domains are discussed, and improvement schemes for different domains are proposed. 

### 3. Future Works
  1. Suggests further research on how to balance the generalization ability and domain specificity of models to improve the effectiveness of knowledge injection techniques.
  2. It is proposed that more flexible knowledge injection methods need to be developed to better adapt to different task requirements and domain changes.
  3. Suggests more interdisciplinary collaborations to explore the potential of knowledge injection techniques in other domains.  
