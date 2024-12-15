# Understanding LLMs: A Comprehensive Overview from Training to Inference
[paper link](https://arxiv.org/pdf/2401.02038) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper focuses on trends in large-scale language modelling (LLM) and related advances in training and inference techniques.          | large-scale language modelling (LLM)         |

## Methodology

### 1. Abstract
With the emergence of applications such as ChatGPT, LLMs are increasingly used in downstream tasks. In order to reduce the cost, low-cost training and deployment has become the way forward. The article discusses various aspects of the training aspect including data preprocessing, training architectures, pre-training tasks, parallel training and related aspects associated with model fine-tuning. On the inference side, the article covers aspects of model compression, parallel computing, memory scheduling and structural optimisation and discusses the application and future development of LLM.

### 2. Method Description 
This paper proposes a new pre-training learning method, Prompt Learning, which enables more efficient model training by using natural language cues instead of the traditional self-supervised learning task.Prompt Learning consists of four main parts: using PLMs as the base encoder, adding appropriate contextual templates, mapping labels to vocabulary, and using continuous cues in the prediction phase.

![image](https://github.com/user-attachments/assets/41f3c312-ab68-4664-8283-7bb78ec4c070)

### 3. Methodological improvements
  1. **Higher efficiency:** since Prompt Learning requires only a simple cue to complete the entire pre-training process, it is more efficient than traditional self-supervised learning tasks.
  2. **Better generalisation:** Prompt Learning is able to better capture the semantic information in the text, thus improving the generalisation ability of the model.
  3. **Fewer data requirements:** Since Prompt Learning requires only a simple prompt to complete the entire pre-training process, it requires much less data than traditional self-supervised learning tasks.

![image](https://github.com/user-attachments/assets/ceea4b1f-114e-4827-84ca-b31b36e2e62c)

### 4. Issues addressed 
Prompt Learning solves the problems in traditional self-supervised learning tasks, including high data requirements and low efficiency. At the same time, it is able to improve the generalisation ability and effectiveness of the model, bringing new development opportunities to the NLP field.

## Experiments
This article focuses on optimisation methods and techniques in the training and inference process of Large Language Models (LLMs). In terms of training, the article mentions distributed training techniques such as data parallelisation, model parallelisation, and parameter servers, and describes the advantages and disadvantages of each technique. In addition, the article discusses approaches in model compression, memory scheduling, parallel computing, and structural optimisation to improve model efficiency and reduce cost.

**In terms of model compression**, the article mentions knowledge distillation techniques, which are used to reduce model size without loss of accuracy by transferring knowledge from a complex model to a smaller model. In addition, the article mentions other model compression methods such as pruning techniques and quantisation techniques.

**In terms of memory scheduling** the article mentions techniques that utilise a combination of multiple GPUs and multiple CPUs to reduce memory consumption, and also describes how caching can be used to accelerate the process of model inference.

**In terms of parallel computing**, the article mentions techniques for model parallelisation and data parallelisation that effectively use multiple GPUs or CPUs to accelerate the model training and inference process.

![image](https://github.com/user-attachments/assets/46e37ef6-2ee0-425c-835b-100805fb90f3)

**In terms of structural optimisation**, the article mentions techniques such as low-rank approximation, forward propagation pruning, and parameter-efficient calling, which can reduce the size and complexity of a model while maintaining its performance.

![image](https://github.com/user-attachments/assets/9f41bffe-b114-4405-8749-8d6c90176eb5)

Overall, this article provides a lot of useful information and techniques that can help researchers better understand and apply the training and inference process of LLMs.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper systematically reviews the development of large-scale pre-training models and discusses future research directions.
  2. The paper describes in detail the design ideas and technical implementations of various large-scale pre-training models, and compares their performances on different tasks.
  3. The paper proposes a low-cost development approach to solve the problem of large-scale pre-training models relying on high computational resources, which is of great significance in promoting the application of natural language processing technology.
  
### 2. Innovative points
  1. This paper proposes a cost-effective training and deployment method based on which the computational cost of large-scale pre-trained models can be reduced and their application efficiency can be improved.
  2. By comparing the performance of pre-trained models of different sizes on multiple tasks, the paper proves that small-scale models also have certain generalisation ability, which provides new ideas for future research.
     
### 3. Future Works
  1. This paper argues that future large-scale pre-trained models will focus more on the improvement of semantic understanding ability and cross-modal application ability.
  2. The authors suggest further exploring how to apply large-scale pre-trained models to domain-specific tasks to meet practical needs.
  3. At the same time, research on the security and privacy protection aspects of large-scale pre-training models needs to be strengthened to ensure their reliability and security in practical applications.
