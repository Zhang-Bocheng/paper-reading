# Hopfield Networks is All You Need
[paper link](https://arxiv.org/pdf/2008.02217) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 |  This paper describes a modern Hopfield network with continuous states and corresponding update rules.        | Deep Learning          |

## Methodology

### 1. Abstract
   This new Hopfield network can store exponential levels of patterns and retrieve a pattern in a single update with exponential levels of retrieval error. The network has three types of energy minima: **global averaging, subset averaging, and individual pattern fixation points**. The new update rules are equivalent to the attention mechanism in transformers, which allows to carve the heads of the transformers model. These heads prefer global averaging at the first few levels and partial averaging through substability at higher levels. 
   
   New modern Hopfield networks can be integrated into DL architectures as layers to allow storage and access to raw input data, intermediate results, or learning prototypes. These Hopfield layers provide new ways of pooling, memory, association and attention mechanisms. Experiments have shown that Hopfield layers have a wide range of applications in several domains, including multi-instance learning problems, immune spectrum classification, small category classification tasks, and drug design datasets.

### 2. Method Description 
  The paper presents a modern continuous state-based Hopfield network and applies it to a DL architecture. By modifying the energy function and introducing new update rules, the method can achieve fast convergence and high storage capacity. In addition, the method can realize multiple query and storage modes with memory functions.

   ![image](https://github.com/user-attachments/assets/8e79e6e8-d97a-4a20-93d0-17d2f43d1d3d)
   
### 3. Methodological improvements
  The method is applied in DL architectures by improving the original Hopfield network so that it can handle continuous states. Specifically, the method uses new energy functions and update rules to achieve faster convergence and higher storage capacity. Also, the method implements multiple query and storage modes with memory functions.
  
### 4. Issues addressed 
  The method mainly addresses two problems in DL architectures: 
  1. how to integrate Hopfield networks with deep learning architectures;
  
  2. how to realize multiple query and storage patterns with memory functions. These problems are very important for many real-world application scenarios, such as image recognition and NLP. Therefore, this method provides an effective solution for these areas.

     ![image](https://github.com/user-attachments/assets/a69b901b-2342-4e82-a570-4478c344efbd)

## Experiments
  This paper presents the results of the authors' experiments applying Hopfield networks in several domains. 
  <br> First, the authors analyze the states of the attention heads in the Transformer and BERT models and find that they are mainly in one of four states: global fixation point, fixation point separated from a single pattern, local stable state, and averaging state.
  
  <br> The authors then applied the Hopfield network to several example learning tasks, including immune spectrum classification, image annotation, and breast cancer classification. Experimental results show that using the Hopfield network significantly improves performance and reaches new optimal levels. 
  
  <br> In addition, the authors tested the performance of the Hopfield network on small datasets and compared it to other machine learning methods. The experimental results show that the Hopfield network outperforms all other methods on small datasets. 
  
  <br> Finally, the authors also applied the Hopfield network to a prediction task in the field of drug design and achieved satisfactory results. Overall, this paper demonstrates the wide range of applications and excellent performance of Hopfield networks in several fields.

  ![image](https://github.com/user-attachments/assets/7bd8005f-3c3d-41b7-b3c3-6d9d508be737)


