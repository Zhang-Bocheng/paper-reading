# Tougher Text, Smarter Models_ Raising the Bar for Adverarial Defence Benchmarks
[paper link](https://arxiv.org/pdf/2501.02654) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper discusses the vulnerability of deep learning models in natural language processing to adversarial attacks and presents a comprehensive benchmark to evaluate the performance of various defence mechanisms on different datasets, models and tasks.          |  Deep Learning        |

## Methodology

### 1. Abstract
The benchmark test covers a wide range of datasets, state-of-the-art defence mechanisms, and extends the evaluation to critical tasks such as single-sentence classification, similarity and synonym recognition, natural language reasoning, and absurd reasoning. This work not only provides a valuable resource for researchers and practitioners, but also identifies future research priorities in the field of textual adversarial defence.

### 2. Method Description 
The paper describes two adversarial training methods: **gradient descent-based PGD, FreeLB and TAVAT**, and two regularisation methods: **Flooding-X, Adversarial Label Smoothing (ALS) and Temperature Scaling (TS)**. These methods aim to improve the robustness of NLP models in the face of adversarial attacks.

### 3. Methodological improvements
Among them, gradient descent-based PGD, FreeLB and TAVAT methods accelerate the optimisation process, but their effectiveness is affected by perturbations in the embedding space. Therefore, ASCDDong et al. (2021) and DNE (Zhou et al., 2021b) propose a more reasonable embedding space defined as the convex hull of lexical synonyms. However, this approach requires pre-computation of synonyms, limiting its adaptability and effectiveness. Therefore, this paper highlights the need for structure free defence strategies that do not rely on knowledge of synonyms.

Furthermore, regularisation methods such as Flooding-X, ALS and TS do not rely on model structure or synonym sets, making them applicable to a wide range of tasks; Flooding-X prevents over-confidence by keeping the loss around a predefined ‘flood’ level; ALS reduces the model's confidence in incorrect predictions by modifying the training target; and TS reduces the model's confidence in incorrect predictions by modifying the training target. ALS reduces the model's confidence in false predictions by modifying the training target; and TS improves the model's true robustness by temperature scaling.

### 4. Issues addressed 
These approaches provide structure-free defence frameworks that do not rely on synonym knowledge, are applicable to a variety of NLP tasks, and improve the robustness of models against adversarial attacks.

## Experiments
This paper focuses on adversarial attack and defence experiments performed on models for different tasks in the field of Natural Language Processing, and the results are analysed and summarised.

Firstly, the authors selected six different NLP datasets including tasks such as single-sentence classification, similarity and semantic understanding, and used three state-of-the-art pre-trained models (BERT, RoBERTa and DeBERTa) as benchmark models. The authors then tested these models against attacks and used seven different defence methods, including temperature adjustment-based methods, label smoothing, pre-attack attacks, and more. Finally, the authors provide a detailed analysis and comparison of the results for each dataset and each attack method.

![image](https://github.com/user-attachments/assets/f3eea14b-4044-47a9-9f20-d3a81b50fc92)

Specifically, in the task of single-sentence classification, TTSO and TTSO++ perform the best, which can effectively alleviate the overfitting problem and improve the robustness of the model. In contrast, in similarity and semantic understanding tasks, the authors found that generative large language models (e.g., Llama and ChatGPT) did not perform as well as smaller, discriminative models (e.g., BERT, RoBERTa, and DeBERTa), which could be attributed to the performance degradation due to their high number of parameters. In addition, the authors point out the limitations of some common attack methods, such as the Flooding-X attack method that may limit the learning ability of the models. 

![image](https://github.com/user-attachments/assets/7426c986-f37f-4227-9449-bbd116a422eb)

![image](https://github.com/user-attachments/assets/7c24d721-828d-4ddd-b784-6c8a3b4e7ff0)

## Conclusion

### 1. Advantages of the Thesis
  1. The method utilises entropy as an uncertainty measure and dynamically adjusts the temperature parameter, which achieves the goal of improving the robustness of the model while maintaining high accuracy under inputs of varying difficulty. Experimental results show that TTSO++ achieves the best performance on multiple datasets with efficient training speed and small computational cost.
  2. And, the article systematically compares and summarises the existing text classification defence methods, which provides a valuable reference for research in related fields.

### 2. Innovative points
  1. The most innovative point of TTSO++ is the introduction of entropy, an uncertainty measure, which improves the robustness and accuracy of the model by dynamically adjusting the temperature parameter to adapt to inputs of different difficulties.
  2. And, the method is very simple to implement, requiring only an additional step in the training process, without changing the model structure or using complex algorithms.
  3. This simple yet effective defence mechanism can be applied to various types of NLP tasks, including single-sentence classification, similarity recognition, natural language reasoning, etc., and thus has wide applicability and utility. 

### 3. Future Works
  1. The defence effect can be improved by further optimising the temperature adjustment strategy;
  2. Exploring other types of data enhancement techniques to further improve the robustness of the model.
  3. In addition, with the development of new neural networks such as LSTM, TTSO++ can also be considered to be applied to these new architectures to validate its effectiveness.   
