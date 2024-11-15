# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval
[paper link](https://arxiv.org/pdf/2401.18059) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method called RAPTOR for improving the capabilities of retrieval-enhanced language models.          |   Text Retrieval System        |

## Methodology

### 1. Abstract
While traditional retrieval-enhanced language models can only retrieve information from short segments, RAPTOR builds a tree structure with information from different levels of abstraction by recursively embedding, clustering and summarising blocks of text. When reasoning, RAPTOR can retrieve information from this tree and integrate information from long documents with different abstraction levels. Experimental results show that retrieval using RAPTOR performs better than traditional retrieval augmented language models on several tasks, and in particular achieves state-of-the-art results on problems requiring complex multi-step reasoning. 

![image](https://github.com/user-attachments/assets/1bb2ac21-8bd4-435f-b4d3-ab6c70d60ebb)

### 2. Method Description 
The paper proposes a text retrieval system called RAPTOR (Recursive Passage Organisation for Thematic Retrieval), which aims to improve the semantic depth and connectivity of long texts. RAPTOR balances topic generalisation and detail presentation by constructing a recursive tree structure, and uses the SBERT embedding technique to convert text segments into vector representations. Then, similar text fragments are grouped using a clustering algorithm and soft clustering is performed using Gaussian Mixture Models (GMMs) to capture the multidimensional relationships of the information. Finally, for each cluster, summary generation is performed using the gpt-3.5-turbo model, thus compressing the large amount of information into a manageable size. The query process consists of two mechanisms, tree traversal and collapsed tree, which are applicable to different levels of information retrieval needs, respectively.

![image](https://github.com/user-attachments/assets/a6faedd2-7d9f-4293-bfc9-83e00e8e6e55)
 
### 3. Methodological improvements
Compared to the traditional Dense Passage Retrieval (DPR) method, RAPTOR has better semantic depth and connectivity when dealing with long texts. It is able to select nodes at different levels according to the level of detail of the question, thus providing more relevant and comprehensive information. In addition, RAPTOR adopts a tree structure and soft clustering strategy, which makes it more flexible and adaptable.

### 4. Issues addressed 
The method mainly solves some problems of traditional text retrieval methods in dealing with long texts, such as the lack of semantic depth and connectivity, and the difficulty of capturing the multi-dimensional relationship of information. By introducing recursive tree structure and soft clustering strategy, RAPTOR is able to better capture the connections between information while maintaining semantic depth, which improves the quality and accuracy of retrieval results. At the same time, the diversity of the tree structure and query mechanism also provides users with more flexible choices to meet the needs of different levels.
 
## Experiments
This paper focuses on the performance of the RAPTOR model on three Q&A datasets and compares it with other models. Specifically, the authors first used SBERT, BM25 and DPR as embedding models combined with Unified QA as a language model to conduct experiments on three datasets, QASPER, NarrativeQA and QuALITY, and concluded the superiority of RAPTOR over other methods. Then, the authors further conducted a more in-depth comparative analysis of RAPTOR using different language models such as GPT-3, GPT-4 and UnifiedQA, and different retrieval methods such as BM25 and DPR. Finally, the authors also explored the effect of tree structure on RAPTOR performance and came up with some interesting findings.

![image](https://github.com/user-attachments/assets/377e5d27-5075-4649-b1c9-f7e7868bf131)

![image](https://github.com/user-attachments/assets/0ba173df-290b-444c-9d07-9bf0c8598997)

In their experiments, the authors used standard BLEU, ROUGE and METEOR metrics to measure the performance of the models. For example, on the QASPER dataset, RAPTOR outperforms the DPR and BM25 approaches with F-1 matching scores of 53.1%, 55.7%, and 36.6% compared to GPT-3, GPT-4, and Unified QA, respectively. On the QuALITY dataset, RAPTOR achieves an accuracy of 62.4%, which is an improvement of 2% and 5.1% over the DPR and BM25 methods. In addition, on the NarrativeQA dataset, RAPTOR performs well on several metrics, such as ROUGE-L, BLEU-1, BLEU-4, and METEOR. 
![image](https://github.com/user-attachments/assets/be445b8c-63a9-41bb-89c0-2e3536151990)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a novel tree structure based retrieval system, RAPTOR, which is able to efficiently capture different levels of information in the text through recursive clustering and summarisation techniques and utilise this tree structure for more effective retrieval in the query phase.
  2. RAPTOR achieves better performance on multiple question and answer tasks compared to traditional retrieval methods, and experimental results on publicly available datasets such as QASPER, NarrativeQA, and QuALITY demonstrate its high reproducibility and effectiveness.
  3. The design principles and implementation details of RAPTOR are described in detail in the paper, and relevant code and datasets are provided for readers' reference.

### 2. Innovative points
  1. RAPTOR uses text summarisation techniques to allow retrieval of enhanced different scales and demonstrates its effectiveness on long document collections.
  2. RAPTOR designed a tree structure to capture different levels of information about the text, allowing it to answer questions effectively at different levels.
  3. RAPTOR employs recursive clustering and summarisation techniques that are able to break large amounts of text into smaller chunks and generate summaries, thus reducing the time and computational cost of retrieval. 

### 3. Future Works
  1. RAPTOR can be further extended to other domains such as natural language reasoning, dialogue systems, etc.
  2. Ways to incorporate more external knowledge sources, such as knowledge graphs or encyclopaedias, can be explored to improve the accuracy and reliability of the system.
  3. It can be investigated how to better process multilingual texts and apply it to domains such as cross-language Q&A.    
