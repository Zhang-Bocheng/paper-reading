# Language Models are Open Knowledge Graphs
[paper link](https://arxiv.org/pdf/2010.11967) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper describes a method for building knowledge graphs (KGs) using pre-trained language models without human supervision.           |  Natural Language Processing(NLP)         |

## Methodology

### 1. Abstract
  Existing KGs usually require humans to create knowledge, whereas deep language models can automatically acquire knowledge from large-scale corpora. The unsupervised approach proposed by the authors converts the knowledge in the language model into KGs and requires only a single forward propagation over the corpus to complete the construction of KGs. By comparing the results with two KGs created by humans (Wikidata and TAC KBP), the authors demonstrate the quality of the constructed KGs and find that these KGs provide new factual knowledge that is not available in existing KGs. The findings of this paper show that pre-trained language models can become open knowledge graphs, which can help advance NLP technology.
  
### 2. Method Description 
  The paper proposes an unsupervised end-to-end method called "MAMA" for constructing an open knowledge graph KG from a pre-trained language model.The method consists of two phases: **matching and mapping**. In the matching phase, the system uses a search algorithm to find facts in the input text that match the knowledge in the pre-trained language model and represent them as triples (head-relation-tail). In the mapping phase, these facts are mapped to existing fixed KG architectures or new open architectures to produce a knowledge graph containing both known and unknown knowledge.

![image](https://github.com/user-attachments/assets/8ae845cc-c8ec-412e-83ff-f580dc5dc686)

### 3. Methodological improvements
 In contrast to traditional rule-based or manually labeled methods, this method does not require any domain expert knowledge or manually labeled datasets. It uses a single forward pass of a pre-trained language model to automatically learn the knowledge in the text and finds the best matching facts through a search algorithm. In addition, the method introduces a new open architecture that allows the knowledge graph to be extended and cover more knowledge domains.
 
### 4. Issues addressed 
  The method solves the problem of requiring a lot of manual annotation and domain expertise in the traditional knowledge graph construction process. It also improves the coverage and accuracy of the knowledge graph, thus helping the application of downstream tasks such as question and answer and common sense reasoning.
  
## Experiments
  This paper focuses on how to generate a knowledge graph by pre-training a language model (LM) and conducts two comparative experiments to validate the effectiveness of the method.

  The first experiment compares the difference between the knowledge graph generated using MAMA and the knowledge graph generated by two open information extraction systems on two datasets, TAC KBP and Wikidata. The results of the experiments show that the knowledge graph generated using MAMA performs well in terms of accuracy, being able to achieve more than 60% accuracy, and performs better than the two open information extraction systems. In addition, the experiments also found that using larger or deeper pre-trained LMs improves the quality of the knowledge graph, while using BERT LMs is more effective than GPT-2 LMs.

The second experiment was to analyze the quality of facts not mapped into the reference knowledge graph. The results of the experiment show that about 35% of the unmapped facts are true, and most of them are partially unmapped facts, i.e., the relations are not in the reference knowledge graph, but the entities are. The remaining errors are mainly due to inaccurate entity detection. Therefore, accurate entity detection is crucial for the success of this approach.

![image](https://github.com/user-attachments/assets/396b5846-43e6-48e6-9508-f17329b81033)

![image](https://github.com/user-attachments/assets/bfd7bd46-eb8f-428c-8200-62243aa9198f)

## Conclusion

### 1. Advantages of the Thesis
 The paper presents a pre-trained language model-based knowledge graph construction method (MAMA) and applies it to the construction of two open knowledge graphs (TAC KBP and Wikidata). Compared to traditional rule-based or manual labeling approaches, MAMA does not require explicitly defining rules or manually labeling entities and relations, but uses pre-trained language models to learn semantic associations between entities and relations, and transforms these associations into facts in the knowledge graph by matching and mapping.
 
### 2. Innovative points
  MAMA has the following advantages over traditional rule-based or manual labeling approaches:

  1. It does not need to explicitly define rules or manually label entities and relations, and can automatically learn semantic associations between entities and relations.
  
  2. Can handle large-scale datasets and is suitable for building open knowledge graphs.
  
  3. Able to discover some new facts, extending the existing knowledge graph.

### 3. Future Works
1. The accuracy and efficiency of MAMA can be improved by improving the techniques of entity detection, entity linking, relation mapping and relation generation.

2. In addition, techniques such as deep RL can be considered to be introduced into MAMA to further improve its performance.

3. The MAMA method provides new ideas and tools for knowledge graph construction and will play an important role in future knowledge graph research and applications.
   
