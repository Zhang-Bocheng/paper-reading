# Tree-Structured Shading Decomposition
[paper link](https://arxiv.org/pdf/2309.07122) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This thesis explores how a tree-structured representation of shadows on an object's surface can be inferred from a single image.         |  Computer Vision        |

## Methodology

### 1. Abstract
Traditional shadow modeling methods use parametric or measured approaches for modeling, but these are neither intuitive nor easy to edit. The authors propose a shading tree representation that combines basic shading nodes and a synthesis method to decompose object surface shading. This approach allows novice users unfamiliar with physical shading processes to edit object shadows efficiently and intuitively. However, the main challenge in inferring the shading tree is that the inference problem involves the discrete nature of the tree structure and the continuous parameters of the tree nodes. 

To address this problem, the authors propose a hybrid approach that introduces an autoregressive inference model to generate rough tree structure and node parameter estimates, and fine-tunes the inferred shading tree with an optimization algorithm. Experimental results show that the method achieves good results on synthetic images, reflectance capture, real images and unrealistic vector mapping, and can be applied to downstream applications such as material editing, vectorized shading and relighting.

![image](https://github.com/user-attachments/assets/c407e910-ed80-49a2-a012-703e7ef011c4)

### 2. Method Description 
This thesis proposes a tree-structure based shadow decomposition algorithm for decomposing complex lighting effects into basic shadow nodes and assembling these nodes into more complex shadow structures using a combinatorial approach. The algorithm consists of two stages: **a recursive reasoning module and an optimization module**. In the first stage, the initial tree structure is predicted by the recursive inference module; in the second stage, for nodes that cannot be successfully decomposed, the optimization module is used to further adjust the parameters and find the optimal substructure.

Specifically, in the recursive inference module, the root node is first added to the node pool, and then non-leaf nodes that have not yet been decomposed are continuously considered. For each non-leaf node, it is inputted into the shared single-step component prediction module M to obtain a representation of its left and right child nodes. Next, these three nodes are inputted into CNNf, and an operation is selected as the operation type of the parent node according to the probability distribution, and the corresponding parameter values are predicted by CNNg. Finally, the single-step reconstruction error is calculated based on the prediction result, and it is judged whether it is necessary to continue decomposing the left and right child nodes. If not, the node is marked as solved.

![image](https://github.com/user-attachments/assets/e570c6b7-fa09-4380-88dd-841ee16a3148)

## Experiments
This paper presents an experimental study of the Shadow Tree Decomposition method and compares it with three other competing baselines. 
1. First, on synthetic datasets and real captured datasets, the authors used three different baseline methods (CNN, LSTM, and Transformer) to compare with their own method. The results show that the authors' method exhibits the best reconstructed tree structure in all three test sets.
   
![image](https://github.com/user-attachments/assets/acf3f094-60d0-4525-8a3a-c0c6cbab3fd6)

3. Second, the authors designed a task called “visual coloring editing analogy” to quantitatively evaluate the reconstructed tree structure and generated a set of different types of coloring editing datasets to evaluate the performance of each method. The results show that the authors' approach performs well in this task because it better understands the semantic meaning of the tree structure.

![image](https://github.com/user-attachments/assets/ae64ea6a-950e-4d31-b793-12def708262b)

4. Finally, the authors also conducted three sets of ablation experiments to verify the effect of the particular design in their method on its performance. These experiments include the effects of components such as multisampling, second-stage optimization, and overall optimization. The results show that multisampling can improve the quality of the results inferred in the first stage, while the second stage optimization can help to solve some difficult problem nodes. Meanwhile, the overall optimization can further fine-tune the structure, e.g., by providing better ambient reflections.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a novel approach to decompose light and represent it as a tree structure, making understanding and editing interpretable and controllable.
 
  2.  The authors use a pre-trained auto-regressive model to predict the tree structure and parameters, as well as a primitive-based structure search to find the optimal structure for all nodes that cannot be efficiently decomposed by the first stage. This approach shows better performance compared to the baseline on multiple datasets.

![image](https://github.com/user-attachments/assets/fee7152f-24a1-4680-9333-0ba3bae26df9)

### 2. Innovative points
The main contribution of this thesis is to propose a new method to decompose light and represent it as a tree-like structure. This tree structure not only represents complex illumination efficiently, but also allows controlled editing by searching primitives. In addition, the authors used a pre-trained auto-regression model to predict the tree structure and parameters, thus improving efficiency and accuracy.

### 3. Future Works
These methods can be applied to virtual reality, game development and other fields to improve rendering quality and interactive experience. At the same time, we can also expect more research focusing on how to extend these methods to other fields, such as image processing, video coding, etc.  
