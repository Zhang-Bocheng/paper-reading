# Autoregressive Diffusion Models
[paper link](https://arxiv.org/pdf/2110.02037) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new model, Autoregressive Diffusion Models (ARDMs), which can be viewed as a generalization of the previously proposed order-independent autoregressive and absorbing discrete diffusion models         | Diffusion Models          |

## Methodology

### 1. Abstract
  Compared to traditional autoregressive models, ARDMs do not require causal masking of the model representation and can be trained with efficient objective functions similar to modern probabilistic diffusion models for high-dimensional data. When tested, ARDMs support parallel generation and can be tuned to a given generation budget. Experimental results show that ARDMs require fewer steps to achieve the same level of performance relative to discrete diffusion models. In addition, the authors applied ARDMs for lossless compression and achieved better results than existing bitwise back propagation based coding methods. Overall, ARDMs is a simple to implement, easy to train, and scalable model with a wide range of applications.
  
### 2. Method Description 
  The main improvement of ARDMs over traditional ARMs is their ability to generate data in any order, rather than only sequentially. This flexibility makes ARDMs more suitable for real-world applications where nonlinear sequences need to be generated. In addition, ARDMs employ deep upscaling techniques, which can further improve the performance of the model by processing the data in stages.
  
### 3. Key concepts
  _Autoregressive models_: A class of statistical models used for analyzing and predicting time series data. The key characteristic of autoregressive (AR) models is that they predict future values based on past values of the same series. These models assume that the current value of the series can be explained by a linear combination of its previous values plus a random error term.
  
### 4. Methodological improvements
  The main improvement of ARDMs over traditional ARMs is their ability to generate data in any order, rather than only sequentially. This flexibility makes ARDMs more suitable for real-world applications where nonlinear sequences need to be generated. In addition, ARDMs employ deep upscaling techniques, which can further improve the performance of the model by processing the data in stages.
  
### 5. Issues addressed 
  Traditional ARMs are unable to generate data of arbitrary order, which limits their applicability in practical applications. ARDMs solve this problem by adopting an order agnostic approach to training, and also introduce a deep upscaling technique to further improve the performance of the model. Therefore, ARDMs are important for applications that require the generation of nonlinear sequences.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a66990a8-658e-4b79-9695-5395fda483ee)

## Experiments
  This paper focuses on the performance of a stochastic generative model (ARDM) based on an inverse absorption-diffusion process on different tasks and compares it with other related methods. Specifically, the paper includes the following three comparison experiments:

  The first experiment compares ARDM with D3PM and other variants to evaluate their performance in character modeling tasks. The authors used the Text 8 dataset with the same neural network architecture and hyperparameter settings. The results show that OA-ARDM and D3PM-absorbing have similar performance when only a quarter step is required, while the other methods perform poorly.

  The second experiment compares the performance of ARDM with other existing methods in a CIFAR-10 image compression task. The authors used the range encoder rANS for lossless compression and avoided the problem of sample imbalance by choosing the optimal order of randomization. The results show that ARDM outperforms all other methods for individual image compression and maintains better performance with fewer steps.

  The third experiment compares the effect of standard order-agnostic modeling and order-agnostic bit-upscaling, and explores the effect of the upscaling factor on the model performance. The authors trained several ARDM models for image and audio data generation and tested the performance under different upscaling factors. The results show that in some cases, smaller upscaling factors may lead to performance degradation, which may be caused by insufficient gradient signaling of the model.

  Overall, this paper demonstrates the superior performance of ARDM on different tasks and provides a valuable reference for research in this area.
  
## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new model, AR (Autoregressive) DM (Discrete Diffusion Model), which has high performance in the field of image compression.

  2. By combining the traditional diffusion process with the autoregressive process, the model is able to better capture the structural information in the data and can effectively optimize the parameters during the training process.

  3. The authors also provide detailed experimental results and comparative analysis to demonstrate the advantages of the model over other existing models.
     
### 2. Innovative points
  1. The ARDM model proposed in this article is a novel hybrid model that combines the advantages of autoregressive and diffusion models to more accurately model the data distribution.

  2. The authors used parallel computing to accelerate the training process, and also used efficient algorithms in the sampling phase to make the model more practical in real-world applications.
     
### 3. Future Works
  1. This research provides a new idea for further development in the field of image compression, and more hybrid models as well as different optimization methods can be explored.

  2. The model can be considered to be applied to other fields, such as NLP, to improve the generalization ability of the model.

  3. In the future, it can also be further explored how to improve the model using deep learning techniques to achieve better performance.

