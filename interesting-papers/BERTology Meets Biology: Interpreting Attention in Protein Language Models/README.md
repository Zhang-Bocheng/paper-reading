# BERTology Meets Biology: Interpreting Attention in Protein Language Models
[paper link](https://arxiv.org/pdf/2006.15222) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the use of attention mechanisms to analyze protein language models and demonstrates three different Transformer architectures (BERT, ALBERT, and XLNet)         |  Transformer   |

## Methodology

### 1. Abstract
  The researchers found that attention can capture protein folding structures, connecting amino acid residues that are far from their positions in the sequence but close together in the 3D structure; it can also focus on binding sites, the functional components of proteins. In addition, as the number of layers increases, attention gradually focuses on more complex biophysical properties. Through 3D visualization techniques, the researchers also present the interaction between attention and protein structure. The study provides new ideas and methods for understanding protein language models.
  
### 2. Method Description 
  This study used pre-trained language models to probe the comprehension of protein structures and evaluated them through attention analysis, probing tasks, and other methods. Specifically, they used five different pre-trained models (including BERT, ProtTrans, etc.) and applied them to three different datasets (contact maps, secondary structures, and binding sites). 
  
  In their experiments, they first calculated the correlation between the level of attention of the different heads in each model and various protein attributes, and then used a probing task to assess the models' ability to represent knowledge about these attributes.
  
### 3. Methodological improvements
  Compared to the traditional protein modeling approach based on sequence information, this study employs higher-level abstract features (e.g., contact maps) as inputs and leverages the strong generalization ability of the pre-trained model to learn the structural and functional information of proteins. In addition, they introduced an attention analysis technique to gain a deeper understanding of how much attention the model pays to different protein attributes, and further validated its knowledge representation capability.
  
### 4. Issues addressed 
  This study addresses the inability of traditional protein modeling methods to effectively capture complex protein structural and functional information, and provides a new technique based on pre-trained models and attentional analysis to better understand and predict protein behavior. This is of great significance for protein design and drug discovery in the biomedical field.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a586e12b-1139-4a2e-84f7-9d4e74399191)
 
## Conclusion
### 1. Advantages of the Thesis
  This article focuses on how Natural Language Processing (NLP) techniques can be applied to protein sequence modeling, and addresses this problem by extending and adapting NLP interpretability methods. The article proposes a Transformer-based language model that recovers protein structural and functional properties and integrates them directly into its attention mechanism. In addition, the authors propose a method to visualize attention in order to better demonstrate learned representations. 
  
### 2. Innovative points
  1. The main contribution of this paper is to combine NLP techniques and protein sequence modeling to propose a new approach to protein sequence modeling. 
 
  2. This approach not only improves the accuracy of protein sequence modeling, but also makes it easier for scientists to understand and utilize the learned knowledge.
     
### 3. Future Works
  1. Although the protein sequence modeling approach proposed in this paper has made some progress, there are still many challenges to overcome. For example, how to further improve the accuracy and interpretability of the model
     
  2.  And how to apply this technique to a wider range of biological process studies, among others. 
