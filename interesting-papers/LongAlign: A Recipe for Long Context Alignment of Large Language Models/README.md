# LongAlign: A Recipe for Long Context Alignment of Large Language Models
[paper link](https://arxiv.org/pdf/2401.18058) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an approach called LongAlign for training large language models for long context alignment.          | Self-supervised Learning         |

## Methodology

### 1. Abstract
The approach involves constructing a long instruction-following dataset built using Self-Instruct, employing a packing and sorting batch strategy to accelerate supervised fine-tuning, and developing a loss-weighting method to balance the contribution of different sequences to the loss. In addition, they introduce the LongBench-Chat benchmark to evaluate the performance of the instruction-following capability on queries of length 10k-100k. Experimental results show that LongAlign improves performance by 30% over existing LLM methods on long context tasks while maintaining its ability to handle short generic tasks.

### 2. Method Description 
In this paper, LongAlign is proposed as a self-supervised learning algorithm based on a large-scale pre-training model, aiming to improve the performance of the model in a long text environment. The method enables the model to better understand and process long text data by introducing long text information in the pre-training process. Specifically, LongAlign splits a long text into multiple short text segments and combines them with the corresponding task queries to form a task sample. During pre-training, the model needs to predict the answer of each short text fragment based on the task query, so as to learn how to process long text data effectively.

![image](https://github.com/user-attachments/assets/c3b708a7-49c2-4170-b73e-3b7c1a98936c)
 
### 3. Methodological improvements
In order to further improve the performance of the model in the long text environment, this paper proposes two effective training strategies: packing and sorted batching. among them, the packing strategy reduces the idle time of the model when processing long text, while the sorted batching strategy accelerates the training process and maintains a relatively uniform length of sequences within a batch The In addition, this paper proposes a new benchmark test set, LongBench-Chat, for evaluating the model's instruction adherence ability in a long text environment.

### 4. Issues addressed 
The main contribution of this paper is to propose a new self-supervised learning algorithm, LongAlign, as well as an effective training strategy and a new benchmark test set to address the poor performance of the model in long text environments. With these approaches, the model can better understand and process long text data and achieve better results in various critical user-intensive scenarios. Also, LongBench-Chat can be used as a criterion for other researchers to evaluate their models' ability to follow instructions in long text environments.

## Experiments
This paper focuses on four experiments conducted by the authors to explore the impact of adding long instruction data to a large-scale pre-trained model on downstream task performance. Specifically, the authors conducted the following four experiments:

**Comparing the effects of different magnitudes of long instruction data on model performance**
In this experiment, the authors used three different magnitudes of long instruction data (0k, 5k, and 10k) to train the model and compare their performance in downstream tasks. The results show that as the amount of long instruction data increases, the performance of the model gradually improves on the long task, while maintaining relatively stable performance on the short task. This suggests that adding sufficient long instruction data to a large-scale pre-trained model can significantly improve the model's ability on long tasks without affecting its performance on short tasks.

![image](https://github.com/user-attachments/assets/b4c8ed42-23a2-42b5-97da-d194538c9589)

**Comparing the effect of different sources of long instruction data on model performance**
In this experiment, the authors compare the effects of two different sources of long instruction data sets (LongAlign and LongAlpaca) on model performance. The results show that the LongAlign dataset better improves the model's performance on both long and short tasks, especially the ability to follow and understand long tasks. This suggests that the diversity and quality of data need to be considered when selecting LongAlign data to obtain better results.

![image](https://github.com/user-attachments/assets/95658c4e-ca67-4f30-b858-a733672f4b6e)

**Exploring the effect of different training methods on model performance and training efficiency**
In this experiment, the authors compare the effects of three different training methods (naive batching, packing and sorted batching) on model performance and training efficiency. The results show that two efficient training methods, packing and sorted batching, can significantly improve the training efficiency while maintaining good model performance. In addition, the authors found that different training methods have different applicability to different types of models, e.g., for the ChatGLM3-6B model, the use of packing+loss weighting strategy can significantly improve the model performance on long tasks.

![image](https://github.com/user-attachments/assets/8694f7de-ae21-4c70-ae5a-647f365e98ca)

**The effects of model size and context length on model performance are discussed and learning curves are analysed**
In this experiment, the authors explored the effects of model size and context length on model performance and analysed the learning curve. The results show that as the model size and context length increase, the performance of the model on long tasks gradually improves, but it is also accompanied by higher computational cost and longer training time. In addition, the authors found that in some cases, too large a model and context length may lead to overfitting of the model, which reduces its generalisation ability. Therefore, when designing large-scale pre-training models, factors such as model size, context length and training time need to be considered to achieve optimal results.

![image](https://github.com/user-attachments/assets/090f2ed9-fcfc-4df9-b692-b471c9244be7)

## Conclusion

### 1. Advantages of the Thesis
  1. By collecting long sequences and generating 10k instruction data using Self-Instruct, LongAlign is able to construct a diverse long instruction following dataset.
A Packing strategy is employed to address the imbalance between inputs of different lengths, and a loss weighting strategy is proposed to balance the contribution of different sequences to the loss.

  2. LongBench-Chat is developed as a benchmark test to evaluate the performance of the model, including open-ended long text inference, encoding, summarisation, and multilingual translation tasks.
  
  3. Experimental results show that LongAlign effectively improves the model's ability to handle contexts up to 64k tokens long without affecting its performance on general tasks.

### 2. Innovative points
  1. The LongAlign framework is proposed to provide a solution for long-term context processing by constructing a diverse long instruction-following dataset, employing an efficient training strategy, and developing a reliable evaluation benchmark.
  
  2. Packing strategy and loss weighting techniques are used to address the imbalance between inputs of different lengths and improve the training efficiency.
  
  3. LongBench-Chat was developed as a benchmark test for evaluating model performance, covering a wide range of long text processing tasks.

### 3. Future Works
  1. Further exploration can be done to increase the diversity of long instruction following datasets by utilising more source data.
  
  2. Attempts could be made to apply the LongAlign framework to other types of natural language processing tasks, such as question and answer systems or machine translation.
  
  3. Improvements to the LongBench-Chat benchmarks could continue to be made to cover a wider variety of tasks and a wider range of contexts.    
