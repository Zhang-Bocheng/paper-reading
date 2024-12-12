# TrajWeaver: Trajectory Recovery with State Propagation Diffusion Model
[paper link](https://arxiv.org/pdf/2409.02124) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper proposes a new trajectory recovery framework, TrajWeaver, which is based on a probabilistic diffusion model and is capable of recovering dense and refined trajectories from sparse original trajectories based on a variety of auxiliary features (e.g., areas of interest along the route, user identity, and waybill information)          | Urban Computing & Diffusion Model      |

## Methodology

### 1. Abstract
With the proliferation of location-aware devices, a large amount of trajectory data is generated as people, vehicles, and goods move through urban environments. However, these raw trajectories are usually sparse and fragmented due to factors such as sampling rate, infrastructure coverage and data loss. Therefore, trajectory recovery aims to reconstruct these sparse raw trajectories into dense and continuous trajectories in order to capture the fine-grained movements of agents in space and time. Existing trajectory recovery methods typically rely on a priori knowledge of travel patterns or movement patterns, and often fail in densely populated areas where accurate maps are missing. 

At the core of TrajWeaver is a novel State Propagation Diffusion Model (SPDM), which introduces a new state propagation mechanism based on the standard diffusion model that allows knowledge computed in earlier diffusion steps to be reused in later steps, thus improving the recovery performance and reducing the number of required steps. Experimental results show that the proposed TrajWeaver can recover original trajectories of various lengths, sparsities and heterogeneous travel patterns and significantly outperforms state-of-the-art baseline models in terms of recovery accuracy.

### 2. Method Description 
This paper proposes TrajWeaver, a diffusion model-based trajectory recovery method whose main inputs include a sparse trajectory, a query sequence, and some contextual information related to the trajectory. The method distinguishes between known and unknown locations by generating a binary mask and uses linear interpolation to generate an initial estimate of the trajectory. Next, a representation of the trajectory containing all timestamps is obtained by embedding the trajectory in a sequence and aggregating it using a self-attentive mechanism. Then, the exact location of each unknown position is predicted through a multi-step diffusion process, and an adaptive state propagation mechanism (SPDM) is used to enable cross-step information sharing and feature reuse to improve the quality of the recovery while reducing the latency.

![image](https://github.com/user-attachments/assets/b1d7ac0e-44ff-4794-8c85-8be6ac8a0baa)

### 3. Methodological improvements
Compared to the traditional diffusion model, TrajWeaver introduces the adaptive state propagation mechanism (SPDM), which makes cross-step information sharing and feature reuse possible. In addition, it employs multi-scale feature extraction and serialised feature representation to enhance the scalability and robustness of the model.

### 4. Issues addressed 
TrajWeaver mainly solves two problems in trajectory recovery: **noise addition and trajectory reconstruction**. In the noise addition stage, it can generate a set of noise sequences based on the combination of random single-step noise and multi-step noise to simulate the trajectory changes in the real environment. In the trajectory reconstruction phase, it is able to achieve cross-step information sharing and feature reuse through the adaptive state propagation mechanism (SPDM) to improve the recovery quality while reducing the delay. 

## Experiments
This paper focuses on TrajWeaver, a deep learning-based trajectory recovery method, and demonstrates its superior performance and efficiency in different scenarios through several comparative experiments.

Firstly, the authors conducted experiments using two dense and smooth taxi trajectory datasets as well as a real logistics scenario dataset collected by a walk-in courier. Among them, the authors used three evaluation metrics to assess seven different methods, including Mean Square Error (MSE), Normalised Dynamic Time Warping (NDTW) and Jensen-Shannon Scatter (JSD). The experimental results show that TrajWeaver performs well in most of the metrics and datasets with strong robustness and validity.

![image](https://github.com/user-attachments/assets/565c83d6-2da3-42a2-8c2c-c76ebe415e59)

Secondly, the authors also compared TrajWeaver with five other baseline methods, including DeepMove, AttnMove, PriSTI, DT+RP, and Tw. The experimental results show that TrajWeaver outperforms the other methods in most of the scenarios, and especially outperforms them in complex scenarios.
In addition, the authors performed scalability analysis and efficiency analysis. In the scalability analysis, the authors used different trajectory datasets with fixed length and sparsity to demonstrate the high performance of TrajWeaver under different conditions. In the efficiency analysis, the authors combine the DDIM acceleration technique with SP-DDIM to achieve efficient trajectory recovery and better recovery quality.

![image](https://github.com/user-attachments/assets/b3cdc49d-0e00-4be0-b2fa-328fcd9aef6c)

Finally, the authors also conducted a case study where courier trajectories in a logistics scenario were recovered using TrajWeaver and compared with real workloads. The experimental results show that TrajWeaver can effectively improve the trajectory density and thus estimate the workload more accurately.

![image](https://github.com/user-attachments/assets/0b8934c8-56ed-4c0e-99f2-4b6816cb4810)

### 1. Advantages of the Thesis
  1. The paper proposes TrajWeaver, a diffusion model-based trajectory recovery framework that can effectively aggregate and fuse multiple conditions for efficient and accurate trajectory recovery.
  2. TrajWeaver introduces State Propagation Diffusion Model (SPDM), a new variant of diffusion model, which achieves cross-step information sharing and feature reuse through state propagation pipelines, improves recovery efficiency and enhances scalability.
  3. The paper carries out a large number of experimental validations, including comparisons with existing methods, ablation studies, and real-world case studies, to demonstrate the effectiveness and applicability of TrajWeaver.
       
### 2. Innovative points
  1. TrajWeaver adopts a new diffusion model variant, SPDM, which introduces a state propagation pipeline into the standard denoising process, enabling cross-step information sharing and feature reuse, improving recovery efficiency and enhancing scalability.
  2. TrajWeaver designs an efficient condition aggregation module that can handle different types of conditions and integrate them into the multi-step recovery process.
  3. TrajWeaver uses a dedicated SPDM training algorithm that optimises the model parameters to improve the quality and speed of trajectory recovery. 

### 3. Future Works
  1. The application of SPDM structures to other domains, such as image or text generation, could be further explored for more efficient high-quality data recovery.
  2. Consideration could be given to integrating advances in other diffusion techniques into TrajWeaver to improve performance or reduce computational costs.
  3. Research can continue on dynamic, real-time data streams to support dynamic, on-the-fly trajectory recovery in rapidly changing urban environments.
