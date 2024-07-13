# Graph Convolutional Neural Networks for Web-Scale Recommender Systems
[paper link](https://arxiv.org/pdf/1806.01973) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This paper presents a large-scale deep recommendation engine called PinSage, which utilizes a graph convolutional neural network (GCN) algorithm that combines efficient random walks and graph convolution to generate embedding vectors for nodes, taking into account both graph structure and node feature information.           |  Graph Convolutional Neural Networks (GCN)        |

## Methodology

### 1. Abstract
   Compared to previous GCN-based approaches, PinSage employs an efficient random walk to build the convolution and designs a new training strategy to improve the robustness and convergence of the model. After deploying PinSage on Pinterest, it was demonstrated through offline metrics, user studies, and A/B testing that PinSage produced higher quality recommendation results than other similar deep learning and graph-based alternatives. This work is one of the largest applications of deep graph embedding to date, paving the way for a new generation of web-scale recommender systems based on graph convolutional architectures.

   ![image](https://github.com/user-attachments/assets/64ca34bc-64e8-47d1-9334-77572d856f87)

### 2. Method Description 
  This paper presents a NN model called PinSage for learning node embeddings in recommender systems. The model uses a local graph convolution operation to aggregate node features and gradually extracts higher-level structural information through multi-layer stacking. 
  
  Specifically, for each node, the importance scores of its neighboring nodes are first calculated, and then a weighted average is performed based on the importance scores to obtain a local graph convolutional representation of the node. Next, this representation is spliced with the output of the previous layer and mapped to the final embedding dimension through a fully connected layer. Finally, the model is trained using a maximum bounded ranking loss function to optimize the node embedding vectors.

  ![image](https://github.com/user-attachments/assets/cca2d774-d6ca-4e1e-a1ad-e3e8fa400428)

### 3. Methodological improvements
  1. Compared to the traditional neighborhood-based recommendation algorithms, the PinSage model introduces the idea of DL, which is able to better capture the complex dependencies between nodes.
  
  2. In addition, PinSage adopts an important neighbor selection strategy, determining the importance of neighboring nodes based on the probability of nodes visiting each other, thus avoiding the limitation of fixed distance and improving the generalization ability of the model.
     
### 4. Issues addressed 
  PinSage model is suitable for recommendation tasks in large-scale social networks, e-commerce platforms and other scenarios, and can effectively improve recommendation accuracy and efficiency. Meanwhile, the model can also be applied to other fields, such as NLP, image recognition, etc., which has a wide range of application prospects.
  
  ![image](https://github.com/user-attachments/assets/b233bc41-e209-4f49-bfb3-3d06f49c830b)

## Experiments
  This paper describes a recommendation task for Pinterest object graphs, and the authors designed a series of experiments to evaluate the effectiveness of PinSage and compare it with other DL and graph-based approaches. Specifically, the authors conducted experiments in the following four areas:

**Experiment setup**: the authors define two tasks, i.e., recommending relevant pins and recommending pins in a user's homepage. for the former, the authors use the K-nearest neighbor algorithm to select the nearest neighbors to the query pin; for the latter, the authors select the pins closest to the user's most recently used items. the authors use offline ranking metrics and a user study to evaluate the performance.

**Training data preparation**: the authors generated a positive sample set from historical user interaction data and randomly selected a negative sample set. In total, 120 million positive samples and 500 negative samples were used. Due to the long training time, the authors trained the model only on subgraphs and used MapReduce pipeline to generate embedding vectors on the whole graph.

**Feature representation**: each pin has an image and a set of text annotations (title and description). The authors combine the visual features and text annotation embedding vectors as input feature vectors.

**Benchmark Methods**: the authors compare PinSage with four benchmark methods including visual embedding, text embedding, joint embedding, and the graph-based method Pixie. the authors use hit rate and MRR as evaluation metrics, and the results are analyzed and interpreted.

![image](https://github.com/user-attachments/assets/6c18bf46-b089-46de-a407-0f28960dbc2b)

![image](https://github.com/user-attachments/assets/6c895d3b-680b-463e-a4de-cddae68b3162)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a stochastic wandering graph convolutional network (GCN) called PinSage that is capable of learning node embeddings in Web-scale graphs containing billions of objects.
  
  2. PinSage is a highly scalable GCN algorithm that enables efficient training and inference and performs well on large-scale recommendation tasks.
  
   3. By using techniques such as significant pooling and hierarchical training, PinSage significantly improves embedding performance, leading to better recommendations.
   
   4. The authors deployed PinSage on Pinterest and conducted extensive offline metrics evaluations, user studies, and A/B tests to demonstrate its superior performance on several recommendation tasks.
      
### 2. Innovative points
   1. PinSage employs random walks to construct the computational graph, avoiding the problem that traditional GCNs need to manipulate the entire graph, and greatly reducing the computational complexity.
   
   2. PinSage introduces an importance pooling technique that weights the importance of node features according to the random walk similarity metric, improving the effect of aggregated information.
   
   3. PinSage also designed a hierarchical training scheme to gradually increase the difficulty of the model, further improving the recommendation effect.

   ![image](https://github.com/user-attachments/assets/6dcd8f90-9177-4f3f-bbdf-e1465d050fb2)
   
### 3. Future Works
  1. The successful application of PinSage provides new ideas and directions for GCN in production recommendation systems.
  
  2. PinSage can be applied to other learning problems with large-scale graph-structured data, such as knowledge graph inference and graph clustering.
  
  3. More complex graph convolutional architectures can be explored in the future to cope with larger scale data and more complex recommendation scenarios.
     
