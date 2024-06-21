# Attention Is All You Need
[paper link](https://arxiv.org/abs/1706.03762) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |   A new neural network architecture, Transformer, which is based entirely on attentional mechanisms and does not require recursive or convolutional operations       |   self-attention mechanism        |

## Methodology
### 1. Abstract 
  This paper introduces a new neural network architecture, Transformer, which is based entirely on the attention mechanism and does not require recursive or convolutional operations. Experiments show that this model outperforms the best available results in machine translation tasks with shorter training time and better parallelization. The authors have also successfully applied Transformer on other tasks such as English syntactic analysis.
  
### 2. Method Description
  The paper proposes a neural machine translation model based on a self-attention mechanism called Transformer. This model consists of an encoder and a decoder, where each layer contains a multi-headed self-attention sublayer, a fully connected feed-forward network, and a position embedding. 
  
  In the self-attention sublayer, each position can attend to the information of all other positions, thus enabling the model to utilize the information of the entire input sequence to predict the output sequence. 
  
  In addition, the model uses a word embedding layer with shared weights and a linear transformation layer, and employs positional embedding techniques to deal with changes in sequence length.

### 3. Key concepts
  **Self-Attention**: Self-attention is a mechanism which particularly in the field of natural language processing (NLP), that allows a model to focus on different parts of an input sequence when producing a representation for a specific part of that sequence.

  **Multi-head Attention**: Multi-head attention is an extension of the self-attention mechanism which enhances the model's ability to focus on different parts of the input sequence in parallel and capture more nuanced dependencies between elements.
  
### 4. Methodological improvements 
  1. Unlike traditional recurrent neural networks and convolutional neural networks, the Transformer model does not rely on sequence length constraints, and thus can handle input sequences of arbitrary length.
    
  2. The model employs a multi-head self-attention mechanism, which can capture the relevant information in the input sequence in different dimensions, thus improving the performance of the model.
     
  3. The model also uses a positional embedding technique to handle variations in sequence length, which allows the model to show better performance on long sequences.

### 5. Issues addressed
  Traditional recurrent neural networks and convolutional neural networks have limitations in processing long sequences because they need to take into account all the previous positional information, which leads to increased computation and difficulty in parallelization. 
  
  The Transformer model avoids this problem by introducing the self-attention mechanism and positional embedding technique, which allows for better processing of long sequences. What is more, the model has better interpretability and high training efficiency, making it an excellent neural machine translation model.
  
## Experiments
  This paper focuses on the performance of the Transformer model proposed by Google on two tasks, machine translation and English syntactic analysis, and conducts several sets of comparison experiments to verify its superior performance.

  For machine translation, the authors used two datasets, WMT 2014 English-German Translation and English-French Translation, to test the performance of the Transformer model. The experimental results show that on both tasks, the Transformer model achieves better results than all previous single models, and the training cost is much lower than the previous optimal model. Specifically, for the English-German translation task, the BLEU score of the big model is 28.4, which exceeds that of all previous single models, and the training time is only 3.5 days, which is only one-fourth of the training cost of other competing models. For the English-French translation task, the BLEU score of the BIG model is 41.0, which also outperforms all previous single models, and the training cost is only one-fourth of the previous optimal model.

  In machine translation, the authors also conducted several sets of variant experiments, including changing parameters such as the number of attentional heads and the dimensionality of attentional keys, as well as changing positional encoding to learned positional embedding, among other operations. The experimental results show that too many attentional heads lead to quality degradation, while too small an attentional key value dimension reduces the model quality. Meanwhile, increasing the model size and adding dropout are able to improve the model performance. Finally, the authors found that the Transformer model has better generalization ability on machine translation tasks compared to the RNN sequence-to-sequence model.

  In addition, the authors conducted experiments on the performance of the Transformer model on the English syntactic analysis task.  Specifically, when using only the Wall Street Journal portion of the dataset, the Transformer model achieved an F1 score of 93.5, outperforming all previous models. And in the case of semi-supervised learning, i.e., when trained with a larger corpus, the Transformer model's F1 score is 93.7, only slightly lower than the best previous model.

## Conclusion
### 1. Advantages of the Thesis
  The paper proposes a new sequence transformation model, Transformer, which is based entirely on the attention mechanism and replaces the recursive layers commonly used in encoder-decoder architectures. Compared to architectures that use recursive or convolutional layers, Transformer can be trained faster on translation tasks and achieves new best results on the WMT 2014 English to German and WMT 2014 English to French translation tasks. 
  
### 2. Innovative points
  The main contribution of the paper is the proposal of the Transformer model, a sequence transformation model based entirely on attentional mechanisms. Conventional RNN typically decompose computations along symbol positions in the input and output sequences, and this sequential nature makes it impossible to parallelize computations within the training examples. Instead, Transformer avoids this problem by relying exclusively on the attention mechanism to establish global dependencies. The advantage of this approach is that it allows for higher parallelization and a new level of optimal quality can be achieved in only 12 hours.

### 3. Future Works
  1. The paper provides new ideas for applications of attention mechanisms that can be applied to problems in other domains, such as images, audio and video.
  2. The authors plan to study locally constrained attention mechanisms to handle large inputs and outputs more efficiently. These research results are expected to advance the development of sequence transformation models and improve their performance and efficiency.


