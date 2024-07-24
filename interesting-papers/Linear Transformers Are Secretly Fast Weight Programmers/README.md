# Linear Transformers Are Secretly Fast Weight Programmers
[paper link](https://arxiv.org/pdf/2102.11174) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the equivalence between linearized self-attention mechanisms and fast weight controllers, and proposes the concept of Fast Weight Programmers (FWPs)         | Neural Network          |

## Methodology

A neural network structure capable of dynamically interacting with a finite memory and learning to manipulate its contents through sequential element programming instructions. The paper also extrapolates the memory capacity limitations of a recently proposed linearized softmax attention variant and proposes a new linearized attention kernel function to balance simplicity and effectiveness. Experimental results show that these methods offer significant advantages in synthetic retrieval problems, standard machine translation, and language modeling tasks

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new update rule for memory units, which enables the model to better learn to use memory units dynamically and interactively by improving the original programming instructions.
  
  2. The authors verify the effectiveness and superiority of the new update rule in several experiments and compare it with existing models.
  
  3. This paper also introduces some new ideas for the design of memory cells, such as a method based on free projection of deterministic parameters, and a linear attention function for fast weighted memory.

![image](https://github.com/user-attachments/assets/2f950116-ab1e-4ac3-8a82-0eccd285df2f)

### 2. Innovative points
  1. **New rules for updating memory units**: by improving the original programming instructions, the model is better able to learn to use memory units dynamically and interactively.
 
  2. **Free projection method based on deterministic parameters**: a simple and easy-to-compute linear projection method is proposed, which can effectively increase the capacity of memory cells.
  
  3. **Linear Attention Function for Fast Weighted Memory**: a new linear attention function is proposed that can effectively handle large-scale datasets and improve model performance.

![image](https://github.com/user-attachments/assets/c08d5758-b2e0-4224-97d5-0ee51dd3eec0)

### 3. Future Works
  1. Further research can be done to investigate how these methods can be applied to more complex tasks and larger datasets.
  
  2. Other types of attention mechanisms, such as adaptive attention or learnable attention mechanisms, can be explored to improve model performance and efficiency.
  
  3. It can be investigated how to combine these methods with other deep learning techniques, such as reinforcement learning or meta-learning, to achieve better results.
