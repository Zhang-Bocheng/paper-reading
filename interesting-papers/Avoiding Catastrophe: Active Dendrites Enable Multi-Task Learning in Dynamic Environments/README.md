# Avoiding Catastrophe: Active Dendrites Enable Multi-Task Learning in Dynamic Environments
[paper link](https://arxiv.org/pdf/2201.00042) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper explores the problem of how to build more adaptive AI systems in dynamic environments         | Deep Learning          |

## Methodology

### 1. Abstract
  The authors present a new approach based on a bio-heuristic architecture that incorporates active dendrites and sparse representations into a standard deep learning framework. Experimental results show that in two task-based reinforcement learning(RL) environments and a continuous learning benchmark test, the model is able to learn multiple tasks fluently and with little forgetting of previously learned knowledge. This is the first study to realize the competitive performance of multi-tasking and continuous learning in the same architecture. This study provides new ideas for solving dynamic scene problems that cannot be solved by traditional neural networks. 
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/1231cbed-9589-48c8-8a57-975a96244138)

### 2. Method Description 
  The paper proposes a deep learning architecture based on a biological neural network model called Active Dendrites Network (ADNet).The core idea of ADNet is to divide neurons into two parts: linear weights responsible for processing regular inputs and nonlinear activations responsible for processing context-specific information. In this way, ADNet enables highly sparse representations and reduces gradient interference and prevents forgetting in multitasking and continuous learning scenarios.
  
### 3. Key concepts
  _Multi-task learning (MTL)_: A paradigm in ML where multiple related tasks are learned simultaneously using a shared representation. The core idea is that learning multiple tasks together can lead to better performance and generalization on each individual task compared to learning each task independently. This is particularly useful when tasks are related and can benefit from shared information.
  
### 4. Methodological improvements
  The main improvement of ADNet over traditional deep learning models is the introduction of the biological feature of active dendrites. Active dendrites are non-linear branches on a neuron that receive context-specific signals and affect the overall response of the neuron. ADNet uses this feature to simulate the behavior of biological neurons and improves the performance through adaptive tuning during training.

In addition, ADNet adopts the k-Winner-Take-All (k-WTA) function as the nonlinear activation function of the hidden layer to ensure the sparsity and high interpretability of the output. Also, ADNet supports optimization strategies such as sparse connectivity and dynamic task allocation to further improve the performance.

### 5. Issues addressed 
  1. **Gradient interference problem**: In multi-task or continuous learning scenarios, the gradients between different tasks may interfere with each other, leading to performance degradation. ADNet mitigates the gradient interference by separating regular inputs from context-specific information and by using the nonlinear responses of active dendrites.

  2. **Forgetting problem**: During continuous learning, the learning of new tasks may overwrite the knowledge of old tasks, leading to forgetting. ADNet mitigates the forgetting problem by preserving the context-specific responses of active dendrites and adapting to different task requirements through adaptive tuning.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/28b02b3f-5a51-4d69-9dbb-282a973fee40)
     
## Experiments
  This paper describes two comparative experiments conducted by the authors to compare the performance of the network in multi-task reinforcement learning and continuous learning scenarios. 
  
  In the first experiment, the authors compared ADN with a standard multilayer perceptron (MLP) and used the task success rate as an evaluation metric. The results show that ADN performs better than the standard MLP in a multi-task reinforcement learning scenario. 
  
  In the second experiment, the authors compared ADN with a benchmark model and used accuracy as an evaluation metric. The results show that ADN performs better than the benchmark model in continuous learning scenarios. In addition, the authors explored whether Dendrites can be equated to larger networks and concluded that ADN cannot be equated to larger or deeper neural networks in dynamic scenarios.
  
## Conclusion
### 1. Advantages of the Thesis
  This paper proposes a new neural network model, Active Dendrites Network (ADN), which solves problems in multi-task learning and continuous learning by introducing biometric features in neurons. Compared with traditional neural networks, ADN has better generalization ability and higher accuracy. In addition, the paper provides experimental results and comparative analysis to demonstrate the effectiveness and superiority of ADN.
  
### 2. Innovative points
  The main innovation of ADN is the introduction of the concept of active dendrites (active dendrites), a biological feature, and its application to the design of neural networks. Specifically, ADN divides each neuron into multiple sub-segments, each corresponding to a different task or situation, and realizes multi-task learning and continuous learning by controlling the activation state of these sub-segments. This design not only improves the flexibility and adaptability of neural networks, but also effectively avoids the occurrence of overfitting phenomenon.
  
### 3. Future Works
  ADN is a very promising neural network model that can play an important role in areas such as multi-task learning and continuous learning. Future research can further explore the application scope and optimization methods of ADN, such as how to better select and combine different contextual signals, and how to improve the training efficiency and stability of ADN. Meanwhile, combining ADN with other deep learning techniques can also be considered to realize more complex and efficient task processing.
