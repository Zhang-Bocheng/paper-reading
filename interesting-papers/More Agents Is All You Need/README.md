# More Agents Is All You Need
[paper link](https://arxiv.org/pdf/2402.05120) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores how the performance of Large Language Models (LLMs) can be improved by a sampling voting method known as ‘agent forests’ and demonstrates the extent to which it correlates with task difficulty.         | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method is independent of existing complex methods and can further enhance the performance of LLMs. The authors conducted extensive experiments to validate their findings and investigated the properties that facilitate this phenomenon. In addition, they make their code base publicly available for others to use and extend.

### 2. Method Description 
This paper propose a method called Agent Forest, which is implemented through a two-stage process: **sampling and voting**. In the sampling phase, the authors use a single pre-trained model (LLM) or integrate it with other methods to generate N samples, each of which is denoted as s = M(x) or fM(x). In the voting phase, the authors compute the cumulative similarity of each sample with respect to the other samples, and select the sample with the highest cumulative similarity as the final answer A.

Specifically, in the voting phase, the authors first compute the cumulative similarity of each sample with respect to the other samples, i.e., V(si) = N j=1,j)=i sim(si, sj), where sim(si, sj) is the metric used to measure the similarity between two samples. For open-ended generative tasks, such as code generation, the authors use the BLEU score proposed by Papineni et al. in 2002 to quantify similarity, while for closed-ended tasks, such as multiple-choice questions, the authors use the frequency of occurrence to measure similarity. 

![image](https://github.com/user-attachments/assets/bde7af2b-c31e-482b-8bff-17709a45b58f)

### 3. Methodological improvements
Compared to the traditional single model, Agent Forest improves the performance and robustness of the model by bringing multiple pre-trained models into collaboration. In addition, Agent Forest introduces diverse sampling strategies, allowing the model to better adapt to different task types and data distributions.

![image](https://github.com/user-attachments/assets/9180d3a6-929e-4b9d-9b25-5e792e7fc7ca)

### 4. Issues addressed 
Agent Forest mainly solves problems in multimodal tasks, such as image classification and NLP. In these tasks, a single model may not be able to capture all the features and patterns, so multiple models are needed to collaborate to improve the performance and robustness of the model. Agent Forest provides a simple but effective way to achieve this goal, which can be applied to a variety of multimodal tasks.

## Experiments
This paper focuses on using the Agent Forest approach to enhance the performance of different tasks and language models, and validates the effectiveness of the approach through several comparative experiments. Specifically, the authors conducted the following comparison experiments:

**Enhancement Effectiveness Comparison Experiment:** this experiment compares the effectiveness of using the Agent Forest method with other related methods, and the results show that the Agent Forest method significantly improves the performance on all tasks and language models, and is able to enable smaller language models to outperform larger ones.

![image](https://github.com/user-attachments/assets/f6433834-9cb6-43e8-9c46-afaa3a4e3ae9)

**Compatibility experiment:** this experiment investigates the effect of combining the Agent Forest approach with other approaches, and the results show that integrating the Agent Forest approach can further improve performance, but in some cases it fails.

**Effectiveness Analysis Experiment:** This experiment explores the relationship between the performance of the Agent Forest method and task difficulty by analysing tasks of different difficulty. The results show that as the task difficulty increases, the performance of the Agent Forest method increases accordingly, but performance degradation may occur at too high a level of difficulty. 

## Conclusion

### 1. Advantages of the Thesis
  1. The method does not require a complex multi-agent collaboration framework or design artefact hints and can be used in conjunction with existing complex methods to further improve performance.
  2. In addition, the authors analyse the impact of problem difficulty on the effectiveness of Agent Forest and propose optimisation strategies to provide directions for further research.
  
### 2. Innovative points
  1. The Agent Forest method proposed in this paper is a simple and effective solution to improve model performance by increasing the number of instantiated LLMs.
  2. The method does not require a complex multi-agent collaboration framework or design artefact hints and can be used in conjunction with existing complex methods to further improve performance.
  3. This approach is a ‘straightforward’ approach that is lacking in existing research and is innovative.
 
### 3. Future Works
The research in this paper provides a new way to improve the performance of large-scale pre-trained models, but there are still some challenges that need to be addressed. Therefore, there is a need to further explore these issues and find more effective solutions in future research.  
