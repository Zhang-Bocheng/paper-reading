# Improving fine-grained understanding in image-text pre-training
[paper link](https://arxiv.org/pdf/2401.09865) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method, called SPARC, for training more fine-grained multimodal representations of image-text pairs.          |  Reinforcement Learning        |

## Methodology

### 1. Abstract
The method exploits the fact that multiple image chunks typically correspond to a single word, and learns a set of image chunks by computing linguistically grouped visual embeddings for each token. These embeddings are used to compare linguistic and visual information, thus encoding both global and local information. Experimental results show that SPARC achieves better performance on both coarse-grained tasks (e.g., classification) and fine-grained tasks (e.g., retrieval, object detection, and segmentation) and improves the accuracy and descriptiveness of the model compared to competing approaches.

### 2. Method Description 
In this paper, a reinforcement learning algorithm called SPARC (Stochastic Policy-based Actor-Critic) is proposed for continuous action space problems. The algorithm combines the advantages of Actor-Critic and policy gradient-based reinforcement learning methods and introduces some new techniques to improve performance and stability.
Specifically, SPARC uses two neural networks: an Actor network and a Critic network.

The Actor network selects an action based on the current state and updates its parameters with a policy gradient to maximise the cumulative payoff. The Critic network estimates a value function for the current state and provides it to the Actor network as a reference.SPARC also uses a method known as a SPARC also uses a technique called ‘differential strategy’ to avoid overfitting during training, and a technique called ‘hierarchical strategy’ to increase exploratory behaviour.

### 3. Methodological improvements
  1. The use of differential strategies reduces oscillations and instability during training.
  2. The use of a hierarchical strategy increases the exploratory behaviour, leading to faster discovery of better strategies.
  3. SPARC can work efficiently in high-dimensional, continuous action spaces without discretising or limiting the range of actions.

### 4. Issues addressed 
In traditional value function-based reinforcement learning algorithms, it is often necessary to discretise the action space or use a finite state representation, which can limit the application of the algorithm. In contrast, SPARC can directly deal with continuous action spaces and thus can be applied to a wider range of problem domains. SPARC can also handle high-dimensional, nonlinear environments and can automatically adjust the action range and step size to better suit different task requirements.

## Experiments
This paper focuses on the performance of the SPARC model on tasks such as zero-shot image classification, cross-modal retrieval and fine-grained localisation, and compares it with baselines such as CLIP, MGCA, PACL, GLORIA and FILIP. The experimental results show that SPARC performs well on all the tasks, especially with better performance on fine-grained localisation tasks. In addition, this paper explores issues such as hyperparameter settings and training stability of SPARC models. Specifically, the paper includes the following experiments:

**Zero-shot image classification:** SPARC and other baselines are tested using ImageNet, ImageNet-V2, ImageNet-R, ImageNet-C and ImageNet-Sketch datasets. The results show that SPARC outperforms other methods on all datasets, especially on challenging datasets such as ImageNet-R and ImageNet-C.

![image](https://github.com/user-attachments/assets/8258d721-e417-4f76-859e-6a39dc3bb035)

![image](https://github.com/user-attachments/assets/016ca23b-e075-41ad-bd0d-20d0af1c6c5c)

**Cross-modal retrieval:** SPARC and other baselines are tested using datasets such as Flickr30k and MSCOCO. The results show that SPARC outperforms other methods on tasks such as zero-shot image text retrieval and cross-modal retrieval.

![image](https://github.com/user-attachments/assets/e04652f6-8a0e-4c97-ba22-9e29f441b514)

**Fine-grained localisation:** SPARC and other baselines are tested using datasets such as LVIS and Visual Genome. The results show that SPARC outperforms other methods on tasks such as object detection and semantic segmentation. 

![image](https://github.com/user-attachments/assets/0b705186-8cdf-40a4-b2f6-8bdad763c899)

## Conclusion

### 1. Advantages of the Thesis
  1. Improved performance on fine-grained tasks: SPARC performs better on finer-grained tasks than pre-trained models based on the image level.
  2. Exploits multimodal data: SPARC uses both image and text data for pre-training, allowing better use of information from multimodal data.
  3. Reduced computational cost: Since SPARC focuses only on statements that are relevant to the current image, unnecessary computational costs can be reduced.

### 2. Innovative points
  1. Comparison learning using sparse matrices: SPARC uses sparse matrices to represent the similarity between images and text, thus avoiding unnecessary computation.
  2. Considering different levels of information: SPARC learns both image-level and text-level information, which can better capture the relationship between them.
  3. Improved Attention Mechanism: SPARC introduces a hierarchical attention mechanism that allows the model to adaptively adjust the attention weights. 

### 3. Future Works
The SPARC model proposed in this paper provides a new idea for visual pre-training, but there are still some issues that need to be addressed. For example, how to further optimise the attention mechanism to improve the performance of the model; how to apply SPARC to other fields, such as natural language processing. These issues are worth further research and discussion.  
