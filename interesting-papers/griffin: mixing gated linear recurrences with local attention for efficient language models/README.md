# Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models
[paper link](https://arxiv.org/pdf/2402.19427.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new neural network model, Hawk and Griffin, for natural language processing tasks.         |   Recurrent Neural Network        |

## Methodology

### 1. Abstract
Traditional recurrent neural networks (RNNs) perform well on long sequences but have problems with training and scalability. Hawk is an RNN with gated linear recursion, while Griffin mixes gated linear recursion with local attention. Experimental results show that Hawk outperforms Mamba on downstream tasks, while Griffin achieves Llama-2 performance levels with small amounts of training data and is capable of extrapolating very long sequences. Both models outperform Transformer in terms of hardware efficiency, inference latency and throughput. Finally, the authors also describe how to perform distributed training on Griffin to improve its scalability.

![image](https://github.com/user-attachments/assets/37e20981-3722-4002-8ee2-72ef4ef4589f)

### 2. Method Description 
The paper proposes a new model architecture including residual block, MLP block and temporal hybrid block. Among them, there are three choices for the temporal hybrid block: global Multi-Query Attention (GMA), local(sliding-window) MQA, and recurrent block. The recurrent block uses Real-Gated Linear Recurrent Unit (RG-LRU), a new recurrent layer based on Linear Recurrent Unit (LRU). The model aims to improve the performance of the language modelling task and its effectiveness is verified experimentally.

![image](https://github.com/user-attachments/assets/d9b37431-85db-45a9-8d24-acb5dfa6e0f3)

### 3. Methodological improvements
Compared to traditional pre-training models such as BERT and GPT, the model introduces a recurrent structure to handle long sequence information. Also, a novel recursive layer like RG-LRU is used to enhance the memory capability of the model. In addition, the choice of temporal mixing blocks provides more flexibility for the model to adapt to different task requirements.

### 4. Issues addressed 
The model mainly solves the problem that traditional pre-trained models have when dealing with long sequential information, i.e., they cannot effectively capture long-term dependencies. At the same time, through the selection of temporal mixing blocks, the model can also cope with the demands of different tasks and improve the generalisation ability of the model. In the experiments, the model shows better performance than the traditional pre-trained model, proving its effectiveness and feasibility.

## Experiments
This paper focuses on two novel language models, Hawk and Griffin, based on Gated Recurrent Units (GRUs) and Long Short-Term Memory Networks (LSTMs), and conducts comparative experiments on several aspects of them.

First, the authors compare Hawk and Griffin with the best available small-scale recursive models on a training dataset and show that they outperform existing models on downstream tasks. The authors then conducted experiments comparing training speed and inference speed using different sequence lengths and model sizes, and found that Hawk and Griffin's decoding phase is faster than existing models when the sequence length is large enough.

![image](https://github.com/user-attachments/assets/6e543c88-ec2f-432f-afad-147b5e5b88cd)

Next, the authors conducted comparative experiments on predictive power, including the ability to understand longer contexts and the ability to replicate and retrieve. The experimental results show that Hawk and Griffin are able to effectively utilise longer contexts to improve the prediction accuracy of their next markers, and also show good performance in replication and retrieval tasks.

Finally, the authors also conducted evaluation experiments on the pre-trained models of Hawk and Griffin to test their performance in replication and retrieval tasks. The results of the experiments show that although Hawk and Griffin may not be as good as the other models in some cases, they are still highly capable of solving these tasks. 

![image](https://github.com/user-attachments/assets/30524028-8a43-4252-92c9-fa4157229d0d)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new RNN model (Hawk and Griffin) and compares it with Transformer. The results show that these new models outperform the traditional RNN and Transformer models in terms of performance and efficiency, and are able to handle long sequence data effectively.
  
  2. In addition, the paper proposes a novel gated linear recurrent layer (RG-LRU), and a hybrid model with a mixture of local attention (Griffin). These innovations provide new ideas and directions for the development of recurrent neural networks.

### 2. Innovative points
  1. The main contribution of this thesis is the proposal of new RNN models (Hawk and Griffin) and their gated linear recurrent layer (RG-LRU). Among them, the Hawk model employs a combined structure of multilayer perceptron (MLP) and recurrent blocks, while Griffin is a hybrid model that combines recurrent blocks and local attention.
 
  2. In addition, the authors propose a new gated linear recursive layer (RG-LRU), which better captures long-term dependencies in sequences and thus improves the performance of the model.
     
### 3. Future Works
In the future, we can further explore how to optimise the design and implementation of these models to improve their performance and efficiency. In addition, we can apply these models to a wider range of natural language processing tasks, such as machine translation, text categorisation, and so on. 
