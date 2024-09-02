# Natural Language Supervision For General-Purpose Audio Representations
[paper link](https://arxiv.org/pdf/2309.05767) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new audio language model, Contrastive Language-Audio Pretraining (CLAP), that learns generic audio representations and enables zero-sample inference on multiple tasks.          |  NLP        |

## Methodology

### 1. Abstract
To train this model, the authors use two innovative encoders and an autoregressive decoder for learning audio and language representations, respectively. The two representations are then fused together through comparative learning. Experimental results show that the CLAP model outperforms the other four models on downstream tasks and has better generalisation capabilities.

### 2. Method Description 
The paper presents a method called Contrastive Language-Audio Pretraining (CLAP) for jointly training audio and text encoders to learn multimodal representations that can be applied to different types of tasks. Specifically, the method uses a trainable projection layer to embed audio and text into a common multimodal space and computes a loss function by measuring the similarity between them to jointly train audio and text encoders and their projection layers.
![image](https://github.com/user-attachments/assets/e2a96a6f-2e0e-4572-9251-32a05ac14f37)

### 3. Methodological improvements
  1. Compared to traditional unimodal pre-training methods, the CLAP method is able to process information from multiple modalities simultaneously, resulting in better generalisation and performance performance.
  
  2. In addition, the CLAP method employs an autoregressive model, GPT2, as the text encoder, enabling it to produce sentence-level representations, further improving the model's performance.
     
### 4. Issues addressed 
The main goal of the CLAP method is to improve performance performance on multimodal tasks, including tasks such as zero-sample classification. By co-training the audio and text encoders, as well as their projection layers, the CLAP method is able to better capture the relationships between different modalities, leading to more accurate and robust multimodal representation learning.

## Experiments
This paper focuses on the performance of the CLAP model on different datasets and tasks and compares it with other models. Specifically, the authors use the two best combinations of the CLAP models CNN14+BERT and HSAT+RoBERTa as well as the CLIP text encoder for comparison. In addition, the authors evaluated different downstream tasks, including sound event classification and speech sentiment analysis.

For training, the authors used log Mel spectral representation for audio data and employed random truncation and padding to ensure that each batch has the same length of data. Also, the authors adjusted the learning rate and optimiser parameters to improve the model performance.
![image](https://github.com/user-attachments/assets/69a6180c-3eb2-4664-9d0e-59a003e838bd)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new CLAP model that uses custom audio and text encoders and is trained on 4.6M training pairs. The authors applied the CLAP model to 26 downstream tasks and achieved the best zero-sample performance (Zero-Shot SoTA).
  
  2. In addition, this paper compares different audio and text encoders and presents the HTSAT-22+GPT2 encoder combination, which outperforms the best combination in the literature.
  
  3. In addition, this paper explores the trade-off between diversity and generalisation capabilities and points out future research directions.

### 2. Innovative points
  1. The main contribution of this paper is the proposal of a new CLAP model that uses custom audio and text encoders and is trained on a large-scale dataset.
  
  2. In addition, the authors propose an improved GPT2 autoregressive model that performs better than other commonly used encoders.
  
  3. And the authors improved the generalisation ability of the model by adding training pairs from different domains and investigated the trade-off between diversity and generalisation ability.
     
### 3. Future Works
The CLAP model proposed in this paper has good application prospects and can be used for various audio-related downstream tasks. Future research directions include further optimising the parameter settings and structural design of the CLAP model, as well as exploring more diversity and generalisation strategies. And, integration of the CLAP model with other models can be considered for better performance. 
