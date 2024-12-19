# Multilingual Instruction Tuning With Just a Pinch of Multilinguality
[paper link](https://arxiv.org/pdf/2401.01854) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper focuses on how to improve a model's instruction adherence for multiple languages when performing instruction fine-tuning in a multilingual environment.          |  Large-scale Multilingual     instruction   |

## Methodology

### Abstract
The authors first find that even fine-tuning with only a monolingual dataset can result in models with some instruction adherence in other languages. Then, they successfully improve the model's instruction adherence ability in multiple languages by integrating a small number of multilingual samples into the English fine-tuning set, and that the use of mixed multilingual training allows for better cross-language generalisation relative to monolingual fine-tuning. Finally, the authors suggest that when building large-scale multilingual instruction fine-tuning models, good results can be achieved by using only a small fraction of multilingual instruction responses.
  
## Conclusion

### 1. Advantages of the Thesis
  1. This paper investigates the performance of a multilingual pre-trained model in a cross-language instruction following task and explores how its performance can be improved by adding multilingual data.
  2. The authors use high-quality natural language instruction and response datasets, as well as an experimental setup based on the PaLM 2 model, making the results more reliable and convincing.
  3. By experimenting with different numbers of languages and proportions of data, the authors found that even using only a very small amount of multilingual data can significantly improve the performance of the model, which provides valuable guidance for practical applications.

### 2. Innovative points
  1. This paper presents a new experimental framework for evaluating the performance of multilingual pre-trained models in a cross-lingual instruction following task.
  2, The authors use an automated evaluation protocol and model scoring method to ensure consistency and reliability of the results.
  3. By designing a series of experiments, the authors discovered the importance of multilingual data and made some useful suggestions such as using fewer languages for multilingual training.

### 3. Future Works
  1. Future research can further explore how multilingual data can be used to improve the performance of other types of natural language processing tasks.
  2. Consideration could be given to extending existing experiments with more languages and larger datasets to gain a more comprehensive understanding of the impact of multilingual data.
  3. Different pre-training models and techniques could also be experimented with in combination with multilingual data to obtain better performance and results.
