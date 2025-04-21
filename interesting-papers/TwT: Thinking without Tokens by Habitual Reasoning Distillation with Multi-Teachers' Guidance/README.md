# TwT: Thinking without Tokens by Habitual Reasoning Distillation with Multi-Teachers' Guidance
[paper link](https://arxiv.org/pdf/2503.24198) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 |  This paper describes a new approach called TwT (Thinking without Tokens), which aims to reduce the cost and maintain high performance when reasoning with large language models (LLMs) through multi-instructor guided habitual reasoning distillation.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The approach introduces the Habitual Reasoning Distillation method to internalize explicit reasoning into the habitual behavior of the model, while generating high-quality and diverse distillation datasets using a multi-instructor model to make it suitable for unsupervised scenarios. Experimental results show that TwT can effectively reduce inference cost and improve performance, achieving up to 13.6% accuracy improvement with fewer output tokens compared to other distillation methods, providing a solution for efficient deployment of LLM.

![image](https://github.com/user-attachments/assets/d91115cd-d04d-442b-a4d4-44fdd55cdbd1)

### 2. Method Description 
The paper proposes a multi-model distillation strategy called TwT (Teacher-Weighted Teaching) for improving the reasoning ability of student models and reducing computational costs. Specifically, TwT employs a dual-indicator rejection sampling (DCRS) strategy to obtain high-quality and diverse distillation samples, and designs a habitual reasoning distillation (HaRD) strategy to gradually internalize the reasoning ability of the teacher's model into the student's model.

![image](https://github.com/user-attachments/assets/6b29558b-29ec-4951-919f-400fb060bfca)

### 3. Methodological improvements
Compared to the traditional distillation method, TwT introduces the DCRS strategy, which provides high-quality and diverse reasoning paths by combining two key selection criteria, namely confidence scores and similarity measures. In addition, TwT devised the HaRD strategy, which progressively internalizes the reasoning power of the teacher model, allowing the reasoning power of the teacher model to be gradually internalized into the student model.

![image](https://github.com/user-attachments/assets/dc1dd33a-4500-486a-8fa3-896fcde522aa)

### 4. Issues addressed 
TwT addresses the problem in traditional distillation methods of how to reduce computational cost without sacrificing reasoning performance. By using the DCRS strategy to obtain high-quality and diverse distillation samples and the HaRD strategy to gradually internalize the reasoning power of the teacher's model, TwT improves the reasoning power and reduces the computational cost of the student model.

## Experiments
This paper focuses on the TwT approach proposed by the authors for three different NLP tasks (NL to python code generalization, commonsense question answering, and mathematical reasoning), and through a series of comparative experiments it is evaluated and analyzed.

First, for the experimental setup, the authors used three benchmark datasets (MBPP, CQA, and MetaMath) and chose GPT-4, GPT-4omni, and Mistral-Large as the teacher models, Mistral-7B-v0.3 and Phi-3.5mini as the student models, and all-mpnet- base-v2 as the pre-trained sentence embedding model. In the experimental process, the authors used the LoRA fine-tuning approach and set the LoRA rank to 8, the learning rate to 1e-5, the batch size to 8, 4 epochs of training, and a context window of 4096 tokens. In the inference phase, the authors used a temperature value of 0, a maximum number of tokens of 2048, and a top-p value of 0.95 for the sampling process and chose a scoring threshold of 0.95. All experiments are performed on four NVIDIA A100 Tensor Core GPUs for large-scale training and efficient computation.

Next, the authors compare TwT with the baseline method and show that TwT outperforms other distillation methods in all specific tasks. Compared to the best-performing baseline method, TwT achieves up to 13.60% improvement while reducing the number of tokens from 397 to 7, which greatly reduces the inference cost. In addition, TwT also succeeded in closing the performance gap between the student model and the teacher model, achieving both high performance and low computational cost of reasoning time.

And then, the authors analyzed the distillation phase of TwT. The authors evaluated the performance of the student model in each fine-tuning phase separately and tracked the number of inference tokens. The results show that TwT's performance steadily improves with increasing distillation stages, while the number of inference tokens gradually decreases. By utilizing our distillation strategy, the model successfully internalizes the reasoning process as part of its own capabilities. In addition, the authors extended the three-stage distillation process to a four-stage process and added an extra step to further compress the students' reasoning process after the second stage. The results showed that the original three-stage process was sufficiently effective.

![image](https://github.com/user-attachments/assets/1609bfea-17da-416e-b5d2-7969e19dc056)

The authors then evaluated the sampling and compression analyses of the DCRS method in TwT. For sampling, the authors compared alternative methods such as Confidence Score-Based Sampling, Log Probability-Based Selection, and Hard Rejection Sampling, and found that the Confidence Score-Based Sampling method outperformed the other two methods in terms of accuracy. This highlights the effectiveness of our strategy to identify high quality distillation data. For compression, the authors compare Teacher-Guided Compression, Fixed-Length Compression, and Compressor-based methods and find that our method better matches teacher output with the limited capacity of the student model, improving training efficiency and overall performance.

![image](https://github.com/user-attachments/assets/2307c397-a2c9-4942-9d11-6e57bfd52e4d)

Finally, the authors conducted an Ablation Study to analyze the contribution of each component in TwT separately. Specifically, w/o Multi-Teacher Strategy evaluated the effect of using a single teacher model, w/o DCRS evaluated the effect of not filtering distilled data, and w/o Compression Distillation Stage analyzed the effect of direct deletion of the reasoning process. The results show that the average accuracy of the single-teacher approach increased by 1.4% compared to the multi-teacher strategy, suggesting that the multi-teacher strategy provides more diverse reasoning paths that contribute to the learning process of the student model. The direct organization of teacher-generated pseudo-labeled data resulted in a 1.5% increase in average accuracy for TwT compared to the DCRS strategy for TwT, emphasizing the importance of sampling high-quality and diverse data prior to distillation. Finally, TwT's multi-stage distillation approach improves the average accuracy by about 3.5% compared to the direct deletion inference process, whereas the uncompressed approach not only performs poorly but also increases the number of output tokens. This confirms the necessity of progressively internalizing the inference capabilities to obtain optimal performance. 

![image](https://github.com/user-attachments/assets/fdd9d9fd-9cc1-420b-a11a-a5cde5e4bf9c)

## Conclusion

### 1. Advantages of the Thesis
This thesis proposes a new knowledge distillation framework, TwT, that achieves efficient knowledge transfer and maintains high performance at low computational cost by internalizing reasoning capabilities under multi-teacher guidance. Specifically, the framework employs a double-criteria rejection sampling phase to obtain a high-quality and diverse distillation dataset, and incorporates a habitual inference distillation strategy to gradually incorporate the reasoning ability into the student model.

### 2. Innovative points
  1. The main contribution of this thesis is the proposal of a novel distillation framework, TwT, which leverages the internalized reasoning capabilities under the guidance of multiple instructors for efficient knowledge transfer.
  2. And, the thesis introduces innovative approaches such as the bicriteria rejection sampling phase and the habitual inference distillation strategy to further improve the effectiveness of the framework.

### 3. Future Works
In future research, it can continue to explore how to further subdivide the distillation stage to enhance the framework effect, and investigate the implicit natural language inference mechanism, so as to improve the robustness and generalization ability of the model.  
