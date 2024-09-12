# Sparse Autoencoders Find Highly Interpretable Features in Language Models
[paper link](https://arxiv.org/pdf/2309.08600) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores a difficult problem in the internal structure of neural networks - polysemy, the situation where neurons are activated in more than one semantic sense.          | Neural Networks         |

## Methodology

### 1. Abstract
This phenomenon makes it difficult to understand the inner workings of neural networks and interpret their outputs. The authors suggest that one of the causes of polysemy is ‘superposition’, where the neural network assigns features to an overcomplete set of directions rather than to individual neurons. To address this problem, the authors use sparse self-coders to reconstruct the internal activations of a language model and learn a set of more interpretable, monosemantic feature sets. Experimental results show that these features are able to more accurately locate causally responsible behaviour in an indirect object recognition task. The method provides a scalable, unsupervised approach to solving the problem of neural network internal structure, and helps to improve the transparency and controllability of the model.

### 2. Method Description 
This paper proposes the method ‘Taking Features Out of Superposition with Sparse Dictionary Learning’ which aims to extract network features from superposition by using sparse dictionary learning technique. The method uses an autoencoder model and imposes sparsity penalties on the hidden layer to train the model. Specifically, the method uses the following steps:

  1. Assume that a given set of vector sets {x<sub>i</sub>}<sup>n<sub>vec</sub></sup><sub>i=1</sub> ∈ Rd is composed of linear combinations of unknown vector sets {g<sub>i</sub>}<sup>n<sub>gtj</sub></sup><sub>j=1</sub> ∈ Rd, where ai is a sparse vector.
  
  2. A dictionary set {fk}nfeatk=1∈Rd  {f<sub>k</sub>}<sup>n<sub>feat</sub></sup><sub>k=1</sub> ∈ Rdis learnt such that for any network feature gj there exists a dictionary feature fk such that gj≈fk.
  
  3. The model parameters are trained using an autoencoder model, which consists of a weight matrix M of size Rd hid × din and a bias vector b of size Rd hid. A ReLU function is used in the hidden layer activation function, along with a weight sharing strategy.
  
  4. During training, the model parameters are optimised by minimising the loss function, where α is a hyperparameter that controls the sparsity of the reconstruction.

![image](https://github.com/user-attachments/assets/8e0213f2-7f78-4ccd-a190-2ce54304de46)

### 3. Methodological improvements
Compared to traditional autoencoder models, the method introduces a sparsity penalty term to encourage the model to produce sparse reconstruction results. In addition, the method employs a weight sharing strategy to reduce the number of model parameters and improve model efficiency.

### 4. Issues addressed 
The method solves the problem that traditional autoencoder models are unable to extract network features efficiently, which can be extracted from hyperlocations by sparse dictionary learning techniques. Meanwhile, the method also provides a scalable interpretability evaluation method, which can effectively measure the interpretability score of dictionary features.

## Experiments
This paper focuses on an automatic interpretation method for language models and verifies the effectiveness of the method through comparative experiments. Specifically, this paper conducts experiments in the following four aspects:

**Comparing the effectiveness of different automatic interpretation methods**: this paper classifies automatic interpretation methods into four categories, which are default basis-based methods, random direction methods, principal component analysis methods and independent component analysis methods. By comparing the effect of these methods on the first feature, it is found that the sparse dictionary feature method proposed in this paper is more interpretable than other methods.

**Comparing the effect of different learning methods**: this paper also uses different learning methods to generate dictionary features, including non-sparse dictionary features, sparse dictionary features and so on. The results show that the sparse dictionary feature method is more effective than other methods in modifying the output probability.

**Comparing the effect of different layers**: this paper also investigates the effect of dictionary features in different layers. The results show that the sparse dictionary feature method is more effective than other methods in the first few layers, but at the last layer, its effect is comparable to other methods.

![image](https://github.com/user-attachments/assets/c4db4dab-a2df-4d12-bd11-ce19b48084ff)

**Comparing the results of human interpretation and automatic interpretation**: finally, the paper also compares the results of automatic interpretation with those of human interpretation. The results show that the automatic interpretation method can effectively find dictionary features with specific meanings, which is in line with the results of human interpretation. 

![image](https://github.com/user-attachments/assets/d19a07dd-ac7b-4619-b53c-9a8a78668d9e)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a sparse self-encoder-based method to decouple features in a language model and verify that these features have higher interpretability and univocality in understanding the model behaviour.
  
  2. The method enables the extraction of non-orthogonal features by training the sparse self-encoder to learn the directions in the activation space.
  
  3. In addition, the authors use techniques such as automatic interpretability scores to demonstrate the semantic significance of the learnt features and conduct a case study to demonstrate their effectiveness in predicting model output.

### 2. Innovative points
  1. The main contribution of this paper is to propose a new approach to address the challenge of polysemy in neural networks. Unlike the traditional neuron as a unit, this paper uses sparse selfencoders to learn the direction of the non-orthogonal features, which achieves effective extraction of polysemous features.
  
  2. In addition, the authors propose a variety of validation methods to ensure the semantic meaning of the learned features, including automatic interpretive scores, task-specific behavioural analyses, and case studies for a small number of features.

### 3. Future Works
  1. Although the authors have achieved good results on residual streaming, the application on the MLP layer still needs more exploration. In addition, the authors also mentioned how to incorporate weight information or dictionary feature information from neighbouring layers into the training process to further improve the quality of feature discovery.
  
  2. the authors hope to apply this decoupling approach to a wider range of models and tasks to better understand the behaviour of the model and achieve better controllability and interpretability. 
