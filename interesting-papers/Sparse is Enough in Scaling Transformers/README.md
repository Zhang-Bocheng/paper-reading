# Sparse is Enough in Scaling Transformers
[paper link](https://arxiv.org/pdf/2111.12763) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper focuses on how to solve the problem of slow training and decoding of large Transformer models by exploiting sparsity.         | Transformer          |

## Methodology

### 1. Abstract
The authors propose Scaling Transformers, a family of novel Transformer models, and use sparse layers for efficient scaling and fast batchless decoding. Surprisingly, the sparse layer is sufficient to achieve the same results as the standard Transformer with the same number of parameters. In addition, the authors integrate previous sparse methods on attention and implement fast inference for long sequences with limited memory. The final results show that this approach achieves performance comparable to the current state-of-the-art in long text summarization tasks.

![image](https://github.com/user-attachments/assets/0e50edd9-d946-4a19-be00-41604493ba06)

### 2. Method Description 
The paper proposes two different sparsification techniques to speed up the decoding process of the Transformer model: **a sparse Feedforward layer and a sparse QKV layer**. For the sparse Feedforward layer, this is done by introducing a fixed structure in the intermediate activation vectors, allowing only one non-zero element in each block, and using a controller to dynamically select the columns or rows to be activated for each input token. For the sparse QKV layer, on the other hand, the attention mechanism is split into multiple blocks and convolutional operations are used instead of the standard fully-connected layer to reduce the number of parameters and computational complexity.

In addition, the paper describes how these sparsification techniques can be applied to the Transformer model on long sequences, i.e., Terraformer. Specifically, the authors redesigned the architecture of the Transformer decoder block by removing the unnecessary encoder-decoder attention mechanism and employing techniques such as invertible layers, recursive layers, and so on, to improve the model's training speed and generalization ability.

![image](https://github.com/user-attachments/assets/68030213-32d9-4fdf-a94f-d80c3d147cc5)

### 3. Methodological improvements
  1. Compared with the traditional Transformer model, the sparsification technique can significantly reduce the number of parameters and computation time of the model, which improves the speed and efficiency of the model.
  
  2. In addition, the training speed and generalization ability of the model can be further improved by redesigning the architecture of the decoder block and adopting techniques such as reversible layers and recursive layers.

![image](https://github.com/user-attachments/assets/7969efdd-db89-4f8a-a963-d7d970072c54)

### 4. Issues addressed 
The sparsification technique can help to solve the speed and efficiency problems of the traditional Transformer model in the decoding process, as well as improve the generalization ability and training speed of the model. This is very useful for handling large-scale natural language processing tasks, especially in application scenarios that require fast response to user requests.

## Experiments
This paper focuses on the performance of the Terraformer model on the abstracting task and compares it with several other Transformer-based models. Specifically, the authors test the model's performance using the arXiv scientific paper dataset, which consists of whole papers and their corresponding abstracts. The authors take the input whole paper as a sequence input and output its corresponding abstract. To ensure fairness, all models were pre-trained on C4 using the same pre-training method. Also, all models had the same number of parameters (800M) and used the same dimension settings and loss sparsity.

The authors chose the ROUGE metric to measure the similarity between the generated summaries and the reference summaries. The results show that the Terraformer model performs well on this task, achieving comparable performance to the baseline model even when only single word masks and greedy decoding are used.

It is worth noting that these ROUGE scores were computed using an open source scorer and there is some confusion. Therefore, the authors report two versions of the ROUGE-L metrics (R-LSent and R-LSum) as well as F1 values. In addition, the authors evaluated the Terraformer model for other downstream tasks, such as a classification task on the GLUE dataset. The results show that the Terraformer model performs similarly to the baseline model on these tasks.

Finally, the authors show that sparsifying the layers leads to faster decoding when the Terraformer model is extended to 17B parameters. Specifically, when all layers are sparsified, the decoding speed can be increased by a factor of 37. This shows that sparsification techniques can significantly increase the speed of the model while maintaining high performance. 

![image](https://github.com/user-attachments/assets/9800f76c-1ca0-4272-8a2c-ab9d72a19b7a)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a sparsified Transformer model and demonstrate its effectiveness in large-scale text classification tasks. Compared with the dense model, the sparse model can achieve faster inference speed and more efficient training on GPU. In addition, the article provides detailed experimental results and code open source for further exploration and application by other researchers.

![image](https://github.com/user-attachments/assets/cdf4ed87-2df0-4115-8bcc-1ee5d40284fd)

Methodological Innovation Points

Future Outlook
  
### 2. Innovative points
The main contribution of this paper is to propose the sparsification method to reduce the number of unnecessary parameters in the Transformer model. Specifically, the sparsification is achieved by introducing both attentional sparsity and positional coding sparsity. This approach not only significantly improves the speed and efficiency of the model, but also reduces the storage cost and computational resource consumption of the model.
 
### 3. Future Works
  1. The effectiveness of the model can be improved by further optimizing the sparsification strategy;
  
  2. the sparsification method can also be extended to other types of neural network structures.
  
  3. In addition, with the development of deep learning technology, the sparsification method may become an important direction for future research.  

