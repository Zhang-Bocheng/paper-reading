# Set Distribution Networks: a Generative Model for Sets of Images
[paper link](https://arxiv.org/pdf/2006.10705) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new generative model for image sets, Set Distribution Networks (SDNs).         |           |

## Methodology

### 1. Abstract
Traditional generative models represent each set as a unique heat vector and learn the conditional generative model p(x|y). However, SDNs target the case where the number of sets is large and unknown, and achieve automatic encoding and free generation of image sets by jointly learning components such as set encoder, set discriminator, set generator, and set prior. 

Experimental results show that SDNs are capable of reconstructing image sets that retain important attributes of the input and can generate novel objects or identities. In addition, the authors evaluated the quality of SDN-generated image sets using pre-trained 3D reconstruction networks and face recognition networks.

### 2. Method Description 
The paper proposes a novel model called Set Distribution Networks (SDNs) for learning the probability distribution of an image set.SDNs consist of four interacting modules: a prior distribution, an encoder, a discriminator and a generator. Among them, the prior distribution employs a binary ensemble code and uses the standard auto-regressive model MADE; the encoder generates the final ensemble code by passing the averaged image feature vectors to a differentiable binarization operation; the discriminator is implemented using the auto-encoder energy function and trains the encoder and the decoder separately to generate a reconstruction; and the generator generates a reconstruction based on a given ensemble code; and the generator randomly samples and independently generates images based on the given ensemble code.

![image](https://github.com/user-attachments/assets/cef91a33-2041-4853-88b6-c643f3fdff21)

### 3. Methodological improvements
The main improvement of the method is the use of conditional probability in the form of generating a new image given an ensemble code. Also, in order to avoid the problem of pattern collapse, the method employs techniques such as learning rate adjustment and architectural design during the training process.

### 4. Issues addressed 
The method can efficiently deal with the problem of modeling probability distributions for image sets with multiple elements, thus opening up possibilities for many applications such as image retrieval, classification and clustering. In addition, the method can be extended to other types of ensemble data modeling.

## Experiments
This paper describes experiments using Set Distribution Networks (SDN) to reconstruct the ShapeNet and VGGFace2 datasets with quantitative and qualitative evaluations. Specifically, the authors conducted the following comparison experiments on the two datasets:

Experiments on the ShapeNet dataset:

  <br>&emsp;Eight elements of the fixed-size dataset were randomly selected as training samples;
  <br>&emsp;The model architecture used in the experiments is similar to SAGAN with the addition of Spectral Normalization (SN) and Self      Attention (SA) modules in the encoder and decoder;
  <br>&emsp;Training was performed using the Adam optimizer with a learning rate of 1e-4;
  <br>&emsp;The parameters θ and ψ are alternately updated during the training process, with a total of about 600K iterations;
  <br>&emsp;The results show that SDN is capable of generating semantically meaningful and consistent reconstruction results, as well as coherent results from prior distributions.
  
Experiments on the VGGFace2 dataset:

  <br>&emsp;For each input image, it is transformed into a fixed dimensional embedding vector;
  <br>&emsp;The authentication performance of the reconstructed and a priori samples is evaluated using ROC curves;
  <br>&emsp;The results show that the ROC curves between the reconstructed and real samples are very close to each other, indicating that the reconstructed samples are diverse and have good internal consistency;
  <br>&emsp;Increasing the number of input images can improve the performance of reconstruction.  

  ![image](https://github.com/user-attachments/assets/3c81491e-af9b-4b7b-8acd-68fcba7f5f0b)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new image set generation model, Set Distribution Networks (SDNs), that learns to randomly reconstruct a given set of images and generates a new set of images simultaneously.
  
  2. Compared to traditional conditional generation models, SDNs have better flexibility and scalability, and can be successfully trained on two real-world datasets.
  
  3. In addition, the authors used pre-trained 3D reconstruction networks and face recognition networks to evaluate the quality of the proposed model and demonstrate its effectiveness in generating high-quality image sets.

### 2. Innovative points
  1. The core idea of SDNs is to encode an image set as a probability distribution and achieve random reconstruction and generation of image sets by jointly training a set encoder, a set discriminator, a set generator and a set prior.
  
  2. This approach not only has better generalization ability, but also can control the features of the generated image set by adjusting the probability distribution. In addition, SDNs employ adversarial training to improve the performance of the model.
  3. 
### 3. Future Works
Future research directions include further optimizing the model structure, exploring more application scenarios, and combining other techniques (e.g., adaptive learning) to improve the performance of the model.   
