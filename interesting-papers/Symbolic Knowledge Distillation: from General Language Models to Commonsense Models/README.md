# Symbolic Knowledge Distillation: from General Language Models to Commonsense Models
[paper link](https://arxiv.org/pdf/2110.07178) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new method, Symbolic Knowledge Distillation, for training general knowledge models.         |  LLMs         |

## Methodology

### 1. Abstract
Traditionally, humans need to write general knowledge maps to train general knowledge models, but this method is inefficient and costly. Symbolic Knowledge Distillation uses large language models as teachers to distill their knowledge in textual form and transfer it to small general knowledge models. High-quality causal common sense can be selectively extracted by carefully designing cues and individually training critic models. Experimental results show that the automated distilled version outperforms the human-written commonsense knowledge graph in all three dimensions: quantity, quality, and diversity, and produces a neural network commonsense model that has greater commonsense power than the teacher model, albeit one-tenth of the size of the teacher model. This work provides a new way of thinking about commonsense reasoning.

### 2. Method Description 
The paper proposes a method called “symbolic knowledge distillation” for automatic construction of general knowledge graphs. The method is divided into three steps: machine-to-corpus, knowledge graph-to-machine, and evaluation.

In the first step, they used GPT-3 as a “loose teacher” to generate a large number of general knowledge facts by providing templates and examples. These facts were combined into a general knowledge graph and compared with the human-written ATOMIC2020 dataset.

In a second step, they introduced a “critic model” to filter low-quality knowledge and combine it with high-quality knowledge to create a new, more accurate general knowledge knowledge graph.

In the third step, they use this new general knowledge graph to train a compact model that automatically generates relevant general knowledge inferences based on input events.

![image](https://github.com/user-attachments/assets/5341a83d-df67-488b-b7a4-4fac9db718cb)

### 3. Methodological improvements
Compared to traditional methods based on human knowledge sources, this approach utilizes large-scale language models (e.g., GPT-3) to generate commonsense knowledge, thus greatly improving the amount and diversity of knowledge. In addition, they introduced a “critic model” that can effectively filter out low-quality knowledge and improve the accuracy of the whole system.

### 4. Issues addressed 
This method solves the problem of traditional human-based knowledge sources, which requires a lot of human cost to write and maintain a common sense knowledge base. At the same time, it also overcomes the problems of errors and inconsistencies that may exist in the language model itself, and further improves the accuracy of the system by introducing a “critic model” to filter out low-quality knowledge.
 
## Conclusion

### 1. Advantages of the Thesis
This paper proposes a new method for automatically constructing a general knowledge knowledge graph, Symbolic Knowledge Distillation, which utilizes a pre-trained language model as a knowledge source, and constructs a general knowledge knowledge graph through automatic machine generation, and is used to train efficient general knowledge inference models. 

Compared with the traditional knowledge graph based on manual authoring, Symbolic Knowledge Distillation has higher scale, diversity and quality, and also reduces the cost of knowledge graph construction. In addition, the method enables quality assessment of knowledge graphs, which further improves the quality and reliability of knowledge graphs.

![image](https://github.com/user-attachments/assets/31d1b19b-68d6-432d-9a21-654d06468c70)

### 2. Innovative points
  1. Utilizing the idea of knowledge distillation, the pre-trained language model is used as a knowledge source to construct a general knowledge knowledge graph by automatic machine generation.
  
  2. In the process of knowledge distillation, the concept of symbolic generation is introduced to make the generated knowledge understandable and assessable by humans.
  
  3. A critic model is introduced to assess the quality of the generated knowledge graph, which further improves the quality and reliability of the knowledge graph.
     
![image](https://github.com/user-attachments/assets/99b76bf0-697b-4230-96af-76d92a9d9299)

### 3. Future Works
  1. Exploring more efficient and accurate symbolic generation algorithms to further improve the quality and diversity of knowledge graphs.
  
  2. Investigating how to combine symbolic knowledge distillation with other commonsense reasoning techniques to further improve the effectiveness and efficiency of commonsense reasoning.
  
  3. Explore how to apply symbolic knowledge distillation on large-scale datasets to further validate its effectiveness and feasibility in real-world application scenarios. 
