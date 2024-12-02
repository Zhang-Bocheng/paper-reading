# Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models
[paper link](https://arxiv.org/pdf/2401.06102) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a framework called Patchscopes for interpreting the meaning of internal representations of large language models (LLMs).         |        Large Language Models (LLMs)  |

## Methodology

### 1. Abstract
By exploiting the model's own ability to interpret its internal representation in natural language, it is possible to better understand the model's behaviour and verify its consistency with human values. The framework is able to answer a wide range of questions about LLM computation and is more expressive and accurate than some of the previous interpretation methods. In addition, Patchscopes opens the door to new possibilities such as the use of more powerful models to interpret the representations of smaller models and multi-hop inference error correction.

### 2. Method Description 
Patchscopes is an approach that exploits the ability of pre-trained models (e.g., LLMs) to generate human-like text to translate their hidden representation information. The method does this by decoding specific information in different reasoning processes and inserting this information into the target model using a mapping function. This approach allows intervening in the computational process and modifying the computed results to reveal whether specific information can be decoded from the patched representation.

Method Improvements
The Patchscopes method has the following advantages over previous research:

Problem solved
The Patchscopes approach addresses limitations that existed in previous research, including:

### 3. Methodological improvements
  1. Parameters such as the target model, target layer and mapping function can be flexibly selected and therefore can be adapted to various application scenarios.
  2. Transfer learning between multiple models can be performed to improve the expressiveness of the model.
  3. Can be used for many types of query tasks, not just classification problems.

### 4. Issues addressed 
  1. For some query tasks, previous probing methods may not accurately detect the presence or absence of specific information.
  2. Prior probing methods are typically only able to analyse for a single model, whereas the Patchscopes method allows transfer learning across multiple models, improving the expressiveness of the model.
  3. Previous probing methods are usually designed based on fixed query tasks, whereas the Patchscopes method can customise the query tasks as needed, making it more flexible.
     
## Experiments
This article mainly introduces the Patchscope method based on language models, and demonstrates its performance and application value on different tasks through several experiments. Specifically, the article is divided into four parts:

The Experiment 1, which aims to explore the effect of different Patchscope methods when decoding the next token prediction. The experiment uses several pre-trained language models and compares different input and output configurations. The results show that Token Identity Patchscope has better results at the early level, while Logit Lens and Tuned Lens are more effective at the later level.

![image](https://github.com/user-attachments/assets/75e8c166-879c-4d0d-a4d9-3aa0a16e4a41)

The Experiment 2 investigates how Patchscope can be used to extract attribute information from specific source cues. The experiment also uses several pre-trained language models and compares different types of attributes and Prompt templates. The results show that the Zero-Shot Feature Extraction Patchscope achieves good results without training data and has better accuracy compared to linear regression probes.

![image](https://github.com/user-attachments/assets/ebc61ccf-a618-4e8b-b2f7-55cc03e0a24c)

The Experiment 3 analyses how the language model handles entity names. The experiment used multiple entity names as input and compared the quality of the descriptions generated at different levels. The results show that at an early level, the model gradually incorporates more context into the entity descriptions.

![image](https://github.com/user-attachments/assets/95a6b2a5-6ffd-4e0d-9f9b-fd23004a4bf9)

The Experiment IV shows how Patchscope can be used to improve the performance of multi-step inference errors. The experiment was designed for a multi-step query task and compares the results of three different Patchscope methods with two baselines. The results show that CoT Patchscope corrects multi-step inference errors more effectively than the other methods.

## Conclusion

### 1. Advantages of the Thesis
  1. The framework exploits the LLM's ability to generate human-like text by ‘patching’ information to query the LSTM for specific information. The authors demonstrate that many existing interpretation methods can be considered special cases of Patchscopes, and that the new configuration improves the ability to extract different types of information.
  2. In addition, the framework has new capabilities such as correcting multi-step inference errors. Thus, the paper provides a key approach to controlling and understanding modern generative AI.

### 2. Innovative points
  1. The main contribution of the thesis is the proposal of Patchscopes, a novel framework that can effectively decode various types of information, including output predictions and knowledge attributes. Compared with existing methods, Patchscopes performs better in terms of accuracy and does not require training data.
  2. In addition, the paper introduces some new configurations to explore different domains of applications and more complex tasks, such as processing multiple tokens simultaneously or cross-layer patching.

### 3. Future Works
  1. There is a need to better understand how to use a given target cue to propagate information to other locations and layers.
  2. There is a need to explore the difference in effectiveness between using a few-sample target cue versus a zero-sample/instruction cue.
  3. There is a need to explore how patching can be done across different families and architectures of models. 
