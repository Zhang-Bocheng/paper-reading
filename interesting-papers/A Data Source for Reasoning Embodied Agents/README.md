# A Data Source for Reasoning Embodied Agents
[paper link](https://arxiv.org/pdf/2309.07974) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a new data generator for machine reasoning tasks.          | Transformer         |

## Methodology

### 1. Abstract
The data generator, in combination with an agent with a body, generates templated textual queries and answers and matches them to a world state encoded into a database. The world state is the result of the agent's actions and world dynamics. The authors show how well these models perform in answering questions about the state of the world by applying pre-trained language models and knowledge graph-based Transformer models to instantiated results from the training set. However, these models experienced difficulties in answering other questions. This suggests new research directions for designing neural inference models and database representations. The authors will release the code for use at github.com/facebookresearch/neuralmemory.

![image](https://github.com/user-attachments/assets/54fdb3ba-e730-4381-a951-fea43d330fa9)

## Experiments
This paper presents experiments conducted by the authors on four different dataset versions and compares the performance of two different models in answering world context questions. The four different datasets include **attribute queries, temporal queries, geometric queries, and all queries**. For each query type, the authors generate data using two temporal snapshots and use one of them for testing. In addition, the authors provide four different types of dataset profiles for use.

In the experiments, the authors used two different models for textual sequence contexts and structured contexts. For text sequence contexts, the authors used the pre-trained GPT-2 mini-model for prediction. Whereas for structured contexts, feature extraction is performed on nodes by learning a convolutional layer and a self-attention mechanism is used to process contextual and query information. The authors also propose a new approach to encode relational information directly into the self-attention mechanism in the sequence context.

![image](https://github.com/user-attachments/assets/55d3d4f9-97ac-48ef-bef3-037492af62b7)

The authors use accuracy as an evaluation metric and show the results for each dataset version. The results show that the method using sequence context plus GPT-2 performs best for attribute queries and geometric queries. Whereas the approach using structured context plus Transformer is more suitable for solving other types of queries. In addition, the authors conducted experiments with various parameters and model variants and drew relevant conclusions. 

![image](https://github.com/user-attachments/assets/a33368ed-9944-4014-b480-5b12eb9b4217)

  
