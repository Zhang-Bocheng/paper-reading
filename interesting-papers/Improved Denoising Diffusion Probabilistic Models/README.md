# Improved Denoising Diffusion Probabilistic Models
[paper link](https://arxiv.org/pdf/2102.09672) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 |This paper describes a generative model called Improved Denoising Diffusion Probabilistic Models (IDDPM) and demonstrates its excellent performance in terms of sample quality and ability to cover the target distribution.          |  Diffusion         |

## Methodology

### 1. Abstract
   A simple modification by the authors allows the model to achieve both competitive log-likelihood and high quality sample generation. In addition, learning the standard deviation of the backpropagation process reduces the number of forward passes required for sampling by an order of magnitude with virtually no difference in sample quality, which is important for the practical deployment of these models. Finally, the authors also found that the sample quality and log-likelihood of the model grow smoothly with model capacity and training computation, making it easily scalable.
   
### 2. Method Description 
  The paper proposes Denoising Diffusion Probabilistic Models (DDPM), a generative model based on the diffusion process. The model gradually destroys the data distribution by adding Gaussian noise at time steps and reconstructs the samples using a reverse diffusion process. Specifically, the DDPM defines a noise-free process **q(xt|xt+1)** and parameterizes its inverse process **pθ(xt|xt+1)** using a NN. These processes are then used to compute an objective function Lvlb that minimizes the difference between the model and the real data distribution.The key challenge in DDPM is how to efficiently sample noises at arbitrary time steps and evaluate their impact. 

### 3. Methodological improvements
 To further improve the performance of the DDPM, the paper proposes the following improvements:

  1. **Using a reweighted objective function**: this objective function improves the sample quality of the model by adjusting the weights to balance the loss contribution at each time step.
  
  2. **Learning the noise scale**: by learning the noise scale instead of fixing it, one can better control the behavior of the model and improve the sample quality and negative log-likelihood.
  
  3. **Improved noise scheduling**: Use a cosine noise scheduler instead of a linear scheduler to smooth out noise variations and retain more information.
  
  4. **Gradient Noise Reduction**: Reducing gradient noise through significant sampling techniques makes optimization more stable and reliable.
     
  ![image](https://github.com/user-attachments/assets/b03af928-94b4-4de2-9851-249a90176e01)

  ![image](https://github.com/user-attachments/assets/79218f01-faf2-435f-ad3f-2ff9b18fb880)

### 4. Issues addressed 
  1. The main advantage of DDPM is its efficiency and flexibility. It can handle a variety of different types of data, including images, text, and audio.
  
  2. In addition, DDPM is scalable and can be adapted to different task requirements by increasing the time step or modifying the noise scheduler.
  
  3. So, DDPM provides a powerful tool for generative modeling research and can be used in a variety of application areas, such as computer vision, natural language processing, and speech recognition.

![image](https://github.com/user-attachments/assets/7fc21583-e721-4651-8436-98a39dedb366)

## Experiments
  This paper focuses on the comparative experiments conducted by the authors in their study of diffusion modeling. Specifically, they conducted experiments in the following four areas:

For the ImageNet 64x64 and CIFAR-10 datasets, the authors compare the performance difference between their model and the traditional convolution-based model as well as the model with full transformer architecture, and find that their model is competitive in terms of Log-likelihood.

On ImageNet 64x64, the authors test the sample quality of their model using different sampling steps and find that using fewer sampling steps improves the efficiency of the model for the same training steps.

The authors also compared their performance with other Generative Adversarial Networks (GANs), measured by metrics such as computational precision and recall. The results show that while GANs perform better in terms of FID, they are inferior to diffusion models in terms of covering distributional patterns.

Finally, the authors explored how the performance of the diffusion model changes as the training time increases. They find that FID improves as a power law relative to the theoretical amount of training, while NLL does not quite follow this trend.

![image](https://github.com/user-attachments/assets/9b15d962-2a38-4722-8b3b-8de1ed188b99)

## Conclusion

### 1. Advantages of the Thesis
  1. First, the authors demonstrate that the Variational Lower Bound (VLB) can be more tightly optimized for better negative log-likelihood values by learning the inverse process variance and using a hybrid learning objective.
  
  2. Additionally, the authors found that directly optimizing the negative log-likelihood value when using a hybrid learning objective leads to more gradient noise, whereas a simple resampling technique can reduce this noise and achieve better negative log-likelihood values.
  
  3. What is more, by incorporating the inverse process variance into the model the authors find that fewer steps can be sampled from the model with little change in sample quality. This greatly improves the sampling speed of the model and makes it more suitable for practical applications.
  
  4. Finally, the authors compare the performance of the DDPM with the GAN in terms of distribution coverage and find that the DDPM has a higher recall, suggesting that it can better cover the target distribution.

![image](https://github.com/user-attachments/assets/e32c920a-527f-49d0-a8ba-e240bb88ded1)

### 2. Innovative points
  1. The authors optimize the VLB more tightly by learning the reverse process variance and using a hybrid learning objective to obtain better negative log-likelihood values.
  
  2. In addition, the authors incorporate the reverse process variance into the model, making it possible to sample fewer steps from the model with little change in sample quality.

![image](https://github.com/user-attachments/assets/a95ff835-e8e8-4f2f-a102-6321a151c59d)

### 3. Future Works
  1. Future research directions may include aspects such as improving the distribution coverage capability of DDPM and extending it to higher dimensional datasets.
  
  2. With the trend of machine learning models consuming more computational resources in the future, there is a need for further research on how to effectively use DDPM on larger scale models and training data.
