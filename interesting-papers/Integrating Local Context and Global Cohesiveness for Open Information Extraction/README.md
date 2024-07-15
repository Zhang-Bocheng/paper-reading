# Integrating Local Context and Global Cohesiveness for Open Information Extraction
[paper link](https://arxiv.org/pdf/1804.09931) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This paper presents ReMine, a new open information extraction system that integrates local contextual and global structural signals in a unified, remotely supervised framework.         | Machine Learning          |

## Methodology

### 1. Abstract
   The system utilizes facts from external knowledge bases as supervision and can be applied to many different domains to facilitate sentence-level tuple extraction using corpus-level statistical information. The system achieves this by solving a joint optimization problem that involves segmenting entity/relationship phrases in individual sentences based on the local context and measuring the quality of tuples extracted from individual sentences using translation objectives. Experimental results show that ReMine has higher effectiveness, generalization and robustness compared to state-of-the-art open information extraction systems.

   ![image](https://github.com/user-attachments/assets/0d2af758-6e13-4f53-aa69-035ed086499d)

### 2. Method Description 
  The ReMine framework proposed in this paper is a multi-stage system for Open IE tasks, including three main modules: **phrase extraction module, tuple generation module and global cohesiveness module**. 
   <br/>&emsp; Among them, the phrase extraction module recognizes entity phrases and relation phrases in sentences by taking entity phrases from external knowledge bases as positive samples and using the multi-type segmentation technique; 
   <br/>&emsp; the tuple generation module generates candidate entity pairs and relation phrases based on the linguistic structure of the sentence, and utilizes the global cohesiveness module to global coherence information provided by the global cohesiveness module to exclude erroneous relational phrases; 
   <br/>&emsp; the global cohesiveness module learns the representation of entity and relational phrases to capture global structural coherence and combines it with local contextual information to further improve the accuracy of relational phrases.

  ![image](https://github.com/user-attachments/assets/6d29c985-353c-4c5d-a4c5-f25cae35233e)

### 3. Methodological improvements
  1. The ReMine framework employs advanced techniques such as multi-type segmentation and random forest classifiers to more accurately identify entity phrases and relational phrases, as well as to provide better robustness and generalization capabilities when dealing with complex sentences.
  
  2. In addition, the framework introduces the global cohesiveness module, which is able to better capture global structural consistency, thus improving the accuracy of relational phrases.

### 4. Issues addressed 
  Traditional rule-based or ML approaches often require manually designing complex rules or features that are difficult to adapt to different types of sentences and different domains. In contrast, the ReMine framework is able to adaptively process sentences of different types and domains with good accuracy and scalability by combining multiple technical tools. Therefore, the framework can effectively solve the problems in Open IE tasks and provide new ideas and methods for NLP research.
  
## Experiments
This paper focuses on the authors' experiments on the extraction of entity phrases and relational triples using the ReMine system, and compares them with several benchmark approaches. Specifically, the authors conducted the following two experiments:

**Entity Phrase Extraction Experiment**: the authors conducted experiments using three publicly available datasets (NYT, Wiki-KBP, and Twitter) and compared the results with three other sequence annotation methods and one quality phrase mining method. The experimental results show that ReMine performs best in the NYT and Wiki-KBP datasets, while in the Twitter dataset, ReMine is also better than the other methods at dealing with misspellings and grammatical problems in short texts.

**Relational triad extraction experiment**: the authors compare the performance of ReMine and its variants with four other open information extraction systems on the NYT and Twitter datasets. The experimental results show that ReMine outperforms the other methods on both datasets and is particularly good on the Twitter dataset because it can better handle noise and non-standard language usage in short texts.

![image](https://github.com/user-attachments/assets/8e477e03-b725-48ce-86ee-12827ff22c39)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new information extraction framework, ReMine, that effectively combines local contextual information and global structural coherence to improve the quality of extraction of relational tuples.
  
  2. The ReMine framework uses a low-dimensional embedding space to represent entities and relational phrases, and evaluates the quality of candidate relational tuples by measuring their coherence in the corpus.
  
  3. The paper also proposes a method based on a context-dependent segmentation algorithm that recognizes multiple types of phrases with high quality.
  
  4. Experimental results show that the ReMine system achieves superior accuracy on two real-world datasets and produces more high-quality relational tuples than several other state-of-the-art open information extraction systems.

     ![image](https://github.com/user-attachments/assets/7a1a60d4-8fb0-4651-a831-d98cf36c3ee3)

### 2. Innovative points
  1. The ReMine framework improves the quality of relational tuples by taking into account not only sentence-level contextual information, but also information from the entire corpus.
  
  2. The ReMine framework uses a low-dimensional embedding space to represent entities and relational phrases, which is a simple but effective approach.
  
  3. The context-dependent segmentation algorithm is a novel approach to recognize multiple types of phrases with high quality.
     
### 3. Future Works
  1. Further research could be done on how to build knowledge graphs using relational tuples and how to apply them in downstream applications such as open quizzing.
  
  2. It could be explored how to combine the ReMine framework with other information extraction techniques for better performance.

