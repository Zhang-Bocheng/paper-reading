# BLEURT: Learning Robust Metrics for Text Generation
[paper link](https://arxiv.org/pdf/2004.04696.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new text generation evaluation metric -- BLEURT         |  Transformer         |

## Methodology

### 1. Abstract
  BLEURT is a BERT-based learning assessment metric that can model human judgments using thousands of potentially biased training samples. The key to the approach is a novel pre-training scheme that uses millions of synthetic examples to help generalize the model. Experimental results show that BLEURT provides state-of-the-art performance on the WMT Metrics shared task and the WebNLG competition dataset, and also outperforms traditional BERT methods when training data is scarce or inconsistently distributed.
  
### 2. Method Description 
  The paper proposes a method to predict human ratings based on a learning function from a training dataset. The reference sentence is first defined as (x1,... ,xr), where each xi is a token; then the predicted sentences are represented as length p's (x'1,... ,xp). Given a training dataset {(xi,x'i,yi)}^N_{n=1}, where yi is a human rating that indicates how good x'i is relative to xi. The goal is to learn a function f:(x,x')→y that predicts human ratings.
  
### 3. Methodological improvements
  Unlike traditional machine translation methods, this method uses a learning function based on a training dataset to predict human ratings. The advantage of this approach is that it can utilize a large amount of known data for model training and can be better adapted to different text types and language styles.
  
### 4. Issues addressed 
  The method solves some problems in traditional machine translation, such as the lack of sufficient training data and the inability to adapt to different text types and language styles. By using a learning function based on the training dataset, the method can achieve better generalization ability among different text types and language styles, thus improving the quality and accuracy of machine translation.
  
## Experiments
  This paper presents research results on the optimization of text generation tasks using self-supervised pre-training techniques. The authors first describe the construction and pre-training process of the BLEURT model and conduct experimental comparisons on several datasets such as the WMT Metrics Shared Task. Specifically, the authors demonstrate that the BLEURT model has better performance performance by comparing it with existing automatic evaluation metrics and other participants' methods. 
  
  In addition, the authors demonstrate the ability of the BLEURT model in adapting to new tasks and dealing with quality drift by conducting experiments on different datasets and different tasks. Finally, the authors also conducted several Ablation experiments to analyze the impact of different pre-training tasks on the BLEURT model.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/94ac6a18-d2d1-4568-951b-133d30816df7)

  In conclusion, the main contribution of this paper is to propose a new text generation model based on self-supervised pre-training techniques and to demonstrate its superior performance by conducting experiments on multiple datasets. Meanwhile, this paper also provides an in-depth analysis and explanation of the BLEURT model, which provides a valuable reference for subsequent research.

## Conclusion
### 1. Advantages of the Thesis
  1. The paper presents a new text generation evaluation metric, BLEURT, that better models human evaluation and shows superior results on multiple tasks.

  2. BLEURT is a BERT-based reference base text generation metric that uses randomly perturbed Wikipedia sentences as well as diverse semantic and lexical level supervised signals for pre-training, improving its generalization ability and robustness.

  3. The paper also conducts a large number of experimental validations, including datasets from different domains such as WMT Metrics Shared Task, WebNLG, etc., to demonstrate the effectiveness and adaptability of BLEURT.
     
### 2. Innovative points
  1. BLEURT is a new evaluation metric for text generation that differs from traditional rule-based or manual feature-based approaches in that it improves its expressive and generalization abilities through pre-training.

  2. BLEURT adopts BERT as its base model and adds customized supervised signals on top of it to make it more suitable for text generation task evaluation.

  3. BLEURT also introduces the concept of synthetic datasets, and by pre-training on large-scale datasets, it enables BLEURT to perform well in different domains and qualities.

### 3. Future Works
  1. The success of BLEURT shows that pre-training techniques can play an important role in the field of natural language processing and more application scenarios can be explored in the future.

  2. Further research can be done to investigate how BLEURT can be used in conjunction with other evaluation metrics to obtain more comprehensive evaluation results.

  3. Extending BLEURT to other languages can be considered to meet the needs of multilingual text generation.
