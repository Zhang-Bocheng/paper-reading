# Recovering from Privacy-Preserving Masking with Large Language Models
[paper link](https://arxiv.org/pdf/2309.08628) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper focuses on how to use large-scale language models for text data processing while protecting user privacy.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
In order to address the problem of discrepancy between actual user data and agent training data, the authors propose a variety of pre-training and fine-tuning based language modelling approaches and evaluate these approaches comparatively through experiments. The results show that after replacing sensitive information with masking tokens, the models trained using the masked corpus can achieve the same or even better performance as the original data. This research result is of great significance for improving the adaptability and security of machine learning models.

### 2. Method Description 
The paper proposes two privacy-preserving techniques: token masking and the use of pre-trained models to replace masked tokens. In token masking, the authors provide three different masking techniques: allowList, vocabThres, and entityTagger. All of these techniques are designed to hide sensitive information automatically and do not require human involvement. After masking, the authors use a pre-trained language model (LLM) to populate each masking symbol in order to make the sentence syntactically correct and complete. The authors also present three strategies to replace masked tokens using LLM: Top-1, Top-K, and Fine-Tuning.

![image](https://github.com/user-attachments/assets/d1909da2-91d5-4ee8-8e5b-d819f94b7c8e)

### 3. Methodological improvements
Compared with traditional data desensitisation methods, this approach is more efficient and accurate. It not only hides sensitive information, but also ensures the syntactic correctness and completeness of statements. In addition, by using pre-trained LLMs, the accuracy of prediction can be improved and the amount of data to be labelled can be reduced.

### 4. Issues addressed 
This method addresses the problem of data privacy leakage and allows machine learning models to be trained without revealing personal identities. Also, this method can be used in other domains such as speech recognition.

## Experiments
 This paper focuses on the authors' comparison of the performance of several baselines and proposed methods in a downstream language modelling task and explores three datasets: the Fisher, Pushshift.io Reddit and Wall Street Journal (WSJ). Specifically, the following experiments were conducted in this paper:

Datasets: The authors used three datasets to compare the performance of different methods: Fisher, Pushshift.io Reddit, and Wall Street Journal (WSJ).
![image](https://github.com/user-attachments/assets/d8cf86d8-dda3-43fd-9074-71bdeb69ac6a)

Experimental Setup: For each dataset, the authors used Transformer as the downstream language model and pre-trained it. For each masking technique, the authors applied it to the training set and calculated its perplexity on the test set. In addition, the authors performed speech recognition experiments on the WSJ dataset.

Masking techniques: the authors considered three different masking techniques including allowList, vocabThres, and entityTagger. allowList contains 5K common words, vocabThres contains the top 10K most frequently occurring words, and entityTagger utilises the BERT-NER model to tag named entities.

Baseline methods: the authors consider Oracle, benchmark methods trained directly on the post-masking corpus, and benchmark methods that weight masked symbols in the loss function as baselines.

LLM-based approach: the authors used pre-trained language models such as BERT, RoBERTa and LLAMA2 for masking substitution and compared their effectiveness.

Results Analysis: The authors conducted experiments on each dataset and compared the perplexity and speech recognition results of the various methods. From the experiments, the authors came up with the following conclusions:

All the proposed methods perform better than the two baseline methods; In all cases, the Top-K method outperforms the method based on a single masked symbol;
Fine-tuned BERT and RoBERTa perform better than the unfine-tuned versions; Since allowList masks more words, the gap between any other method is larger compared to Oracle; RoBERTa performs the best of all masking techniques, and in the case of vocabThres and entityTagger, its perplexity is close to that of Oracle, indicating that most of the missing information can be recovered in the masked dataset; LLaMA2 (Top-1, FT) is a competing method, but not as good as fine-tuned BERT or RoBERTa.

![image](https://github.com/user-attachments/assets/7575fa42-5f49-46b5-a476-c38e7ef26970)

![image](https://github.com/user-attachments/assets/19fc9bd8-feb1-4e8c-9cdd-71794b3743cc)

![image](https://github.com/user-attachments/assets/b7c685fa-8439-4457-9bc1-695149db67bd)

## Conclusion

### 1. Advantages of the Thesis
The paper proposes a method to recover privacy-preserving text masks and improve the performance of downstream NLP tasks using pre-trained language models (LLMs). By replacing sensitive information with generic tokens and using LLMs to provide suitable candidate words to populate these tokens, the method can efficiently process masked data without destroying the original semantic structure.

### 2. Innovative points
  1. The main contribution of this thesis is to propose a new method for solving the privacy-preserving text masking problem using pre-trained language models.
  
  2. The method not only effectively recovers the masked information, but also maintains the semantic structure of the original utterances.
  
  3. In addition, the authors propose three different masking techniques and evaluate them to verify the effectiveness and applicability of the proposed solution.
      
### 3. Future Works
Further optimisation of the masking technique and tuning of the parameters of the LLMs can be considered to obtain better performance. In addition, other types of NLP tasks, such as machine translation and sentiment analysis, can be explored to evaluate the effectiveness of the method more comprehensively. 
