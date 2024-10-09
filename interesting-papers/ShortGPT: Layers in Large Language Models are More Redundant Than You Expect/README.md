# ShortGPT: Layers in Large Language Models are More Redundant Than You Expect
[paper link](https://arxiv.org/pdf/2403.03853) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the problem of a large number of redundant layers in large language models (LLMs) and proposes a metric called Block Influence (BI) to measure the importance of each layer.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
Based on this observation, the authors define a simple and straightforward pruning method, layer removal, to improve model performance by removing redundant layers. Experiments show that this method performs better than previous state-of-the-art techniques and, in combination with other methods such as quantisation, can further reduce parameters and computation. This finding suggests a high degree of redundancy in the architecture of LLM.

### 2. Method Description 
The paper proposes a Block Influence (BI) metric-based layer deletion method for reducing the amount of redundant computation in large language models. Firstly, they use the Block Influence (BI) metric to evaluate the degree of influence of each layer on the hidden state, and use this metric to perform layer removal operations. Specifically, they collected a sample set of unlabelled text as a calibration set, reasoned on this sample set and collected the hidden states of each layer, and then calculated the BI score of each layer based on these hidden states, and deleted the layers with lower scores sequentially after sorting the scores from smallest to largest.

![image](https://github.com/user-attachments/assets/e3defa6d-c693-4e1f-b587-f00ddb283d1a)

![image](https://github.com/user-attachments/assets/066035ef-a02b-4ebd-b7cd-fcfc09e8ba44)
 
### 3. Methodological improvements
Compared to the traditional pruning method, the method more accurately identifies those layers that play a smaller role in the model, thus achieving better performance improvement results. At the same time, the method is also able to flexibly control the number of layers removed to balance the trade-off between speed and performance.

### 4. Issues addressed 
The method solves the problem of redundant computation that exists in large language models, which can effectively reduce the computational complexity of the model and improve the speed and efficiency of the model. In addition, the method can help researchers better understand the internal structure and mechanism of the model and provide valuable references for subsequent research work.

## Experiments
This paper focuses on pruning methods for large language models, and compares and analyses them through several benchmark tests. Specifically, the authors use an importance-based layer removal strategy, where the importance of each layer is calculated to decide whether or not to retain the layer. In their experiments, the authors used four popular large language models (Llama2-7B, Baichuan2-7B, Llama2-13B, and Baichuan2-13B) and compared them with three common pruning methods (LLMPrune, SliceGPT, and LaCo). The experimental results show that the method proposed in this paper exhibits better performance in most of the benchmark tests, which indicates that this method can effectively reduce the number of parameters without affecting the capability of the model.

![image](https://github.com/user-attachments/assets/999d92da-c760-4588-87ee-fdc9368121d5)

In addition, the authors conducted experiments with different pruning ratios and observed the model's perplexity and Multi-Natural Language Understanding Benchmark Test (MMLU). The results show that the performance of the model decreases as the pruning ratio increases, but significant performance degradation occurs at some specific number of layers, which may imply the presence of some particularly important layers. 

Additionally, the authors explored the redundancy between depth and width and found that both types of redundancy are high, but the width redundancy does not follow any clear pattern, which may be due to the symmetry between the heads. Finally, the authors also compare several different importance measures and find that the BI method proposed in this paper is more effective than the others. Furthermore, the authors show that the method in this paper is orthogonal to the quantitative approach, which means that both techniques can be applied simultaneously in model optimisation. 

![image](https://github.com/user-attachments/assets/cac5eb3e-f4b0-413a-8d0a-7b531ea65df7)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new layer-importance-based model compression method that reduces the number of parameters and computation by removing redundant neural network layers for more efficient deployment.
 
  2. The method achieves significant results in experiments and is simpler and easier to implement compared to other complex compression methods. In addition, the study reveals the redundant nature of deep hierarchies in large language models, providing a valuable reference for future model optimisation.
 
### 2. Innovative points
  1. The methodological innovation of this thesis is that the Block Influence (BI) metric is proposed as an effective metric for judging the importance of neural network layers and applied to the compression of large language models.
  
  2. The method not only can effectively identify redundant neural network layers, but also can achieve the purpose of compression by simple deletion operations. Compared with other complex compression methods, the method has higher efficiency and scalability.
     
### 3. Future Works
Future research can focus on the following aspects: first, to continue to improve and refine the existing compression methods to enhance their efficiency and accuracy; second, to explore more compression strategies and techniques to meet the needs of different application scenarios; and third, to explore in depth the internal mechanisms and characteristics of large-scale language models, in order to better understand their workings and provide better guidance for their optimisation. 

