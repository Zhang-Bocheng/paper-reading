# Not All Memories are Created Equal: Learning to Forget by Expiring
[paper link](https://arxiv.org/pdf/2105.06548) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper describes a new method called Expire-Span for learning to forget unnecessary information and retain the most important information.         | Transformaer          |

## Methodology

### 1. Abstract
This method can be applied to sequence modeling tasks where long-term memory is required and can efficiently process information with tens of thousands of forward time steps. The authors conducted experiments on a reinforcement learning task and a very long contextual task and demonstrated the effectiveness of the method. In addition, Expire-Span has higher efficiency and less memory usage than other existing methods.

### 2. Method Description 
This paper proposes a method called EXPIRE-SPAN for distinguishing and deleting irrelevant memory information in the Transformer to improve model efficiency and performance. The method accomplishes this by calculating the "expire-span" of each memory cell and permanently deleting it when necessary. This approach reduces the average memory size without affecting model performance and focuses attention on task-relevant information.

![image](https://github.com/user-attachments/assets/dd1763c0-f2f0-46ed-984d-bed5ba1f55b7)

### 3. Methodological improvements
In order to address the problems in the existing methods, the following improvements are proposed in this paper:

  1. **Use of soft mask function**: since the use of discrete masks can lead to the inability of Expire-Span to obtain the gradient, this paper adopts the soft mask function proposed by Sukhbaatar et al. in order to train Expire-Span.
  
  2. **Adding an auxiliary loss term**: in order to further reduce the memory size, an auxiliary loss term is added in this paper to penalize the Expire-Span values for the L1 paradigm. This helps to narrow down the range of memories that contribute less to the main task, thus allowing the model to focus on less but more important information.
  
  3. **Block-level parallel processing**: in order to allow permanent memory deletion in Expire-Span, this paper introduces a block-level parallel processing mechanism. In this way, when processing a block, only queries in the current block will consider all hidden states within this block, while other blocks will not be affected.
  
  4. **Model stability and regularization**: in order to prevent model overfitting, this paper suggests randomly shortening the memory size during training. In addition, when L takes very large values, a simple correction method can be used to avoid small changes that lead to huge changes in model behavior.

### 4. Issues addressed 
The main goal of EXPIRE-SPAN is to help Transformer models better handle long sequence data while maintaining high efficiency and accuracy. Specifically, it addresses the following problems:

  1. **Excessive memory consumption**: traditional autoregressive models need to store all historical inputs, which may lead to excessive memory consumption, affecting the running speed and efficiency of the model.
  
  2. **Presence of irrelevant memory**: since traditional models only focus on the information of the first few time steps, they may ignore some historical inputs that are irrelevant to the task, leading to a decrease in model performance.
  
  3. **Risk of overfitting*: when the model needs to learn a large number of historical inputs, overfitting may occur, leading to a decrease in generalization ability.

## Experiments
This paper describes several experiments conducted by the authors to demonstrate the effectiveness of their method, EXPIRE-SPAN, in a variety of tasks and to compare it with other models. Specifically, they conducted the following experiments:

  1. **Task of memorizing key information**: in this task, the authors show that EXPIRE-SPAN can effectively handle situations where only a small amount of information needs to be memorized. They tested it in an RL grid world task and a conversational story generation task and found that EXPIRE-SPAN was able to achieve better performance with smaller memory capacity.

  2. **Tasks to memorize long sequences of information**: In this task, the authors show that EXPIRE-SPAN is able to better handle situations where a large amount of information needs to be memorized. They tested it in a task where a portal passes through multiple rooms and found that EXPIRE-SPAN was able to achieve better performance with a smaller memory capacity.

  3. **Very difficult task**: In this task, the authors showed that EXPIRE-SPAN can learn how to forget irrelevant information. They used a task taken from the LIGHT text world game, in which the model had to find specific instructions in a large amount of irrelevant text. The results showed that EXPIRE-SPAN was better able to focus on the correct line of instructions than the other models.

  4. **Scalability experiment**: in this experiment, the authors show that EXPIRE-SPAN can be scaled across different tasks and datasets. They tested it on tasks such as character-level language modeling, moving object tasks, and found that EXPIRE-SPAN was able to achieve better performance with less memory and faster speeds.

![image](https://github.com/user-attachments/assets/a1179ff1-fb3e-4738-85fd-782b15cc75e5)

## Conclusion

### 1. Advantages of the Thesis
  1. It realizes effective processing of long term memory, which can help the model better capture key information and ignore irrelevant information.
 
  2. Compared with existing long-term memory methods, EXPIRE-SPAN is more efficient and can achieve better performance with less memory and training time.
  
  3. Experiments are conducted on several natural language processing tasks and reinforcement learning tasks with state-of-the-art results.

![image](https://github.com/user-attachments/assets/2c903bfc-5752-4fbb-ad43-8ecf3169e08a)

### 2. Innovative points
  1. Introducing a predictor to decide which information needs to be retained and which information needs to be forgotten, thus effectively solving the long term memory problem.
  
  2. By designing the forgetting process to be progressively differentiable, it allows the entire model to continue to be trained end-to-end using the backpropagation algorithm.
  
  3. Running EXPIRE-SPAN independently in different layers allows each layer to focus on a different time scale.
     
### 3. Future Works
  1. Exploring how to further optimize the parameter settings of EXPIRE-SPAN for better performance.
  
  2. Investigating how to combine EXPIRE-SPAN with other techniques, such as adaptive learning rate tuning or regularization methods, to improve the generalization ability of the model.
  
  3. Apply EXPIRE-SPAN to other domains, such as computer vision or speech recognition, to explore its applicability and effectiveness in different domains. 
