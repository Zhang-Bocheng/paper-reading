# RLVF: Learning from Verbal Feedback without Overgeneralization
[paper link](https://arxiv.org/pdf/2402.10893) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores how high-level verbal feedback can be used to modify or tailor the behaviour of large language models to meet specific requirements and preferences.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
Using high-level verbal feedback alone can lead to overgeneralisation to irrelevant contexts. To address this problem, the authors propose a new approach, Contextualised Critiques with Constrained Preference Optimization (C3PO), which improves the performance of large language models (LLMs) by transforming high-level verbal feedback into a small synthetic preference dataset and fine-tuning it while keeping the original model behaviour intact, effectively applying verbal feedback to relevant scenarios while reducing the problem of overgeneralisation.

### 2. Method Description 
This paper presents an approach called Contextualized Critiques with Constrained Preference Optimization (C3PO), which aims at adapting the behaviour of a model through higher-order verbal feedback without the need for extensive manual annotation. The method uses a powerful generic model (e.g., GPT-4) to translate a piece of verbal feedback z into a dataset that can be used for fine-tuning to address feedback adherence issues and avoid overgeneralisation. 

The dataset consists of three sub-datasets, Dinscope, Dout-of-scope and Dnear-scope, which are used to demonstrate changes in the desired behaviour, to keep the model outside of the feedback range, and to antagonistically design the dataset used to fine-tune the model's understanding of when to apply feedback, respectively.

![image](https://github.com/user-attachments/assets/aefca9e3-bd41-4297-8f7f-9c40ec31349d)

### 3. Methodological improvements
  1. The main innovation of C3PO is its ability to efficiently process higher-order verbal feedback and transform it into datasets that can be used to train models.
  2. Specifically, it first uses GPT-4 to generate a set of feedback-related cue categories, and then for each category it generates a set of feedback-related cues that should actually be needed to adjust the model's behaviour.
  3. In addition, a set of cues that approximate the feedback but are not actual inputs is generated in order to control for model degradation on completely irrelevant behaviours. Finally, a fixed set of feedback-independent cues was used to avoid this degradation.

### 4. Issues addressed 
The goal of C3PO is to help machine learning models better understand and adapt to user feedback, thereby improving model performance. Traditional reinforcement learning methods can lead to overgeneralisation of the model, i.e., applying feedback not only when it should be applied, but also when it should not be applied.C3PO addresses this problem by optimising the model with constraints so that it applies feedback only in appropriate scenarios. This approach helps machine learning models adapt to user needs faster and improves model accuracy and efficiency.

## Experiments
This paper describes five experiments conducted by the authors to address the issue of learning to give verbal feedback, and explores the effects and influences of different approaches. A detailed description of each experiment is given below:

Experiment 1: Investigates **the occurrence of the overgeneralisation problem** and the effect of C3PO on this problem. The effect is assessed by comparing the existing methods with the change in behaviour of the model after adapting to feedback with C3PO. The results show that C3PO is more effective than other methods in reducing the overgeneralisation problem while maintaining in-range feedback compliance.

Experiment 2: Investigates whether **simple modifications are effective in improving the standard method's handling of verbal feedback**. The experiment explored two modifications: In-Context+ CoT and SCD+ Negatives, and the results showed that both approaches reduced the overgeneralisation problem, but they did so at the expense of in-scope feedback compliance.

Experiment 3: Investigates whether **C3PO can learn more than one feedback and explores the effect of choosing the form of constraint loss on C3PO**. The results show that mixing two different feedback parameters did not reduce in-range feedback compliance or alter out-of-range behavioural change.

Experiment 4: Examined **how in-range feedback compliance and out-of-range behavioural change were weighed when using C3PO**. Results show that C3PO balances both aspects more effectively than other methods.

Experiment 5: Investigates **how C3PO limits changes in model behaviour rather than simply maximising the probability of the baseline model**. The results show that this stronger constraint significantly impairs in-range feedback compliance.  

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new method, C3PO, for learning the behaviour of large language models (LLMs) and tuning them with single-sentence feedback.
  2. C3PO uses existing LLMs to generate small fine-tuned datasets that contain both user-supplied feedback descriptions and non-relevant input behaviour that should be retained.
  3. Experimental results show that C3PO significantly reduces overgeneralisation when adapting to feedback and is able to keep behaviours corresponding to irrelevant inputs unchanged.
  4. The researchers also explored several future questions, such as how to perform continuous learning and whether stricter constraints are needed.
 
### 2. Innovative points
  1. C3PO uses the powerful prior knowledge of existing LLMs without the need for additional human supervision or large amounts of manually labelled data.
  2. C3PO proposes a new joint optimisation objective to maximise implicit rewards for feedback scenarios and minimise cross-entropy losses, thus adapting to feedback while keeping the model's behaviour unchanged on uncorrelated inputs.
  3. C3PO's approach is highly efficient and accurate, and has shown promising results in several examples. 

### 3. Future Works
  1. Further research can be done on how to better handle complex feedback information and how to achieve better performance in different tasks and application scenarios.
  2. It could also be explored how to combine C3PO with other techniques, such as adaptive control and reinforcement learning, to improve the adaptability and robustness of the model.
  3. In addition, it could be investigated how to make models more explanatory in order to better understand their decision-making processes and behaviour.   
