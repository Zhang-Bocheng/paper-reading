# HyperTransformer: Model Generation for Supervised and Semi-Supervised Few-Shot Learning
[paper link](https://arxiv.org/pdf/2201.04182) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper presents a model called HyperTransformer for supervised and semi-supervised small sample learning tasks. The model is based on the Transformer architecture and generates Convolutional Neural Network (CNN) weights directly from support samples.         | Transformer          |

## Methodology

### 1. Abstract
   Since the task-specific dependencies of a small generated CNN model are encoded by the high-capacity Transformer model, authors effectively decouple the complexity of the large task space from the complexity of individual tasks. This approach is particularly effective for small-target CNN architectures, where learning a fixed, task-independent generic embedding is not optimal, and performance is better when task information is available to tune all model parameters. For larger models, we find that generating only the last layer is sufficient to produce competitive or better results than those obtained using state-of-the-art methods, and is end-to-end differentiable.
   
   ![image](https://github.com/user-attachments/assets/33978a77-1598-4c37-a2be-cf0dd21ade3c)

### 2. Method Description 
  The paper proposes a weight generation model (HyperTransformer) based on a self-attention mechanism for learning task-specific CNN layer weights. The core of the model uses the Transformer as a core component to process complex multimodal task descriptions and encode the information into unordered sets of Transformer tokens. During training, the parameters in the weight generation model are updated using stochastic gradient descent by optimizing the cross-entropy loss function.

  ![image](https://github.com/user-attachments/assets/64691824-8ccf-4928-9492-c14eeeb9e972)
  
### 3. Methodological improvements
  The method has the following advantages over traditional weight generation methods based on CNNs:

  1. **Flexibility**: due to the use of the self-attention mechanism, the method can handle arbitrarily complex task descriptions without the need to manually design a specific architecture.
  
  2. **Learning capability**: the method is able to learn valid weights from a small number of samples, making it suitable for small sample learning problems.
  
  3. **Scalability**: the method can be extended by adding more layers or adjusting hyperparameters, etc. to adapt to different task requirements.
     
### 4. Issues addressed 
  The method addresses some of the limitations of traditional convolutional neural network weight generation methods, such as the need to manually design specific architectures and the inability to handle complex multimodal task descriptions. At the same time, the method is also suitable for small sample learning problems and can achieve better performance on limited datasets.
  
## Experiments
  This paper presents the performance and findings of HYPERTRANSFORMER (HT) in several experiments. 
  
  First, experiments were conducted on the OMNIGLOT, MINI-IMAGENET, and TIEREDIMAGENET datasets and compared with MAML++ and RFS. The experimental results show that generating the logits layer of a CNN using a simple self-attentive mechanism can be a simple learning algorithm for a small number of samples. In these experiments, the HT model generates only the final fully-connected logits layer of the CNN and gives better results than MAML++ and RFS in all tasks, especially for smaller models. However, as the size of the generated CNN increases, the performance of HT gradually approaches that of MAML++ and RFS. 
  
  In addition, the authors conducted experiments on Semi-Supervised Results to solve the semi-supervised problem by adding unlabeled data to the support set. The experimental results show that adding unlabeled data significantly improves test accuracy and that the model achieves optimal performance when the encoder has at least two layers. Finally, the authors also explore whether it is necessary to generate more CNN layers for better performance and find that generating more CNN layers does improve performance in some cases.
  
  ![image](https://github.com/user-attachments/assets/0571fdeb-6783-4803-ba2f-44c4f818336c)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper propose a new Transformer model-based few-shot learning method that achieves the goal of decoupling task space complexity from individual task complexity by using the Transformer model to generate all weights of the CNN model. 
  
  2. The method achieves comparable or better performance than current state-of-the-art methods on multiple benchmark datasets and can be further improved by adding unlabeled samples.
  
  3. In addition, the method has an end-to-end learning approach that does not require complex nested gradient optimization and other meta-learning methods.
  
### 2. Innovative points
   The method utilizes the Transformer model's self-attention mechanism, allowing it to handle varying numbers of sample classes and to encode complexity in the training data. In addition, the method can be extended to support unlabeled data and can significantly improve performance in small-sized CNN models.
   
### 3. Future Works
  1. When dealing with more complex tasks, a larger Transformer model capacity may be required, which may lead to an increase in computational cost.
  
  2. In addition, the method needs more experiments to verify its applicability and robustness in other domains.
  
  3. how to better utilize the Transformer model's multi-head self-attention mechanism to improve performance, and how to apply it to larger-scale tasks.

