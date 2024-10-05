# SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents
[paper link](https://arxiv.org/pdf/2403.08715) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an interactive learning method called SOTOPIA-π that aims to improve the social intelligence of linguistic agents.          | Large Language Model (LLM)         |

## Methodology

### 1. Abstract
The method uses behavioural cloning and self-reinforcement training to filter social interaction data based on Large Language Model (LLM) ratings. The authors show experimentally that using this approach allows a 7B LLM to achieve the social goal completion ability of an expert model (GPT-4 based agent) and improves the security of the language agent while maintaining generalised question and answer ability on the MMLU benchmark test. In addition, the authors find that this training paradigm reveals some of the difficulties that exist when assessing social intelligence based on LLMs: LLM-based assessors overestimate the abilities of linguistic agents dedicated to social interactions.

### 2. Method Description 
This paper proposes a framework called SOTOPIA-π for improving the social intelligence capabilities of linguistic agents. The framework is implemented in three steps: **social task generation, training data collection and agent strategy update**. In the social task generation phase, a series of social tasks are automatically generated using the dynamic task generation principle, and scenarios and social goals are generated using the GPT-4 model. In the training data collection phase, based on the generated social tasks, the interaction between two GPT-4 models is used as a data source for behavioural cloning and self-reinforcement learning is performed using a role-playing agent strategy. Finally, in the agent strategy update phase, the agent strategy is updated using supervised fine-tuning based on the collected training data.

![image](https://github.com/user-attachments/assets/3ffc2541-dd69-48b8-a45b-d9eab1ed6ae7)

### 3. Methodological improvements
Compared to the previous SOTOPIA approach, SOTOPIA-π employs an automated and scalable approach to generate a large number of unfiltered social tasks, avoiding the time and effort costs associated with manually filtering tasks. In addition, SOTOPIA-π introduces self-reinforcement learning, allowing agents to learn and optimise without expert data.

### 4. Issues addressed 
The main goal of SOTOPIA-π is to improve the social intelligence capabilities of language agents so that they can better adapt to diverse social environments and achieve better social performance. At the same time, the framework provides an effective learning paradigm for AI research in other fields, such as dialogue systems and natural language processing.

## Experiments
This paper focuses on the results of the authors' experiments in SOTOPIA-π and compares them with the GPT-4. Specifically, they used three approaches to improve the behaviour of the Mistral-7B-based expert model and the GPT-4: behavioural cloning, self-reinforcement, and a combination of these two approaches. They then trained and evaluated these models in SOTOPIA to determine whether they were able to improve the social intelligence abilities of language agents.

In their experiments, the authors first used the GPT-4 to generate 100 social tasks, each consisting of a dialogue between two characters, for training the models. For each task, they ran 10 social interactions, each involving a different role-player (i.e., the agent model), collecting and filtering multiple rounds of dialogue as training data. They then used this training data to train three improved methods and compared them to a benchmark model based on GPT-3.5-turbo. Finally, they evaluated the models by both automatic and human scoring to determine their performance on different social dimensions.

![image](https://github.com/user-attachments/assets/1dee3ee8-31e1-4bec-95d7-0da11cded389)

Overall, the authors found that the performance of the agent model on goal completion could be significantly improved through methods such as behavioural cloning and self-reinforcement, but that this method of evaluation may overestimate the model's capabilities. In addition, they found that these methods achieved similar results across all social tasks in SOTOPIA. However, they also noted some limitations during the evaluation process, such as the fact that the GPT-4 may not accurately reflect the true performance of the model based on the evaluation.

![image](https://github.com/user-attachments/assets/802ec371-c824-4179-bcec-d373bb77c848)

In addition to this, the authors explored the impact of SOTOPIA-π on other aspects, such as safety and continuous learning ability. By analysing a specific task, they found that SOTOPIA-π-trained models were better able to avoid generating harmful content while maintaining social interactions, and their performance in areas such as problem solving ability and understanding context was not significantly affected. This suggests that there may be some independence between social and generalised intelligence.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes an interactive learning method, SOTOPIA-π, to improve the linguistic social competence of AI agents by utilising the scores of large-scale language models (LLMs) as learning signals, and achieve significant performance gains in social intelligence benchmark tests.
 
  2. In addition, the approach improves security and does not degrade general-purpose question-answering capabilities. Although SOTOPIA-π shows strong social intelligence improvement, there are still some directions to further improve the method, such as online reinforcement learning, and training agents using human datasets.

### 2. Innovative points
This paper proposes the SOTOPIA-π interactive learning method, which uses the scores of a large-scale language model (LLM) as learning signals to improve the linguistic social competence of an AI agent. The method also explores the use of human datasets to train agents to reduce potential social biases.
 
### 3. Future Works
Future directions for improvement include 

(1) online reinforcement learning, 
(2) using human datasets to train agents, 
(3) exploring how to develop safety metrics for all socialisation tasks, and 
(4) considering more robust assessment and learning signals. 

In addition, there is a need to continue to examine the potential for social bias when using LLMs as evaluators and to take steps to address these issues. There is also a need for increased research to ensure that AI systems are safe and socially responsible.   
