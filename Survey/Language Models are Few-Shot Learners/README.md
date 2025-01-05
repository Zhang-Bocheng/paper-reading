# Language Models are Few-Shot Learners
[paper link](https://arxiv.org/pdf/2005.14165.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores the performance of language models for learning with fewer samples.         |  Large-scale Language Models (LLMs)        |

## Methodology

### 1. Abstract
The authors used a pre-trained language model, GPT-3, with a parameter count of 17.5 billion, and tested it without fine-tuning on a number of natural language processing tasks with excellent results. This shows that large-scale language models can significantly improve their generalisation ability in the case of fewer samples, and can even rival traditional fine-tuning methods. However, the authors also point out that the model still has some limitations on certain tasks, and discuss the implications of this finding for society and the challenges it may pose.

### 2. Method Description 
The paper describes methods for unsupervised learning using language models based on autoregressive models such as GPT-3. Specifically, they explore the effects of training large models with different data sizes, diversity, and lengths, and propose three new learning styles: learning with few samples, learning with a single sample, and learning with zero samples. Each of these learning approaches is accomplished with a given task description and a small number of examples, without requiring any labelled data or gradient updates.

![image](https://github.com/user-attachments/assets/fad9cbd6-473a-4aee-b0db-a14a9e67db60)

![image](https://github.com/user-attachments/assets/8d65959c-9421-4e98-8602-24c12a7e6050)

### 3. Methodological improvements
Compared to traditional supervised learning methods, this approach avoids relying on large amounts of labelled data and is better adapted to a variety of different tasks. In addition, the paper proposes a number of technical means to improve the performance of the model, such as using alternating dense and locally banded sparse attention patterns to construct the Transformer layer, and using multiple high-quality datasets to enhance the diversity of the training data.

### 4. Issues addressed 
The approach addresses the problem of requiring large amounts of labelled data for many existing natural language processing tasks, as well as providing an important direction for future research. In addition, the paper proposes a new evaluation criterion that assesses the capability of a model by comparing its performance under different learning approaches, which will help further research and development of more efficient and flexible natural language processing algorithms.

## Experiments
This paper describes the performance of GPT-3 on several natural language processing tasks and compares it to previous research. A detailed description of each task is given below:

  1. **Traditional language modelling tasks and related tasks**: these include tasks such as language model prediction with zero, one, and few examples and text completion. The authors used Perplexity as an assessment metric, and the GPT-3 scored well in all of these tasks.

![image](https://github.com/user-attachments/assets/e496e9d0-038a-445a-ab9d-9bd9d657f1d1)

  2. **Close Book Quiz task**: This task requires answering questions about broad factual knowledge but does not allow searching for relevant information. The authors used Accuracy as an evaluation metric, and in this task GPT-3 outperformed the previous best unconditional pre-trained model on all three datasets.

![image](https://github.com/user-attachments/assets/5ffcdf21-fd79-4b7d-8ca9-615e644dd706)

  3. **Translation task:** In this task, the authors tested the translation ability of GPT-3 between three different language pairs. The authors used BLEU as an evaluation metric, and in this task, GPT-3 outperformed some previous unsupervised machine translation methods and got better results as the model capacity increased.

![image](https://github.com/user-attachments/assets/b95174c2-cbb4-4261-a8b7-698cd5d7b8df)

  4. **Winograd style task**: this task involves determining the word to which a pronoun refers when the word is grammatically ambiguous but semantically explicit. The authors used Accuracy as an assessment metric, and in this task the GPT-3 achieved good results in all three settings.

![image](https://github.com/user-attachments/assets/20df7b85-b9e8-4564-a40b-aa46fe703566)

  5. **Common Sense Reasoning Task**: this task was designed to capture physical or scientific reasoning rather than sentence completion, reading comprehension, or broad common sense question answering. The authors used Accuracy as the assessment metric, and in this task the GPT-3 achieved excellent results in all three datasets.
      
## Conclusion

### 1. Advantages of the Thesis
  1. A comprehensive and detailed description of GPT-3's strengths, such as its high-precision text generation capability and its ability to handle a variety of natural language tasks.
  2. The limitations and potential problems of GPT-3, such as low sample efficiency and social bias, are analysed for subsequent research.
  3. Some solutions to these problems, such as improving training data and developing new techniques, are proposed, which have some practical value.

### 2. Innovative points
  1. The main innovation of this thesis is a comprehensive and in-depth analysis of GPT-3, which reveals its capabilities and limitations in text synthesis, as well as the possible problem of social bias.
  2. At the same time, some solutions are proposed to provide certain ideas and directions to solve these problems.

### 3. Future Works
  1. Strengthening the combination with practical application scenarios and exploring how to apply GPT-3 to a wider range of fields.
  2. Further study the social biases of GPT-3 and explore how to reduce or eliminate them.
  3. Explore other types of large-scale language models and compare the differences and advantages and disadvantages between them and GPT-3, in order to better understand the nature and development trend of language models.   
