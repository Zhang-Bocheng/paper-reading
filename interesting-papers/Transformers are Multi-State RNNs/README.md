# Transformers are Multi-State RNNs
[paper link](https://arxiv.org/pdf/2401.06104) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the connection between Transformer models and RNN models, and proposes a novel compression strategy, Token Omission Via Attention (TOVA), which effectively compresses without training the Transformer's key value cache.          |  Transformer        |

## Methodology

### 1. Abstract
Experimental results show that using the TOVA strategy achieves a similar performance to the full model, while compressing the cache size to 1/8 of the original one, thus improving the throughput by a factor of 4.8. These findings help alleviate one of the most vexing computational bottlenecks in large language models - the size of the key-value cache.

### 2. Method Description 
This paper proposes a new sequence modelling method, Multi-State Recurrent Neural Network (Multi-State RNN), and discuss how to apply this method to the Transformer model based on the self-attention mechanism. Specifically, they define a multi-state matrix Ht l, where each row represents a ‘state’, and each state can contain any amount of information. 

The number of multi-states is controlled by setting different functions g to achieve multi-state RNN with different capacities. In practice, when the multi-state reaches its capacity limit, it needs to be compressed to a specified size using a compression strategy. The authors propose the Token Omission Via Attention (TOVA) algorithm as an alternative to this compression strategy.

![image](https://github.com/user-attachments/assets/c36e9ac4-ae73-4f94-9e5e-071ef2fedd32)

### 3. Methodological improvements
Compared to traditional recurrent neural networks, multi-state recurrent neural networks have a larger memory capacity and can be flexibly controlled by tuning the function g. In addition, the TOVA algorithm is a training free compression strategy that can improve the efficiency of the model without changing the model structure.

### 4. Issues addressed 
Multi-state recurrent neural networks and the TOVA algorithm address the problem of long-term dependencies in natural language processing and improve the efficiency of Transformer models based on self-attention mechanisms. These approaches can help to better understand the behaviour of deep learning models and inform future research.

## Experiments
This paper focuses on a study in language model compression that explores how pre-trained Transformer LLMs can be made to approach the effect of unlimited state sizes by comparing different multi-state sizes and compression strategies. Specifically, the authors conducted the following three comparison experiments:

**Language Modelling Task:** the authors used four different compression strategies (Window, Window+4, H2O, and TOVA) to test three different sizes of pre-trained Transformer LLMs and compare their perplexity performance on the PG-19 dataset. The results show that the TOVA strategy performs the best, needing to use only up to a quarter of the original multi-state size to achieve similar results to the full model, while the other strategies require at least half of the multi-state size to achieve the same results.

**Long-Range Understanding Tasks:** The authors apply three instructively trained LLMs to two long-range understanding tasks (SQuALITY and QASPER) and compare their performance in these tasks. The results show that in the SQuALITY task, the TOVA strategy significantly outperforms all baseline strategies, and only needs to be used up to half of the multi-state size to achieve similar results as the full model. In the QASPER task, on the other hand, the TOVA strategy still performs well, but needs to use up to the full multi-state size to achieve similar results to the full model.

![image](https://github.com/user-attachments/assets/08be0b86-c30e-40cf-961c-6f4920b89b0b)

**Text generation task:** The authors used a pre-trained model based on LLAAMA-2 for the text generation task and compared the performance of the TOVA strategy and the full model in this task. The results show that the performance of the TOVA strategy gradually approaches that of the full model as the multi-state size increases, but at smaller multi-state sizes, the TOVA strategy performs slightly worse than the full model. 

![image](https://github.com/user-attachments/assets/d330ef67-76a9-41c7-939f-dc3930f43181)

## Conclusion

### 1. Advantages of the Thesis
The TOVA method is simple and easy to understand, requiring only the selection of tokens to be retained based on the attention score, and is comparable to the uncompressed model in many cases, while requiring the use of only 1/8 to 1/3 of the uncompressed model's In addition, TOVA can handle long inputs of up to 70K tokens.

### 2. Innovative points
TOVA is a token selection strategy based on an attentional mechanism that determines whether or not to keep tokens based on their importance. This approach is more pervasive and scalable than other existing methods as it does not require any a priori knowledge or manual tuning of parameters. In addition, TOVA is highly efficient and accurate and can significantly reduce memory footprint and increase throughput without degrading performance. 

### 3. Future Works
While TOVA performs well in tasks such as long text generation, it may encounter challenges in other tasks. Therefore, future directions for exploration include how to optimise TOVA for different tasks and languages and further improve its performance and efficiency. 
