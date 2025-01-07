# Direct Preference Optimization Using Sparse Feature-level Constraints
[paper link](https://arxiv.org/pdf/1709.04109) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a new method called Feature-level constrained Preference Optimization (FPO), which aims to simplify the process of aligning large language models with human preferences and ensure stability.          |  Large-scale Language Model (LLM)       |

## Methodology

### 1. Abstract
The method utilises a pre-trained sparse self-encoder and feature-level constraints for efficient and mandatory alignment. Experimental results show that FPO achieves an absolute win rate improvement of more than 5% on a benchmark dataset and has a lower computational cost compared to state-of-the-art baselines, making it a promising solution for efficient and controllable large-scale language model alignment.

### 2. Method Description 
This paper proposes the Feature-level Direct Preference Optimization (FPO) method, which optimises the Language Model (LM) by combining the advantages of SimPO and TDPO. Compared to existing methods, FPO has the following features:

  1. Introduces a length normalisation technique, which makes the reward difference calculation more stable.
  2. Using SParse Autoencoder (SAE) instead of KL divergence to control the diversity of model generation results.
  3. Avoiding the instability problem associated with the direct use of the reference model by calculating the results of the reference model offline.

![image](https://github.com/user-attachments/assets/4024256a-7c6b-4574-9216-e6073ba4e2be)

### 3. Methodological improvements
  1. The SimPO-based method introduces a length normalisation technique to make the reward variance calculation more stable.
  2. Use SParse Autoencoder (SAE) instead of KL divergence to control the diversity of model generation results.
  3. Avoid the instability problem caused by directly using the reference model by calculating the results of the reference model offline.
  4. Replacing the KL divergence constraint in the original TDPO algorithm with a feature-level constraint based on SAE to improve efficiency and reduce computational cost.

### 4. Issues addressed 
  1. **Stability:** there is an instability problem when using methods without reference models, such as SimPO and TDPO.
  2. **Diversity:** Existing methods mainly focus on the accuracy of the model without considering the diversity of the generated results.
  3. **Computational cost:** using KL divergence as a constraint increases the computational cost, especially when dealing with large-scale vocabularies.

The FPO method solves the above problems and improves the stability and efficiency of the method by introducing the length normalisation technique and SParse Autoencoder (SAE), as well as computing the results of the reference model offline.

## Experiments
This paper focuses on how Diversity-Promoting Objective (DPO) can be used to improve the diversity and quality of generated results in the task of dialogue generation for large-scale pre-trained language models, and compares it with a number of benchmark approaches.

Firstly, the authors select a range of models with different parameter sizes for testing, including Gemma-2-2B and Gemma-2-9B, etc., to ensure that the performance of the DPO approach can be evaluated under different model architectures. Also, to ensure transparency, the authors selected only the base models that were not subjected to supervised fine-tuning or alignment processes and fine-tuned them through a uniform format to create a baseline model.

Then, the authors used the UltraFeedback dataset to further align the base model with different alignment methods, such as TDPO series, SimPO, etc., and performed hyperparameter searches to determine the best hyperparameter configuration.

Finally, the authors compare the DPO method with other benchmark methods, including base methods, methods with explicit KL control and reference freedom. Evaluation metrics include length-controllable win rate, win rate, and score. The results show that the DPO method achieves better performance on several evaluation metrics relative to other benchmark methods, especially on the MT-Bench dataset.

![image](https://github.com/user-attachments/assets/562b598b-259a-4b4f-a721-ad73652cf89e)

In addition, the authors analysed the trade-off between diversity and quality of the DPO method and compared it with other strongly aligned benchmark methods. The results show that the DPO method can increase the diversity of the generated results while maintaining high quality, and performs better compared to other benchmark methods.  

## Conclusion

### 1. Advantages of the Thesis
  1. The method reduces the computational overhead required by traditional alignment methods such as DPO and TDPO by using sparse self-encoders and pre-computed offline references. Experimental results show that FPO achieves significant improvements in accuracy and diversity with low resource consumption.
  2. In addition, the authors provide detailed theoretical proofs and experimental details to ensure the reproducibility and transparency of the study.

### 2. Innovative points
  1. This approach does not require an additional reference model loading process and only minimises the I/O overhead to complete the training. In addition, due to the use of sparse activation values, the FPO only needs to process the activation values, thus reducing the computational overhead.
  2. Compared to existing reference-independent methods, FPO still needs to precompute the log-probability and SAE feature activations of the reference model, but this operation reduces peak computation and memory requirements, making the model easier to run on smaller devices. 

### 3. Future Works
  1. Future research directions may include ways to further optimise FPO, such as exploring more efficient feature extraction strategies or tuning constraint parameters for better performance.
  2. And, FPO can be combined with other reinforcement learning techniques to improve alignment and extend its application.
  3. Finally, with the development of hardware technology, larger scale language models as well as higher complexity tasks can be considered to validate the effectiveness of FPO in real-world application scenarios.    
