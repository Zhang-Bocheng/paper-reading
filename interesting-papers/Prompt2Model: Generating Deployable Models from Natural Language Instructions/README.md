# Prompt2Model: Generating Deployable Models from Natural Language Instructions
[paper link](https://arxiv.org/pdf/2308.12261) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes an approach called Prompt2Model that converts natural language task descriptions into deployable special-purpose models.          | Machine Learning         |

## Methodology

### 1. Abstract
Compared to traditional special-purpose NLP models, Prompt2Model does not require significant computational resources and can be accessed through an API.Prompt2Model performs multistep processing by retrieving existing datasets and pre-trained models, generating datasets using LLMs, and performing supervised fine-tuning on these retrieved and generated datasets. 

Experimental results show that given the same small number of cued inputs, Prompt2Model trains a model that is on average 20% better than the strong LSTM gpt-3.5-turbo, while being only 700 times its size. In addition, this approach can be used to obtain reliable performance estimates, enabling model developers to assess model reliability prior to deployment.Prompt2Model is open-sourced on GitHub. 

![image](https://github.com/user-attachments/assets/a37b90ee-c2f2-4552-a28b-f7fe63a8c2a8)

### 2. Method Description 
Prompt2Model is an automated machine learning pipeline system that provides a platform to automate the components of data collection, model training, evaluation and deployment. The centerpiece of the system is an automated data collection system that obtains labeled data relevant to user needs by using datasets generated from dataset retrieval and LLM (pre-trained language models). The authors then use the pre-trained models and fine-tune them on the training dataset to improve performance. Finally, they evaluate the trained model on the test dataset and optionally create a Web UI to interact with the model.

Prompt2Model is a generalized set of methods designed to be modular and extensible; each component can be implemented differently or disabled as needed. We first provide an overview of our framework and then describe our reference implementation in the next section.

![image](https://github.com/user-attachments/assets/c1764098-8ad5-4a76-af24-3822920ab1ee)

### 3. Methodological improvements
**Prompt Parser**: as the main part of the input, the user is provided with prompts similar to those used for pre-training language models. These prompts include a command and optionally some examples demonstrating the behavior of the task. While this open interface is user-friendly, an end-to-end machine learning process may benefit from a Prompt Parser that handles these inputs.

**Dataset Retriever**: the authors first try to discover manually annotated data that supports the user's task description. There are three directions for design decisions: which datasets should be searched? How to index datasets for the search? Which dataset columns are necessary for the user's task and which should be ignored?

**Dataset Generator**: not all possible tasks have any existing annotated data, and many tasks are only marginally relevant to existing datasets. To support a wide range of tasks, the authors introduce a dataset generator that generates synthetic training data according to user-specific requirements. This component faces challenges in terms of cost efficiency, generation speed, sample diversity, and quality control.

**Model Retriever**: in addition to the training data, the author must determine the appropriate model to fine-tune. They treat this problem as a retrieval problem, where user-generated descriptions and metadata such as popularity or number of supported tasks are represented in each model. Model Retriever in our reference implementation uses pre-trained models on Hugging Face for searching.

**Training**: given the retrieved and generated datasets and the pre-trained models, the authors use Model Trainer to fine-tune a subset. Currently, they perform model training by treating all tasks as text-to-text generation but they emphasize that this approach can be extended to support new methods.

**Evaluation**: after fine-tuning the model, the authors give the remaining data to the Model Evaluator module. Choosing the correct metrics for arbitrary tasks is a difficult problem. They present a suggested strategy for task-independent evaluation.

**Web App Creation**: to enable developers to make models available to partners or users, the authors also include an optional component called Demo Creator to create a graphical interface to interact with models.

### 4. Issues addressed 
  1. Prompt2Model is designed to support a variety of tasks and provide an automated platform to handle the components of data collection, model training, evaluation, and deployment.
  
  2. The core of the system is an automated data collection system that obtains labeled data relevant to user needs by utilizing dataset retrieval and LLM-generated datasets.
  
  3. In addition, the system is modular and extensible, allowing different components to be implemented or disabled as needed. This makes Prompt2Model a flexible tool for a wide range of tasks, helping to speed up the machine learning process and improve model performance.
  
## Experiments
This paper focuses on the performance of the Prompt2Model system on different tasks and compares it with other methods. Specifically, the following three comparison experiments are conducted in this paper:

**Performance Comparison between Prompt2Model and LLM In this experiment**, the authors tested the Prompt2Model system using three tasks, namely, SQuAD, MCoNaLa, and Temporal, and compared the results with the pre-trained model, gpt-3.5-turbo. The experimental results show that Prompt2Model produces more accurate models than gpt-3.5-turbo on both tasks, which indicates that Prompt2Model is able to generate high-quality models efficiently.

**Performance Comparison of Prompt2Model with Manually Labeled Data In this experiment**, the authors compared the data generated by Prompt2Model with manually labeled data to assess the quality of the data generated by Prompt2Model. The experimental results show that the data generated using Prompt2Model can achieve similar performance as manually labeled data, which means that Prompt2Model can help users save a lot of time and cost.

**Performance Comparison between Prompt2Model and Real Data In this experiment**, the authors use the data generated by Prompt2Model to evaluate the performance of several candidate models and compare the results with real data. The experimental results show that Prompt2Model-generated data can effectively identify real modeling improvements and can be used to differentiate between different candidate models so as to select the model that is most likely to perform well in downstream tasks.

![image](https://github.com/user-attachments/assets/520491d0-0115-40fe-acbc-df32f39a24c9)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a framework called Prompt2Model that automatically builds task-specific models, using natural language prompts to do so.
  
  2. The framework is easy to use and generates accurate mini-models as well as datasets for estimating real-world performance.
  
  3. In addition, Prompt2Model is designed to be scalable and modular, making it a platform for advancing model distillation, dataset generation, synthetic evaluation, dataset retrieval, and model retrieval.

Future Outlook

### 2. Innovative points
  1. The main innovation of Prompt2Model is its ability to automatically build task-specific models, which enables users to create their own NLP models without the need to have knowledge of deep learning.
  
  2. In addition, Prompt2Model provides an easy-to-use interface that enables users to quickly generate their own models and test them.
  
  3. The framework can also generate different datasets as needed to help users better understand how their models perform in different situations.
     
### 3. Future Works
  1. The paper raises a number of interesting research questions, such as how to determine the amount of data to generate and how to mix the retrieved datasets to achieve complementary advantages.
  
  2. Additionally, the paper addresses the issue of human involvement in correction, either by providing potential strategies to help humans iteratively improve the prompts or by allowing humans to post-process the task metadata extraction and generated data if it does not match their intentions.
  
  3. At the same time, the authors also point out some limitations such as the system's dependence on closed-source APIs and the lack of support for non-English languages, which are among the directions for future research. 
