# Safety-tuned LLaMAs: Lessons from Improving the Safety of Large Language Models That Follow Instructions
[paper link](https://arxiv.org/pdf/2309.07875) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the security of training large language models to follow instructions.          | LLMs         |

## Methodology

### 1. Abstract
The authors argue that models that emphasise only usefulness without considering harmlessness may follow malicious instructions and generate harmful content. Therefore, they propose an approach that incorporates some security examples when training the model to improve its security, and demonstrate that this approach does not significantly reduce the model's capabilities or usefulness. However, excessive security training may cause the model to reject cues that appear to be secure but are actually safe. Overall, this study sheds light on the need to trade off helpfulness and security when training large language models.

### 2. Method Description 
The aim of this study is to explore how to ensure safety and accountability when using instruction fine-tuning models in Natural Language Processing (NLP). The authors begin by describing existing research on the issue of LLM security and point out that the lack of security data is an important factor limiting the model's ability to follow instructions. To address this issue, the authors create a new safety training dataset and combine it with a generic instruction response dataset to evaluate the safety performance of the model.

![image](https://github.com/user-attachments/assets/e5fa908b-1062-4d32-ac69-5615c62bc673)

### 3. Methodological improvements
The authors improved the security performance of the model by adding security data to the training dataset. They used the red team questions and their corresponding model responses from the Anthropic Red Teaming Dataset, as well as the ‘safe’ responses generated by GPT-3.5-turbo, and after manually reviewing the responses and confirming their safety and appropriateness, they converted them into the command response dataset The GPT-3.5-turbo was used to generate the command response dataset. They then randomly selected 20,000 instructions from the Alpaca dataset and added varying numbers of safe instructions (100, 300, 500, 1000, 1500, and 2000) to study the impact of increasing the amount of safe data. Finally, they used Low Rank Adaptation (LoRA) technique to fine-tune three different models and select the best checkpoints with minimal loss of validation.

### 4. Issues addressed 
The main objective of this study was to address the security issues that can arise when using instructions to fine-tune models. The authors argue that if security is not considered during the fine-tuning process, the fine-tuned model may produce harmful content. Therefore, the authors propose a new training dataset containing safety data and improve the safety performance of the model by adding safety data. This research provides a more responsible and safe approach to fine-tuning in the field of NLP.

## Experiments
This paper focuses on research in the area of adding security data to large language models to improve their security. The authors used six different secure datasets to train the language models and compared the security and quality of the different models with two different evaluation methods and metrics. The following is a detailed description of each comparison experiment:

**Effect of Adding Safety Data on Model Harmful Responses**
The authors used a reward model based on absolute harm to measure the extent of a model's harmful response, and combined this model with OpenAI's Content Audit API to determine whether the response provided by the model was malicious. The results show that adding safety data significantly reduces the harmful responses generated by the model.

**Impact of different types of instructions on the model**
The authors created three new types of directives (involving controversy, immigration, and violence, among others) and used them to test the model's performance. The results show that even on these more sensitive topics, adding safety data still allows the model to provide safer responses.

![image](https://github.com/user-attachments/assets/d6f20b4c-942d-4b10-ac1d-67110d01f26b)

**Manual labelling experiment**
The authors manually conducted a preference study comparing model response quality and safety. They selected 50 instructions from four different datasets and recorded whether the models provided good or bad responses. The results show that adding safety data does not significantly affect the general answering ability of the model, but significantly improves the safety of the model.

![image](https://github.com/user-attachments/assets/596a2a48-db0e-4aca-89ad-b0d7c0b18927)

**Differences between model opinions and behaviour**
The authors found that when models were asked for their opinion on one of their questions, they were more inclined to provide secure responses than when they were directly instructed to perform a malicious behaviour. This suggests that there is an inconsistency between a model's behaviour and its opinion.

![image](https://github.com/user-attachments/assets/25c910f6-9edd-4255-bc15-cda854af2eab)

**Impact of the amount of security data**
The authors found that the security performance of the model improved significantly after adding a certain amount of security data. However, too much safety data may cause the model to exaggerate safety issues.

![image](https://github.com/user-attachments/assets/9bace20d-5ed6-49e4-9fa9-680806f21fd9)

**Impact of different prompt formats on the model**
The authors used three different cue formats (question, instruction, and hybrid) to train the models and compare their performance on different datasets. The results show that the cue format used by the model during training has a significant impact on its response security.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper addresses the security problem of LLMs, which has attracted much attention in recent years, and propose an effective solution.
  
  2. The authors find experimentally that adding some security samples during training can significantly improve the security performance of the model without affecting its overall performance.
  
  3. In addition, the article introduces a variety of evaluation metrics and test datasets that enable other researchers to easily reproduce and extend these results.

### 2. Innovative points
  1. The main contribution of this article is to propose a simple yet effective method to improve the security performance of LLMs.
  
  2. The core idea of the method is to introduce a small set of well-designed safety samples in the training phase to enhance the model's ability to recognise dangerous queries.
  
  3. The advantage of this approach is that it is easy to implement and does not require significant additional computational resources.
  
  4. In addition, the article provides some useful tips and suggestions to help readers better understand and apply these techniques.

### 3. Future Works
Although the scheme proposed in this article has achieved some success, there are still many challenges and limitations. For example, issues such as how to select appropriate security samples and how to balance security and practicality in different application scenarios require further research and exploration. Therefore, we expect to continue to explore these issues in depth and develop more efficient and reliable techniques to secure LLM in our future work. 
