# TruthfulQA: Measuring How Models Mimic Human Falsehoods
[paper link](https://arxiv.org/pdf/2109.07958) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper presents a new benchmarking method for measuring whether language models are truthful and trustworthy when answering questions.         |  LLMs         |

## Methodology

### 1. Abstract
The test included 817 questions covering 38 categories including health, law, finance and politics, some of which were questions that humans would give false answers to due to false beliefs or misunderstandings. The results showed that the best models could only answer 58 per cent of the questions correctly, compared to a human performance of 94 per cent. 

In addition, these models generated many false answers that mimicked popular misconceptions and could deceive humans. While performance improves with increasing model size in other NLP tasks, the results of this study suggest that this trend does not apply if the false answers are learnt from the training distribution. Therefore, the authors recommend fine-tuning using training objectives other than text imitation, rather than just scaling up the model size, to improve veracity.

![image](https://github.com/user-attachments/assets/cb07612b-f403-49a1-97b1-ee5e5ea0bd7b)

### 2. Method Description 
The paper presents a benchmark test, called TruthfulQA, for evaluating the performance of NLP models in generating truthful answers. TruthfulQA consists of 817 questions covering 38 categories and is only applicable in a zero-sample setting. The questions were written by the authors to elicit responses that mimic errors. Each question has authenticity references and sources that support these answers (e.g., Wikipedia pages). These questions were designed to test for weaknesses in the model's performance on truthfulness, rather than testing the model's performance on useful tasks.

![image](https://github.com/user-attachments/assets/a7e4576c-7abb-4eff-89aa-a6b3f67863fb)

### 3. Methodological improvements
TruthfulQA employs a strict truth criterion, whereby a statement can only be considered true if it corresponds to a real-world reality. This approach is similar to criteria such as scientific articles or Wikipedia. For the generated statements, they are assigned a real number between 0 and 1, which can be interpreted as the probability that the statement is true. This approach also allows for adjusting thresholds as needed to improve interpretability.

In addition, TruthfulQA takes into account the amount of information, since the answer should not only be true, but also provide information about the question to reduce uncertainty. Therefore, when evaluating the model, an evaluation regarding the amount of information is also performed.

### 4. Issues addressed 
TruthfulQA aims to measure the performance of NLP models in generating truthful answers. It uses rigorous criteria to define truthfulness and associate it with reliable, publicly available evidence. In this way, TruthfulQA can help researchers better understand how models perform in terms of truthfulness and informativeness, and facilitate the development of more accurate and reliable NLP techniques.

## Experiments
This paper focuses on zero-sample benchmarking of language models on the TruthfulQA dataset. The authors used four different model families and compared them with different sizes and different prompts. In addition, they performed two additional tasks, including a multiple-choice task and a comparison between automated evaluation metrics and human evaluations.

First, the authors applied four different model families (GPT-3, GPT-Neo/J, GPT-2, and UniﬁedQA) to the generation task on the TruthfulQA dataset. The results showed that the largest GPT-3 model performed the worst in terms of truthfulness, with only 58% of the responses being truthful, compared to 94% of the truthful responses from human participants. In addition, for all model sizes and cues, the best model (GPT-3-175B with ‘useful’ cues) produced only 21% true and informative answers. 

Second, the authors conducted a multiple-choice task to examine the performance of the model when choosing answers rather than generating them. The results showed that large models performed worse than small models in the multiple-choice task, regardless of model size. For example, the largest GPT-Neo/J was 17% untruthful, compared to only 60 times as much for the 125M-sized model. These results suggest that while larger models may be more capable in some situations, they may sacrifice veracity for information.

Finally, the authors conducted a comparison between automated evaluation metrics and human evaluation. They used a new automated metric, GPT-judge, which was fine-tuned from the GPT-3-6.7B model to classify answers to TruthfulQA questions as true or false. The results show that GPT-judge is able to predict human ratings of truthfulness with a validation accuracy of 90-96%. In addition, GPT-judge can be well generalised to new answer formats, such as UniﬁedQA models, whose architecture and pre-training approach are different from GPT models, and which generate answers with very different forms and contents. 

![image](https://github.com/user-attachments/assets/592074db-7d96-4a72-879c-1568d6774ed8)
![image](https://github.com/user-attachments/assets/85acc222-8a08-4632-a0a8-43e7d31570a8)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new benchmark test, TruthfulQA, for assessing the truthfulness of large language models when answering general knowledge questions.
  
  2. The researchers measured the model's ‘mimetic lies’ by designing a series of questions about issues that humans often misspeak or misunderstand, such as about historical events, scientific facts, and so on.
  
  3. The paper conducted experiments using GPT-3 and several other models and found that current language models perform poorly in zero-sample situations and lack truthfulness.
  
  4. The researchers also explored how truth can be used as an objective function to train the models to improve their truthfulness and reliability.

### 2. Innovative points
  1. TruthfulQA is a new benchmark test that focuses on whether a model is truthful in answering general knowledge questions, rather than focusing on the model's accuracy like other tests.
  
  2. The researchers designed a series of questions to measure the model's ‘mimetic lies’ in areas of knowledge that humans often misstate or misunderstand, such as historical events and scientific facts.
  
  3. The paper also proposes a phenomenon called ‘backscaling,’ where the probability of making an error increases as the size of the model increases because the model tends to learn distributions that are similar to the training data, which may contain more misinformation.
     
### 3. Future Works
  1. This study provides a new benchmark test for assessing the fidelity and reliability of large-scale language models, which can facilitate research and development in related fields.
  
  2. Future research could explore how to further improve the model's veracity and reliability, for example, by modifying the training objective function or using better datasets for training.
  
  3. In addition, researchers could consider applying TruthfulQA to other fields, such as healthcare and law, to help ensure the reliability and safety of the model in real-world applications.  
