# OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web
[paper link](https://arxiv.org/pdf/2402.17553) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a dataset and benchmark test called OmniACT, designed to evaluate the capabilities of a virtual agent that can automatically generate executables to complete computer tasks.          | Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
The dataset covers a wide range of basic tasks for desktop applications and includes long-period tasks. Given screenshots and natural language task descriptions, the goal is to generate a script that will allow it to fully execute the task. The authors used several powerful baseline language models to run on their benchmark, with the strongest baseline being GPT-4, which performs the best on this benchmark, but its performance level only reaches 15 per cent of human capabilities, demonstrating the challenging nature of traditional web agents on this task. This benchmark provides a platform for measuring and evaluating advances in the automation of computer tasks by language modelling agents, and inspires future work to build multimodal models that link large language models to the visual basis of the computer screen.

### 2. Method Description 
This paper presents OmniACT, a new dataset and benchmark designed to measure the performance of autonomous agents in web and desktop applications. The dataset contains parallel data including natural language tasks, UI screenshots and PyAutoGUI scripts required to implement these tasks. 

By defining the input state as the current screen S and the natural language task T, the goal is to learn the transition function f : T × S → A, where A denotes the sequence of operations that can successfully complete the task T. The task T can be performed by a sequence of actions. Tasks can be executed by mouse and keyboard operations, such as clicking, dragging, scrolling, etc. To ensure high quality data, the authors used the following steps:

![image](https://github.com/user-attachments/assets/ee0544c1-7544-4fd0-af52-343714142ed3)

&emsp;**Application and website selection**: multiple applications and websites were selected and bounding boxes were created for each application or website and labelled with their functionality.
<br>&emsp;**Screen segmentation**: manually create bounding boxes to annotate and segment screens using different techniques.
<br>&emsp;**Functionality labelling**: use Amazon Mechanical Turk workers to map each bounding box to the correct functionality description.
<br>&emsp;**Task Creation**: Create tasks using all human-annotated bounding boxes and their labels to execute on a single screen.
<br>&emsp;**Reverse Mapping and Filtering**: Build scripts to map text labels back to numeric coordinates and verify that the task will execute on the screen. Remove all non-working or syntactically incorrect data points and manually review the task collection.

### 3. Methodological improvements
  1. The main innovation of the OmniACT dataset is that it is a multimodal dataset covering both desktop and web applications.

  2. In addition, the dataset provides detailed task descriptions and visual guides, making it more interpretable and usable. The dataset has a larger action space than previous benchmarks, including multiple mouse actions and keyboard actions.

### 4. Issues addressed 
This dataset addresses some of the challenges in autonomous agent evaluation, such as the lack of a common benchmark across different tasks and applications and the lack of detailed task descriptions and visual guides. By providing a comprehensive multimodal dataset, OmniACT helps to advance the development of autonomous agents, thereby improving their performance in real-world applications.

## Experiments
This paper focuses on evaluating metrics and benchmarking models for tasks targeting desktop applications, and comparing the performance of different models through a series of experiments. Specifically, the authors first propose two new evaluation metrics: **sequence scores and action scores**, which are used to measure a model's ability to predict the correct sequence of operations as well as to execute code correctly. Then, the authors conducted experiments using three types of models: **cue-based language models, fine-tuned language models, and cue-based multimodal models**. Among them, the cue-based language models include LLaMA-7B, Vicuna-7B, LLaMA-13B, Vicuna-13B, Palmyra-Instruct-30B, CodeLLaMA-34B, Palmyra-X 43B, GPT-3.5-turbo-0613, and GPT-4; the fine-tuned language models include LLaMA-13B and Vicuna-13B; and cue-based multimodal models include GPT-4 and GPT-4 Vision API.Finally, the authors also collected human evaluation data and compared it with machine learning models.

![image](https://github.com/user-attachments/assets/2bafde74-1e7d-45e5-a0a7-5838152c9ff2)

For the cue-based language models, the authors found that GPT-4 performed the best, with higher sequence scores and action scores than the other models. Meanwhile, CodeLLaMA-34B also performed well, with both sequence scores and action scores outperforming other models of the same size. However, these models have serious problems in handling click coordinates because they only rely on text signals. To address this issue, the authors conducted experiments with cue-based multimodal models and showed that using the entire image as input significantly improves the model's ability to predict coordinates. In addition, the authors tested human performance and found that in most cases humans were able to perform the task well, but in some cases experienced difficulties, such as not being able to fully understand the task, having difficulty relating the task to the screenshots provided, or not being familiar with the UI. 

## Conclusion

### 1. Advantages of the Thesis
  1. A new task and dataset is proposed: the OmniACT, containing over 9.8K pairs of images and commands, for evaluating the capabilities of autonomous virtual agents.

  2. The research team designed customised performance metrics to measure the performance of the models in performing computer tasks.

  3. Multiple agents based on language models were benchmarked and the gap between existing models and human performance was demonstrated.

  4. The performance of current state-of-the-art multimodal models was analysed and directions for future research were proposed.

### 2. Innovative points
  1. A new module, DetACT, is proposed for creating textual representations of the screen, using information such as OCR signals, colours and icon template matching.

  2. Mouse and keyboard operations are automated through the use of the PyAutoGUI library, enabling the model to perform specified tasks in a variety of applications.

  3. A unique dataset was designed to cover UI screens and natural language instructions across different operating systems and web environments.
     
### 3. Future Works
  1. Research based on this dataset could advance the broader field of application automation.

  2. Future efforts should focus on developing more general and flexible multimodal models to better understand visual and user interface elements on computer screens.

  3. Further research and improvements in language and multimodal models are needed in order to address possible illusions and biases of specific data types in the models.  
