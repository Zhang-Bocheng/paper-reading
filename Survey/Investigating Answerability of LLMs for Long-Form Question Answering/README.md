# Investigating Answerability of LLMs for Long-Form Question Answering
[paper link](https://arxiv.org/pdf/2309.08210) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper focuses on the answerability of Large Language Models (LLMs) in long-form question-answer tasks, and proposes an abstract summary-based question generation method to evaluate the performance of different types of LLMs.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Experimental results show that the method is able to challenge the inference and deduction abilities of LLMs, while revealing performance differences between LLMs, especially for longer texts from abstracts, where the generative ability of open-source LLMs decreases significantly. This study contributes to a better understanding of the capabilities, limitations, and differences of LLMs, providing guidance for future research.

### 2. Method Description 
The evaluation method presented in this paper uses Wikipedia articles as a data source and collects articles from different domains by controlling the diversity of the categorised lists. For articles of longer length, the SpaCy lexicon is used to extract data from each section and combine the shorter sections. In order to fairly compare different models, a maximum context length of 2k tokens was set in the experiments. 

What is more, a preprocessing filter was used to filter out non-informative documents. In the question generation process, a summary of the original document is first generated using ChatGPT, and then questions are generated based on the summary. To avoid random order question generation, ChatGPT was instructed to provide the first three complex questions to answer. Finally, a total of 1350 questions were generated for 50 articles in each setting.

![image](https://github.com/user-attachments/assets/53fab4fd-bf08-4104-8d60-a3e0bb1fea95)

### 3. Methodological improvements
The methodological improvement in this paper lies in the use of ChatGPT to generate questions, rather than just generating questions directly from articles. This approach makes better use of natural language processing techniques and improves the quality and accuracy of the questions.

### 4. Issues addressed 
This paper addresses the problem of how to generate a high-quality and diverse dataset of questions and answers. The method can be used not only for evaluating the performance of various language models, but also for dataset construction for other NLP tasks.

## Experiments
This paper focuses on an evaluation methodology for generating question complexity and uses it to conduct comparative experiments on several pre-trained language models. Specifically, the authors devised multiple metrics for evaluating question complexity and used these metrics to evaluate questions generated from two different contextual sources (summaries and paragraphs). 

![image](https://github.com/user-attachments/assets/4a79d1ff-c859-4077-9c20-222c71e264dc)

During the experiments, the authors used a variety of pre-trained language models, including ChatGPT, Alpaca-7B, 13B, LLama-7B, 13B, and LLama, and validated the assessment metrics by comparing them to human answers. Finally, the authors draw several experimental results and conclusions, including the performance differences of different models, the effect of context length on model performance, and so on.

![image](https://github.com/user-attachments/assets/9c607518-246c-4d34-ab2a-191ab4f63784)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes an automated evaluation setup for generating questions and evaluating LLM answers using GPT-4.
  
  2. The results show that this approach is very challenging for testing the reasoning capabilities of LLMs, revealing a performance gap between large-scale LLMs and open-source LLMs.
  
  3. The researchers also explored the limitations and restrictions of the LLM, such as the fact that the ability of GPT-4 as an evaluator is not yet fully understood, and that the distribution of the training data is unknown.
 
### 2. Innovative points
  1. A question generation method based on document summaries is proposed for more in-depth testing of the inference capabilities of LLM.
  
  2. The use of GPT-4 for answer quality assessment is highly correlated with human assessment results, increasing the reliability of the study.

### 3. Future Works
  1. Explore more tasks applicable to LLM, such as long text generation.
  
  2. Develop better methods to utilise longer contextual information to improve LLM performance.
  
  3. Gain insight into the training data distribution and the learning process of LLM to better understand its capabilities and limitations.  
