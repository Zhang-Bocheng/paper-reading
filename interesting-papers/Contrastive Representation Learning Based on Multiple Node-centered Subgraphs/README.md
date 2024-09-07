# Contrastive Representation Learning Based on Multiple Node-centered Subgraphs
[paper link](https://arxiv.org/pdf/2308.16441) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores a comparative learning approach based on multi-node centred subgraphs for learning the representation of nodes in graph data in an unsupervised manner.          | Representation Learning         |

## Methodology

### 1. Abstract
The authors argue that a single node can extract multiple subgraphs centred on that node from the entire graph (e.g., in social networks, a person can have multiple social circles based on his different connections). To implement this idea, the authors design a series of regional subgraphs for the central node and maximise the mutual information between different subgraphs of the same node by contrast loss. Experimental results show that the model achieves state-of-the-art results on a variety of real-world datasets and downstream tasks.

![image](https://github.com/user-attachments/assets/da0ec916-7f6c-4681-9352-103cc181662f)

### 2. Method Description 
The paper presents MNCSCL, a graph representation learning algorithm based on self-supervised learning for learning the embedding vectors of nodes. The algorithm uses multiple subgraphs of different types to generate positive and negative samples and trains the model by maximising the mutual information (MI) between them. Specifically, the algorithm first uses a noise function to perturb the structure and attributes of the input graph, and then takes the original graph and the perturbed graph as inputs and passes them through a shared encoder to obtain the embedding vectors of the nodes, respectively. Next, the algorithm uses a subgraph generator to sample a number of different types of subgraphs from the original graph and generate corresponding negative samples from the perturbed graph. Finally, the algorithm uses these subgraphs and their corresponding negative samples to compute the mutual information of the node embedding vectors and uses a gradient descent optimiser to update the model parameters.

![image](https://github.com/user-attachments/assets/f7bafd04-af55-435d-b7ec-b5c30f9833a5)

### 3. Methodological improvements
Compared to traditional graph representation learning algorithms, MNCSCL introduces several different types of subgraphs to generate positive and negative samples, which improves the generalisation and learning capabilities of the model. In addition, the algorithm adopts the idea of self-supervised learning, which avoids the problem of needing a large amount of labelled data, and can also effectively reduce the risk of overfitting.

### 4. Issues addressed 
The goal of MNCSCL is to learn the embedding vectors of nodes in order to better handle tasks such as node classification and link prediction in downstream tasks. While traditional methods usually only consider local features of nodes, MNCSCL can capture global features of nodes using several different types of subgraphs to improve the performance of the model. In addition, MNCSCL can be applied to learn large-scale unlabelled graph data, which has a wide range of applications.

## Experiments
This paper focuses on the use of a multi-perspective self-supervised learning approach, MNCSCL, in node classification and link prediction tasks, and compares it with other traditional unsupervised algorithms. Specifically, the authors employ five commonly used benchmark datasets, including three citation networks (Cora, Citeseer, and Pubmed), a social network (Reddit), and a multi-graph protein interaction dataset (PPI), and design a different experimental setup and evaluation metrics for each of them. In the node classification task, the authors compare MNCSCL with the direct use of row features, the traditional unsupervised algorithm Deep Walk, two supervised graph neural networks GCN and FastGCN, and five state-of-the-art self-supervised methods DGI, GMI, GIC, GRACE, and MV-GRL. 

In the link prediction task, the authors instead directly used effective link prediction methods such as GIC. The final results show that MNCSCL achieves the best performance on all datasets, outperforming other competing self-supervised and traditionally supervised methods. In addition, the authors conducted several ABlation studies to explore the effects of different subgraph combinations, neighbourhood ranges and clustering strategies on model performance.

![image](https://github.com/user-attachments/assets/d6b77d7b-f898-4b76-b89d-8d13000c882a)
 
## Conclusion

### 1. Advantages of the Thesis
The paper proposes a novel self-supervised graph representation learning method, Multiple Node-centered Subgraphs Contrastive Representation Learning (MNCSCL), which obtains comprehensive node representations by observing individual nodes in the network from different semantic viewpoints of individual nodes in the network to obtain subgraphs under multiple viewpoints, and uses contrast learning to maximise the mutual information among these subgraphs to obtain a comprehensive node representation. Experimental results show that MNCSCL achieves state-of-the-art in both conductive and inductive node classification tasks as well as link prediction tasks.

### 2. Innovative points
  1. The main innovation of MNCSCL is to consider a single node as a centre and sample its subgraphs from different semantic perspectives, resulting in several different perspectives.
  
  2. In addition, MNCSCL employs two types of contrast loss functions to maximise the mutual information between different subgraphs for a more comprehensive node representation.

### 3. Future Works
MNCSCL is an effective method for learning self-supervised graph representations, but further optimisation may be needed in practical applications. For example, issues such as how to better select the number and semantics of subgraphs and how to handle large-scale network data can be explored. In addition, combining MNCSCL with other graph neural network models can be considered to improve its performance and applicability.  
