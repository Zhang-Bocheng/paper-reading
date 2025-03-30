# Knowledge Graph-Guided Retrieval Augmented Generation
[paper link](https://arxiv.org/pdf/2502.06864) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 |   This paper presents a knowledge graph-guided augmented generation framework called KG2RAG for addressing the problem of false information that can occur when large language models (LLMs) answer questions.        | Retrieval Augmented Generation (RAG)         |

## Methodology

### 1. Abstract
The framework utilises knowledge graphs to provide fact-level relationships, thereby improving the diversity and coherence of retrieval results. Specifically, KG2RAG first performs semantic-based retrieval to provide seed chunks, and then presents relevant and important knowledge in the form of ordered paragraphs through a knowledge graph-guided chunk expansion process and a knowledge graph-based chunk organisation process. Experimental results show that KG2RAG has advantages over existing augmented generation-based techniques in terms of both answer quality and retrieval quality.

![image](https://github.com/user-attachments/assets/f9ab0f08-d6e0-4609-917b-87959bc10572)

### 2. Method Description 
G2RAG (Knowledge Graph Enhanced Retrieve and Generate) is a text retrieval and generation model based on knowledge graph enhancement. The model achieves cross-document knowledge association and information retrieval by slicing a document into several chunks and associating a knowledge graph for each chunk. Specifically, KG2RAG adopts the following three main steps:

**Document offline processing:** All documents are sliced into chunks according to a preset chunk size and further processed, such as adding relevant contexts and extracting metadata.
**KG enhanced chunk retrieval:** KG2RAG uses a two-phase retrieval process to enhance chunk retrieval capability. The first stage is semantic similarity-based retrieval and the second stage is knowledge graph-based extended retrieval. In the first phase, KG2RAG uses an embedding model to compute the semantic similarity between a query and a chunk and selects the most relevant chunk as the retrieval result; in the second phase, KG2RAG builds a subgraph based on the retrieved chunks by traversing its neighbouring nodes and further extends the set of chunks based on this.
**Contextual organisation of KG base:** KG2RAG uses knowledge graph to filter and organise the retrieved results to form a more semantically coherent and self-consistent context input to the pre-trained language model.

![image](https://github.com/user-attachments/assets/a7cb5d04-6a19-4b44-9659-48c096b085f0)

### 3. Methodological improvements
Compared to the traditional semantic similarity-based retrieval method, KG2RAG introduces information from the knowledge graph, which improves the accuracy and comprehensiveness of chunk retrieval. Also, KG2RAG designs a knowledge graph-based context organisation module that can better integrate relevant information and improve the comprehension and generation performance of the language model.

### 4. Issues addressed 
KG2RAG aims to solve the problems of traditional text retrieval and generation models, such as isolated chunks and lack of inter-entity relationships. By introducing the information of knowledge graph, KG2RAG can effectively capture the inter-entity relationships in documents, and then achieve cross-document knowledge association and information retrieval. In addition, KG2RAG makes the retrieval results more semantically coherent and self-consistent through the knowledge graph-driven context organisation module, which helps to improve the comprehension and generation performance of language models.

## Experiments
This paper focuses on three experiments conducted by the authors on the HotpotQA dataset, namely the experimental setup, experimental results and analyses, and experimental details. In particular, the experiments were set up with two versions of the dataset, i.e., HotpotQA-Dist and HotpotQA-Full, and manual extraction and correlation of KG-chunks were performed. The experimental results and analyses section then evaluates the response quality and retrieval quality by comparing the different methods and derives the advantages of KG2RAG over other methods. The Experimental Details section presents information about the models and parameters used in the experiments.

Specifically, for the experimental setup, the authors used the HotpotQA dataset and divided it into two versions, namely HotpotQA-Dist and HotpotQA-Full. In HotpotQA-Dist, ten documents were provided as support material, while in HotpotQA-Full, it was necessary to identify the most useful knowledge from all 66,581 documents to identify useful knowledge. In addition, the authors manually extracted entities and relationships and associated each triad with its source block. The distribution of the number of these blocks is shown in Figure 4, showing a long-tail phenomenon.

![image](https://github.com/user-attachments/assets/b6e1db22-e622-4899-81b5-f6fedc3be4a9)

In terms of experimental results and analyses, the authors compared the response quality and retrieval quality of KG2RAG with four other baseline methods (LLM-only, Semantic RAG, Hybrid RAG, GraphRAG and LightRAG). In terms of response quality, the authors used F1 score, precision, and recall as evaluation metrics and found that all methods utilising RAG performed better than LLM-only methods, with particularly significant performance on the Shuffle-HotpotQA dataset. In terms of retrieval quality, the authors used the evaluation script provided by HotpotQA to measure F1 scores, precision and recall between retrieved blocks and reference facts and found that KG2RAG outperformed the other methods in terms of both precision and recall.

![image](https://github.com/user-attachments/assets/f2bea1fb-1e21-4995-8287-cb755fb3ff38)

## Conclusion

### 1. Advantages of the Thesis
  1. **Proposed the KG2RAG framework**: the framework enables the model to better capture the factual information in documents by establishing the association relationship between documents and knowledge graphs, thus improving the response quality.
  2. **Innovatively designed the KG-enhanced chunk retrieval module**: the module adopts a combination of semantic retrieval and graph-guided extension, which preserves information with high semantic similarity and increases related entities and triples on the graph structure to improve the response quality.
  3. **The KG-based context organisation module was designed**: it was able to filter the most relevant knowledge points and organise them into internally coherent paragraphs, improving the response quality.
  4. Experimental validation was conducted on the HotpotQA dataset and compared with other RAG methods, and the results showed that KG2RAG has better performance performance.

### 2. Innovative points
  1. The concept of knowledge graph is introduced, and the information of entities and relationships in the knowledge graph is utilised to improve the response quality.
  2. KG-enhanced chunk retrieval module is designed, which combines both semantic retrieval and graph-guided extension to increase related entities and triples on the graph structure to improve the response quality.
  3. KG-based context organisation module is designed, which is able to filter the most relevant knowledge points and organise them into internally coherent paragraphs, improving the response quality.
     
### 3. Future Works
Although the KG2RAG framework proposed in this paper has achieved better performance on the HotpotQA dataset, there is still some room for improvement. For example, the introduction of more knowledge graphs or the use of more complex graph structures can be considered for extension; attempts can also be made to apply the KG2RAG framework to other domains or tasks to further validate its effectiveness.   
