# Towards Conversational Diagnostic AI
[paper link](https://arxiv.org/pdf/2401.05654) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an artificial intelligence system called AMIE, which is based on a large-scale language model (LLM) designed to help doctors make diagnoses through dialogue.          |  Large-scale Language Model (LLM)        |

## Methodology

### 1. Abstract
The authors used a novel self-playing simulation environment and used automated feedback mechanisms to train the system to deal with a variety of disease conditions, specialised domains and contexts. To evaluate the system's performance, the authors designed a framework that included clinically meaningful axes of history, diagnostic accuracy, managerial reasoning, communication skills, and empathy. In a randomised double-blind crossover trial, the authors compared AMIE with primary care physicians and showed that AMIE performed better in most conditions, with higher diagnostic accuracy and better patient communication skills.

### 2. Method Description 
This paper presents an AI system called AMIE for diagnosing conversational competence and clinical communication skills. The system is trained on multiple real-world datasets, including multiple-choice medical quizzes, long medical reasoning written by experts, electronic medical record summaries, and heavily transcribed medical dialogue interactions. During training, a multi-round self-learning environment and a self-play strategy were used to improve the system's knowledge and capabilities and to adapt to a variety of medical conditions and contexts.

![image](https://github.com/user-attachments/assets/0a22391c-c59c-447e-b717-ce37703aef53)

### 3. Methodological improvements
To address the problem that existing real-world datasets do not cover a wide range of healthcare situations and scenarios, as well as the problem of limited model generalisation and applicability due to poor data quality, this paper designs a self-play simulation learning environment that enables AMIE to self-learn in a virtual care environment. Through this environment, the knowledge and capabilities of AMIE can be extended to enable them to deal with more diverse healthcare situations and contexts.

### 4. Issues addressed 
By combining multiple real-world datasets and self-playing simulation learning environments, the system is able to cope with a wider range of medical situations and contexts, thus improving its knowledge, capabilities, and range of applications. This approach is very helpful in improving communication and understanding between doctors and patients, as well as contributing to the quality and efficiency of healthcare delivery.

## Experiments
This paper presents a multifaceted evaluation and comparative experiments on the application of a large-scale language model-based dialogue system in the field of medical diagnosis. Specifically, the authors used two different research methods to evaluate the performance of the system: first, an objective and quantitative evaluation by means of a dialogue with a human physician, and second, a questionnaire and other means to obtain subjective feedback from patients on the quality of the dialogue.

In the first experiment, the authors designed a remote On-Site Simulated Clinical Examination (OSCE) to test the differences between a dialogue system based on a large-scale language model (AMIE) and a real doctor (PCP). The experiment was divided into two parts: first, each simulated patient would have an online text-chat style consultation with a virtual doctor, and then they would have another consultation with a real doctor. Finally, all participants fill out a questionnaire about their experience of the dialogue. The results showed that AMIE had a higher diagnostic accuracy than real doctors and also outperformed real doctors in most aspects of dialogue quality and management.

![image](https://github.com/user-attachments/assets/2ef04e32-5e0f-48ae-89ef-b7526ddba413)

In the second experiment, the authors used two different self-learning strategies to train AMIE and evaluated it automatically. The results show that the inward self-learning strategy significantly improves the dialogue quality of AMIE.  

![image](https://github.com/user-attachments/assets/9fca8422-8d3e-4753-8e21-51afae57408d)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new AI system, AMIE, which is capable of optimising clinical dialogues and has diagnostic reasoning capabilities.
  2. Through comparative experiments with PCPs, AMIE is demonstrated to outperform PCPs on multiple clinically relevant axes and to simulate realistic clinical dialogue in the absence of traditional OSCE assessments.
  3. The study used a wide range of datasets, including patient data from different countries and regions, as well as evaluations of physicians and patients, increasing the reliability and utility of the study.

### 2. Innovative points
  1. A pre-trained language model (LLM) was used to build the AI system to enable it to conduct multi-round dialogues in a natural language environment.
  2. A virtual OSCE framework was used for evaluation in a simulated scenario, allowing the study to be conducted without real patients.
  3. A participatory design approach was used to collect feedback from doctors and patients, further improving the usefulness and user-friendliness of the system. 

### 3. Future Works
  1. AMIE can be applied to a wider range of healthcare areas, such as medication recommendations.
  2. Further research on how to improve the fairness and inclusiveness of the system to avoid bias and inequality in historical dialogues.
  3. Develop a more intelligent AI system that can automatically learn and update medical knowledge to improve diagnostic accuracy and efficiency. 
