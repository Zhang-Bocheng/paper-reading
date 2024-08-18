# Synthesizer: Rethinking Self-Attention for Transformer Models
[paper link](https://arxiv.org/pdf/2005.00743.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the importance of the dot product attention mechanism in the Transformer model and proposes SYNTHESIZER as a new model.          | Transformer          |

## Methodology

### 1. Abstract
Through extensive experiments, the authors find that randomized alignment matrices perform very well in terms of performance, while learning self-attention weights is not so important. The authors further compare the performance of SYNTHESIZER with other models such as Dynamic Convolution and Linformer, and show that SYNTHESIZER is not only faster, but also performs better on coding tasks. These findings provide new ideas for improving the Transformer model.

### 2. Method Description 
The SYNTHESIZER model is a new synthesizer model proposed based on the Transformer model. The core idea of this model is to use our proposed Synthetic Attention module in the self-attention module instead of the original self-attention module. In addition, the model combines the advantages of Dense Synthesizers and Random Synthesizers and achieves good results in experiments.

![image](https://github.com/user-attachments/assets/840264f7-ac04-4040-954f-9a1131109801)

### 3. Methodological improvements
  1. Compared with the traditional Transformer model, the SYNTHESIZER model employs a new Synthetic Attention module, which can better handle long-distance dependencies in sequences, thus improving the performance of the model.
  
  2. The model also combines the advantages of Dense Synthesizers and Random Synthesizers, making the model more flexible and adaptable to different task requirements.
     
### 4. Issues addressed 
The main purpose of the SYNTHESIZER model is to improve the effectiveness and performance of synthesizer models. Traditional synthesizer models often have problems such as long distance dependencies that are difficult to capture and insufficient datasets, while the SYNTHESIZER model successfully solves these problems by introducing the new Synthetic Attention module and combining the advantages of Dense Synthesizers and Random Synthesizers, making the model to perform better in different fields of application.

## Experiments
This paper describes three variants of the Synthesizer model: the Dense Synthesizer, the Random Synthesizer, and the Factorized Synthesizers, and compares their effects experimentally. Specifically, the authors conducted the following experiments:

**Comparison of Dense Synthesizer with the standard Transformer model**: the authors used Perplexity as an evaluation metric and tested it on the Wikitext-2 dataset. The results show that Dense Synthesizer performs slightly better than the standard Transformer model on short sequences, but not as well as the standard Transformer model on long sequences.

**Comparison of Random Synthesizer with the standard Transformer model**: also using Perplexity as an evaluation metric, it was tested on the Wikitext-2 dataset. The results show that Random Synthesizer slightly outperforms the standard Transformer model on long sequences, but is not as effective as the standard Transformer model on short sequences.

**Comparison of Factorized Synthesizers with the standard Transformer model**: also using Perplexity as an evaluation metric, it was tested on the Wikitext-2 dataset. The results show that Factorized Synthesizers slightly outperform the standard Transformer model on long sequences, while the results on short sequences are comparable to the standard Transformer model.

**Comparison of Mixture of Synthesizers**: the authors mixed different Synthesizers together and tested them on the Wikitext-2 dataset using Perplexity as an evaluation metric. The results show that Mixture of Synthesizers slightly outperforms the standard Transformer model on long sequences, while the results on short sequences are comparable to the standard Transformer model. 

![image](https://github.com/user-attachments/assets/a1412c94-70da-446e-88f6-b9e62dac5968)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new model of self-attention, SYNTHESIZER, and experimentally validates its competitiveness on several tasks.
  
  2. By comparing different types of attention mechanisms, the authors find that SYNTHESIZER is highly complementary to standard DOT PRODUCT ATTENTION and can improve performance.
  
  3. The authors also conducted extensive quantitative and qualitative analyses to delve into the principles of action and performance characteristics of synthetic attention.

### 2. Innovative points
  1. The paper proposes SYNTHESIZER, a new self-attention model, which realizes an effective alternative to standard dot product attention by generating attention weights in a random or dense way.
  
  2. Meanwhile, the authors also designed a series of experiments to explore the performance differences of different types of attention mechanisms in different tasks, which provides a valuable reference for the design of self-attention models.

![image](https://github.com/user-attachments/assets/bf8ee5ad-4b89-4268-9f7d-da818f4b30fa)
     
### 3. Future Works
  1. The SYNTHESIZER model proposed in this paper has a certain degree of universality and extensibility, and can be applied in other NLP tasks for research.
  
  2. It can be further explored how to combine different attention mechanisms to construct a more efficient and flexible self-attention model.
  
  3. In addition, combining SYNTHESIZER with other deep learning techniques, such as pre-training models, can be considered to further improve its performance and effectiveness. 
