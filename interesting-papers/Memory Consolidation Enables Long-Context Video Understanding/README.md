# Memory Consolidation Enables Long-Context Video Understanding
[paper link](https://arxiv.org/pdf/2402.05861) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new approach, Memory Consolidated Visual Transformer (MC-ViT), for processing long time-series video comprehension tasks.          |    Transformer      |

## Methodology

### 1. Abstract
Traditional video encoders based on self-attention mechanisms suffer from high computational complexity and difficulty in scaling long-term contexts, etc. MC-ViT easily scales its context by non-parametrically extracting memories of past activations, re-training an existing pre-trained video converter, and utilising a redundancy reduction technique, thus achieving the best results on the EgoSchema, Perception Test, and Diving48 datasets, among others, to achieve the latest best results. This approach is effective in improving model performance without adding too many parameters.

### 2. Method Description 
This paper proposes a model based on Video Vision Transformers (ViT), the Memory-Consolidated Visual Attention Model (Memory-Consolidated ViT). The model processes the data by dividing the video into multiple time segments and using a multi-head self-attention mechanism in each segment. Also, the model introduces a cross-attention mechanism that enables the model to transfer information across time segments. Ultimately, the model can effectively process longer video sequences with high expressiveness and efficiency.

![image](https://github.com/user-attachments/assets/36bce3c9-e6a0-42dd-bc54-2b5e7eb14176)

### 3. Methodological improvements
In order to solve the computational complexity problem caused by the long video length, the paper proposes three different memory merging strategies: random selection, greedy clustering and k-mean clustering. These strategies enable the model to handle large amounts of data more efficiently and improve its expressive power.

### 4. Issues addressed 
The memory-merged visual attention model proposed in this paper can efficiently process longer video sequences and can improve the expressiveness and efficiency of the model with different types of memory-merging strategies. This approach can be applied in many computer vision tasks, such as video classification and behaviour recognition.

## Experiments
This paper focuses on MC-ViT, a multi-segment autoregressive model for long video comprehension tasks, and verifies its effectiveness and superiority through several comparative experiments. Specifically, the authors conducted the following four experiments:

**Impact of long video length on performance:** this experiment explores the performance of MC-ViT in processing videos of different lengths by training and testing on videos of different lengths. The results show that as the video length increases, the performance of MC-ViT is also improved and performs better on longer videos.

![image](https://github.com/user-attachments/assets/fc18eb3c-46f7-494c-ace2-bb13c72583ea)

**Comparison of different models in terms of efficiency:** this experiment compares MC-ViT with two other methods (joint spatio-temporal attention and ST-ViT) in terms of memory usage and computational complexity. The results show that MC-ViT not only outperforms the other two methods in terms of efficiency, but also improves significantly in terms of accuracy.

![image](https://github.com/user-attachments/assets/915ae88c-4bd9-4cec-91e3-f6c3267285a1)

**Analysis of memory merging mechanism:** This experiment analyses the different ways of memory merging in MC-ViT (k-means clustering and random selection), as well as the different merging algorithms (coreset and past-activations). The results show that k-means clustering is the optimal memory merging method, while random selection can also achieve good results.

![image](https://github.com/user-attachments/assets/477bb2cb-231b-4225-b328-75450896142e)

**Comparison Experiment:** This experiment compares MC-ViT with a number of other existing methods, including tasks such as fine-grained action recognition and long video quizzing. The results show that MC-ViT outperforms other methods in all these tasks, especially in the long video comprehension and quiz tasks.  

## Conclusion

### 1. Advantages of the Thesis
The model employs a non-parametric memory integration technique that integrates the activation of past segments into a compact memory bank, thus extending the capability of long-term contextual understanding. In addition, the model offers the following advantages:

  1. Compared to traditional video architectures, MC-ViT does not require any specialised architecture or training strategy and can efficiently utilise existing video architectures.
  2. MC-ViT is able to achieve better performance than other methods with the same computational resources, e.g., achieving more than 10x efficiency gains while using less memory and computation.
  3. The non-parametric nature of MC-ViT makes it easy to reuse pre-trained video Transformer models, thus reducing the overall training time.

### 2. Innovative points
  1.**Non-parametric memory integration:** the model uses a simple non-parametric mechanism to form representative memories, which effectively compresses memories and improves representational capabilities.     
  2. **Streaming processing:** the model uses streaming processing to limit its complexity and thus better adapt to long video sequences.  
  3. **Simple tuning strategy:** the model can be implemented by simply fine-tuning the pre-trained video Transformer model without complex modifications.

### 3. Future Works
  1. **Exploring more memory integration strategies:** in addition to the non-parametric memory integration technique proposed in this paper, other memory integration strategies, such as dynamic weight-based memory integration, can be considered.
  2. **Application to other domains:** the ideas of the model can also be applied to other domains of sequential data processing, such as natural language processing and audio processing, in order to improve the model's long-term contextual understanding and inference.
  3. **Multimodal joint reasoning:** the model can be combined with information from other modalities (e.g., text, images, etc.) to achieve multimodal joint reasoning for better understanding and answering questions.  
