# A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future
[paper link](https://arxiv.org/pdf/2504.12328) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | The purpose of this paper is to provide a comprehensive investigation of Reward Model (RM) and explore its applications and challenges in enhancing Large Language Models (LLM).          | Large Language Models (LLM)         |

## Methodology

### 1. Abstract
The article first introduces the current state of research on the concept of RM, collecting preference information and modeling, and then describes the application scenarios as well as the evaluation criteria of RM. In addition, the paper provides an in-depth analysis of the challenges in the field and suggests future research directions. Overall, this paper provides a comprehensive introduction to RM for beginners and helps to promote the further development of the related field.

![image](https://github.com/user-attachments/assets/ff1a4363-ddc4-4e16-9e3e-091c813c59ef)

### 2. Method Description 
The paper proposes two reward models: **preference collection and reward modeling**. Preference collection includes direct transmission of human preferences and indirect transmission based on agent modeling. Reward modeling, on the other hand, is divided into three types: discriminative rewards, generative rewards, and implicit rewards. Among them, discriminative reward predicts the quality of the response through a classifier; generative reward uses a trained generative model to evaluate the response and compare it with the target response; and implicit reward enables unsupervised learning of rewards by optimizing certain metrics.

![image](https://github.com/user-attachments/assets/81becc99-21c4-4087-81b6-96b6affb81ce)
![image](https://github.com/user-attachments/assets/f5bd251f-1ca7-4d06-b86d-240e9be217fb)

### 3. Methodological improvements
The method proposed in this paper focuses on the reward problem in reinforcement learning. Through the design and application of the reward model, the performance of the model on a specific task can be effectively improved. At the same time, the method is also universal and applicable to various types of reinforcement learning scenarios.

### 4. Issues addressed 
The reward model proposed in this paper can effectively solve the problem of unclear or hard-to-define rewards in reinforcement learning. By designing a reasonable reward model, the model can be made to more accurately understand the goals and desired behaviors of the task, thus improving the performance of the model. In addition, the method can be applied to other fields, such as dialog systems, reasoning, etc., providing a new idea and method for research in related fields.

## Experiments
This article focuses on the application of reinforcement learning based on reward mechanisms in natural language processing, and discusses some of the problems and future directions.

  1. The article mentions the problem that evaluation using rule models (RMs) also introduces intrinsic biases, which may come from the evaluator's own characteristics, e.g., length, specificity, and so on. Therefore, more robust evaluation benchmarks need to be constructed to detect and mitigate these problems.

  2. The article discusses the trend of combining scalar rewards with rule-based rewards. In industrial-scale large-scale language models, fusing rule rewards and model rewards can improve the robustness of the model. Rule rewards provide clear guidelines for the task, while model rewards enable the model to learn from the predicted results. In addition, rule rewards are typically applied to tasks with clear truths (e.g., math, programming), while model rewards are applied to tasks without clear truths (e.g., creative tasks), thus enhancing the applicability of the model in the real world.

  3. The article mentions issues such as how to design high-quality multimodal reward signals and how to enhance cross-domain generalization capabilities. Meanwhile, exploring some technical tools, such as small number of samples learning and data synthesis, to reduce the reliance on human annotators is also one of the future research directions.
 
## Conclusion

### 1. Advantages of the Thesis
  1. Relevant research on reward modeling in the LLM era is systematically presented, and a detailed classification system is presented.
  2. Practical applications, challenges, and potential research directions of reward modeling are discussed.
  3. Some open questions are provided for further exploration.
 
### 2. Innovative points
  1. A systematic organization and presentation of reward models is provided, filling a gap in the literature in the related field.
  2. A detailed classification system is presented, including aspects of preference collection, reward modeling, and use.
  3. The advantages of reward models in reducing human involvement, increasing the consistency of intelligentsia behavior with human values, and interpretability are emphasized.

### 3. Future Works
  1. More research may be needed to address some of the challenges facing reward modeling, such as reward hacking.
  2. More in-depth research may be needed to determine whether rule-based rewards are sufficient to support reinforcement learning.
  3. More research may be needed to compare the advantages and disadvantages between hybrid expert models and Bayesian inference models.
  
