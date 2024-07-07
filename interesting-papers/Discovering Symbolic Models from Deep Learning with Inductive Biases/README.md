# Discovering Symbolic Models from Deep Learning with Inductive Biases
[paper link](https://arxiv.org/pdf/2006.11287) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new approach to refining symbolic representations of deep learning models by introducing a strong induction bias.         | Deep Learning         |

## Methodology

### 1. Abstract
  The authors focus on graph neural networks (GNNs) and use supervised training to encourage sparse implicit representations and apply symbolic regression to extract explicit forms of known physical relationships. Experimental results show that correctly known equations and force laws, among others, can be extracted from the neural networks. In addition, symbolic expressions extracted from GNNs using this technique generalize better to outlier data than GNNs themselves. This approach provides alternative directions for interpreting NN and uncovering novel physical principles.
  
### 2. Method Description 
  The paper presents a new DL modeling framework for the problem of interacting particle systems. The framework consists of four main components:

  1. Engineering the design of a deep learning model with an internal structure that matches the characteristics of the data.
  
  2. Training the model using the available data.

  3. Mapping the functions learned by the model into symbolic expressions.
  
  4. Replace the use of these functions in the deep model and extend the process by discovering new symbolic expressions.

  They chose to use Graph Networks as the core ML model because they share many of the intrinsic properties of physical problems. They also used symbolic regression techniques to map the functions learned by the model to symbolic expressions.
  
### 3. Key concepts
  _Graph Networks (GNs)_: A class of NN specifically designed to work with graph-structured data. Graphs are mathematical structures used to model pairwise relations between objects, and they consist of nodes (or vertices) and edges connecting them. GNs leverage this structure to perform tasks such as node classification, edge prediction, and graph classification.
  
### 4. Methodological improvements
  The main improvement of the framework over traditional DL models is the design of its internal structure. The GNN provides three well-defined roles: the edge model, the node model and the global model. These three models are responsible for different tasks, such as message passing, node updating and global aggregation. In addition, they used symbolic regression techniques to further explain the functions learned by the models and map them into symbolic expressions.
  
### 5. Issues addressed 
  The framework addresses the problem of dealing with interacting particle systems. It provides an engineered DL modeling framework that can efficiently handle this type of data. By using GNN and symbolic regression techniques, the framework is able to discover new symbolic expressions and apply them to high-dimensional datasets. In addition, the framework helps us understand the functions learned by the model and map them to symbolic expressions, thus improving the interpretability and reliability of the model.
  
## Experiments
  This paper presents four sets of experiments: Newtonian dynamics, Hamiltonian dynamics, Dark matter halos for cosmology, and Symbolic generalization.These experiments aim to explore the effectiveness of NN in different domains and to verify their can extract useful physical laws from data.

  The first set of experiments is for the prediction of forces for a simple N-body system, where the authors use different training strategies to optimize the NN model, and ultimately find that the model with L1 regularization performs the best. Then, the authors demonstrated that the messages learned by the NN can be interpreted as forces by interpreting the relationship between message components and true forces. Finally, the authors also performed symbolic regression to extract the true force formula from the message function.

  The second set of experiments was trained on the same dataset under Hamiltonian dynamics, and the authors successfully extracted the potential energy formula from the message function.

  The third set of experiments was on the problem of predicting the dark matter halo, where the authors used the same method to train the NN and extract formulas from it. The results show that the formulas proposed by the authors are more accurate than those designed by humans.

  The fourth set of experiments was on the ability of symbolic generalization, where the authors compared the performance of NN and symbolic expressions on unseen data by masking the data. The results show that symbolic expressions have better generalization ability on unseen data.
  
![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/49e07ecd-614e-4e4f-833b-dcb48411c4d3)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new DL framework that combines the benefits of DL and symbolic regression for learning interpretable representations and improving zero-sample generalization.
  
  2. The authors use GNN as models and implement physically heuristic inductive bias by implementing bottleneck or L1 regularization in the message passing layer, or flattening Hamiltonian GNN into symmetric and parallel terms.
  
  3. In addition, the authors demonstrate a general technique for finding unknown force laws from these models: symbolic regression can fit explicit equations to the message functions of our training models.
  
  4. Finally, the authors demonstrate their algorithm on a non-trivial dataset and find new laws for dark matter. The main strength of the article is that it proposes a new DL framework that can take advantage of both DL and symbolic regression to better handle complex ML problems. 
  
### 2. Innovative points
  1. The methodological innovation of this paper is to propose a new DL framework that combines the advantages of DL and symbolic regression in order to solve the problem of high computational complexity in traditional symbolic regression methods.
 
  2. And, the authors introduce some specific tricks and techniques, such as implementing bottleneck or L1 regularization in the message passing layer, or flattening the Hamiltonian GNN into symmetric and parallel terms to achieve physically heuristic inductive bias.
     
### 3. Future Works
  1. Similar frameworks can be used to extract interpretable features and patterns in areas such as NLP and CV.
  
  2. And, how symbolic regression can be combined with other DL techniques to solve more complex ML problems can be further explored.

