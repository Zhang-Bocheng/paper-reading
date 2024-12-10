# GPT-4V(ision) is a Human-Aligned Evaluator for Text-to-3D Generation
[paper link](https://arxiv.org/pdf/2401.04092) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a text-to-3D model generation assessment metric that is automatic, flexible and consistent with human preferences.          | Text-to-3D Generation         |

## Methodology

### 1. Abstract
While traditional evaluation methods focus on a single criterion, the metric proposed in this paper allows comparison based on user-defined criteria and evaluation of 3D models with GPT-4V-generated cues. Experimental results show that the metrics are highly consistent with human preferences under different evaluation criteria.

### 2. Method Description 
The paper presents a methodology for evaluating the performance of a text-to-3D model generator. It is divided into two main parts: **automatic cue generation and a 3D asset comparator.** Firstly, the selection of appropriate prompts as input text prompts is achieved by using meta-prompts to guide GPT-4V on how to automatically generate a list of prompts based on the input evaluation criteria. Secondly, a meta-prompt that can compare any two 3D shapes is designed and fed into the 3D shape generator along with random noise to obtain a set of 3D shapes generated for each model. Finally, each model was assigned a score and ranked using the Elo scoring system.

![image](https://github.com/user-attachments/assets/7230ed44-becb-4a94-a51a-cf9ba6d4b3dd)

### 3. Methodological improvements
The method improves on the previous manual creation of cue lists by using meta-cues to automatically generate multiple cue lists of varying complexity and creativity, allowing for more precise control of the input cue distribution in order to better examine the performance of the text-to-3D model generator.

![image](https://github.com/user-attachments/assets/276283f0-aad6-43ce-9af9-323867c7e203)

### 4. Issues addressed 
This method addresses the problem of evaluating the performance of a text-to-3D model generator by providing a more flexible and automated method for generating cues suitable for specific evaluation criteria, and by allowing the distribution of input cues to be controlled by adjusting parameters such as complexity and creativity in order to more accurately examine the performance of the generator.

## Experiments
This paper presents a study of evaluation methods for text-to-3D model generation. Firstly, the authors propose the use of an Elo scoring system to quantify the performance between different models and maximise the likelihood estimation to obtain a final Elo score. Then, the authors perform a preliminary evaluation comparing the method to five criteria of human judgement, showing that the method performs best on four criteria and has the highest average correlation. In addition, the authors show how the method can be used to perform a comprehensive evaluation of different models and provide radar charts and rankings under different criteria. Finally, the authors discuss how the method can be extended to accommodate other criteria of interest to users.
![image](https://github.com/user-attachments/assets/99a95de0-cd5d-4fa9-9db8-0a2024c49840)

## Conclusion

### 1. Advantages of the Thesis
  1. A novel approach is proposed to use GPT-4V to build an evaluation metric for text-to-3D model generation tasks that is customisable, scalable and consistent with human judgement.
  2. A meta-prompting system was used to enable GPT-4V to automatically generate input prompts based on the evaluator's needs, increasing the flexibility of the evaluation metric.  
  3. A guidance template was designed to enable GPT-4V to compare two 3D shapes and score them according to user-defined criteria, resulting in automatic ranking.
Experimental results show that the method outperforms existing metrics across a range of criteria and can more accurately reflect human judgement.

### 2. Innovative points
  1. The capabilities of Large Multimodal Models (LMMs), in particular GPT-4Vision (GPT-4V), are utilised to meet the three basic capabilities of the evaluation metrics: generating input textual cues, understanding human intent, and reasoning about the 3D physical world.  
  2. A ‘meta-prompt’ system was designed to enable the GPT-4V to automatically generate input prompts based on the needs of the evaluator, increasing the flexibility of the evaluation metrics.  
  3. A guidance template was designed to enable GPT-4V to compare two 3D shapes and score them according to user-defined criteria, thus enabling automatic ranking.

### 3. Future Works
  1. Further expand the study to validate the hypotheses and improve the accuracy of the evaluation metrics.
  2. Address possible error issues with GPT-4V, such as illusions and biases, to ensure the validity and reliability of the evaluation metrics.
  3. Improve the efficiency of evaluation metrics by using GPT-4V intelligent selection of input prompts.
  4. Explore how GPT-4V can be applied to the design of evaluation metrics in other domains. 
