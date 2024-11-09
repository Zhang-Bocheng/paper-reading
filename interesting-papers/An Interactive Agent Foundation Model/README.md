# An Interactive Agent Foundation Model
[paper link](https://arxiv.org/pdf/2402.05929) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new approach, called the Interactive Agent Foundation Model, for training AI agents that perform well across multiple domains, datasets, and tasks.          | Multimodal         |

## Methodology

### 1. Abstract
The approach uses multiple pre-training strategies, including visual mask autoencoders, language modelling and next-step prediction, to achieve an AI framework that is flexible enough to adapt to different scenarios. Experimental results show that the model is capable of generating meaningful and contextually relevant outputs in domains such as robotics, gaming AI, and healthcare, as well as effective multimodal and multitask learning using multiple data sources. This approach provides a promising avenue for the development of general-purpose, action-capable, multimodal systems.

### 2. Method Description 
The model presented in this paper is a pre-trained model based on visual, linguistic and action capabilities for generating powerful general-purpose tools in a variety of interaction tasks. The model combines three main components: **textual cues, video inputs and action sequences**. On each sample, three loss functions are used: **language modelling, automatic coding of masked images and action modelling**. For the pre-training process, the authors used a wide range of robotics and game datasets and represented each input sample as a sequence S = (W, V1, A1, V2, A2,... , VT, AT), where W is the labelled sequence of text instructions, Vi is the sequence of image blocks for frame i, and Ai is the sequence of action labels for frame i. For each sample, the loss function includes the above three components.

![image](https://github.com/user-attachments/assets/4a029b7f-cdf7-4523-aeb3-5eb523917c78)

### 3. Methodological improvements
The main innovation of this paper is the proposal of a multi-task learning framework aimed at evaluating the performance of the model in different scenarios. Specifically, the authors apply the model to three main domains: robotics, gaming and healthcare. For each domain's task definition and dataset, the authors fine-tuned the model separately to validate its performance in various interaction tasks. In addition, the authors also annotate some game videos using GPT-4V in order to more accurately guide the robot's operation.

### 4. Issues addressed 
The main goal of this paper is to design a general-purpose model that is capable of handling a variety of interaction tasks, such as robot manipulation, game play, and healthcare. Through the application of a multi-task learning framework, the authors demonstrate that the model has a considerable competitive advantage in these domains, exhibiting reasonable performance. This multitask learning approach provides a promising direction for the study of cross-domain interaction tasks.

## Experiments
This paper describes a number of comparative experiments conducted by the authors, including the application and comparison of the effectiveness of pre-trained models in a number of domains, as well as model tuning and performance analysis for different tasks.

Firstly, the authors conducted experiments with pre-trained models, using a variety of datasets to train the models, with detailed parameter settings and descriptions of the training process. Then, the authors applied the pre-trained models to different domains, such as gaming, robot manipulation, and healthcare, and evaluated and compared their performance. Specifically, the authors tested the pre-trained models in several games such as Language Representation, Calvin and Minecraft, and the results showed that the pre-trained models performed better in these games compared to the models trained from scratch. 

In addition, in robot manipulation, the authors tested using two datasets, Language-Table and Calvin, and the results showed that the pre-trained models also outperformed in these tasks. Finally, in healthcare, the authors tested the models using three tasks: video description, visual quizzing and activity recognition, and the results showed that the pre-trained models also performed better in these tasks.

![image](https://github.com/user-attachments/assets/7de2712e-f43b-4cf1-ac1c-097d0dec923d)

![image](https://github.com/user-attachments/assets/6346d609-a574-437b-8c9c-1b7d0e77ca79)

## Conclusion

### 1. Advantages of the Thesis
The paper presents a new Interactive Agent Foundation Model (IAFM) capable of processing text, visual data, and motion inputs, and has been tested in a wide range of applications in several domains. The authors used a variety of robotics and game data to pre-train the model so that it can perform well on tasks in different domains. In addition, the model is scalable and versatile and can be used to build intelligences in multimodal systems.

### 2. Innovative points
The methodological innovation of this thesis is the proposal of a unified pre-training framework that treats text, visual data and actions as independent tokens and jointly trained. By using the pre-trained linguistic and visual linguistic models to initialise the sub-modules, the model is enabled to better understand the environment and the user's behaviour. The model can also be applied to multiple domains, including robotics, game AI, and healthcare.

### 3. Future Works
Although the model has been applied in several domains, more research is needed to further improve its performance and reliability. For example, in healthcare, the model may need more testing and validation before it can be widely used in clinical practice. In addition, with the development of technology, we can also expect the development of more advanced and complex multimodal systems to meet the growing demand.   
