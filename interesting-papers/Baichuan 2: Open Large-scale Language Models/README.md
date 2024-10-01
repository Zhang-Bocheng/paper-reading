# Baichuan 2: Open Large-scale Language Models
[paper link](https://arxiv.org/pdf/2309.10305) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a large-scale multilingual model called ‘Baichuan 2’, which uses more than 2.6 trillion tokens and contains 7 billion and 13 billion parameters during training.          | Large language models (LLMs)         |

## Methodology

### 1. Abstract
The model is able to perform a variety of natural language tasks with a few natural language commands and excels in verticals such as medicine and law. Additionally, the model was able to match or exceed similarly sized open-source models in public benchmarks. The researchers will release all pre-trained model checkpoints to facilitate understanding of Baichuan 2 training dynamics.

### 2. Method Description 
The paper mainly introduces Baichuan 2, a NLP technology based on large-scale pre-training models, and elaborates on its technical details in terms of data collection, pre-processing, architectural design, optimisation and distributed training system. Specifically, Baichuan 2 employs a wider range of corpus sources, higher vocabulary size, better lexers, more efficient activation functions and normalisation methods, and more accurate optimisation algorithms to improve model performance.

 ![image](https://github.com/user-attachments/assets/1589e950-1f82-46aa-a174-beae453da8e2)
 
### 3. Methodological improvements
Compared with its predecessor model, Baichuan 2 adopts more optimisation measures, such as using a larger vocabulary list, adjusting the lexer, adopting a more efficient activation function and normalisation, optimising the optimisation algorithm, and so on. In addition, the model also adopts a new positional encoding approach (RoPE) and memory-efficient implementation of attention (xFormers) to further improve the performance of the model.

### 4. Issues addressed 
Baichuan 2 aims to construct a more efficient, accurate and secure large-scale pre-training model through more efficient technical means of data acquisition, pre-processing, optimisation and distributed training system, so as to provide more comprehensive support for research in the field of NLP. At the same time, the model can also be applied to intelligent customer service, intelligent Q&A, machine translation and other fields, which has a wide range of application prospects.

## Experiments
This paper describes the performance of Baichuan 2's pre-trained model in a number of domains and compares it with other models of similar size. Specifically, the paper covers the following six areas of comparison experiments:

**Overall performance comparison**: the authors chose eight standard benchmarks to compare Baichuan 2 with other models, including different types of questions such as multiple-choice and single-choice questions. The results show that Baichuan 2 has a significant advantage over the other models, especially performing well on maths and code problems.

**Vertical comparison of industry domains**: the authors chose two industry domains, law and medicine, and compared Baichuan 2 with other models using datasets from the corresponding domains. The results show that Baichuan 2-7B-Base outperforms models such as GPT-3.5 Turbo and ChatGLM 2-6B in the legal domain, while Baichuan 2-7B-Base also outperforms models such as LLaMA 2-7B in the medical domain.

**Comparison of Maths and Code Ability**: the authors compared the maths and code ability of Baichuan 2 with other models using several datasets such as GSM8K and MATH. The results show that Baichuan 2 outperforms the other models in both maths and code.

**Comparison of Multilingual Ability**: The authors compared the multilingual ability of Baichuan 2 with other models using datasets in several languages such as Flores-101. The results show that Baichuan 2 outperforms the other models in all test tasks.

![image](https://github.com/user-attachments/assets/a6640e9a-a43d-4a1b-b7d9-0d8fe11e7281)

**Security Evaluation**: the authors evaluated the security of Baichuan 2 using multiple datasets such as Toxigen and BHED. The results show that Baichuan 2 has some advantages over other models in terms of security.

![image](https://github.com/user-attachments/assets/6f2d4d9e-3025-4a92-bcab-be4f4bcc0c9a)

**Intermediate Checkpoint Comparison**: the authors also show the performance of Baichuan 2 for intermediate checkpoints (from 22 to 264 billion). The results show that the performance of Baichuan 2 continues to improve as training progresses and there is still room for further improvement.

## Conclusion

### 1. Advantages of the Thesis
  1. **Huge size**: Baichuan 2 has two versions, with 700 million and 1.3 billion parameters, respectively, and has been trained on over 2.6 trillion tokens of training data, which makes it one of the largest language models available.
  
  2. **Multi-language support**: Unlike most other open source language models, Baichuan 2 not only focuses on English, but also supports multiple languages, including Chinese and others.
  
  3. **Powerful performance**: Baichuan 2 has achieved significant performance gains in multiple benchmarks, especially on maths and code problems, as well as medical and legal domain tasks.
  
  4. **Open source**: Baichuan 2 is completely open source, which allows researchers to freely access and use the model to accelerate research and development.
 
### 2. Innovative points
  1. Improved Transformer Architecture: Baichuan 2 employs an improved Transformer architecture that includes larger layers and more attention heads to improve the expressiveness and efficiency of the model.
  
  2. Better preprocessing techniques: Baichuan 2 uses better preprocessing techniques such as adaptive learning rate adjustment and dynamic scaling to speed up training and improve model quality.

  3. Dialogue Understanding and Contextual Understanding: Baichuan 2 also introduces two chat models dedicated to dialogue and contextual understanding, which perform well on related tasks.
     
### 3. Future Works
  1. Improving multilingual support: although Baichuan 2 already supports multiple languages, it can be further extended to more languages to better meet the needs of users worldwide.
  
  2. Enhancing safety and ethical considerations: While Baichuan 2 has already taken some steps to reduce bias and toxicity, safety and ethical considerations need to be further enhanced to ensure that its application does not have a negative impact.
  
  3. Promoting an open source culture: The success of Baichuan 2 proves the importance of open source language models, and therefore the promotion of an open source culture should be continued in the future to encourage more researchers to participate in the research and development of this field.
  
