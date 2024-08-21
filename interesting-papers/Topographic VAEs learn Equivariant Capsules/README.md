# Topographic VAEs learn Equivariant Capsules
[paper link](https://arxiv.org/pdf/2109.01394) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a novel deep generative model, called the ‘terrain-variant self-encoder’, which can efficiently train latent variables characterised by terrain organisation and organise activations according to salient features such as digit class, width and style.          | Neural Networks          |

## Methodology

### 1. Abstract
The authors show how predefined latent spatial transformation operations can be encouraged through temporal topographical organisation, thus achieving a kind of unsupervised learning equivalence. Experimental results show that the model can learn a set of features (i.e., a ‘capsule’) that approximate equivalence directly from sequences, and that higher probability values can be obtained when transforming test sequences accordingly. Finally, the authors also demonstrate the model's approximate equivalence for complex transformations, extending the capabilities of existing swarm equivalence neural networks.

### 2. Method Description 
The model proposed in this paper is a generative model based on the Topographic Product of Student's-t (TPoT) model. The model uses independent standard normal random variables to construct the TPoT random variables and is trained by variational inference for an efficient training process. Topographic neighbourhoods are extended in time, temporal correlations are introduced, and unsupervised learning is encouraged to approximate equivalent subspaces, called ‘capsules’.

![image](https://github.com/user-attachments/assets/bbdf40c9-cd0d-4617-996d-7777e1a6535e)

### 3. Methodological improvements
In contrast to previous work, this paper proposes a method for constructing the TPoT distribution as a deterministic function of Gaussian random variables, allowing for variational inference and efficiently maximising the likelihood through the Evidence Lower Bound (ELBO). In addition, this paper introduces a capsule structure that achieves the goal of unsupervised learning to approximate equivalent subspaces.

### 4. Issues addressed 
The model proposed in this paper can be trained efficiently and has good performance. Also, the model can be used for unsupervised learning of approximate equivalent subspaces, which solves the problem that cannot be solved by traditional methods.

## Experiments
Six experiments are presented：
<br>&emsp;the first of which demonstrates the feasibility of Topographic VAE and proves that it can learn topologically organised representations with deep neural networks. 
<br>&emsp;The second experiment validates global and local topology in capsule space by using 2D convolution and loop filling in Topographic VAE without temporal correlation. 
<br>&emsp;The third experiment explores how Topographic VAE can be used to learn capsule models with full sequence transformation invariance. 
<br>&emsp;The fourth experiment compares the performance differences between Topographic VAE and standard normal variational autocoders as well as BubbleVAE with static temporal correlation. 
<br>&emsp;The fifth experiment investigates how Topographic VAE learns capsule models with full serial transform invariance. 
<br>&emsp;The sixth experiment explored how Topographic VAE learns capsule models with full sequence transform invariance and also provided evidence of sophisticated learning capabilities.

For these experiments, the authors used different evaluation methods and metrics, including visualisation methods, error rates, and cross-correlation coefficients. For example, in the first experiment, the authors used visualisation methods to show whether the model was able to learn a topologically organised representation with a deep neural network. In the second experiment, the authors used error rates to measure whether the model was able to implement global and local topologies in capsule space. In the third experiment, the authors used visualisations to show whether the models were able to learn capsule models with full sequence transformation invariance. In the fourth experiment, the authors used cross-correlation coefficients to measure whether the models were able to learn capsule models with full sequence transformation invariance. In the fifth experiment, the authors used the error rate to measure whether the model was able to learn a capsule model with full sequence transform invariance. In the sixth experiment, the authors used visualisation methods to show whether the model was able to learn the capsule model with full sequence transform invariance and also provided evidence of complex learning ability.  

![image](https://github.com/user-attachments/assets/816a4cee-86ce-4fe9-b1b3-1f9bb7e50da5)

## Conclusion

### 1. Advantages of the Thesis
TVAE has the following advantages over traditional VAE:

  1. TVAE is able to learn the topology directly from sequence data without using any supervisory information, which enables more efficient feature extraction.

  2. TVAE can learn a feature representation similar to that of a capsule network, which has better invariance and generalisation capabilities.
  
  3. TVAE achieves better performance than traditional VAE in experiments.

### 2. Innovative points
 1. **Topology**: TVAE maps the input data into a topological space such that there is some kind of similarity relationship between neighbouring data points, which helps to improve the quality of feature representation.
  
  2. **Convolutional Layer**: The convolutional layer in TVAE considers not only the pixel values within a local region, but also the topological relationships between them, which better captures the spatial structure of the image.
  
  3. **Network Architecture**: The design of TVAE is inspired by the capsule network, which maps the input data into a set of capsules, each of which contains some specific type of features. The benefit of this design is that it avoids overfitting while improving the generalisation ability of the model.

### 3. Future Works
  1. **Model complexity**: the network structure of TVAE is relatively complex, requiring more computational resources and training time.
  
  2. **Data volume limitation**: Since TVAE needs to map the data topologically, overfitting may occur for small-scale datasets.
  
  3. **Application Scenario**: Currently TVAE is mainly used in the field of image processing, and in the future, we can explore the possibility of applying it to other fields, such as NLP.
