# Empower Sequence Labeling with Task-Aware Neural Language Model
[paper link](https://arxiv.org/pdf/2410.09507) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an interactive platform called AERA Chat for automating the assessment of student answers and providing interpretable grading results.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Due to the lack of publicly available reasoning data and high annotation costs, current approaches typically rely on noisy reasoning generated by large language models (LLMs). To address these issues, the authors have developed the AERA Chat platform, which features innovative visualisations and powerful assessment tools that can be used by educators to assist in the marking process as well as by researchers to evaluate the performance of assessments and the quality of reasoning generated by different LLMs.

### 2. Method Description 
This paper presents a platform called AERA Chat, which aims to provide educators and AI researchers with a comprehensive environment for interpretable student answer assessment decisions. The main features of the platform include batch interpreting student answer assessment and reasoning, and interacting with Large Language Models (LLMs) to obtain detailed explanations or reflective assessment rationales.

![image](https://github.com/user-attachments/assets/e9633749-02c9-4bcd-b37e-b6243b223fb4)

Specifically, the AERA Chat platform contains the following two main components:

  1. **The batch marking interface**: the user can set up questions and a batch of student answers to be assessed. Once these inputs are submitted to the system, the backend will simultaneously process the student answers and query all LLMs selected by the user to obtain a marking decision and a rationale explaining this marking decision. Upon completion, our platform can highlight key components or rationales in the student's answer to draw the user's attention for better contextual understanding. In addition, our platform can automatically evaluate the assessment performance of LLM and display the metrics in a histogram.

![image](https://github.com/user-attachments/assets/e55d790e-b24b-4e47-8605-8aab7e4eda14)
  
  2. **Dialogue Interface:** In order to take advantage of the powerful chat capabilities of the LLM and use them to help with interpretive scoring of student answers, our platform also includes a dialogue interface that allows users to bring information about questions and rationales from the batch scoring system into their interactions with the LLM. Educators can use this feature to request more detailed explanations from LLM, while researchers can use LLM to reflect on their incorrect assessment rationale and regenerate assessment decisions.

![image](https://github.com/user-attachments/assets/5a4877c3-4b3f-4651-aaba-533e31c8ec1c)

### 3. Methodological improvements
In contrast to traditional rule- or feature-engineering based approaches, the AERA Chat platform employs deep learning techniques, specifically pre-trained language models (e.g., GPT-3.5-turbo, GPT-4, and AERA models), for automated student answer scoring and rationale generation. Instead of manually designing features or rules, this approach improves accuracy and efficiency by learning underlying patterns and regularities directly from raw text data.

In addition, the AERA Chat platform provides a rich set of tools and features to support users in assessing and editing grading quality and rationales. For example, users can select labels for correcting errors, choose better or worse rationales, and upload their own rating annotations as data for supervised fine-tuning. These features allow users more flexibility in adjusting the performance of the model and the quality of the output.

### 4. Issues addressed 
  1. because student answers are typically highly diverse and complex, an adaptive approach is needed to handle a wide range of answer types.
  2. the manual grading process is time-consuming, labour-intensive and error-prone, so an automated approach is needed to increase the speed and accuracy of grading.
  3. the scoring process lacked transparency and interpretability, making it difficult to discover the real reasons behind scoring decisions. By introducing the AERA Chat platform, it is able to effectively address these issues and provide users with an efficient, reliable and easy-to-use solution.

## Experiments
This paper focuses on an experiment to validate the evaluation capabilities of an automated assessment and interactive annotation interface using the AERA Chat platform. Four sub-datasets from the ASAP-AES dataset were used in the experiments to validate the performance of the models in different subject domains, and a unified evaluation methodology was used to compare the three model settings. Specifically, the experiments included the following two aspects:

  1. **Comparison of evaluation performance:** the experiments were conducted using external API models (gpt-3.5-turbo-0125 and gpt-4o-2024-05-13) as well as the AERA model with the same prompt statements as input. The results show that the AERA model performs best with zero sample queries because it was trained specifically for these datasets and is familiar with the prompt format, making this an in-domain test scenario. In contrast, generic models like GPT-3.5-turbo and GPT-4o show more accurate evaluation performance in zero-sample reasoning.
  
  2. **Human Assessment of Reasoning Quality:** To assess the quality of the generated reasoning, the experiments used the AERA Chat platform for human assessment. Specifically, the experiment randomly selected five student responses in each dataset for human assessment and used AERA Chat's built-in annotation feature to assess the rationales in two different ways: (1) the correctness of the rationales, i.e., the degree of matching with the key elements of the answer and the degree of following the scoring criteria; and (2) the user's preference for rationales generated by different LLMs. The results show that ChatGPT performs best in terms of correctness of justifications, especially when assessing responses with a score of zero. In contrast, GPT-4o and AERA are more capable of correctly assessing responses that score higher values. In the assessment of rationale preferences, AERA received the highest preference score, followed by GPT-4o.Although GPT-4o and ChatGPT produced more detailed rationales, they occasionally deviated from the assessment context, leading to incorrect assessment decisions, which was less popular with annotators.

![image](https://github.com/user-attachments/assets/030ada6c-b733-49d6-bf57-fa4f28c284c0)

## Conclusion

### 1. Advantages of the Thesis
  1. The platform automates assessment and rationale generation through the use of multiple LLMSs and features a novel user interface design that enhances the user's focus, as well as providing an environment for comparing rationales generated by different LLMs, and for verifying the quality of the rationales through direct annotation or selection of preferences.
  2. In addition, the platform demonstrates the effectiveness of its evaluation capabilities, including automated evaluation metrics and human preference evaluations using three LLMs on four datasets.

### 2. Innovative points
  1. The main contribution of this thesis is the development of the first open-source interactive platform dedicated to the scoring of explanatory student answers using LLMs.
  2. The platform employs novel design concepts, such as the use of a multilingual model, the optimisation of the visual interface, and the environment for rationale annotation, which provide a more practical and easy-to-use tool for researchers and practitioners in education.
  3. And, the platform can support both public and private LLM assessments, thus increasing its applicability and flexibility. 

### 3. Future Works
  1. The AERA Chat platform proposed in this thesis will have great prospects for development in the future. For example, it can further explore how to improve the performance and efficiency of LLMs to better adapt to different application scenarios;
  2. it can also consider how to incorporate other advanced techniques, such as deep learning and knowledge graphs, to improve the accuracy and reliability of the platform.  