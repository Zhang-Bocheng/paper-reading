# Multilingual E5 Text Embeddings: A Technical Report
[paper link](https://arxiv.org/pdf/2402.05672) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This technical report describes the training methodology and evaluation results of the open source multilingual E5 text embedding model, which was released in mid-2023.          | Embedding Model         |

## Methodology

### 1. Abstract
Three different sizes (small/base/large) of embedding models are provided to balance the relationship between inference efficiency and embedding quality. The training process follows the English E5 model recipe and includes comparative pre-training using 100 million multilingual text pairs and fine-tuning on a combined labelled dataset. In addition, a new instruction-tuned embedding model is introduced, which performs comparably to a similarly sized English-only model.

### 2. Method Description 
In this paper, we propose a weakly supervised contrast learning pre-training model, which is fine-tuned using multiple high-quality labelled datasets to further improve the embedding quality. The model employs diverse multilingual text pairs as input and is trained under the standard InfoNCE contrast loss function. In the first phase, the model is continuously trained on a data mixture containing a variety of sources, totalling about 1 billion text pairs. In the second phase, the model is better enabled for knowledge distillation by fusing high-quality labelled datasets through parameter fine-tuning

## Experiments
This paper focuses on the performance of the multilingual embedding model on the English language task and validates its performance by comparing it with other multilingual and English alone models. Specifically, the authors conducted the following three comparison experiments:

**English Text Embedding Benchmarking:** the authors used the MTEB benchmarking (Muennighoff et al., 2023) to compare the performance of different models on the English task. The results show that the authors' best mE5 model outperforms the previous best multilingual model, Coheremultilingual-v3, in this benchmark, as well as a powerful English-alone model, BGElarge-en-v1.5. Although the smaller models perform less well, their faster inference and lower storage costs make them suitable for many applications.

![image](https://github.com/user-attachments/assets/051440fb-5fef-4d40-9edf-170aaca33880)

**Multilingual retrieval capability evaluation:** the authors used the MIRACL benchmark test (Zhang et al., 2023) to evaluate the multilingual retrieval capability of the different models. The results show that the mE5 model significantly outperforms the mDPR model, which has been fine-tuned on the MIRACL training set, in both nDCG@10 and recall metrics. Detailed individual language results can be found in Appendix Table 6.

![image](https://github.com/user-attachments/assets/254b10a0-bd76-4188-a4d5-6d26f9563733)

**Cross-language similarity search task:** The authors used the bitext mining task to evaluate the performance of the different models in cross-language similarity search. The results show that the mE5 model performs competitively on a variety of resource-rich and low-resource languages, especially on top of models dedicated to bitext mining such as LaBSE.

![image](https://github.com/user-attachments/assets/b69e63be-7778-4960-8e0f-dcedc478aa42)  

## Conclusion

### 1. Advantages of the Thesis
  1. Compared to existing models trained only on English texts, mE5 has better cross-linguistic performance and can be applied to multiple applications such as information retrieval, semantic similarity and clustering tasks.
  2. In addition, the authors propose an mE5-large-instruct model based on instruction tuning, which improves the quality of the model by utilising synthetic data. This model is not only applicable to a single task, but also can be adapted to different task requirements through instruction adjustment, which further improves the generalisation ability of the model.

### 2. Innovative points
  1. The main contribution of this paper is to propose a method based on the multilingual text embedding model, which can effectively solve the current problems encountered in multilingual text processing. Specifically, the mE5 model proposed in this paper adopts a two-phase training approach, including two phases of weakly supervised contrast learning and labelled data fine-tuning.
  2. Meanwhile, the authors also developed an mE5-large-instruct model based on instruction tuning, which enables the model to be adjusted according to the needs of different tasks, so as to better meet the needs of practical application scenarios.
     
### 3. Future Works
There are still some problems that need further research. For example, when using a small amount of high-quality annotated data for fine-tuning, how to better balance the generalisation ability and accuracy of the model is an issue worth exploring. In addition, as more and more languages are included in the research field of natural language processing, how to design more general multilingual text embedding models is also an important research direction.    
