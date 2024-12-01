# Tuning LLMs with Contrastive Alignment Instructions for Machine Translation in Unseen, Low-resource Languages
[paper link](https://arxiv.org/pdf/2401.05811) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an approach called AlignInstruct to address two challenges encountered by Large Language Models (LLMs) in machine translation: the extension of supported languages to previously unseen languages and the lack of data for low-resource languages.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Through comparative experiments, the authors find that the use of MT instructions effectively applies the LLM to new languages, whereas the use of contrast-aligned instructions achieves consistent translation quality improvement over 48 translation directions involving English, and that discriminator-based instructions outperform their generator counterparts, with better performance over 30 zero-sample directions.

### 2. Method Description 
This study proposes two methods for fine-tuning language models based on multilingual model (MT) training: **the MTInstruct and the AlignInstruct**. where the MTInstruct is the baseline, which uses MT commands to fine-tune the language model, and the AlignInstruct addresses the cross-linguistic signalling caused by limited parallel training data in low-resource languages deficiency problem. This approach transforms the discrimination task into a task with no additional training corpus by enhancing cross-language supervised learning.

![image](https://github.com/user-attachments/assets/a9f29f60-cdfe-4c43-b311-717f83b186f5)

### 3. Methodological improvements
Compared to the baseline MTInstruct, AlignInstruct improves performance in low-resource languages by enhancing cross-lingual supervised learning. Specifically, AlignInstruct exploits the similarity of the multilingual model between the source and target languages to generate translation indications that are used for language model fine-tuning. This approach can effectively increase the amount of training data and thus improve the generalisation ability of the model.

### 4. Issues addressed 
The main objective of this research is to address the problem of lack of sufficient training data for language model fine-tuning in low-resource languages. Since these languages usually do not have sufficient parallel corpora for standard fine-tuning, a new approach is needed to enhance cross-language supervised learning and improve model performance. The AlignInstruct method proposed in the study addresses this problem by generating translation instructions, which effectively increases the amount of training data and improves model performance.

## Experiments
This paper presents a study of improved methods for machine translation of low-resource languages. Specifically, the authors use two comparative experiments to validate the effectiveness of their approach:

The first experiment was conducted on the BLOOMZ model, which is a multilingual pre-trained model based on the Bloom language model. The authors used the OPUS-100 dataset as training data and used three different combinations of tasks for fine-tuning, including MTInstruct and AlignInstruct. they also compared the performance of different model sizes and evaluated them on a test set. The results show that using AlignInstruct significantly improves translation quality and performs better on the zero-sample translation task compared to using only MTInstruct.

![image](https://github.com/user-attachments/assets/cf8e36c5-a20b-4ca6-bdf5-70d671167470)

The second experiment was conducted on the BLOOMZ model, but this time only three unseen languages were used for fine-tuning, i.e. German, Dutch and Russian. The authors divided these languages into two groups, one that fine-tuned these three languages individually, and the other that fine-tuned these three languages by adding Arabic, French and Chinese to them. The results show that fine-tuning with multiple languages is more effective than fine-tuning one language alone in a zero-sample translation task. 

![image](https://github.com/user-attachments/assets/c2644b27-bfd2-48af-86cc-acb588ff27e2)

## Conclusion

### 1. Advantages of the Thesis
  1. This study proposes a cross-language alignment-based instruction fine-tuning method (AlignInstruct) for the translation problem of low-resource languages, and successfully applies it to the machine translation task of multi-language models.
  
  2. By comparing the experimental results, it is found that the use of AlignInstruct can significantly improve the translation quality of low-resource languages, and it also achieves better results in zero-sample translation.
  
  3. The study also explores the effects of different sizes of multilingual models, different types of instructions, and hybrid adaptive methods on translation performance, providing a reference for subsequent research.
  
### 2. Innovative points
  1. The AlignInstruct method proposed in this study is a cross-language instruction fine-tuning method based on statistical word alignment, which can improve the translation quality of low-resource languages without relying on additional training data.
  
  2. In the experiments, the method is compared with existing instruction fine-tuning methods to demonstrate its superiority and feasibility.

  3. In addition, this study also explores the effects of different sizes of multilingual models, different instruction types, and hybrid adaptive methods on translation performance, which further extends the application scope of the method.

### 3. Future Works
  1. In the future, the authors can further explore how to utilise richer corpora to improve the translation quality of low-resource languages, and also consider combining this approach with other techniques to achieve better performance improvement.
  
  2. In addition, this technique can also be considered to be applied to other fields, such as speech recognition and text categorisation, in order to extend its application scenarios.
