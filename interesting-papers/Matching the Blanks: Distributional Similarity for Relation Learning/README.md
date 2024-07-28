# Matching the Blanks: Distributional Similarity for Relation Learning
[paper link](https://arxiv.org/pdf/1906.03158) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper explores how to construct task-independent relationship representations by learning textual representations and applying them to a relationship extraction task.         | BERT          |

## Methodology

### 1. Abstract
The authors use techniques such as Harris' distributional assumptions and BERT to obtain task-independent relational representations that can significantly outperform previous approaches by learning entity-linked text. These relational representations, fine-tuned on task-specific datasets, also outperform previous methods on datasets such as SemEval 2010 Task 8, KBP37, and TACRED.

### 2. Method Description 
The paper proposes methods for learning mapping relationships, i.e., learning relationship representations from entity tokens in input sequences. Specifically, they used a pre-trained BERT model and conducted experiments for different input and output architectures. Among other things, entity labeling can be achieved by inserting special lemmas or adding positional embeddings between each entity. Finally, they used a classification layer to map relationship representations to predefined relationship types.

![image](https://github.com/user-attachments/assets/4db13636-e78d-47fb-8397-740b894e27f8)

### 3. Methodological improvements
1. In contrast to traditional rule-based or feature-engineering approaches, this method does not require manual design of features or rules, but utilizes the power of DL to automatically learn features.

2. In addition, they introduce a new learning method, Matching Blanks, which avoids simply re-learning the entity linking system and can be used for relationship extraction tasks without additional tuning.

![image](https://github.com/user-attachments/assets/71a54884-a18b-4429-8df3-84e73007626f)

### 4. Issues addressed 
  1. This method solves the problem of traditional methods that require manual design of features or rules, and also avoids the disadvantage of simply re-learning the entity linking system.
  
  2. This method is applicable to various types of text data, including social media, news articles, etc. Also, it can handle relationships between long-distance entities, which may be difficult for other methods.

## Experiments
This paper focuses on the application of the BERT model in relation matching and relation extraction tasks, and several sets of comparison experiments are conducted to verify its effectiveness.

First, in **the FewRel task**, the authors compare the performance of the BERT model and the BERT+MTB model. The results show that the BERT+MTB model significantly outperforms the previous best method even without training data. The BERT+MTB model also performs even better when training data is added, requiring only a small amount of data to achieve the same or even better performance than the BERT model.

Second, in **the relationship extraction task**, the authors used three different datasets for their experiments. The results show that the BERT model outperforms the previous best results on each of these tasks, and the F1 score is further improved with the addition of MTB training. Additionally, the authors analyzed the performance in the case of reducing the amount of task-specific tuning data and found that MTB training was more effective for the low-resource case.  

![image](https://github.com/user-attachments/assets/2d664c77-bf7a-4b2d-a6dd-1496f610a744)

![image](https://github.com/user-attachments/assets/00e76c1a-14b9-466f-b39a-ee23887a80c1)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new approach to learning relational representations that extracts useful relational representations directly from text.
  
  2. Through the use of matching blanks, the method allows for unsupervised training of relationship representations and achieves state-of-the-art results on multiple relationship extraction tasks.
  
  3. The method is particularly well suited for relationship extraction in low-resource environments and can significantly reduce the labor investment required to create a relationship extractor.

### 2. Innovative points
  1. The paper proposes a novel training setup called "Matching Blanks", which relies only on entity recognition annotations.
  
  2. The paper also introduces a new architecture for fine-tuning the BERT relationship representation.
  
  3. The method does not require any supervision from the knowledge graph or human annotators, and thus can be trained without external datasets.

### 3. Future Works
  1. The thesis plans to investigate BERT+MTB-based clustering of relational statements for true general-purpose relation identification and extraction.
  
  2. The thesis will also investigate embeddings of entity and relation representations that can be used to store relation triples, inspired by recent work on knowledge base embeddings. 
