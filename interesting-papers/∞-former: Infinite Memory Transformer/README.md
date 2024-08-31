# ∞-former: Infinite Memory Transformer
[paper link](https://arxiv.org/pdf/2109.00301) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new model, the ∞-former, which can effectively deal with the problem of memorising long sequences.         |  Transformer         |

## Methodology

### 1. Abstract
The traditional transformer model requires an increase in computation as the length of the context grows, thus making it difficult to handle long-term memory effectively. To address this problem, the authors propose the ∞-former model and achieve attention to long-term memory by using a continuous space attention mechanism. This has the advantage that the attention complexity of the ∞-former is independent of the context length, but rather sacrifices precision for longer memory length. 

In order to control the trade-off between accuracy and memory length, ∞-former also introduces ‘sticky memory’, which allows the model to process context information of arbitrary length while maintaining a fixed computational budget. Experimental results show that ∞-former performs well in tasks such as sorting, language modeling, and document grounded dialogue generation, retaining information from long sequences.

### 2. Method Description 
The Infinite Memory Transformer (IMT) proposed in this paper is a NN model based on a continuous attention mechanism for processing text sequences of arbitrary length. The model achieves long-term dependency learning by converting the input sequence into a continuous signal and performing continuous attention computation on the signal. 

Specifically, the model contains an LTM (Long-Term Memory) and an STM (Short-Term Memory), where the LTM stores the input embedding or hidden states of past text sequences, while the STM consists of the hidden states of the current text sequence and is attended to by the continuous self-attention mechanism. In addition, the model uses a technique called ‘Sticky Memories’ to adjust the importance of each region in the LTM according to the distribution of attention in the previous step in order to improve the memory capacity of the model.

![image](https://github.com/user-attachments/assets/ddca4c98-5c80-4d0e-ba98-ca0a11f2abb0)

### 3. Methodological improvements
The main improvements of the Infinite Memory Transformer over the traditional Transformer model are the introduction of two memory structures, LTM and STM, as well as the continuous self-attention mechanism and the Sticky Memories technique. These improvements allow the model to better capture long-distance dependencies and have stronger memory capabilities. In addition, the model employs a convolutional layer as a gating mechanism to smooth the input sequences and reduce training difficulty.

### 4. Issues addressed 
The infinite memory Transformer proposed in this paper mainly addresses the difficulties of traditional Transformer models in dealing with long-distance dependencies. Since the self-attention mechanism in the traditional Transformer model is localised, it cannot capture dependencies across multiple time steps well. It effectively solves this problem by introducing two memory structures, LTM and STM, as well as the continuous self-attention mechanism and the Sticky Memories technique, which enables the model to better handle long-distance dependencies and has a stronger memory capability.

## Experiments
This paper describes four experiments designed to explore the validity and applicability of long-term memory models. These experiments include a sequencing task, language modelling, document-guided dialogue generation and an analysis of long-term memory.

First, in the sequencing task, the authors designed an input sequence based on a mixture of distributions and sequenced it using three different models (Transformer-XL, Compressive Transformer and ∞-Former). The results show that the infinite-length memory model outperforms the other two models when the length of the sequence increases, suggesting that it has better performance in handling long sequences.

Secondly, in the language modelling task, the authors applied the infinite-length memory model to the pre-trained language model GPT-2 and compared it with the compressed memory model. The results show that the infinite-length memory model improves the perplexity on both the Wikitext-103 and PG-19 datasets, whereas the compressed memory model shows only a slight improvement on the PG-19 dataset.

Third, in the document-guided dialogue generation task, the authors used the CMU Document Grounded Conversation dataset to evaluate the effectiveness of the long-term memory model. The authors compared the infinite-length memory model to a compressed memory model and to the GPT-2 without access to auxiliary documents. The results showed that both the Infinite Long Memory Model and the Compressed Memory Model were able to generate better responses and that the Infinite Long Memory Model achieved better scores on all of the assessment metrics.

Finally, in the analysis of long-term memory, the authors investigated the trade-off between memory accuracy and computational efficiency by varying the number of basis functions in the infinite-length memory model. The results show that as the number of basis functions increases, the regression error of the model reaches a plateau while the accuracy starts to decrease. This suggests that memory accuracy may decrease when increasing the efficiency of the model or expanding the size of the context it can handle.

![image](https://github.com/user-attachments/assets/c2c6457c-626e-44f0-99f4-85819535919e)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new Transformer model, ∞-Former, which is able to handle contexts of arbitrary length and maintain a fixed computational budget by introducing a continuous-space attention framework that makes its attentional complexity independent of the context length.
 
  2. The model also adopts the method of updating memory, which makes the model have ‘sticky memory’, i.e., it is forced to persist the relevant information in memory for a certain period of time. Experimental results show that ∞-Former scales to long sequences and maintains high accuracy in sequential synthesis tasks, and that ∞-Former shows several metrics of improvement after fine-tuning the pre-trained language model in tasks such as language modelling and document dialogue generation.
 
### 2. Innovative points
  1. The main contribution of this paper is the novel Transformer model ∞-Former, whose core idea is to use a continuous spatial attention framework to reduce the complexity of attention and to achieve ‘sticky memory’ by updating memory.
  
  2. This approach is of great significance in solving the computational limitation problem of the Transformer model when dealing with long contexts, and provides new ideas and methods for subsequent research.
      
### 3. Future Works
Future research can further explore how to optimise the design of the continuous spatial attention framework, and how to make better use of the ‘sticky memory’ mechanism to improve the model performance. In addition, ∞-Former can be applied to more complex tasks, such as machine translation and question-answer systems, to verify its effectiveness.
