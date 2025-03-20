# Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning
[paper link](https://arxiv.org/pdf/2205.05638) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper compares two pre-trained language modeling approaches for processing new tasks; In-context Learning (ICL) and Parameter-efficient fine-tuning (PEFT)          |  Parameter Fine-Tuning        |

## Methodology

### 1. Abstract
ICL is a method for processing new tasks that does not require gradient training, but requires processing of all the training data, and is therefore computationally, memory, and storage costs are high. In contrast, PEFT requires only a small fraction of parameters to be trained for a new task and has better accuracy and lower computational cost. The authors also introduce a new PEFT method (IA)3 that significantly improves performance and introduces relatively few new parameters. In addition, they present a simple formulation, T-Few, that can be applied to new tasks without task-specific adjustments or modifications. By applying T-Few in the RAFT benchmark test, they achieved superhuman performance and improved absolute accuracy by 6% over the best available method.

### 2. Method Description 
This paper proposes a new parameter-efficient fine-tuning method called **Infused Adapter by Inhibiting and Amplifying Inner Activations (IA3)** for adapting to new tasks without the need for large amounts of labeled data. The method adds some new parameters to the original pre-trained model and adapts to new tasks by learning specific task-relevant vectors. This method provides higher accuracy and lower computational cost than traditional fine-tuning methods.

![image](https://github.com/user-attachments/assets/c8d8ab30-336d-4767-be27-1a3b4e8722c2)

### 3. Methodological improvements
The main improvement of the IA3 method over the traditional fine-tuning method is the introduction of new parameters and the learning of specific task-related vectors. Specifically, it adds three vectors of length d, lk, lv, and lff, which are applied to self-attention and encoder-decoder attention mechanisms and intermediate activations in position-wise feed-forward networks, respectively. These vectors can be added to the model by initializing them as all-one matrices without affecting the behavior of the original model. And, IA3 supports mixed task batches, which means that several different tasks can be processed at the same time, further improving the efficiency of the model.

### 4. Issues addressed 
The method proposed in this paper mainly addresses the problem of how to efficiently adapt to new tasks with limited labeled data. While traditional fine-tuning methods require a large amount of labeled data to achieve good results, IA3 can achieve high accuracy with relatively little data. In addition, since IA3 supports mixed task batches, it can also cope with multi-tasking scenarios that are common in real-world applications.

## Experiments
This paper focuses on the model T-Few for the zero-sample learning task and conducts several sets of comparative experiments to verify its performance and efficiency advantages. Specifically, the following comparison experiments are conducted in this paper:

**Performance comparison experiments**: the authors compare T-Few with other models on multiple datasets, including T0, T5+LM, GPT-3, etc. The results show that T-Few outperforms other models on all datasets, especially in the case of small samples.

![image](https://github.com/user-attachments/assets/bf68aa27-6171-48c4-93ba-e96826e4ba42)

**Computational Cost Comparison Experiment**: the authors compare the cost of different methods by calculating the FLOPS and training/reasoning time of the models. The results show that T-Few not only has higher accuracy, but also outperforms other methods in terms of computational cost.

**Practical Application Comparison Experiment**: the authors applied T-Few to a real-world task, RAFT, and compared it with human and other models. The results show that T-Few achieves state-of-the-art accuracy in this task and can be applied to a variety of new real-world application scenarios.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a parameter-efficient few-sample learning method called “T-Few”, which outperforms traditional few-sample learning methods in terms of model performance and is computationally less expensive.
  2. The authors make the model better able to perform the classification task by introducing a new PEFT method (IA)3 and by using two additional loss terms to encourage the model to output lower probabilities and to account for the length of different answer choices.
  3. And, the authors show that T-Few performs superhumanly in the RAFT benchmark test and can reason in mixed task batches. These results provide new perspectives on how best to use large language models for learning with fewer samples.
 
### 2. Innovative points
  1. The methodological innovation of this paper is the proposal of a new PEFT method (IA)3 that produces better performance than full model fine-tuning while requiring only a small number of model parameters to be updated.
  2. In addition, the authors added two additional loss terms to encourage the model to output lower probabilities and to account for the length of different answer choices, thus improving the model's performance. 

### 3. Future Works
The authors stated that they will apply T-Few to generative tasks such as summarization and quizzing in future work. The authors would like to further investigate how T-Few can be extended to other domains such as natural language understanding, image processing, etc.   
