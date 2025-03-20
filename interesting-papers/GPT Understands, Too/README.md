# GPT Understands, Too
[paper link](https://arxiv.org/pdf/2103.10385) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a new method called P-Tuning for natural language understanding (NLU) of pre-trained language models.           | Pre-trained Language Models (PLM)        |

## Methodology

### 1. Abstract
The method uses a combination of trainable continuous cue embeddings and discrete cues that can stably improve performance on NLU tasks. Experimental results show that P-Tuning is effective in improving performance in both fully-supervised and few-sample settings on a wide range of tasks such as LAMA and SuperGLUE.

### 2. Method Description 
The paper proposes a method called “P-Tuning” to improve the adaptive performance of pre-trained language models (PLM). In NLP tasks, using pre-defined templates as prompts can improve model performance. However, these manually designed cues are often unstable and inconsistent, so researchers have tried to solve the problem by automating the search for cues. This approach may not fully utilize the gradient information, leading to unsatisfactory results. To solve this problem, the paper proposes a new method, continuous cue learning (P-Tuning), which embeds cues into a continuous space and maps them to hidden states using an additional embedding function.

![image](https://github.com/user-attachments/assets/4a2b8f13-c67f-4de9-b94f-0fb61a493a5f)

### 3. Methodological improvements
The main improvement of P-Tuning over traditional cue design methods is the use of continuous cue embedding. This embedding approach not only captures the relationship between cues and inputs better, but also improves the adaptive performance of the model in a more stable way. At the same time, Prompt Encoder can further enhance the connection between prompts, thus further improving the model performance.

### 4. Issues addressed 
The main contribution of this thesis is to provide an effective method to solve the problem of prompts for pre-trained language models. While traditional cue design methods suffer from poor stability and ineffectiveness, P-Tuning utilizes continuous cue embedding to solve these problems. The method can be applied not only to frozen language models but also to fine-tuned language models. In addition, Prompt Encoder can also enhance the connection between prompts, thus further improving the model performance. In conclusion, P-Tuning is a simple but effective cue learning method that can be applied in a variety of natural language processing tasks.

## Experiments
This paper focuses on P-tuning, a method for using continuous prompts instead of hand-designed discrete prompts in the field of natural language processing, and evaluates and compares it through several experiments. Specifically, the article is divided into three parts:

The first part is **the Knowledge Exploration Unit**, which focuses on the Knowledge Exploration Unit in the LAMA dataset, and compares the effects of discrete prompts and continuous prompts. The experimental results show that P-tuning can significantly improve the performance by increasing the optimal performance from 43.3% to 50.6% and from 45.2% to 64.2% compared to discrete cueing.

![image](https://github.com/user-attachments/assets/fbbe0012-1827-41b7-a1e9-2d0d0cb3f4e5)

The second part is **the fully supervised learning unit**, which focuses on the fully supervised learning tasks in the SuperGLUE dataset, including seven tasks such as question answering, textual entailment, coreference parsing, causal inference, and word sense disambiguation. The experimental results show that P-tuning can achieve better performance on both BERT and GPT models.

![image](https://github.com/user-attachments/assets/6ef61dd2-7432-488b-ae2b-88c737f8eca3)

The third part is **the small number of samples learning unit**, which focuses on the task of small number of samples learning, i.e., how to better utilize the pre-trained language models when there is only little training data. The experimental results show that P-tuning can improve the performance over the PET method by more than 1 point on average on the ALBERT-xxLarge model.  

![image](https://github.com/user-attachments/assets/6769ca0a-3767-4c27-ab55-5a86ebd5b4e4)

## Conclusion

### 1. Advantages of the Thesis
This paper presents a new method, P-Tuning, which uses trainable continuous cue embeddings in combination with discrete cues to improve the performance of PLMs and stabilize their training process. The authors conducted experiments in two NLU benchmark tests and demonstrated that P-Tuning has better performance performance relative to manual discrete cues and search cues. And, P-Tuning reduces the performance difference between different discrete cues, thus improving the stability of language model adaptation.
 
### 2. Innovative points
P-Tuning combines continuous cue embeddings with discrete cues as inputs to be passed to the language model and updates the continuous cue embeddings through backpropagation to optimize the task objective. This approach learns a degree of variability to counteract the effects of small changes in discrete cues, thus improving training stability. And, the authors use encoders such as LSTM or MLP to model dependencies between successive cue embeddings, further improving performance. 

### 3. Future Works
Future research directions include exploring more types of continuous cue embeddings and more complex encoder structures, as well as applying it to other natural language processing tasks. In addition, P-Tuning can also be considered to be used in conjunction with other automatic prompting techniques to further improve performance and stability.   
