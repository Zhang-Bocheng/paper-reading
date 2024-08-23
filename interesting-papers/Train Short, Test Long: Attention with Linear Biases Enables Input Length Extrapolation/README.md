# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation
[paper link](https://arxiv.org/pdf/2108.12409) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper explores how to achieve extrapolation capabilities for models on long sequences that have not been seen at training time.         |   Transformer        |

## Methodology

### 1. Abstract
The authors first point out that extrapolation can be achieved by changing the positional representation and propose a simple but effective positional representation, Attention with Linear Biases (ALiBi). This approach achieves this by penalising query-key attention scores proportionally to the distance between them. Experimental results show that models trained using the ALiBi method can extrapolate from an input length of 1024 to a length of 2048 and achieve the same perplexity as a sinusoidal positional embedding model trained to a length of 2048, but are 11% faster and use 11% less memory than the latter. In addition, ALiBi has a stronger preference for recent information, outperforming several powerful location representation methods in the WikiText-103 benchmark.

### 2. Method Description 
The paper proposes two approaches in the text classification task: **sinusoidal position method** and **rotary position method**. both approaches achieve classification by mapping the input sequence into a high dimensional space. Among them, sinusoidal position method is based on position embedding by sinusoidal function, while rotary position method is based on rotation matrix.

![image](https://github.com/user-attachments/assets/acc2223c-5300-4b1a-9756-d81fa92dd8ef)

### 3. Methodological improvements
In their experiments, the authors found that the sinusoidal position method, although it should be able to extrapolate efficiently in theory, has very limited extrapolation capabilities in practice. In contrast, the rotary position method performs better than the sinusoidal position method, but still fails to achieve satisfactory results. Therefore, the authors proposed a new position embedding method, the T5 bias method, and found that the T5 bias method can perform better extrapolation while keeping other factors constant.

![image](https://github.com/user-attachments/assets/1287e49d-338f-413d-b416-151df5986731)

### 4. Issues addressed 
This paper addresses the problem of choosing the positional embedding method in text classification task. Although both the traditional sinusoidal position method and rotary position method can be used for text classification, they both have certain limitations. The T5 bias method proposed by the authors not only achieves better results in experiments, but also can be computed more efficiently. This provides a more efficient solution for text categorisation tasks.

## Experiments
This paper focuses on the performance impact of using different positional methods on language models, and proposes a new positional method, ALiBi (Additive Linear Biases), and conducts experiments on several datasets to prove its effectiveness.

In their experiments, the authors first compare the performance of language models using different positional methods on the WikiText-103 dataset. They found that using the ALiBi method improves the performance of the model without increasing the training time compared to the traditional sinusoidal method. In addition, the ALiBi method also outperforms other positional methods, such as rotary and T5 bias, when longer input sequences are used.

Next, the authors applied the ALiBi method to a larger dataset and a larger model and compared it to other location methods. The results show that the ALiBi method not only performs well on small-scale datasets, but also achieves good results on large-scale datasets. Meanwhile, the ALiBi method also has the advantages of lower memory consumption and faster training speed. 

![image](https://github.com/user-attachments/assets/a83ce69f-92b8-4176-9835-6e1b9c27872c)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new positional embedding method, ALiBi, which can effectively solve the problem of Transformer model's generalisation ability when the length of the input sequence exceeds the training set.
  
  2. The method is simple and easy to implement, does not require additional parameters or computational overheads, and can reduce the training cost while ensuring performance. Experimental results show that the model using the ALiBi method can achieve comparable or even better performance than the traditional positional embedding method with the same amount of training data.

![image](https://github.com/user-attachments/assets/e75883fd-2904-4c25-bc0e-3daffdf865e2)

### 2. Innovative points
  1. The main contribution of this paper is to propose a new location embedding method, ALiBi, which improves the distribution of attention weights by introducing linear negative bias to improve the generalisation ability of the model.
  
  2. Compared with the traditional sinusoidal positional embedding method and other alternatives, ALiBi has higher efficiency and simpler implementation.
  
  3. In addition, the authors experimentally demonstrate the effectiveness and superiority of the ALiBi method.
     
### 3. Future Works
  1. When dealing with large-scale natural language data, ALiBi can help the model to better capture contextual information, thus improving the prediction accuracy.
  
  2.  Meanwhile, the method can also be applied to other types of neural network structures, such as CNN.
  
  3.  Therefore, the research of ALiBi method not only helps to improve the NLP technology, but also helps to promote the further development of the deep learning field. 
