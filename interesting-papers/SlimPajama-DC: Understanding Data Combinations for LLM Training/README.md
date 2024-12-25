# SlimPajama-DC: Understanding Data Combinations for LLM Training
[paper link](https://arxiv.org/pdf/2309.10818) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |The aim of this paper is to investigate the impact of different data combinations on the pre-training of large language models and to empirically analyse them through the SlimPajama-DC research design.|     Large Language Models (LLM)     |

## Methodology

### 1. Abstract
Two key observations were identified in the study: first, the effect of global versus local de-duplication on model performance; and second, the effect of the proportion of highly de-duplicated multi-source datasets in the combination on model performance. The experiments were conducted using the Cerebras-GPT model and tools such as Alibi and SwiGLU for large-scale training on a Cerebras 16× CS-2 cluster. Ultimately, it was found that increasing data diversity is crucial for model effectiveness after global de-emphasis

### 2. Method Description 
The paper presents a large-scale text dataset called SlimPajama, which contains data from multiple sources and is optimised by removing low-quality documents, global de-duplication and other processing. In addition, the impact of the proportion of data from different sources on model performance and the use of techniques such as importance sampling and DSIR for data selection are explored.

### 3. Methodological improvements
Compared to traditional text datasets, SlimPajama has a larger scale and more diverse sources, which makes it better able to capture the complexity and diversity of human language. Also, by pre-processing the data, such as de-duplication and filtering, it improves training efficiency and reduces the risk of overfitting.

### 4. Issues addressed 
In large-scale natural language processing tasks, a large amount of high-quality data is required to train models. However, acquiring these data is often a time-consuming and expensive task. Therefore, how to build a large-scale and diverse text data integration has been a key concern for researchers. The SlimPajama dataset proposed in this thesis provides a new idea and solution to solve this problem.

## Experiments
This paper focuses on the performance of different combinations of data on different tasks using the SlimPajama model and draws some conclusions and recommendations from the analysis.

Firstly, the authors evaluated the SlimPajama model using the Huggingface Leaderboard Evaluation framework. They tested four key benchmarks including AI2 Reasoning Challenge, HellaSwag, MMLU, and TruthfulQA. the results showed that all other data combinations except DC-4 had higher average scores than RedPajama-1.3B, which was also trained based on 330B tokens. Among them, the data combination relying only on SlimPajama Commoncrawl (DC-1) achieved the highest score on ARC and MMLU, but its performance on TruthfulQA was the worst. On the other hand, DC-6 achieved the best average accuracy and was also the best performer on HellaSwag. As seen in DC-1, 2, 5, and 6, more domain combinations and diverse training data can lead to better overall accuracy. In addition, one potential strategy is to train step-by-step in the order of DC-1, DC-6 and DC-7.

![image](https://github.com/user-attachments/assets/1b42a335-c3ae-42f9-8d71-85cd684a8dd8)

Secondly, the authors also conducted additional domain evaluations to investigate the fine-grained capabilities provided by different data combinations. The inclusion of additional sources other than DC-7 typically improved average performance. For example, DC-1 performed best in ARC Challenge and Race, while DC-4 outperformed other combinations in Wino-grande and Xstory cloze, and DC-5 performed best in the WSC273 evaluation. In addition, all configurations except DC-4 had higher average performance in comparisons with GPT-neo-1.3B and RedPajama-1.3B.

![image](https://github.com/user-attachments/assets/26ad1874-3e6e-4b4f-8494-52f5bc4bf18a)

In order to more accurately demonstrate the true potential of the model and to reflect the capabilities of different data combinations, the authors introduced a new metric, RRGS (Risky Random Guess Score), to assess the degree of random guessing in the model predictions. The metric uses the average l1 distance to measure the difference between model predictions and random guesses. The results show that the higher the average model score, the lower the probability of random guessing.

Finally, the authors show training loss curves for different combinations of data and draw several observations from them. While the DC-7 showed the highest average accuracy in the quantitative evaluation, it also had the highest training loss. This suggests that lower training losses do not necessarily lead directly to better model performance. Additionally, the large amount of data from the code domain resulted in the lowest training loss for DC-3, which means that the training loss decreases as the amount of code in the training data increases. The training loss values for the other combinations seem to be relatively stable.

![image](https://github.com/user-attachments/assets/91f27262-72d8-4aec-b753-f1b9e35b1e7a)

## Conclusion

### 1. Advantages of the Thesis
This paper presents a data-domain weighting and combination research methodology called SlimPajama-DC that operates on compact models and whose benefits can be seamlessly transferred to models several times larger, thus significantly accelerating training on SlimPajama. With this study, the authors aim to further explore data-centric approaches to enhance the understanding and efficiency of pre-training large language models.
  
### 2. Innovative points
The main contribution of this article is the proposal of the SlimPajama-DC method, which explores how to manage the integration and scaling issues of diverse datasets by performing global and local de-duplication of datasets from multiple sources, as well as the study of different ways of combining thoroughly de-duplicated datasets. In addition, the article explores the trade-off between specialisation and generalisation and provides application cases regarding efficient large-scale batch training.

### 3. Future Works
Future research could further explore how more sophisticated algorithms and techniques can be used to optimise the distribution of different domains and types in a dataset to improve model performance and efficiency. It is also possible to consider applying this approach to machine learning tasks in other domains to achieve better results.
