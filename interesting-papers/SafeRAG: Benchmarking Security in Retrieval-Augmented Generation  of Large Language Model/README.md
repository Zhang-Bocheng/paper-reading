# SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model
[paper link](https://arxiv.org/pdf/2501.18636) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper presents a security assessment benchmark called SafeRAG, which aims to evaluate the security of Large Language Models (LLMs) based on Retrieval Augmented Generation (RAG).           |  Retrieval Augmented Generation (RAG)        |

## Methodology

### 1. Abstract
The benchmark classifies the attack tasks into Silver Noise, Contextual Conflict, Soft Advertisement, and White Denial of Service, and simulates various attack scenarios that may be encountered by manually constructing a security assessment dataset. The experimental results show that RAG is significantly vulnerable to all attack tasks, and that even the most obvious attack tasks can easily bypass existing retrievers, filters, or advanced LLMs, leading to a degradation of RAG's quality of service.

![image](https://github.com/user-attachments/assets/76b329be-a4ff-4144-9008-555ee2aca1ee)

### 2. Method Description
The article first introduces the background and significance of the study, and presents the objectives and methods of the study. Then, the article describes in detail how to construct a security threat framework, including the collection and processing of raw news texts, as well as the methods and techniques for generating various attack texts. Then, the article presents the evaluation metrics and experimental results, including the evaluation of different stages of RAG components for different types of attack tasks, such as noise, conflict, and virulence, and compares the effectiveness of different models and filters. Finally, the article summarises the main contributions of the research and directions for future work.

## Experiments
Specifically, in terms of experiments, the article employs a number of different attack methods and techniques, including noise injection, conflict creation, and soft advertisement insertion. For each attack task, the article designed corresponding evaluation metrics and experimental scenarios, and conducted experimental validation using multiple datasets and models. Among them, for different types of attack tasks, the article selects different evaluation metrics, such as RA, F1Variant, ASR, etc., and gives specific scores and conclusions. 

For example, in the noise injection experiments, the authors found that there are differences in the anti-noise capability of RAG components at different stages, while some compression techniques may lead to information loss, which affects the quality of the generated response. In the conflict creation experiments, the authors found that there are also differences in the ability of different models to combat conflict, while some filters may weaken the conflict details and thus reduce the F1(avg) score. In conclusion, through these experiments, the authors drew many valuable conclusions and recommendations for future related research.

![image](https://github.com/user-attachments/assets/f2432680-372f-42b8-a327-7a855d0cd6df)

## Conclusion

### 1. Advantages of the Thesis
The paper presents a benchmark test called SafeRAG, designed to evaluate the security of RAG systems under data injection attacks. The authors identify four key attack tasks: **noise, conflict, toxicity, and denial of service, and reveal significant weaknesses in the retriever, filter, and generator components of the RAG system.** By proposing novel attack strategies such as silver noise, cross-context conflict, soft advertisement, and white denial of service, the authors expose significant flaws in existing defences and demonstrate the vulnerability of the RAG system.

The strength of the paper lies in presenting a comprehensive security assessment framework that can effectively evaluate the security of RAG systems under different stages of data injection attacks. And, the authors developed a series of lightweight RAG security assessment datasets, mainly constructed by humans with the assistance of LLM, which helps to improve the reproducibility and accuracy of the experiments.

### 2. Innovative points
The methodological innovation of the paper is the proposal of four new attack tasks, namely **Silver Noise, Cross-Context Conflict, Soft Advertisement and White Denial of Service**. These attack tasks can bypass most of the existing security filters, thus compromising the diversity of the RAG system. And, the authors introduce a cost-effective and accurate RAG security assessment framework based on attack-specific metrics that is highly consistent with human judgement.

### 3. Future Works
Future research directions include further exploring the security of RAG systems under other types of data injection attacks, such as malicious code injection. What is more, it could be investigated how deep learning techniques can be used to automatically detect and defend against these attacks. There is a need to further explore how to enhance the robustness and reliability of RAG systems to cope with increasingly sophisticated threats.
  
