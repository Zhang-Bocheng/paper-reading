# The FinBen: An Holistic Financial Benchmark for Large Language Models
[paper link](https://arxiv.org/pdf/2402.12659) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a comprehensive financial benchmark test called FinBen for evaluating the performance of large language models in finance.          |  Large Language Models (LLMs)        |

## Methodology

The benchmark consists of 36 datasets and 24 tasks covering seven key aspects of information extraction, text analysis, question and answer, text generation, risk management, forecasting and decision making. The authors also present a number of innovations, such as the first assessment of stock trading and three new open-source assessment datasets. By evaluating 15 representative large-scale language models, the authors find that these models perform well in information extraction and text analysis, but struggle with complex tasks such as text generation and prediction. In addition, the authors describe FinBen's use in hosting the first shared task on financial language models and demonstrate its potential to drive innovation in large-scale language models in finance.

## Experiments
This paper focuses on financial evaluation tasks based on zero-shot and small amount of supervised learning, including five aspects, such as information extraction, text analysis, question answering, generation and decision making, and designs corresponding datasets and evaluation metrics for each task. Among them, the information extraction task focuses on entity recognition, relationship extraction and causal detection, while the text analysis task involves sentiment analysis, news headline classification and risk prediction. In these tasks, the authors use a variety of financial domain datasets, such as EDSUN, FINRED, Fin Arg AUC, etc., and employ a variety of evaluation metrics, such as accuracy, precision, recall, F1 score, etc., to measure the performance of the models. Ultimately, the authors tested and compared several pre-trained language models related to the financial domain, and came up with the performance, strengths and weaknesses of each model on different tasks, which provides a reference for subsequent research.

![image](https://github.com/user-attachments/assets/fbeb8051-14c0-4398-aee3-3d200313101c)

## Conclusion

### 1. Advantages of the Thesis
  1. This broad coverage makes FinBen one of the most comprehensive benchmarks available for evaluating LLMs in the financial domain, allowing for a more comprehensive assessment of LLM capabilities and demonstrating their ability to handle complex financial scenarios.
  2. In addition, this paper proposes several new evaluation strategies, such as agent-based evaluation and retrieval-augmented generation (RAG)-based evaluation, which provide a more dynamic and realistic way of evaluating LLMs, reflecting their ability to interact with large-scale data and retrieve relevant information from it.
  3. Also, this paper presents three novel datasets that provide a new standard for the research community to advance LLM research.
 
### 2. Innovative points
  1. **New tasks:** FinBen introduces a large number of new tasks and datasets, making it one of the most comprehensive benchmarks for LLM assessment in finance that currently covers the largest number of tasks and datasets.
  2. **Broader coverage:** FinBen covers seven areas of finance, including essential tasks such as stock trading, which involves complex decision-making processes that affect market dynamics and investment strategies.
  3. **New Evaluation Strategies:** FinBen is the first assessment benchmark to introduce agent-based evaluation and RAG-based evaluation, which provide a more dynamic and realistic approach to LLM assessment.
  4. **Novel datasets:** FinBen proposes three novel datasets for text summaries, Q&A, and stock trading tasks, providing a new standard for the research community to advance LLM research. 

  
