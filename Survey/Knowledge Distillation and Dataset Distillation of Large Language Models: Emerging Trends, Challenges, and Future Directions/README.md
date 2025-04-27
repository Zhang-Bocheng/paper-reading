# Knowledge Distillation and Dataset Distillation of Large Language Models: Emerging Trends, Challenges, and Future Directions
[paper link](https://arxiv.org/pdf/2504.14772) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper focuses on two approaches to compressing large language models (LLMs): knowledge distillation (KD) and dataset distillation (DD).          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Both approaches aim to compress LLMs while preserving advanced reasoning capabilities and linguistic diversity. The authors first examine key approaches in KD, such as task-specific alignment, inference-based training, and a multi-teacher framework, while also investigating DD techniques, which synthesize compact, high-impact datasets through optimization-based gradient matching, latent space regularization, and generative synthesis. Despite significant progress, challenges remain in preserving emergent reasoning and linear linguistic diversity, efficiently adapting to evolving teacher models and datasets, and establishing comprehensive evaluation protocols.

![image](https://github.com/user-attachments/assets/1f152112-f487-4af2-b750-e1d9806a0517)

### 2. Method Description 
  1. Traditional Knowledge Distillation: using static output distribution and adaptive optimization methods to compress the knowledge of large-scale models.
  2. Dataset distillation: reduces the amount of training data by synthesizing small and high-quality datasets.
  3. Theoretical research: the principles and mechanisms of knowledge distillation are explored and a new theoretical framework is proposed.

![image](https://github.com/user-attachments/assets/5e0db60c-2fcc-4910-9e99-c9459544ab68)
![image](https://github.com/user-attachments/assets/8949c5ad-457a-48c7-b63f-bb50cdf36b6e)
![image](https://github.com/user-attachments/assets/332efc4e-e64c-4339-9cb4-9c0c81a989b2)

### 3. Methodological improvements
  1. Incorporating multiple teacher models: utilizing different perspectives of multiple AI models to improve the performance of student models.
  2. Dynamic learning: enabling two-way collaborative learning by simultaneously training teacher and student models.
  3. Self-distillation: allowing student models to generate and deliver knowledge on their own, thus avoiding reliance on pre-trained teacher models.

### 4. Issues addressed 
  1. How to transform large-scale language models into smaller and more efficient student models?
  2. How to reduce the amount of training data without losing accuracy?
  3. How to improve the performance of student models by utilizing different perspectives from multiple models?

## Experiments
This article mainly introduces the application of knowledge distillation (knowledge distillation) technology in the field of NLP, and compares and analyzes some of these studies. The article first outlines the basic concepts and principles of knowledge distillation, and then explores its specific applications from different task perspectives respectively. Next, it describes each experiment in detail according to different domains.

**Medical and Healthcare Domain:**
In this domain, the authors focused on applications in medical diagnosis, clinical decision support, and drug discovery. By using knowledge distillation techniques, it is possible to compress large models into smaller ones while maintaining the delivery of key information. These smaller models can be run with limited computational resources, resulting in increased efficiency and reduced costs. And then, knowledge distillation improves the robustness and generalization of models, making them applicable to a wider range of scenarios.

**Education Domain:**
In this domain, the authors have focused on tasks such as automated grading and course planning. Large-scale NLP models are difficult to deploy in standard school environments because they require significant computational resources. To address this problem, the researchers propose knowledge distillation techniques that can compress large models into smaller ones, thereby reducing computational requirements and memory footprint. And, knowledge distillation increases the speed and accuracy of the models, enabling real-time feedback and scoring.

**Bioinformatics field:**
In this field, the authors have focused on tasks such as protein analysis, genome research, and biomedical entity identification. Knowledge distillation can help bioinformaticians analyze large amounts of data faster while improving model performance and accuracy. For example, in protein analysis, knowledge distillation can integrate knowledge from multiple pre-trained models into a compact model, resulting in an efficient protein embedding representation.

## Conclusion

### 1. Advantages of the Thesis
  1. In this paper, the authors propose an approach that combines Knowledge Distillation (KD) and Dataset Distillation to address the problems of computational resource consumption and storage space occupation in the training of LLMs.
  2. The approach converts complex large models into smaller ones by sharing parameters among multiple teacher models and uses an adaptive strategy to adjust temperature parameters during learning.
  3. In addition, the authors propose Multi-Teacher Architecture, Rationale-Based Guidance, and Dynamically Updated Teacher-Student Co-Evolution methods to further improve the model performance.

### 2. Innovative points
  1. The “knowledge distillation + data compression” method proposed in this paper is a novel solution that can effectively reduce the consumption of computational resources and storage space of LLMs.
  2. At the same time, the authors also introduce a variety of new technical tools, such as multi-task joint distillation, evidence-based reasoning, and dynamically updated teacher-student network structure, etc.   3. The introduction of these methods makes the model more flexible and efficient, and also improves the model's generalization ability.
 
### 3. Future Works
Although the “knowledge distillation + data compression” method proposed in this paper has achieved certain results, there are still some problems that need to be solved, such as how to better balance the relationship between model size and performance, and how to better deal with domain-specific knowledge. Therefore, in future research, it can consider further exploring these issues and proposing more effective solutions.    
