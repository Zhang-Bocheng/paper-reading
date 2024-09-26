# Sorted LLaMA: Unlocking the Potential of Intermediate Layers of Large Language Models for Dynamic Inference
[paper link](https://arxiv.org/pdf/2309.08968) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new approach, called Sorted LLaMA, for implementing dynamic reasoning in large language models to improve model efficiency and reduce storage and transition costs.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
The approach is based on the previously proposed SortedNet technique and applies it to NLP tasks. Compared to traditional standard fine-tuning, Sorted LLaMA uses the Sorted Fine-Tuning (SoFT) technique to achieve more efficient reasoning without increasing memory usage. Experimental results show that Sorted LLaMA is able to effectively unlock intermediate layers in large language models, resulting in better performance on tasks such as instruction following and closed-ended quizzing.

### 2. Method Description 
This thesis proposes the SortedNet method to unlock the potential of intermediate layers for an all-in-one generative LLAM model. The method first divides the LLAM model into deep sub-networks and trains each sub-network using a shared output prediction header. Then, a RMSNorm layer is used to add normalisation across all sub-models to help Sorted LLAMA generalise better. Finally, experimental evaluations were performed using the Stanford Alpaca dataset and the TriviaQA open-domain quiz benchmarking dataset.

### 3. Methodological improvements
The SortedNet method makes the model more efficient and able to handle multiple tasks simultaneously by dividing the LLAM model into multiple deep sub-networks with shared parameters. In addition, normalisation using the RMSNorm layer helps to improve the generalisation of the model.

### 4. Issues addressed 
The SortedNet approach solves the problem that traditional LLAM models are unable to handle multiple tasks efficiently, while improving the generalisation ability and efficiency of the model. The method is important for natural language processing applications that need to handle multiple tasks simultaneously.

## Experiments
This paper describes experiments with Sorted Fine-Tuning (SFT) on large-scale language models and compares it to traditional Regular Fine-Tuning (RFT). The experiments used two tasks: **instruction following and open domain question and answer**. The experimental results show that sequential training significantly improves the performance of the middle layer, making the generated output closer to the performance of the full model. In addition, the article describes two methods for accelerating text generation: speculative decoding using submodels and instance-aware dynamic reasoning. Finally, the article analyses the effectiveness of sequencing training by comparing the learned probability distributions and hidden state representations.

In the instruction-following task, the authors first divide the original model into multiple sub-models according to different layers, and then train each sub-model and sort them separately. The experimental results show that the sequencing training can significantly improve the performance of the sub-models and make them close to the performance of the full model. Meanwhile, the authors also adopt two methods to accelerate text generation: speculative decoding using sub-models and instance-aware dynamic reasoning. Experimental results show that both approaches can effectively improve the speed of text generation.

![image](https://github.com/user-attachments/assets/10f560a1-3789-4831-9855-efb74197c763)

In the open-domain question and answer task, the authors similarly divide the original model into multiple sub-models with different layers and train them with sequencing. The experimental results show that the sequencing training can significantly improve the performance of the sub-models, bringing them close to the performance of the full model. Meanwhile, the authors also adopt two methods to accelerate text generation: speculative decoding using sub-models and instance-aware dynamic reasoning. The experimental results show that sequencing training can also significantly improve the performance of the submodel in question and answer tasks, bringing it close to the performance of the full model.  

![image](https://github.com/user-attachments/assets/9618266d-3578-47bb-85a5-22c8ce3cf6d1)

## Conclusion

### 1. Advantages of the Thesis
  1. This approach unlocks the potential of the middle layer to enable dynamic adaptation without pre-training or additional cost. The approach provides an optimisation pathway for generative language models in NLP and makes deploying these models more efficient.
  
  2. In addition, the study evaluates the performance of Sorted LLaMA on instruction adherence and Q&A benchmark tests, challenging conventional wisdom and demonstrating that the middle layer can produce high-quality results.

### 2. Innovative points
  1. This approach orders the submodels by their computational/accuracy characteristics, which enables efficient deployment during inference.
  
  2. In addition, the method employs an update scheme that combines random submodel sampling with gradient accumulation to minimise training costs.

### 3. Future Works
Further research is needed to better understand the scope of the Sorted Net approach in LLM. For example, applying this method during pre-training, sorting other model dimensions (e.g., attention head and hidden dimensions), as well as investigating the impact of choosing a specific architecture may provide potential research directions. At the same time, the research in this paper may have some bias and further human evaluation is needed to verify its effectiveness.   
