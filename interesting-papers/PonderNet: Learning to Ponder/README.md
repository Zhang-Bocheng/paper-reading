# PonderNet: Learning to Ponder
[paper link](https://arxiv.org/pdf/2107.05407) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new neural network algorithm, PonderNet, which is able to adaptively adjust the amount of computation according to the complexity of the problem, thus achieving an effective balance between training prediction accuracy, computational cost, and generalization ability.         |  Neural Network         |

## Methodology

### 1. Abstract
Experimental results show that PonderNet outperforms previous adaptive computational methods on a complex synthesis problem and successfully passes an extrapolation test that cannot be accomplished by traditional NN. In addition, the method was able to achieve the current best results on a real-world question-answering dataset and used fewer computational resources. Finally, PonderNet also achieved state-of-the-art results on a complex task designed to test the inference capabilities of NN.

### 2. Method Description 
This paper proposes a new NN architecture, PonderNet, and design a novel loss function to train it. The architecture requires a step function and an initial state, and calculates the predicted value and the stopping probability by recursively applying the step function up to N times. The predicted value is obtained by randomly sampling a probability distribution based on stopping units. In addition, the authors propose a maximum step correction scheme to ensure that the sum of the probabilities of all possible stopping units is 1 for a finite number of iterations.

### 3. Methodological improvements
  1. Compared to other models, such as ACT, PonderNet's predictions are obtained by randomly sampling based on the probability distribution of stopping units, rather than a weighted average.
  
  2. PonderNet are more general and allows for easy computation of expected predictions. In addition, the authors introduced a regularization term to encourage the network to explore more possibilities.

### 4. Issues addressed 
  1. The PonderNet proposed in this paper solves the problem of long-term dependency in NN and provides a new approach to deal with dynamic length sequence data.
  
  2. the authors also consider the practical situation where only a finite number of iterations can be performed and propose a correction accordingly.

## Experiments
This paper describes the authors' comparative experiments on the performance of the PonderNet model on different tasks and contrasts it with existing approaches. Specifically, the authors conducted the following three comparison experiments:

**On the Parry problem (parity) task**, the authors varied the number of random elements in the input vectors from 1 to 64, and then trained and tested the model by setting different average thinking steps. The results show that the PonderNet model performs better on this task and uses less computational resources than the ACT model.

![image](https://github.com/user-attachments/assets/e4912a3c-a54f-4856-a896-600f8f69f21d)

**On the bAbI Q&A dataset**, the authors used the same model architecture but used a different computational time optimization method. The results show that the PonderNet model is able to achieve the same level of performance as the best available results at a faster rate and with a lower error rate.

**On the Paired associative inference (PAI) task**, the authors compared it to other methods. The results show that although the PonderNet model uses the same architecture as Universal Transformer, it achieves higher accuracy on this task.

![image](https://github.com/user-attachments/assets/78eae5b4-d8b2-4964-be91-527bcc6b0f77)
 
## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new algorithm, PonderNet, for learning to adapt to the computational complexity of NN. The algorithm achieves this goal by optimizing a regularization term that combines predictive accuracy and explorability, and achieves the highest accuracy across multiple tasks.
  
  2. In addition, the authors show that adapting existing recursive architectures to PonderNet is easy, requiring only the addition of an extra stopping unit and loss function.
  
  3. Most importantly, the authors show that this additional loss term is robust to the hyperparameter λp that defines the network stopping probability, which is an important advantage that other methods such as ACT do not have.

### 2. Innovative points
  1. The main contribution of this paper is the proposal of a new algorithm, PonderNet, which automatically adjusts the computational complexity of the NN as needed to improve the performance of the model.
  
  2. Compared with traditional RNN, PonderNet has higher flexibility and efficiency, and can achieve better performance in multiple tasks. In addition, the authors show how PonderNet can be applied to existing recursive architectures to make them easier to use and deploy.
     
### 3. Future Works
The PonderNet algorithm proposed in this paper provides a new idea and method to solve this problem, which can provide reference and reference for future related research. Meanwhile, the authors can further explore how to combine PonderNet with other deep learning techniques to realize more powerful and efficient machine learning systems.  
