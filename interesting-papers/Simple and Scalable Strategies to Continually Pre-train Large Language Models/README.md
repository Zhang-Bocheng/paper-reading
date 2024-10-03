# Simple and Scalable Strategies to Continually Pre-train Large Language Models
[paper link](https://arxiv.org/pdf/2403.08763) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores how continuous pre-training of large language models can be performed using simple and scalable strategies to save the significant computational resources required for re-training.          | Large Language Models  (LLMs)  |

## Methodology

### 1. Abstract
The authors find that the performance of complete retraining from scratch can be matched by a combination of strategies such as reheating of the learning rate, re-decaying and replaying of previous data. Experimental results show that these simple strategies are effective in updating autoregressive transformer-type language models under different data distribution offsets and can achieve the same level of performance as retraining using only a small fraction of the computational resources. In addition, the authors propose alternative cosine learning rate scheduling strategies to help avoid the forgetting problem caused by learning rate reheating.

### 2. Method Description 
The Continual Pre-Training (CPT) method proposed in this paper is a continuous updating strategy for LLMs. The method is based on sequential pre-training on multiple datasets and keeping the model performance stable through techniques such as dynamically adjusting the learning rate, using partially replicated data, and reheating at appropriate stages.

Specifically, the approach assumes that a pre-trained LLM model needs to go through a serialisation process with two or more pre-training stages. This means that our results apply to models that are randomly initialised and sequentially pre-trained on datasets D0, D1, ... DN-1, where N ≥ 2 and the number of tokens in Di is greater than or equal to 100 B. This includes both existing open-source models and organisations that may wish to pre-train the initial LLM and use it on new data.

![image](https://github.com/user-attachments/assets/ed2f0572-4f03-4697-b61c-7e5e06502148)

## Experiments
This paper focuses on the problem of how to effectively adapt to new data when constantly pre-training a LLM, and proposes a new learning rate scheduling strategy. The article verifies the effectiveness of the strategy through several comparative experiments.

1. The authors conducted experiments on the effect of linear warmup on forgetting and adapting, and the results show that a short period of warmup can increase the rate of adaptation, but the rate of forgetting and adapting gradually slows down with the increase of time. Therefore, the authors chose to set the duration of warmup to 1% of the total number of iterations.

![image](https://github.com/user-attachments/assets/ddcf0b24-1188-4e8e-80e1-c916805d287f)

2. The authors compared the effects of different learning rate scheduling strategies. The authors found that with re-warming and re-decaying strategies, appropriate adjustment of learning rate can balance the relationship between forgetting and adapting. Specifically, the model forgets and adapts more when the value of ηmax is high, and forgets and adapts less when the value of ηmax is low. In addition, the authors find that stronger distributional shifts lead to greater forgetting and adaptation.

![image](https://github.com/user-attachments/assets/15aed0a6-de06-4a51-9aa6-a9c848f99477)

3. The authors explored the effect of the replay method on forgetting and adapting using an equivalent amount of computation. The experimental results show that replay significantly reduces forgetting and increases adaptation, especially in the presence of strong distributional shifts.

![image](https://github.com/user-attachments/assets/5d2fcca5-5c9c-4501-abf9-07888da39325)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new method to improve the effectiveness of Continual Pre-training (CPT) is proposed and experimentally validated. The authors used two different model sizes (405M and 10B) and evaluated it under two distributional variations.
  
  2. In addition, the article explores the possibility of an infinite learning rate scheduling table and proposes a simple combinatorial strategy including reheating, re-decaying and replaying for more efficient continuous pre-training.

### 2. Innovative points
  1. The main contribution of this paper is to propose a new method to improve the effectiveness of continuous pretraining. The authors found that reheating and re-decaying the learning rate are important for adapting to new data and that the forgetting problem can be alleviated by replay.
  
  2. In addition, the authors explore the possibility of infinite learning rate scheduling tables and propose a simple but effective combination strategy for more efficient continuous pretraining.

### 3. Future Works
  1. The methods presented in this paper provide valuable insights for future research. The authors suggest further testing of infinite learning rate scheduling tables on larger models and datasets, and consider other possible optimisation methods such as hybrid experts or block expansion.
  
  2. In addition, the authors plan to apply this approach to multimodal or visual language models and explore how existing models can be used to create replay buffers. These studies will further advance the development of continuous pre-training and are expected to be widely used in future research. 
