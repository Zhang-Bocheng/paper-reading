# NVAE: A Deep Hierarchical Variational Autoencoder
[paper link](https://arxiv.org/pdf/2007.03898) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper presents a deeply hierarchical variational autocoder model called Nouveau VAE (NVAE), which is designed using techniques such as separation convolution and batch normalization, and stabilizes the training process using residuals parameterized by a normal distribution as well as spectral regularization.         |   Neural Networks        |

## Methodology

### 1. Abstract
This paper presents a deeply hierarchical variational autocoder model called Nouveau VAE (NVAE) and experimental results show that NVAE achieves state-of-the-art results in non-autoregressive likelihood modeling on the MNIST, CIFAR-10, CelebA 64, and CelebA HQ datasets, and provides a strong baseline on the FFHQ dataset. In addition, NVAE is the first variational auto-encoder model that has been successfully applied to natural images with a size of 256x256 pixels.

### 2. Method Description 
The deep hierarchical variational self-encoder (NVAE) proposed in this paper aims to generate high-quality large images. The design of NVAE focuses on solving two main challenges: **designing expressive NNs specialized for variational self-encoders (VAEs)** and **scaling up the training with large number of hierarchical groups** and image sizes and maintaining the training stability. The NVAE uses conditional dependency graphs to deal with these challenges and it comes with novel network architecture modules and approximate a posteriori parameterization for stable training.

NVAE employs residual cells as its core component, which helps to model long-range correlations in the data. NVAE increases spatial dimensions by increasing spatial dimensions layer-by-layer, starting with a small spatial arrangement of latent variables, and then incrementally increasing spatial dimensions grouped in hierarchies. This multi-scale approach allows NVAE to capture global long-range correlations at the top level and local fine-scale dependencies at the bottom level.

![image](https://github.com/user-attachments/assets/1a1a5767-db12-47a7-81d1-55e68bd81612)

### 3.Methodological improvements
The expressive power of the inflated convolution is limited because it only operates independently on each channel. To solve this problem, 

  1. the authors borrowed ideas from MobileNetV2 by applying a 1×1 regular convolution after the expansion convolution to expand the number of channels and using another 1×1 regular convolution to map the output back to the original number of channels.
  
  2. In addition, the authors adjusted the momentum hyperparameters of the BN and applied regularization to the normalization parameters of the BN layer to ensure that small statistical matches are not amplified by the BN.

  3. NVAE also used residual units in the encoder model, but instead of using inflated convolution, regular convolution was used.

  ![image](https://github.com/user-attachments/assets/a6e77aef-76b0-421a-a99e-6111049b286b)
   
### 4. Issues addressed 
  1. The main goal of NVAE is to generate high quality large images. To address this problem, NVAE employs a multiscale approach to capture long-range correlations and local dependencies at different levels.
  
  2. In addition, NVAE employs techniques such as inflated convolution and batch normalization to improve the expressiveness of the network and stabilize the training process.
     
## Experiments
  This paper focuses on the performance of the NVAE model on several image datasets, and several sets of comparative experiments are conducted to explore the effect of different components on the model performance.

First, in the **main quantitative results section**, the authors compare the performance of NVAE with some non-autoregressive streaming and variational self-encoder models and achieve better results. Specifically, NVAE reduces the BPD of IAF-VAE and BIVA from 2.98 to 2.91 on CIFAR-10, and its performance is even comparable to autoregressive models. 

In addition, the authors found that even without using the stream function, NVAE can compensate for the statistical challenges with a well-designed network structure and normally distributed encoders to achieve good performance.

Second, in the **qualitative results section**, the authors show that NVAE generates high quality and diverse samples, even at low temperatures. In addition, the authors propose a method to improve the quality and diversity of the generated samples by using single batch statistics during sampling instead of the default running average, and avoiding the problem of relying on other data points by rescaling the mean and standard deviation in the batch normalization layer.

Finally, in the **AB experimental section**, the authors conducted multiple sets of experiments to explore the effects of different components on NVAE performance. Specifically, they compared the effects of different types of normalization and activation functions, residual cells, and residual normal distributions, and observed that BN was more suitable for ELU than WN, while residual cells and deep convolution produced different effects at different locations in the network. 

In addition, the authors find that removing any of the components degrades the performance, while SR not only stabilizes the training, but also slightly improves the generative performance. Finally, the authors also show the reconstruction results and a posteriori collapse of the NVAE and explain the role of the KL balancing mechanism.

![image](https://github.com/user-attachments/assets/34fecb9c-bae8-46d6-9212-6bc0970510bf)

![image](https://github.com/user-attachments/assets/bd5739bf-fd00-45ec-8c49-36811067f893)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new deep convolutional variational autocoder (NVAE) with a deep generative model and a regular encoder model, and uses residual parameterization to improve the minimization of the KL term.
  
  2. By introducing a spectral regularization technique, the authors successfully stabilize the training process for very deep models.
  
  3. The authors also provide practical solutions to reduce the memory burden of the VAE, thus speeding up the training.
  
  4. The study achieves state-of-the-art results on public datasets such as MNIST, CIFAR-10, CelebA 64, and CelebA HQ-256, and provides a robust baseline for FFHQ-256.

### 2. Innovative points
  1. The paper proposes a new NN architecture design idea to meet the different needs of VAE, including preserving the information content of the input data, dealing with long-range correlations, and avoiding overfitting.
  
  2. The authors use depth-separated convolution as the generative model and use regular convolution as the encoder model, which allows the network to rapidly increase the receptive field without significantly increasing the number of parameters.
  
  3. The authors propose an approximate posterior distribution for residual parameterization to improve the minimization of the KL term and demonstrate that spectral regularization is important for stable training.
  
  4. The authors also provide practical solutions to reduce the memory burden of VAEs, such as using batch normalization and truncating the input data size.

### 3. Future Works
  1. The authors suggest the use of more complex normal streams for VAEs in order to further improve performance.
  
  2. The authors believe that more work is needed to investigate the role of batch normalization in VAE and how to better deal with bias in data collection.
  
  3. The authors suggest further research on automated architecture search for VAE to automate architecture design and improve performance.
  
  4. The authors believe that this research can be applied to the fields of content generation, computer graphics, data augmentation, semi-supervised learning, and representation learning to help reduce bias in generated content, produce more diverse output, and better represent minority groups. 
