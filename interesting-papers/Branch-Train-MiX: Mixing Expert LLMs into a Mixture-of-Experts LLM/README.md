# Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM
[paper link](https://arxiv.org/pdf/2403.07816) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an approach called ‘Branch-Train-MiX’, which aims to train Large Language Models (LLMs) to have skills in multiple domains of expertise, such as programming, mathematical reasoning and world knowledge.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method starts with a seed model, branches it into multiple specialists for parallel training, and merges their feedforward parameters into specialists in the MoE layer after asynchronous training, and then learns token-level routing through the MoE fine-tuning phase. BTX achieves the best accuracy-efficiency balance compared to alternative approaches.

### 2. Method Description 
The paper proposes a method called ‘Branch-Train-MiX’ for improving the performance of pre-trained language models in specific domains. The method consists of three stages: **branching, training and mixing**. Firstly, based on the existing pre-trained models, multiple expert models are trained separately for different domains with corresponding datasets. These expert models can be trained in parallel, thus improving the overall training efficiency. Then, these expert models are merged into a single language model and fine-tuned to further improve its performance.

![image](https://github.com/user-attachments/assets/ce93fff0-7527-4b7e-b708-361cca27c74e)

### 3. Methodological improvements
The main improvement of the method is the adoption of a Mixture-of-Experts approach to combine expert models from different domains. Specifically, the method constructs a Mixture-of-Experts sublayer by combining feedforward sublayers from experts in different domains in each layer. In addition, for the Self-Attention sublayer, the method combines the weights from different domain experts by averaging them. This approach can effectively utilise knowledge from different domains without adding too many parameters, thus improving the performance of the model.

### 4. Issues addressed 
This approach addresses the problem of poor performance of pre-trained language models in specific domains. While traditional individual pre-trained models often struggle to capture detailed information about a particular domain, the method is better able to adapt to domain-specific task requirements by introducing expert models from different domains. At the same time, the method also features efficient parallel training, which can complete the whole training process more quickly.

## Experiments
This paper focuses on the authors' experiments with continuation training using the BTX method and compares it to multiple baselines. Specifically, they used the Llama-2 pre-trained model as a seed model and continued training it in the domains of maths, code and world knowledge. They then evaluated it for zero/few sample performance in a variety of benchmark tests and compared it to expert models in other domains. The experimental results show that the BTX model outperforms the single-domain continuation-trained model on all tasks and is more efficient than other data matching methods such as dense and sparse upgrading. In addition, the authors provide a deeper understanding of the performance of the BTX model by analysing the routing decisions and suggest some optimisations for design choices.

![image](https://github.com/user-attachments/assets/1542a8c4-20b4-41ef-bdd0-c56908aca42a)

![image](https://github.com/user-attachments/assets/56fa6eb8-c48b-4c64-90e7-8f18b9d6ad77)

## Conclusion

### 1. Advantages of the Thesis
This method combines the advantages of the previously proposed Branch-Train-Merge (BTM) method, i.e., parallelised training improves efficiency significantly and avoids communication costs and the risk of hardware failures in simultaneous training, and introduces the advantages of the Mixture-of-Experts (MoE) method, i.e., large-scale model scaling using a small number of parameters which improves the model performance without increasing the computational effort. Experimental results show that the BTX approach can significantly improve domain-specific performance while maintaining the original capabilities, and especially excels on mathematical and code-related tasks.
 
### 2. Innovative points
  1. Multiple expert models are used for parallel training and then they are merged into a single MoE model. This approach retains the capabilities of the original model while being able to leverage the strengths of the expert models on specific domains, thus improving overall performance.
  
  2. A network of routers is used in the MoE model to select which expert models should be activated. This learned routing approach makes the MoE model more flexible, allowing the weights of individual expert models to be dynamically adjusted according to the input data, thus further improving the model's performance.
     
### 3. Future Works
  1. Although the BTX approach has achieved good results on specific domains such as maths and code, it still has some limitations and room for improvement. For example, only three different domains were used in the experiments, and better results may be found if experiments can be conducted on more domains.
  
  2. In addition, attempts could be made to optimise the design of the MoE model, for example by using a more complex network of routers or by better controlling the capacity of each expert model.
  
  3. Finally, it would also be interesting to consider how the BTX approach could be applied to other types of models, for example in areas such as image recognition or speech recognition.   
