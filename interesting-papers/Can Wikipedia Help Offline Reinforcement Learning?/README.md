# Can Wikipedia Help Offline Reinforcement Learning?
[paper link](https://arxiv.org/pdf/2201.12122) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 |  This paper explores how pre-trained sequence models and generalized sequence modeling techniques can be used to accelerate the rate of convergence in reinforcement learning (RL) tasks and improve the rewards         | Reinforcement Learning          |
 
## Methodology

### 1. Abstract
  The authors found that when applying these models to offline RL tasks such as control and gaming, they can achieve optimal performance in multiple environments. To further improve transferability, the authors also propose techniques for cross-domain knowledge sharing. Experimental results show that this approach can significantly improve convergence speed and achieve better rewards, while also achieving state-of-the-art performance levels across multiple tasks.
  
### 2. Method Description 
  The paper proposes a new approach to better adapt pre-trained language models to handle trajectory data, especially for applications in offline RL tasks. They do this by using autoregression to represent trajectories and analogizing them to the sequence x. The paper also presents a new approach to the representation of trajectories by using autoregression. In addition, they introduce techniques to encourage similarity between the language representation and the input representation in order to further extract the capabilities of the language model.
  
### 3. Key concepts
  _A Markov Decision Process (MDP)_: A mathematical framework used to model decision-making in environments where outcomes are partly random and partly under the control of a decision-maker. MDPs are widely used in various fields, including robotics, economics, and artificial intelligence, particularly in RL.
  
### 4. Methodological improvements
  To address the lack of alignment between the input representation and the language representation, the paper proposes a similarity-based objective function for maximizing the similarity between the language embedding set and the input representation set. In addition, they used K-mean clustering to reduce the size of the embedding set to the number of clusters and computed the loss using vectorization optimization. And, they tried to train both language modeling and trajectory modeling simultaneously in order to make the model capable of handling both language and trajectory.
  
### 5. Issues addressed 
  The paper addresses the question of how to better utilize pre-trained language models in offline RL tasks. They propose a new approach to handling trajectory data and use a number of techniques to improve the similarity between the language representation and the input representation, which improves the performance of the model.
  
## Experiments
  This paper focuses on the use of pre-trained language models for offline RL and conducts several comparison experiments to verify their effectiveness. Specifically, the following comparison experiments were conducted in this paper:

  1. The performance of using different pre-trained models (GPT2 and CLIP) versus a purely randomly initialized DT model on the Atari game task is compared and significant improvements are achieved;

  2. Compared the performance of using different sizes of language pre-training models (including small-scale ChibiT and large-scale GPT2) with the direct use of a purely randomly initialized DT model on the OpenAI Gym task, and found that the use of a pre-training model resulted in a significant performance improvement;

  3. Compares the effects of using different sizes of verbal pre-training models and visual pre-training models (ImageGPT), and finds that verbal pre-training models outperform visual pre-training models for the same number of parameters;

  4. Compared the effects of using different lengths of contextual information on model performance and found that longer contextual information did not lead to better results;

  5. compared the difference in model performance between freezing the model weights and training only the action, state and reward projection layers, and found that the former performed worse;

  6. Conducted experiments with pre-trained positional embeddings and other techniques for ablation, and demonstrated that these techniques play an important role in improving model performance.

Overall, this paper demonstrates the effectiveness of pre-trained language models in offline RL through several comparative experiments and provides a reference for future research. 

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/70635403-7474-4e80-97da-65249f185ed7)

## Conclusion
### 1. Advantages of the Thesis
  1. The paper presents a new approach to improve the effectiveness of offline RL problems by using pre-trained language models.

  2. It shows that small transformer or GPT2 models trained from Wikipedia can provide significant performance and convergence speed advantages over the basic Decision Transformer and other offline benchmarks based on RL.

  3. The researchers conducted extensive experiments and found that factors such as verbal pre-training (as opposed to visual pre-training), model size, and fine-tuning (as opposed to freezing the parameters) had a critical role in the final performance.

  4. The findings of the paper have important implications for accelerating the application of pretraining in RL and may provide better migration capabilities for the application of other sequence modeling techniques.
     
### 2. Innovative points
  1. This paper presents a methodology for applying pre-trained language models to offline RL, which improves the performance of the algorithm and the speed of convergence.

  2. The researchers also conducted extensive experiments and found the effects of key factors such as language pre-training, model size and fine-tuning.

  3. The results of this study provide implications for the application of other sequence modeling techniques to RL.
     
### 3. Future Works
  1. The results of this study bring new ideas and possibilities to the field of RL.

  2. Future research can further explore the ways in which linguistic structures and neural networks can be combined to achieve better generalization capabilities and adaptability.

  3. Techniques of pre-training can be explored to be applied to other types of sequence modeling tasks to improve their effectiveness and efficiency
