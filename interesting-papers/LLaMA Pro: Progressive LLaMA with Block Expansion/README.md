# LLaMA Pro: Progressive LLaMA with Block Expansion
[paper link](https://arxiv.org/pdf/2401.02415) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a new post-training method for improving the knowledge level of large language models (LLMs) and reducing forgetting.         |  large language models (LLMs)        |

## Methodology

### 1. Abstract
The method is implemented by extending the Transformer block to be tuned using only the new corpus, thus effectively improving the knowledge level of the model. The experimental results show that LLAMA PRO-8.3B, which is based on the LLAMA2-7B initialisation, performs well in a variety of tasks, including general tasks, programming and mathematics. In addition, LLAMA PRO and its instruction-following version (LLAMA PRO-INSTRUCT) achieved advanced performance in a variety of benchmarks, showing great potential as an intelligent agent for diverse tasks. These findings provide valuable insights into the integration of natural and programming languages and provide a solid foundation for the development of high-level language agents that can operate effectively in diverse environments.

![image](https://github.com/user-attachments/assets/f82998c4-8a24-472f-a71f-1ebc0be0904d)

### 2. Method Description 
The ‘LLAMA Block’ proposed in this paper is a model block that combines a Multihead Self Attention (MHSA) mechanism with a location-independent Fully Connected Network (FFN), which also contains the SwiGLU activation function. The block maps inputs to outputs through residual connections and uses an ‘Identity LLaMA block’ approach to keep the outputs constant during training.

![image](https://github.com/user-attachments/assets/61cf87cf-9c89-442b-920c-789e71d852c8)

### 3. Methodological improvements
In order to solve the possible problem of the ‘Identity LLaMA block’ method, which may result in the RM-SNorm module being unable to be trained, a new initialisation method is proposed in this paper. Specifically, we set the W_O and W3 weight matrices to zero during initialisation, which ensures that MHSA(RMSNorm(x))=0 and FFN(RMSNorm(x))=0, and thus achieves the ‘Identity LLaMA block’.

Moreover, in order to increase the capacity of the model to accommodate domain-specific knowledge, this paper employs a ‘block expansion’ approach. This method expands the model by copying some layers within each group and stacking them on top, while keeping its output behaviour unchanged.

### 4. Issues addressed 
  1. The ‘Identity LLaMA block’ method may result in the RM-SNorm module not being trained.
  2. The original LSTM model is not well adapted to domain-specific knowledge.

## Experiments
This paper presents the authors' experiments using the LLAMA PRO model in a number of domains and compares them with other related models. Specifically, the authors first describe the pre-training and scaling process of the model, and give the relevant experimental setup and parameter configurations. Then, the authors compare the performance of the model in the domains of natural language processing, code and mathematics, respectively, and demonstrate its superior performance. Then, the authors also tested the model on tasks such as fine-tuning and multi-round interaction, and achieved remarkable results. Finally, the authors validate the effectiveness and scalability of the model through a series of experiments and draw the appropriate conclusions.

![image](https://github.com/user-attachments/assets/9136cb25-9e28-45c9-bfab-3cfbeec1c15e)

Specifically, in terms of experiments, the authors first conducted pre-training and scaling experiments of the model, expanding LLAMA PRO from 32 to 40 blocks by combining Stack-dedup and Proof-pile-2 datasets, and employing the flash-attention mechanism to improve the training efficiency. The authors also designed different datasets for tasks in different domains, and analysed and compared them in detail. For example, in the domain of natural language processing, the authors used BigCode Evaluation Harness2 to evaluate the performance of the model on tasks such as HumanEval and MBPP and compared it with other models. In the code and maths domain, the authors used datasets such as GSM8K and MetaMath to evaluate the model's performance and found that LLAMA PRO performed well on these tasks. In addition, the authors tested the model on tasks such as fine-tuning and multi-round interactions and achieved significant results.

![image](https://github.com/user-attachments/assets/15042a63-4fd6-4fcb-af1a-d7c19b51fed3)

![image](https://github.com/user-attachments/assets/5f14e8a4-fd50-49f1-ab34-ec52e2cdb3ea)

## Conclusion

### 1. Advantages of the Thesis
  1. A novel approach to post-pretraining, called block expansion, is proposed that allows for the injection of new knowledge while preserving initial capabilities.
  2. Two multimodal general-purpose language models, LLAMA PRO and LLAMA PRO- INSTRUCT, are introduced, which nicely blend natural and programming languages and excel in general tasks, programming and mathematics.
  3. The performance of the LLAMA PRO family is evaluated on a wide range of benchmarking datasets, including traditional and agent-oriented tasks, demonstrating its superiority and great potential in a wider range of complex applications.

### 2. Innovative points
  1. Extending pre-trained large language models with better domain-specific capabilities using replicated Transformer blocks.
  2. Newly added blocks use zero-initialised linear layers for identity mapping, while other blocks are frozen, thus avoiding the problem of forgetting the original general capabilities.
  3. The extended blocks were trained for about 7 days using open-source code and math data, and then further optimised for performance through command fine-tuning (SFT). 

### 3. Future Works
  1. Apply this approach to other domains, such as maintaining raw language capabilities for multimodal large language models(LLMs) and the multilingual domain.
  2. Further explore how this approach can be combined with other techniques to improve the capability and efficiency of large language models.
  3. Investigate how to better address the challenges of highly specialised domains and enable wider application in various application scenarios.   
