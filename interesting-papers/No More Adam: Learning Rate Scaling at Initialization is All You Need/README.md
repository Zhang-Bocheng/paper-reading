# No More Adam: Learning Rate Scaling at Initialization is All You Need
[paper link](https://arxiv.org/pdf/2412.11768) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This thesis presents a simple but effective optimisation method called SGD-SaI for training deep neural networks. The method scales the learning rate of different sets of parameters at initialisation and adjusts them according to their respective gradient signal-to-noise ratios (g-SNR).         | Deep Neural Networks (DNN)        |

## Methodology

### 1. Abstract
Compared to AdamW, which uses adaptive second-order momentum, SGD-SaI does not need to rely on adaptive second-order momentum to adjust the learning rate, thus avoiding the problem of training imbalance and reducing the optimiser's memory usage by half. Experimental results show that SGD-SaI performs well in a variety of tasks, including image classification and language model pre-training, with high robustness and practicality. In addition, SGD-SaI achieves significant memory savings, resulting in a 5.93GB and 25.15GB reduction in memory usage for the optimiser state, relative to AdamW in the full-precision training setting.

### 2. Method Description 
The SGD-SaI proposed in this paper is a new optimisation algorithm that removes the adaptive gradient component by calculating the learning rate scaling factor in the initial batch using g-SNR. The algorithm can capture the intrinsic gradient characteristics of different parameter blocks without introducing dynamic terms and is computationally efficient as it adds only a small amount of extra computation during training.

![image](https://github.com/user-attachments/assets/a8cecdf8-2708-4efd-9835-d4ce597e2250)

![image](https://github.com/user-attachments/assets/fc66055e-ee74-46a2-a467-9e7e21074bd3)

### 3. Methodological improvements
  1. A learning rate scaling factor is calculated for each parameter block using g-SNR to reflect its true sparsity and noise characteristics.
  2. A decoupled weight decay method is used to apply regularisation directly to the parameters rather than incorporating them into the gradient computation to ensure that gradient statistics are accurately computed without affecting the gradient computation.
  3. Computational efficiency is maintained by adding only the extra computational effort required to compute the g-SNR during training.

### 4. Issues addressed 
The SGD-SaI method proposed in this paper addresses two problems that exist in traditional SGD methods: (1) performance degradation due to differences in gradient sizes between different parameter blocks, and (2) the adaptive gradient component may lead to instability or overfitting problems. By using g-SNR to compute the learning rate scaling factor and adopting the decoupled weight decay method, SGD-SaI can effectively deal with these problems and improve the training of the model.

## Experiments
This paper focuses on the results of experiments comparing the use of the SGD-SaI optimiser with a conventional optimiser on different tasks. Specifically, it includes experiments in the following areas:

In **a large language model pre-training task**, the authors compare SGD-SaI with other common optimisers (e.g., SGDM, Adam, AdamW, and Prodigy) and analyse their performance under different hyperparameter settings. The experimental results show that SGD-SaI performs well in terms of both memory efficiency and convergence speed, and is especially advantageous when dealing with long sequences.

![image](https://github.com/user-attachments/assets/87116879-d3e7-43cd-a6af-34674d7c51c5)

In **the vision task**, the authors pre-trained the ViT model and compared the performance of SGD-SaI with other common optimisers such as SGDM, Adam, AdamW and Prodigy. The experimental results show that SGD-SaI is more stable than the other optimisers and maintains high accuracy with different hyperparameter settings.

![image](https://github.com/user-attachments/assets/b8beba4f-cd8e-40e4-b397-7478495c0a00)

In **the PEFT task**, the authors applied SGD-SaI to the fine-tuning task of LLM and Diffusion Model and compared it with other optimisers such as _scaled-SGD and _scaled-AdamW. The experimental results show that SGD-SaI outperforms the previous methods in the LoRA fine-tuning task and also achieves better results in the Diffusion Model fine-tuning task.

![image](https://github.com/user-attachments/assets/7feaa658-b9de-408f-b62b-f326e2346fb4)

In **the CNN task**, the authors evaluated the ResNet-18 model and compared it with other optimisers such as SGD and Adam family. The experimental results show that SGD-SaI performs well in terms of stability and achieves higher accuracy with multiple search spaces and hyperparameter settings.  

![image](https://github.com/user-attachments/assets/4296d05c-1469-430a-b09f-cdfbfaeb9b3b)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new optimisation method, SGD-SaI, which balances the learning progress of different parameters by using g-SNR to adjust the learning rate, thus achieving efficient training without increasing memory and computational burden.
  2. The researcher reveals the relationship between g-SNR and model performance through statistical analysis of g-SNR, and proposes a corresponding theoretical framework for subsequent research.
  3. The paper also conducts extensive experimental validation, including comparing the effectiveness of SGD-SaI with other optimisers on multiple tasks, proving its superiority and universality.

### 2. Innovative points
  1. An adaptive learning rate scaling method based on g-SNR is proposed, which can effectively reduce memory and computational burden and improve training efficiency.
  2. The metric of g-SNR is utilised to measure the difference in the gradient distribution of different parameters and thus balance the learning progress of different parameters, which has certain theoretical basis and practical significance.
  3. Experimental results on several tasks show that SGD-SaI performs better than other optimisers, indicating that the method has strong practical value. 

### 3. Future Works
  1. It is possible to further explore how g-SNR can be applied to more types of neural network structures and how it can be combined with other technical tools (e.g., dynamic learning rate) to further improve the training effect.
  2. Attempts can be made to apply g-SNR to areas such as hyperparameter tuning to improve the generalisation ability and stability of deep learning models.
  3. The relationship between g-SNR and other metrics can be further explored to better understand the complex phenomena in the gradient propagation and learning process.  

