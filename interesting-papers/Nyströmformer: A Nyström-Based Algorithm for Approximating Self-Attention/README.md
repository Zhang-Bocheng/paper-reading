# Nyströmformer: A Nyström-Based Algorithm for Approximating Self-Attention
[paper link](https://arxiv.org/pdf/2102.03902) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new model called Nystromformer for solving the problem of sequence length constraints in natural language processing.         | Transformer          |

## Methodology

### 1. Abstract
The model is based on the Nystrom method, achieves scalability by approximating the standard self-attention mechanism to O(n) complexity, and is evaluated on several downstream tasks. Experimental results show that the Nystro¨mformer performs comparably or slightly better than standard self-attention and performs well on longer sequence tasks. 

### 2. Method Description 
This paper proposes a new NNs architecture, the Nystro¨mformer. the model uses the Segment-means algorithm to compute the landmark point matrices K˜ and Q˜ of the input keypoints K and the query Q. The landmark point matrices K˜ and Q˜ are then computed by approximating the Moore-Penrose pseudo-inverse of the Nystrom approximation. In addition, to aid in training, the model adds a jump connection of value V , implemented using 1D deep convolution.

![image](https://github.com/user-attachments/assets/7de5d9e9-b75d-47a7-b00e-0273e06ad72d)

### 3. Methodological improvements
Unlike traditional NNs, Nystromformer uses the Nystrom approximation to reduce the amount of computation and thus improve the model efficiency. Also, the design of jump connections helps to speed up the training process.

![image](https://github.com/user-attachments/assets/c008831a-7435-4321-bbc4-58962d9215a3)

### 4. Issues addressed 
The main goal of this method is to improve the efficiency and speed of NNs to cope with the demands of large-scale data processing. By using technical tools such as Nystrom approximation and jump connections, Nystromformer can accomplish the task more quickly and has high practicality in real applications.

## Experiments
This paper describes three comparative experiments conducted by the authors, namely language model pre-training, downstream task fine-tuning, and long sequence task comparison:

The first experiment is **a comparative experiment on the efficiency and accuracy of language model pre-training**. The authors used BookCorpus and English Wikipedia as the training corpus and reported MLM and SOP accuracy on the validation set. The authors compared Nystroformer with BERT-Small and BERT-Base and found that Nystroformer performed better in both efficiency and accuracy.

The second experiment was **a comparative experiment on fine-tuning of downstream tasks**. The authors selected several tasks from the GLUE benchmark test as well as the IMDB review dataset and fine-tuned Nystroformer on these tasks. The results show that Nystroformer outperforms BERT-Base on all tasks.

The third experiment was **a comparison with other efficient self-attention methods in an LRA benchmark test**. The authors chose tasks such as Listops, byte-level IMDb comment text categorization, byte-level document retrieval, image categorization, and Pathfinder, and compared Nystroformer with other self-attentive methods on these tasks. The results show that Nystroformer has higher average accuracy and is more efficient than other self-attentive methods on all tasks. 

![image](https://github.com/user-attachments/assets/620cb4f9-12b7-4380-aaf7-3f729f1bd88b)

![image](https://github.com/user-attachments/assets/0bdacb08-448b-46ba-971d-c2a93d591c8b)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new approximation of the self-attention mechanism, called the Nystromformer, which reduces computational and memory requirements by using stochastic projections and low-rank assumptions.
  
  2. The researchers show how the Nystrom method can be applied to deep transformer architectures and provide an effective approximation of self-attention.
  
  3. Experimental results show that the Nystromformer performs well on multiple downstream tasks with higher speed and accuracy than the BERT model.

### 2. Innovative points
  1. This research capitalizes on the strengths of the Nystrom method by applying it to the self-attention mechanism in deep transformer architectures, thus providing an efficient approach to self-attention approximation.
  
  2. The researchers also considered how to make all the key operations map to popular deep learning libraries for easy implementation.
     
### 3. Future Works
  1. This research provides an important step toward building transformer models that can handle very long sequences.
  
  2. Future research could explore other approximations of the self-attention mechanism and further optimize the performance and efficiency of the Nystromformer.    

