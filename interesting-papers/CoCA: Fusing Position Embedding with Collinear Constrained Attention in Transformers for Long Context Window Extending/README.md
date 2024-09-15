# CoCA: Fusing Position Embedding with Collinear Constrained Attention in Transformers for Long Context Window Extending
[paper link](https://arxiv.org/pdf/2309.08646) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new attention mechanism, Collinear Constrained Attention (CoCA), for solving the problem of anomalous behaviour of transformer models in long context window extensions.          | Attention         |

## Methodology

### 1. Abstract
The authors significantly enhance the model's ability to extend for long context windows by seamlessly integrating rotational position embedding with self-attention and forcing the covariance constraints between Q and K to be satisfied. Experimental results show that CoCA can easily extend the context window length from 512 to 32K without fine-tuning, while achieving 32K extrapolation on LLaMA-7B.

### 2. Method Description 
In this paper, Collinear Constrained Attention (CoCA) method is proposed to solve the problem of anomalous behaviour between RoPE and attention matrix. CoCA seamlessly integrates RoPE into the query and key computation process by introducing a covariance constraint into the self-attention mechanism to achieve the extraction of long-range context information. Specifically, CoCA first computes a query vector based on each position in the input sequence and introduces a co-linearity constraint coefficient for each key vector. Then, by multiplying the query vectors and the covariance constraint coefficients, the key vectors of the extended dimension are obtained. Finally, the RoPE function is applied and the attention score is calculated.

![image](https://github.com/user-attachments/assets/b017f453-bff5-49f2-9422-74d8eb181f30)

### 3. Methodological improvements
Compared with the traditional self-attention mechanism, CoCA has a better performance performance when dealing with long-range contextual information. Also, CoCA provides a Slack constraint-based implementation to reduce the computational complexity. In addition, CoCA can be used in combination with other effective attention mechanisms, such as Longformer, StreamingLLM, etc., to further improve the performance of the model.

### 4. Issues addressed 
CoCA solves the problem of anomalous behaviour that exists between RoPE and attention matrix, i.e., when the relative angle between query vectors and key vectors varies greatly, it will lead to anomalous values of attention scores. CoCA effectively reduces the occurrence of this anomalous behaviour by introducing the covariance constraints, and improves the model's capability of capturing contextual information over long distances.

## Experiments
This paper focuses on how to improve the processing of long texts by improving the self-attention mechanism in large-scale pre-trained language models. The authors conducted several experiments to validate the effectiveness of their proposed method of rotational positional coding (CoCA) and compared it with other methods.

First, the authors used the metric perplexity to evaluate the model's ability to process long sequences. They divided the training data into two parts, short and long sequences, and calculated perplexity on a test set.The results show that the CoCA method performs better when dealing with long sequences, especially when increasing the sequence length.

![image](https://github.com/user-attachments/assets/70dec68c-31e5-42c0-bc61-015e1f13e4c6)

Secondly, the authors also performed a theoretical analysis of long-term decay, which proved that the CoCA method has stronger stability. In addition, they analyse the rotational boundary problems and propose new solutions that enable the CoCA method to better handle these boundary problems.

![image](https://github.com/user-attachments/assets/c518f344-0ac7-4bd7-bcbf-ad1ed740cfcd)

Finally, the authors also conducted comparison experiments with existing methods, including the direct application of dynamic approximation kernel techniques and methods such as PI. The results show that the CoCA method not only performs better on long sequences, but also preserves its expressiveness on short sequences. 

![image](https://github.com/user-attachments/assets/3050276d-b7e2-4912-bdea-b4a72fa70bef)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new positional encoding approach, Collinear Constrained Attention (CoCA), and applies it to a long sequence language model, which effectively improves the performance of the model in long context retrieval tasks.
  
  2. Compared with the existing extended RoPE methods, CoCA can solve the rotation boundary problem more effectively and with higher accuracy.
  
  3. In addition, CoCA has less computational and spatial complexity and can be used as a seamless replacement solution for the existing Transformer model.

### 2. Innovative points
  1. CoCA achieves a seamless integration between the self-attention mechanism and position coding by initialising the angle between the Q and K vectors to zero.
  
  2. This novel approach solves the problem caused by the initial angle difference present in RoPE, thus avoiding undesirable behaviours at the boundaries of the context window.
  
  3. In addition, CoCA can be used with other extended RoPE methods to further improve the capability of long context retrieval.

### 3. Future Works
Future research can explore how CoCA can be combined with other advanced deep learning techniques to further improve the performance and efficiency of the model. In addition, it can also be investigated how CoCA can be applied to other types of sequence data, such as audio or video.   
