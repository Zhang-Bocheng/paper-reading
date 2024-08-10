# Pretrained Transformers as Universal Computation Engines
[paper link](https://arxiv.org/pdf/2103.05247) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the generalization ability of using a pretrained transformer model on different modal tasks, and finds that pretraining on natural language tasks improves performance and computational efficiency on non-linguistic downstream tasks.         | Transformer          |

## Methodology

### 1. Abstract
The authors refer to this model as the "Frozen Pretrained Transformer" and experimentally analyze it, showing that it can perform well on tasks such as numerical computation, vision, and protein folding prediction. In addition, the authors compare the performance of a randomly initialized transformer with that of an LSTM and combine the two insights to conclude that a transformer model pre-trained in natural language can achieve strong performance in a wide range of non-linguistic tasks.

![image](https://github.com/user-attachments/assets/e3dad978-4728-46c1-a1a5-7d68cbe80c6f)

### 2. Method Description 
The study used the GPT-2 model and fine-tuned it on different tasks to evaluate its cross-modal computational capabilities. Specifically, they considered the following tasks:

  **Bit Memory**: given five binary strings of length 1000 bits, and then randomly replacing some positions of one of the strings with either 0 or 1, allowing the model to predict the original string.
  
  **Bit XOR**: Given two binary strings of length 5, let the model predict the result of their dissimilarity.
  
  **ListOps**: Given a mathematical expression, let the model predict the final result number.
  
  **MNIST**: given a picture of a handwritten number, have the model categorize it.
  
  **CIFAR-10**: given a picture, let the model classify it.
  
  **CIFAR-10 LRA**: This is a variant of CIFAR-10, where the picture is converted to a grayscale image and expanded into a one-dimensional vector, allowing the model to learn longer sequence patterns.
  
  **Remote Homology Detection**: Given a protein amino acid sequence, let the model predict its folding type.

![image](https://github.com/user-attachments/assets/dcfe6aa2-9164-47f7-ab73-c23a169c4068)

### 3. Methodological improvements
  1. To better assess the model's cross-modal computational ability, the researchers used a fine-tuning approach to the GPT-2 model on each task.
  
  2. In addition, they considered some specific architectural adjustments in each task, such as reinitializing the input layer and freezing the self-attentive connections.

### 4. Issues addressed 
The aim of this study is to investigate whether pre-trained language models have generalized computational capabilities, i.e., whether they can be fine-tuned to learn representations of different domains. Through experiments on multiple tasks, the researchers found that the pre-trained language model can indeed adapt well to new domains and can be fine-tuned for cross-modal computation. This suggests that pre-trained language models may be a powerful tool that can play an important role in a variety of tasks.

## Experiments
This paper focuses on how to migrate pre-trained natural language models to tasks in other modalities, and conducts a number of comparative experiments to verify the effects and influences of migration. Specifically, the paper describes the following aspects of the experiments:

**Effectiveness of cross-modal migration**: the authors compare the performance of models using different pre-training methods (random initialization, bit-memory-based pre-training, image-based pre-training) on different tasks, and find that the natural language-based pre-training method is the most effective.

**Impact of model architecture on migration**: the authors compare the performance of different model architectures (random LSTM and pre-trained GPT-2) using the same pre-training method on different tasks and find that pre-trained GPT-2 performs better on all tasks.

**Effect of initialization method on migration**: the authors compare the performance of different initialization methods (direct replication of parameters, initialization using pre-trained mean-variance) using pre-trained GPT-2 on different tasks and find that direct replication of parameters makes better use of pre-trained knowledge.

**The effect of training method on migration**: the authors compare the performance of two different training methods, fine-tuning only the output layer and fine-tuning both the output and input layers, on different tasks, and find that fine-tuning both the output and input layers results in better performance.

**Impact of model depth on migration**: the authors compare the performance of pre-trained models using different depths on different tasks and find that shallower models can also effectively utilize pre-trained knowledge. 

![image](https://github.com/user-attachments/assets/7d7cb52c-22c3-4e2f-8f6d-ce5cca645bd3)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new approach to solving non-verbal modal tasks using pre-trained language models and demonstrates the effectiveness of this approach through extensive empirical evaluations.
  
  2. The authors find that these models can achieve performance comparable to transformer models trained entirely on downstream tasks without fine-tuning the self-attention and feed-forward layers, thanks in large part to their reliance on frozen language model parameters for most of the computation.
  
  3. In addition, this research provides a basis for future cross-modal transfer and suggests other data-rich modalities (e.g., vision) or a mix of multiple domains for use in providing the necessary pre-training of a general-purpose computational engine.

### 2. Innovative points
  1. The authors use a pre-trained language model, GPT-2, and fine-tune only its input and output layers as well as its positional encoding and layer normalization parameters to achieve efficient cross-modal transfer.
  
  2. In addition, the authors also delved into the sources of performance of the FPT model by experimenting with different components.

### 3. Future Works
  1. In the future, the authors would like to explore other data-rich modalities (e.g., vision) or a mixture of multiple domains to provide a basis for better pre-trained general-purpose computational engines.
  
  2. And, the authors also believe that further research is needed on how to mitigate bias issues in cross-modal transfer and how to better utilize representative datasets to improve model performance.  
