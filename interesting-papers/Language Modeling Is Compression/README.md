# Language Modeling Is Compression
[paper link](https://arxiv.org/pdf/2309.10668) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |This paper explores the relationship between language models and compression, and presents a view of the prediction problem as a compression problem.          | large language models (LLMs)         |

## Methodology

### 1. Abstract
By evaluating the compression capabilities of large language models, the authors find that these models have strong generalised predictive capabilities and provide new insights from a compression perspective, such as the law of scale, disambiguation and context learning. Experimental results show that data can be compressed better using large language models like Chinchilla 70B than algorithms dedicated to image and speech compression. In addition, the paper demonstrates the ability to build conditional generative models using any compressor (e.g., gzip). In summary, this paper provides a new perspective on language models with significant results in practical applications.

![image](https://github.com/user-attachments/assets/52fc0895-e2b0-49f3-b6f8-498a4f665cc0)

## Experiments
This paper focuses on experiments using language models to compress data and compares them with other traditional compression algorithms. Specifically, the following experiments have been conducted in this paper:

The effects of compressing text, image and audio data using different compression algorithms are compared. The experimental results show that large language models exhibit excellent compression performance on all data types, outperforming traditional compression algorithms dedicated to specific data types.

The optimal model sizes for different sized language models on different data sets are investigated. Experimental results show that for each dataset, there exists an optimal model size that allows the best balance between the tuned compression rate and the number of model parameters.

![image](https://github.com/user-attachments/assets/19ef633b-b249-45ca-b5e7-7af07272a9df)

The possibility of using the compressor as a generative model is explored. Experimental results show that, despite theoretical guarantees, in practice the use of a compressor as a sequence prediction model is not guaranteed to produce high-quality generated samples.

![image](https://github.com/user-attachments/assets/452ece23-0584-4f27-8cb8-bdaaec42fff9)

The effect of using different compression algorithms and language models for compression at different sequence lengths is analysed. Experimental results show that, where appropriate, increasing the sequence length improves the compression rate, but the compression rate decreases rapidly as the sequence length increases.

The effect of different disambiguation methods on the compression rate is examined. The experimental results show that increasing the vocabulary in the participle method can improve the compression rate to some extent, but the effect is not obvious for larger models. 

![image](https://github.com/user-attachments/assets/79df14d4-c7e2-461e-b781-5287d40dffc0)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a method for equating sequence models to compressors, and experimentally verify the effectiveness and superiority of the method. The authors use a large language model as a compressor and compare it with standard compression algorithms.
  
  2. The results show that the compression method based on language models has higher compression rate and faster speed. In addition, the article provides insights on how to build efficient compressors, providing a valuable reference for future compression research.
 
### 2. Innovative points
  1. This paper proposes a new compression methodology that equates sequence models with compressors. This approach exploits the powerful predictive capabilities of large language models to compress textual data efficiently.
  
  2. In addition, the authors explore how to use self-encoders to train large language models and demonstrate the effectiveness of this approach. These innovative approaches bring new ideas and methods to the field of compression.
 
### 3. Future Works
It can expect more researchers to explore in this direction to further improve the compression efficiency and speed. At the same time, it also needs to pay attention to how to use this compression method under the premise of privacy protection to ensure the security and reliability of data.  
