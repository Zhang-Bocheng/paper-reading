# Reformatted Alignment
[paper link](https://arxiv.org/pdf/2402.12219) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | The aim of this paper is to improve the consistency of Large Language Models (LLMs) with human values by reformatting existing instruction data to better conform to predefined criteria and evidence through a simple but effective method, REALIGN.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method reduces manual labelling, illusions and scaling difficulties, and maintains orthogonal relationships with existing conformance techniques. Experimental results show that REALIGN significantly improves the general consistency ability, mathematical reasoning, factuality and readability of LLM. Furthermore, the general consistency ability of the Alpaca dataset can be improved by 67% using only 5% of the REALIGN data. Thus, this work highlights the need for further research into the scientific and mechanistic interpretations of LLM. The authors have publicly released the code and data to support future research.

### 2. Method Description 
This paper proposes a method called REALIGN for improving the performance of NLP models on specific tasks. The method is divided into three main steps: (1) defining predefined criteria, (2) retrieving external information to enhance the quality of responses for knowledge-intensive tasks, and (3) reorganising the original responses to conform to the specified criteria. Through these three steps, REALIGN is able to effectively improve the performance of the model on different tasks.

![image](https://github.com/user-attachments/assets/6ace9c29-e03f-4beb-b582-ee827f7d55a5)

### 3. Methodological improvements
Compared to traditional methods based on manually labelled data, REALIGN adopts a more automated approach, which reduces the cost of human intervention and allows for quicker adaptation to new task requirements. At the same time, REALIGN leverages the capabilities of large-scale language models, allowing the models to answer questions with a stronger knowledge base and understanding.

### 4. Issues addressed 
  1. The problem of poor performance of NLP models on specific tasks. By classifying and formatting tasks and using external knowledge sources, REALIGN can significantly improve the performance of models on different tasks.
  2. Traditional methods based on manually labelled data are costly and inefficient. REALIGN uses an automated strategy that significantly reduces the cost of data preparation and can be adapted to new task requirements in a short period of time.

## Experiments
This paper describes a series of comparative experiments conducted by the authors when using deep learning models to make instruction calls to natural language text. The main experiments include the following:

**Dataset selection and model selection:** the authors selected two high-quality manual datasets and one data-enhanced dataset based on generative methods, and chose two commonly used open-source base models for fine-tuning.

**Command calling ability assessment:** the authors designed a variety of assessment metrics to evaluate the command calling ability of the models, including general command calling ability and domain-specific command calling ability (e.g., mathematical reasoning, factual truthfulness, and readability, etc.).

**Analysis of experimental results:** the authors found through experiments that the model with the addition of data augmentation showed significant improvement in both general instruction invocation ability and domain-specific instruction invocation ability. Meanwhile, the authors also conducted a comparison of data enhancement methods and an impact analysis of data enhancement ratios, and concluded that a small amount of data enhancement is sufficient to improve model performance.

![image](https://github.com/user-attachments/assets/f0ea4bba-a5d1-4acd-8bde-3b2488b638d1)
 
## Conclusion

### 1. Advantages of the Thesis
Instead of creating instruction data from scratch, the method uses existing instruction data to generate higher quality data. The authors used five different existing instruction datasets and verified REALIGN's performance in a variety of benchmark tests, including general alignment, mathematical reasoning, and factuality and readability. The experimental results show that REALIGN significantly improves a variety of tasks.

### 2. Innovative points
The REALIGN method is a simple but effective way to combine human-defined preferences with the generative capabilities of LLM to produce better command data. The method is implemented in three main steps:(1) defining criteria; (2) retrieving enhancements; and (3) reformatting. These steps enable humans and LLMs to work together to produce more accurate, structured and supported responses. In addition, the method provides a detailed evaluation framework that can help researchers better understand its performance.

### 3. Future Works
Further research and definition of additional tasks and formats is needed to cover more diverse and regionalised scenarios. Finally, the reasons behind the success of REALIGN need to be explored in depth for additional scientific and mechanistic explanations.    
