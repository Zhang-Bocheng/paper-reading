# Transformer Memory as a Differentiable Search Index
[paper link](https://arxiv.org/pdf/2202.06991) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 |  This paper introduces a new information retrieval method, micro-searchable indexing (DSI)        |  Transformer         |

## Methodology

### 1. Abstract
This method uses a single Transformer model to map text queries directly to relevant document IDs, thus simplifying the entire retrieval process. Experiments show that with appropriate design choices, DSI significantly outperforms powerful baselines, such as the dual-coded model, and has strong generalisation capabilities, outperforming the BM25 baseline in the zero-sample setting.

### 2. Method Description 
The paper proposes a sequence-to-sequence (seq2seq) based document indexing and retrieval model (DSI). The model learns to map words in a document to their corresponding unique identifiers (docid) and uses these identifiers to enable document retrieval. The model uses a number of different indexing strategies and document representation strategies, and experimental comparisons were made, leading to the identification of the direct indexing method as the best choice.

![image](https://github.com/user-attachments/assets/fd2548ce-4dbd-45b3-8aaf-0aa98101f1d9)

### 3. Methodological improvements
  1. The thesis innovates on the traditional problem of document indexing and retrieval by introducing a sequence-to-sequence based model for the process.
  
  2. And the thesis conducted experimental comparisons of different indexing strategies and document representation strategies to arrive at the optimal choice.
  
  3. In addition, the thesis considers how to perform retrieval efficiently, including issues such as decoding methods and sorting of retrieval results.

### 4. Issues addressed 
The thesis addresses the limitations and shortcomings in traditional document indexing and retrieval models, such as the inability to handle long texts and capture semantic information. By introducing a sequence-to-sequence based model and an optimised indexing strategy and document representation strategy, the thesis improves the effectiveness and efficiency of document indexing and retrieval.

![image](https://github.com/user-attachments/assets/735d038e-9c06-412a-be9f-0902e24032e5)

## Experiments
This paper focuses on experiments comparing the DSI model (Dynamic Semantic Identifiers) with the traditional dual encoder (DE) model for the retrieval task of natural language queries and documents. The NQ dataset is used in the experiments with different divisions including NQ10K, NQ100K and NQ320K.The experimental results show that the DSI model outperforms the DE model on all datasets, especially on large datasets. In addition, the authors explore the effects of different types of docid representations, indexing strategies, and zero-sample learning, and draw some useful conclusions.

![image](https://github.com/user-attachments/assets/768bd93e-7627-4bcb-b4dc-6b3c476115af)

Specifically, the authors first compare the performance differences between the DSI model and the DE model under supervised fine-tuning and zero-sample learning. 
<br>&emsp;For supervised fine-tuning, the DSI model performs well on all datasets, especially on large datasets. 
<br>&emsp;And for zero-sample learning, the DSI model also performs much better than the DE model on all datasets. 
<br>&emsp;In addition, the authors compared the effects of different types of docid representations and indexing strategies. 

![image](https://github.com/user-attachments/assets/0170047b-eb84-4445-b393-bda3fa899c74)

They found that the direct indexing method was the best choice, while the set processing method with stopwords preprocessing did not bring additional advantages. In addition, the authors explore the scaling properties of the DSI and DE models and find that scaling on the DSI model is more optimistic.  

## Conclusion

### 1. Advantages of the Thesis
  1. Differentiable Search Index (DSI), a new search system architecture, is proposed to map queries directly to relevant document IDs by using the Transformer model.
  
  2. Experimental results show that DSI outperforms common baselines such as BM25 and Dual Encoders under standard fine-tuning settings and zero-shot settings.
  
  3. The advantage of DSI is that all information is encoded in the parameters of the Transformer model, and instead of requiring a special fixation search process, standard model inference is used to map encodings to docids.
  
  4. DSI maps all aspects of retrieval to known problems in machine learning tasks, which may provide new potential avenues for solving long-term IR problems.
Methodological Innovation Points

### 2. Innovative points
  1. Multiple methods for representing documents and docids are explored, and different model architectures and training strategies are explored.
  
  2. For document representation, the ‘naive’ full-text representation and the bag-of-words representation used by traditional IR engines are considered.
  
  3. For docid representation, several ways of representing docids are investigated, including plain integers as text strings, unstructured atomic docids, and some simple baseline methods to construct semantic docids with hierarchical clustering structure.
 
  4. In terms of indexing, a training approach is proposed that pairs each document with its docid in addition to pairing the query with the associated docid in order to train the model to understand information about each document.
     
### 3. Future Works
  1. Ways to represent documents and docids and how to extend the memory capacity can be further explored.
  
  2. Methods of how to update the dynamic corpus, for example when documents are added or removed, can be explored.
 
  3. The possibility of DSI as an unsupervised representation learning method and/or a memory storage method for other language models can be further investigated.
