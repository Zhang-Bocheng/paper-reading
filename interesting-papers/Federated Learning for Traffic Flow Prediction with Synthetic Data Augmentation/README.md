# Federated Learning for Traffic Flow Prediction with Synthetic Data Augmentation
[paper link](https://arxiv.org/pdf/2412.08460) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the large amount of data and privacy issues required for deep learning-based traffic flow prediction models and proposes federated learning (FL) as a decentralised data-driven approach to address these issues.          |  Federated Learning  (FL)      |

## Methodology

### 1. Abstract
The authors propose FedTPS, a cross-agency FL framework that generates synthetic data to augment each client's local dataset by training a diffusion trajectory generation model. Experimental results show that FedTPS outperforms multiple other FL baselines in terms of global model performance. This research provides a better solution for traffic flow prediction applications.

### 2. Method Description 
The paper proposes a federated learning framework called FedTPS (Federated Trajectory Prediction System) for sharing trajectory data between multiple organisations and training predictive models. The framework consists of two phases: **first generating synthetic data through a diffusion model, and then using this synthetic data along with local data to train a traffic flow prediction model.**

In the first phase, the DiffTraj diffusion model is used to generate synthetic data. The traditional diffusion model cannot be directly applied to this situation as the raw data is distributed across different organisations. In this case, the FedAvg algorithm is used to coordinate the model updates between the various organisations and ultimately results in a global model. This global model is used by each client to generate condition information, which is then merged by the server to form a central synthetic dataset.

In the second phase, local and synthetic data are used to train the traffic flow prediction model. The authors introduced the Graph Attention with Temporal Attention Unit (GATAU) model to deal with the relationships between different areas of the city. The model employs an Encoder-Decoder architecture and uses a multi-head graph attention mechanism to capture the relationships between nodes. The model also employs a Temporal Attention Unit to capture the dynamic changes in the sequence.

![image](https://github.com/user-attachments/assets/65d3c894-c642-484d-b0a0-8c15d540fa10)

### 3. Methodological improvements
  1. The main contribution of this thesis is to propose a methodology suitable for trajectory data generation and traffic flow prediction model training in a federated learning environment. By using a diffusion model and a multi-head graph attention mechanism, the method is able to efficiently utilise information from distributed data sources while protecting user privacy.
  
  2. And, the method provides a complete federated learning framework, including the processes of data generation, model training and parameter aggregation. This framework can be easily extended to other similar application scenarios.

### 4. Issues addressed 
  1. How to share trajectory data across multiple organisations to better understand traffic flows in cities.
  2. How to generate synthetic data without compromising user privacy to enhance the generalisation of the model.
  3. How to train traffic flow prediction models in a distributed environment to improve the accuracy and efficiency of the models.

## Experiments
 This paper describes federated learning experiments conducted on real-world traffic data and provides a comparative analysis of different frameworks and models. The experiment is divided into the following five main parts:

**Dataset description:** a dataset of urban taxi trip trajectories in Chongqing provided by DDT is used, and the data is divided into training, validation and test sets, and preprocessed and grouped.

![image](https://github.com/user-attachments/assets/4dd55667-e29e-4971-b8ab-f726066a6f0e)

**Experimental setup:** several experiments are designed to evaluate the effectiveness of different federated learning frameworks and models, including experiments on generative trajectory prediction, traffic flow prediction and pre-training.

![image](https://github.com/user-attachments/assets/883f442e-88b1-4473-9349-8c4ef71d7078)

**Model performance evaluation:** the performance of different models is evaluated by calculating metrics such as mean absolute error (MAE) and root mean square error (RMSE).

**Analysis of results:** The experimental results are analysed and interpreted in detail, the strengths and weaknesses of the different frameworks and models are discussed, and suggestions for improvement are made.

![image](https://github.com/user-attachments/assets/1251100e-fb63-4ed8-b5ec-1e270c18c270)

**Discussion and outlook:** the future direction and application prospects of federated learning in the future are discussed, and some possible research directions and challenges are proposed. 

## Conclusion

### 1. Advantages of the Thesis
  1. A federated synthetic data generation model is trained and used to generate a synthetic dataset of regional traffic flows based on a global distribution, which is then distributed to all clients to augment their local datasets.
  
  2. The framework is able to reduce the heterogeneity between client data and increase the amount of information available during local training, thereby consistently outperforming other federated learning mechanisms across a variety of different client settings and different traffic flow prediction models.
  
  3. The authors also develop a novel traffic flow prediction model, GATAU, which builds on top of an existing spatio-temporal model, TAU, and utilises the graph attention mechanism.
  
  4. The authors simulate a federated learning environment for the traffic flow prediction task on a large shared mobility dataset in Chengdu to validate the effectiveness of FedTPS.

Methodological Innovations
 
### 2. Innovative points
  1. The paper proposes a new federated learning framework, FedTPS, for data augmentation in the traffic flow prediction task.
  
  2. The framework first trains a federated synthetic data generation model, then uses the model to generate a synthetic dataset of regional traffic flows based on a global distribution, and finally distributes the synthetic dataset to all clients to augment their local datasets.
  
  3. The framework is able to reduce the heterogeneity between client data and increase the amount of information available for local training, thus enabling the use of different traffic flow prediction models in a variety of different client settings and different
     
  
