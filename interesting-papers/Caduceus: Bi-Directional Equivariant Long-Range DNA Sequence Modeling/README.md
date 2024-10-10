# Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling
[paper link](https://arxiv.org/pdf/2403.03234) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a biological language model called Caduceus for dealing with problems such as long-distance sequence interactions and DNA reverse complementarity.          | Large Language Model (LLMs)        |

## Methodology

### 1. Abstract
The model is constructed based on Mamba blocks and introduces BiMamba components and MambaDNA blocks that support bidirectionality and reverse equivalence. The authors obtained the Caduceus DNA base model through a pre-training and fine-tuning strategy and outperformed larger scale models that do not use bidirectionality and equivalence in downstream benchmarking. This study provides new ideas and methods for large-scale sequence modelling in biology and genomics

![image](https://github.com/user-attachments/assets/e2740b32-c270-4755-a749-19bcc564dc41)

### 2. Method Description 
This paper propose a bidirectional DNA language model architecture called Caduceus, which satisfies the requirement of temporal inversion invariance (RC equivariance) when processing DNA sequences. Specifically, the model uses two main components: BiMamba and MambaDNA.

BiMamba is a bi-directional sequence transformer based on Mamba modules, which passes the input sequences through a forward and a backward Mamba module, respectively, and combines their results to obtain a more comprehensive representation of the information. MambaDNA, on the other hand, is a special BiMamba module that processes both the original sequence and its time-reversed (reverse complement) version, and shares parameters to avoid increasing memory overhead.

![image](https://github.com/user-attachments/assets/75376e2d-451b-49cc-a4da-3eab1effd9ff)

### 3. Methodological improvements
Compared to previous models, the Caduceus model introduces the concept of RC equivariance, which allows the model to better capture important information in DNA sequences. In addition, Caduceus achieves efficient parallel computation and low memory consumption through the design of two components, BiMamba and MambaDNA.

### 4. Issues addressed 
Traditional DNA sequence modelling methods often do not handle the time-reversal invariance of DNA sequences well, resulting in models that do not make full use of the critical information in DNA sequences. In contrast, the Caduceus model improves the performance performance of the model by improving the handling of DNA sequences so that it can meet the requirements of time inversion invariance. In addition, through the design of two components, BiMamba and MambaDNA, Caduceus also solves the problems of high memory consumption and low parallel computing efficiency that exist in traditional models.

## Experiments
This paper focuses on a study of pre-training and downstream task evaluation using deep learning models in the field of genomics. The authors conducted the following two comparison experiments:

**Pre-training Module Comparison Experiment**: the authors compare the performance of two DL based sequence encoders, Mamba and HyenaDNA, on a human reference genome and find that Mamba performs better on cross-entropy loss and is more robust to higher learning rates. In addition, the authors compare the performance difference between BiMamba and a two-way Mamba model without weight sharing in an MLM pre-training task, and show that the parameter-efficient BiMamba implementation performs better than a two-way Mamba model without weight sharing.

![image](https://github.com/user-attachments/assets/eb37e278-ecd4-400c-8a6d-d879a6f0e73d)

**Downstream task evaluation experiments**: the authors applied the Genomics Benchmarks suite (Genomics Benchmarks) to Mamba models and other non-Mamba baseline models, including CNN models and HyenaDNA models. The results show that the Caduceus model performs best in the entire annotation category, and in particular, the Caduceus-Ph model is the optimal model for all tasks. 

Next, the authors also applied the Nucleotide Transformer Task Suite to the Caduceus model and other models, such as DNABERT-2 and Enformer. The results show that the Caduceus model performs well in most prediction tasks, especially in the task of predicting protein tags and enhancer annotations, and even outperforms the Attention Mechanism approach with a much larger number of parameters. 

![image](https://github.com/user-attachments/assets/2ef96d03-ab43-48ee-9b12-8ea0624e9587)

Finally, the authors also explored the SNP impact on gene expression prediction task and compared the performance of Caduceus, HyenaDNA, Nucleotide Transformer, and the supervised baseline Enformer. The results show that the performance of the Caduceus model gradually improves as the distance from the SNP to the nearest transcriptional start site increases, outperforming Enformer even at distances of more than 100k from the TSS.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new sequence model, Caduceus, for processing genomic information in biological data and achieves excellent performance in predicting gene expression.
  
  2. Compared to other models based on natural language or proteins, Caduceus better handles the characteristics of DNA sequences, such as bidirectionality and reverse complementarity.
  
  3. In addition, the paper presents two new modules, BiMamba and MambaDNA, which can efficiently handle long sequences and support bidirectionality and reverse complementarity. These modules can be used as base components for other bioinformatics models.
 
### 2. Innovative points
  1. The BiMamba module is proposed, which is an efficient and parameter-poor component for modelling bidirectional sequences that can handle long sequences without increasing the computational cost.

  2. Based on the BiMamba module, the MambaDNA module is further proposed, which not only supports bi-directionality, but also has reverse complementarity to better process the information of DNA sequences.

  3. Based on the MambaDNA module, the Caduceus model was constructed, which is the first DNA sequence model supporting reverse complementarity, and can achieve better performance in predicting gene expression and so on.

### 3. Future Works
  1. Testing the effectiveness of the Caduceus model on a wider range of biological datasets to validate its performance on different tasks.

  2. Compare the Caduceus model with other existing bioinformatics models to evaluate its strengths and weaknesses.

  3. Explore how the Caduceus model can be applied to real-world biomedical research, such as predicting disease risk or drug screening.  
