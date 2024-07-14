# Implicit Neural Representations with Periodic Activation Functions
[paper link](https://arxiv.org/pdf/2006.09661.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new neural network architecture, the periodic activation function implicit neural representations (SIRENs), which can be used to model complex natural signals and their derivatives, and can solve some challenging boundary value problems.         | Neural Network          |

## Methodology

### 1. Abstract
   The advantage of SIRENs over traditional NN architectures is their ability to better handle detail information and spatial/temporal derivatives. In addition, the authors propose a SIRENs-based hypernetwork approach for learning the spatial prior knowledge of SIRENs functions. The experimental results show that SIRENs perform well in the fields of image, wavefield, video and sound.

   ![image](https://github.com/user-attachments/assets/087dc29c-706d-4a1f-b064-584ee6687c1c)

### 2. Method Description 
  This paper propose SIREN (Spectral Normalization Integrated Residual Network), which is a neural network-based implicit function representation method for solving problems such as image processing, audio signal processing, etc. SIREN uses periodic sinusoidal activation function as a nonlinear transform and spectral normalization technique to ensure the stability of the weight matrix.
  
  ![image](https://github.com/user-attachments/assets/ee20b112-7479-4eaf-b62e-caf93cc1f461)

### 3. Methodological improvements
  SIREN has the following advantages over traditional NN:

  1. **Faster convergence**: SIREN is able to learn the features of the objective function faster, thus achieving better performance in a shorter time.
  
  2. **Higher accuracy**: Since SIREN can fit complex high-dimensional data better, it can solve problems with higher accuracy.
  
  3. **Better generalization ability**: SIREN can improve the generalization ability of the model by adjusting the hyperparameters to make it suitable for more application scenarios.

### 4. Issues addressed 
  SIREN can be applied to a variety of problems, such as image processing and audio signal processing. SIREN can predict unknown data points more accurately and learn the characteristics of the objective function faster. In addition, SIREN can  understand complex phenomena in NN, such as the problems of gradient vanishing and gradient explosion.
  
  ![image](https://github.com/user-attachments/assets/9a05d809-9c88-488f-b243-fd6df27f4ff8)

## Experiments
  This paper presents four experiments using SIREN to solve different types of boundary value problems. These experiments include:

  1. **Solving the Poisson equation**: reconstructing images and solving image editing problems by supervising the derivatives of the model;
  
  2. **Representing SDFs of shapes**: fitting SDFs directly on point clouds and using SIREN to significantly increase the detail of complex scenes;
  
  3. **Solving Helmholtz and fluctuation equations**: parameterizing wavefields and solving them numerically using SIREN;
  
  4. **Learning powerful priors in implicit function spaces*: mapping SIREN's parameters into low-dimensional subspaces and using hypernetworks to generate SIREN's weights for the task of interpolating images from sparse observations.
     
For each experiment, the article provides details of the experimental design, results and conclusions. 

In the first experiment, the authors compare the effects of using SIREN and ReLU neural networks to reconstruct an image and find that SIREN captures the details of the image better. 

In the second experiment, the authors show how SIREN significantly improves the representation of shapes and can handle more complex scenes. 

In the third experiment, the authors compare the results of using SIREN with other neural network methods to solve the Helmholtz and fluctuation equations, and demonstrate that SIREN is able to solve these problems efficiently with high accuracy. 

Finally, in the fourth experiment, the authors show how SIREN can be used to learn a powerful implicit function space prior and apply it to an image interpolation task. 

![image](https://github.com/user-attachments/assets/6789cb23-222f-455e-a150-5ffae37837c9)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper propose a new NN architecture, SIREN (Sinusoidal Activation Functions for Representation Learning), which uses periodic activation functions to achieve continuous implicit representation learning.
  
  2. SIREN can efficiently process complex natural signals, such as images, audio and video, and can accurately represent these signals and their derivatives.
  
  3. SIREN offers many advantages such as more efficient memory usage, computable gradients and higher order derivatives, and the ability to solve inverse problems.

![image](https://github.com/user-attachments/assets/21e143c5-4453-4896-b8e7-f4ea67e64b2f)

### 2. Innovative points
   1. SIREN's periodic activation function is able to better represent the detailed information and higher order derivatives in the signals compared to the traditional ReLU activation function.
   
   2. SIREN also provides a new toolbox for solving inverse problems such as differential equations.
    
### 3. Future Works
  1. Future research directions include exploring other types of inverse problems and application areas such as neural ODEs.
  
  2. In addition, SIREN may be used to generate spurious signals, which requires further research to prevent its misuse.

