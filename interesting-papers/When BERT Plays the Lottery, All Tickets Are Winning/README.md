# When BERT Plays the Lottery, All Tickets Are Winning
[paper link](https://arxiv.org/pdf/2005.00561.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores the use of structured and size-pruning methods to validate the “lottery ticket stub hypothesis” in BERT models.         | BERT          |

## Methodology

### 1. Abstract
Using this approach, the authors find that even small trained sub-networks can achieve similar performance to the full model, and that most of the pre-trained BERT weights are useful. In addition, they analyzed successful subnetworks, but did not find them to have better linguistic knowledge or meaningful self-attention patterns.

### 2. Method Description 
In this study, the pre-trained model BERT-base lowercase was used and fine-tuned in the Transformers library. The model was fine-tuned on 9 GLUE tasks and evaluated using the metrics shown in Table 1. All experiments were performed on the development set, as the test set is not publicly distributed. For each experiment, the authers tested 5 random seeds.
![image](https://github.com/user-attachments/assets/a51fe837-c6e6-4146-b76c-f39ab58bf666)

### 3. Methodological improvements
In this study, a BERT-based NLP technique was used to improve the performance of the pre-trained model by fine-tuning it. This approach reduces the amount of data required and also makes better use of the existing large-scale corpus. In addition, the generalization ability of the model can be further improved by fine-tuning multiple tasks.

### 4. Issues addressed 
This research addresses the problem of how to utilize pre-trained models to improve the performance of natural language processing tasks. By fine-tuning the BERT-base lowercase model, better performance can be obtained on different tasks, which improves the generalization and usefulness of the model. In addition, this study explores the effects of different parameter settings on model performance, which provides a reference for subsequent research.

## Experiments
This article focuses on how model size can be reduced by structured and unstructured pruning methods in large-scale pre-trained language models (e.g., BERT), and verifies that these pruned sub-networks still retain the performance of the original model. The following comparison experiments are included in the article:

**Comparing the effects of different pruning methods**: two pruning methods, mask-based and structured, are used to prune BERT and compare their performance on the GLUE task. The results show that the mask-based method can reduce the number of parameters more effectively, while the structured method can retain the critical neurons better.
![image](https://github.com/user-attachments/assets/d9897f75-5d25-434b-83a4-3e7b0156af28)

**Comparing the effect before and after pruning**: after dividing BERT into different sub-networks and pruning them, comparing their performance with the original BERT on the GLUE task. The results show that even after pruning, these sub-networks maintain a similar level of performance as the original BERT.

**Analyzing the pruned sub-networks**: important neurons in the pruned sub-networks are analyzed to understand how they affect the performance of BERT. The results show that the distribution of neurons in the pruned sub-networks is not stable and more research may be needed to understand their role.

## Conclusion

### 1. Advantages of the Thesis
  1. The lottery hypothesis in BERT Fine-tuning was systematically tested using two pruning methods: weight size-based pruning and BERT self-attention head and MLP importance pruning.
  
  2. It was found that for both methods, “good” sub-networks can individually achieve comparable performance to the full model, while “bad” sub-networks can also achieve stronger performance by re-initializing to the pre-trained BERT weights and Fine-tuning respectively. performance.
  
  3. The results suggest that most of the pre-trained BERTs may be potentially useful in Fine-tuning, and that their success may have more to do with optimizing surfaces than with specific linguistic knowledge.

### 2. Innovative points
  1. A systematic study of the lottery ticket hypothesis in BERT Fine-tuning was conducted and used both weight-size based pruning and importance pruning of BERT self-attention head and MLP.
  
  2. Information on the carbon footprint and social cost of the work was generated using an experimental impact tracker.

### 3. Future Works
  1. It can be further explored whether similar loss topography maps can be obtained for non-linguistic pre-training tasks and applied to natural language processing tasks.
  
  2. One can continue to explore the relationship between optimization surfaces and linguistic knowledge in BERT Fine-tuning and try to design more effective Fine-tuning strategies. 


