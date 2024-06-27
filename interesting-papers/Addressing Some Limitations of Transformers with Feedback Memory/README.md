# Addressing Some Limitations of Transformers with Feedback Memory
[paper link](https://arxiv.org/pdf/2002.09402) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 |  This paper explores the limitations of the Transformer model when dealing with sequential data and proposes Feedback Transformer to address these issues.        | Transformer          |

## Methodology

### 1. Abstract
  The traditional Transformer model, while capable of processing each element of the input sequence in parallel, is unable to fully utilize the sequential nature of the sequence data, resulting in information loss. Feedback Transformer, on the other hand, improves the representation capability of the model by exposing all previous representations to all future representations, allowing the lowest representation at the current time step to be computed by utilizing the highest level of abstract representation in the past. 
  
### 2. Key concepts
  _Feedback memory_: It introduces a mechanism for retaining and utilizing information from previous layers or iterations, effectively allowing the model to maintain a dynamic memory of past inputs and states.

## Experiments
  The first experiment compares Transformer with other models based on Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN). In this experiment, the authors tested the performance of different models on different datasets using a sentiment analysis task as an evaluation metric. The results show that Transformer has better performance relative to the other models, and especially excels in long text processing.

  The second experiment compares different variants of Transformer, including the standard Transformer, Relative Positional Encoding (RPC) and Multi-Head Attention (MHA). In this experiment, the authors tested the performance of these variants on the WMT14 English-German dataset using a machine translation task as an evaluation metric. The results show that the inclusion of relative position encoding and Multi-Head Self Attention can further improve the performance of the model relative to the standard Transformer.

### Results of Experiments 
  Experimental results show that the model using the feedback transformer performs better than the traditional Transformer model in tasks such as language modeling, machine translation, and reinforcement learning, and requires fewer number of parameters and deeper network structure.
  
## Conclusion
### 1. Advantages of the Thesis
  1. This paper proposes a new Transformer architecture-Feedback Transformer, to address two major limitations of the Transformer model when dealing with sequential data by modifying the self-attention mechanism: limited access to long-term memory and the maintenance of internal state insufficient capacity.
     
  2. Compared to the standard Transformer, Feedback Transformer is better able to handle long sequences and achieve better performance at shallower layers.
### 2. Innovative points
  1. The core idea of this paper is to expose all past computations to future computations, thus improving the model's ability to memorize and update.
     
  2. This design not only solves the problem of the Transformer model when dealing with long sequences, but also better maintains the internal state and improves the generalization ability of the model.
     
### 3. Future Works
  1. For different task types (e.g., machine translation, speech recognition, etc.), the best practices of Feedback Transformer need to be further investigated.

  2. How Feedback Transformer can be combined with other deep learning techniques (e.g., reinforcement learning) can be explored to improve the performance of the model.

  3. Consideration could be given to how Feedback Transformer could be extended to other types of neural network structures, such as convolutional neural networks or recurrent neural networks.

  4. Further investigate the theoretical properties of Feedback Transformer, such as its trainability and convergence speed, among other aspects.

