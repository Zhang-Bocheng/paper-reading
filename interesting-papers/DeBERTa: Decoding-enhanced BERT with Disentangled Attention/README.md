# DeBERTa: Decoding-enhanced BERT with Disentangled Attention
[paper link](https://arxiv.org/pdf/2006.03654) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new pre-trained neurolinguistic model, DeBERTa (Decoding-enhanced BERT with disentangled attention), which improves the BERT and RoBERTa models through two novel techniques Performance.         | self-attention mechanism         |

## Methodology

### 1. Abstract
  First, a separation of attention mechanism is employed, where each word is represented using two vectors for its content and position respectively, and a separation matrix is used to compute the attention weights between them. Second, an augmented mask decoder is introduced in the decoding layer to predict the mask tokens, while a virtual adversarial training method is used for fine-tuning to improve the generalization ability of the model. Experimental results show that these techniques significantly improve the pre-training efficiency of the model and the performance of downstream natural language understanding and generation tasks. Compared to RoBERTa-Large, the DeBERTa model trained with half of the data performs better on several NLP tasks, including MNLI, SQuAD v2.0, and RACE. 

### 2. Method Description 
  The DeBERTa model proposed in this paper is a pre-trained language model based on a self-attention mechanism, which uses a bidirectional encoder to capture contextual information and introduces relative position encoding to account for the distance relationship between words in the self-attention computation. Specifically, the model employs a hierarchical multi-head self-attention mechanism, where each head contains two independent vector representations: one for the content of the vocabulary and the other for the relative position of the vocabulary to the surrounding words. This design allows the model to better capture the semantic and syntactic relationships between words, thus improving the effectiveness of NLP tasks.
    
### 3. Methodological improvements
  1. Compared to the traditional self-attention mechanism, the DeBERTa model introduces relative positional encoding instead of absolute positional encoding, which helps to reduce the number of parameters and improve the model efficiency.
  
  2. DeBERTa uses an Enhanced Mask Decoder to take into account the absolute positional information of words to further improve the predictive power of the model.
     
### 4. Issues addressed 
  The DeBERTa model solves the problems that the traditional self-attention mechanism cannot effectively capture the distance relationship between words, as well as the inability to simultaneously consider the absolute positional information of words, by introducing the technical means of relative position encoding and enhanced occlusion decoder, thus achieving better results on several NLP tasks.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/578fce69-9e03-473f-9549-5adcfe04df05)

## Experiments
  This paper focuses on the performance of the DeBERTa model on several NLP tasks and compares it with other pre-trained language models. The authors have conducted experiments using both large and base models with detailed descriptions of datasets, hyperparameters, etc. The experimental results show that DeBERTa exhibits better performance on a variety of tasks compared to other similarly structured pre-trained language models such as BERT, RoBERTa, XLNet, ALBERT and ELECTRA. And the authors analyze the base model of DeBERTa and demonstrate the importance of each component through Ablation Study. The authors also demonstrate DeBERTa's performance on larger datasets and more complex tasks, including outperforming humans in the SuperGLUE benchmark.
  
## Conclusion
### 1. Advantages of the Thesis
  The paper proposes a new neurolinguistic model, DeBERTa, that improves the BERT and RoBERTa models by using two novel techniques: a split-attention mechanism and an enhanced mask decoder. These techniques significantly improve pre-training efficiency and downstream task performance. 
  
  Experimental results show that the DeBERTa model outperforms human performance in the SuperGLUE benchmark and excels on a wide range of NLP tasks. And, the paper presents a new virtual adversarial training method for fine-tuning PLMs to improve their generalization capabilities. This approach is very effective in improving the performance of the models.
  
### 2. Innovative points
  **Separate Attention Mechanism**: Each word is represented by two sets of vectors encoding its content and positional information, and the corresponding attention weight matrices are computed based on their content and relative position.

  **Enhanced Mask Decoder**: In the mask language modeling task, DeBERTa uses the content and location information of context words for prediction. Also, the absolute position embedding is added before the softmax layer in order to better take into account the absolute position of the words in the sentence.
  
### 3. Future Works
  Although DeBERTa has achieved good results in many NLP tasks, it is still unable to achieve human-level natural language comprehension. Therefore, in future research, ways to make DeBERTa more explicitly contain combinatorial structures, thus enabling it to combine symbolic and neural computation like humans, could be explored to further improve its performance.
