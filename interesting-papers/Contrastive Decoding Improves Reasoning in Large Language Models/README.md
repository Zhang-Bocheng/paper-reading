# Contrastive Decoding Improves Reasoning in Large Language Models
[paper link](https://arxiv.org/pdf/2309.09117) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a text generation method called ‘Contrastive Decoding’, which is a simple, lightweight and untrained generation method. The method improves the quality of generation by searching for strings that maximise the weighted difference between strong and weak models.           |   Large Language Models (LLMs)       |

## Methodology

### 1. Abstract
Experimental results show that contrastive decoding can significantly outperform greedy decoding on a range of inference tasks and performs well on several benchmark tests. Furthermore, the analysis shows that contrastive decoding is able to prevent a number of abstract inference errors and avoid behaviours such as simply copying input segments. As a result, contrastive decoding becomes a powerful and general method that can be used in language modelling to generate long texts as well as in reasoning tasks.

### 2. Method Description 
The paper proposes a decoding strategy called Contrastive Decoding (CD) for improving the quality of expert model-based text generation. The method enhances the quality of the generated results by introducing a penalty term in the generation process to limit the similarity between the generated results and the expert model.

Specifically, the CD algorithm first selects two parameters: **α and the amateur temperature τa**. where α is a scaling factor indicating that a fraction of the maximum probability assigned to each token by the expert model is retained; and τa is the temperature parameter of the amateur model, which controls the randomness and diversity in the generation process. The CD algorithm then calculates a penalty term based on these parameters and adds it to the generation process to ensure that the generation results are closer to the predictions of the expert model.

Compared to the original CD algorithm, the improved version proposed in this paper is easier to explain and implement, and also allows better control of the randomness and diversity in the generation process. In addition, the algorithm can be regarded as a minor perturbation to the predicted results of the expert model, which can be used to balance the quality and diversity of the generated results by adjusting the strength of the penalty term.

![image](https://github.com/user-attachments/assets/8ac4a812-a3f9-4d59-a422-fbd0897009dc)

### 3. Methodological improvements
  1. **Easier to interpret and implement**: the original article requires manual selection of the two hyperparameters α and τa, and some complex mathematical operations to get the final results. In contrast, the improved version proposed in this paper can work directly in logit space and only needs to choose the hyperparameter β.
  
  2. **Better control of randomness and diversity in the generation process**: the improved version proposed in this paper can balance the quality and diversity of the generated results by adjusting the hyperparameter β. When β tends to 0, the penalty term disappears and the generated results will be more diverse; while when β tends to infinity, the generated results will be more inclined to the prediction results of the expert model.
  
  3. **A small perturbation to the prediction result of the expert model**: since the CD algorithm is introducing a penalty term in the generation process to limit the similarity between the generated results and the expert model, it can be regarded as a small perturbation to the prediction result of the expert model. This perturbation can be used to balance the quality and diversity of the generated results by adjusting the strength of the penalty term.
     
![image](https://github.com/user-attachments/assets/a8f22fba-b981-4cfe-a24b-22bb4172c6b8)

### 4. Issues addressed 
  1. **Generation results are not accurate or diverse enough**: traditional expert model-based text generation methods often only consider the prediction results of the expert model and ignore the diversity and randomness in the generation process. This leads to generation results that are often too homogeneous or inaccurate.
  
  2. **How to balance the quality and diversity of the generated results**: although existing methods can increase the diversity of the generated results by adjusting hyperparameters such as temperature parameters, how to balance the quality and diversity of the generated results is still a challenge. The CD algorithm proposed in this paper can balance the quality and diversity of the generated results by introducing a penalty term, which makes the generated results both accurate and diverse.

## Experiments
This paper focuses on an experimental study of Contrastive Decoding, an enhancement method for chained thought reasoning models based on self-supervised learning. The study validates the effectiveness of Contrastive Learning by comparing the performance of models of different sizes and types on multiple tasks, and explores its principles and limitations.

First, the authors conducted experiments comparing contrastive learning with **other enhancement methods**, including Self-Consistency and Negative Prompting. The results showed that contrastive learning achieved the best results on most tasks, especially on tasks requiring higher-order reasoning skills, such as logical reasoning and common-sense reasoning.

![image](https://github.com/user-attachments/assets/8826a439-64b5-46b9-b72d-be52f5db97d0)

Second, the authors also conducted experiments on **the selection of key parameters** in contrast learning, including mask ratio, contrast strength, and amateur model size. The results showed that the best results were obtained with a mask ratio of 0.1, the best results were obtained with a contrast strength of 0.5, and a small amateur model could improve the effectiveness of contrast learning.

![image](https://github.com/user-attachments/assets/1b2c3cce-1875-4cd5-950a-e6295be84406)

In addition, the authors conducted experiments on the application of contrast learning in different types of tasks, including arithmetic reasoning, general knowledge reasoning and multiple choice ranking. The results show that in the arithmetic reasoning task, contrast learning can help the model to better understand the questions and generate more accurate answers; while in the general knowledge reasoning task, contrast learning is helpful for the small-scale model but does not significantly improve the large-scale model; and in the multiple-choice ranking task, contrast learning can significantly improve the ranking accuracy of the model.

![image](https://github.com/user-attachments/assets/d271a9b5-a302-43f3-8510-48ac1ac63567)

![image](https://github.com/user-attachments/assets/364cc2c0-c2f0-46a1-bde7-7fd54bf103ff)

Finally, the authors also conducted experiments on some other aspects of contrast learning, such as the relationship between contrast learning and alpha masking, and whether contrast learning relies on chained thinking cues. These experiments further demonstrate the effectiveness and applicability of contrast learning. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes an approach called Contrastive Decoding (CD) to address the poor performance of large language models on inference problems.CD finds strings by searching for maximised weight differences, thus avoiding unwanted patterns in the distribution of expert models, such as short or generic strings, which are usually the most likely to appear in any model in a model.
  
  2. Experimental results show that CD performs better than traditional greedy decoding methods on several tasks, including benchmark test sets such as GSM8K and HellaSwag.
  
  3. In addition, the article analyses the reasons for CD's improvement and points out that it can reduce duplicates or other undesirable patterns, which provides directions for further improvements to the method.

### 2. Innovative points
  1. The CD method proposed in this paper is a new decoding algorithm that improves inference performance in large language models. Unlike traditional greedy decoding methods, CD can avoid unwanted patterns by maximising the difference in weights so that the model can answer questions more accurately.
  
  2. In addition, CD reduces the surface-level replication rate and decreases the number of missed inference steps, which is important for improving model performance.

### 3. Future Works
CD needs to be further optimised to address issues such as commonsense reasoning, and a better understanding of how CD affects the behaviour of models is needed. Therefore, in future research, the scope of CD and how it can be combined with other techniques to achieve better text generation and reasoning capabilities needs to be further explored. 
