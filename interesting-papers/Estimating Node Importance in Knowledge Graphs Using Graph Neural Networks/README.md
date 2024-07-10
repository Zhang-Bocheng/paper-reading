# Estimating Node Importance in Knowledge Graphs Using Graph Neural Networks
[paper link](https://arxiv.org/pdf/1905.08865) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper describes a method called GENI for estimating the importance of nodes in a knowledge graph.          | Graph Neural Networks         |

## Methodology

### 1. Abstract
  The method is based on supervised learning algorithms and graph neural network techniques (GNN), which enable better utilization of information in KGs and have higher flexibility to handle complex relationships and importance between entities. The authors experimentally demonstrate that GENI outperforms existing methods in predicting the importance of nodes in KG, improving the NDCG@100 metric by 5-17%. 

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/79bc5c68-1958-4aac-8c37-1e3a23353856)

### 2. Method Description 
  The paper proposes a graph neural network (GNN)-based node importance estimation algorithm called GENI.The algorithm replaces the traditional neighbor vector aggregation by directly aggregating the importance scores of the neighbors, and is designed with three main enhancements: neighborhood importance awareness, an attention mechanism using predicates, and centrality adjustment. In addition, the algorithm employs a flexible adaptation strategy that can adaptively handle different types of importance inputs and can adjust the model parameters according to different task requirements.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/1d7919a2-88d3-4c79-9fe2-1b96148b2cb4)

### 3. Key Concepts
  _Graph Neural Networks (GNNs)_: A class of neural networks designed to operate on graph-structured data. In contrast to traditional NN that process grid-like data such as images or sequences, GNNs are specialized for handling data that can be represented as graphs, where nodes represent entities and edges represent relationships between them.
  
### 4. Methodological improvements
  The algorithm improves on the traditional GNN framework by introducing three new components to improve its performance. 
  
  1. First, it proposes a score aggregation framework for directly aggregating the importance scores of neighbors instead of neighbor vectors.
  
  2. Second, it devises a predicate-aware attention mechanism to take into account the differences in roles between different predicates.
  
  3. Finally, it applies centrality adjustment to consider the centrality of nodes together with the importance of inputs.
     
### 5. Issues addressed 
  The algorithm solves the problem that traditional GNN frameworks cannot effectively utilize the importance information of inputs and improves its performance by introducing new components. And, the algorithm can adaptively handle different types of importance inputs and can adjust the model parameters according to different task requirements. These improvements enable the algorithm to have better generalization ability and higher accuracy in practical applications.
  
## Experiments
  This paper focuses on the GENI method for the problem of node importance estimation in knowledge graphs and validates its performance by comparing it with a variety of untrained and supervised learning algorithms. Specifically, the authors use four different real-world KGs as datasets, including FB15K, MUSIC10K, TMDB5K, and IMDB, and categorize these KGs into two parts, inner and outer domains, for evaluation. In the inner domain evaluation, the authors used two metrics, NDCG@100 and SPEARMAN, to measure the prediction quality of the model, while in the outer domain evaluation, two metrics, NDCG@100 and NDCG@2000, were used. The final results show that the GENI method exhibits better performance in both the inner and outer domains relative to other untrained and supervised learning algorithms. In addition, the authors performed a sensitivity analysis on some parameters of the GENI method and found that increasing the number of fractional aggregation layers and heads improves the model performance.
  
![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/21a6cde0-5dbe-4c05-baac-64e9c25e8a98)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new method, GENI, for estimating the importance of nodes in KG.
  
  2. GENI utilizes the rich KG information to model the complex relationship between entities and their importance in a flexible way.
  
  3. The paper demonstrates through experimental results that GENI performs better than existing methods in predicting the importance of nodes in KG, improving the NDCG@100 metrics by 5-17%.

### 2. Innovative points
  1. GENI uses an attention mechanism to aggregate edge type information to capture the relationship between neighboring nodes and target nodes.
  
  2. GENI allows flexible score adjustment based on node centrality, capturing the connectivity of nodes in the network topology.
  
  3. The paper proposes a solution based on a supervised learning algorithm that allows the model to learn from real data and utilize auxiliary information in KG.
     
### 3. Future Works
  1. The paper could consider multiple independent input sources for node importance prediction in the future.
  
  2. Further research can be done on how to handle the importance and relationships of different types of entities in KG.
