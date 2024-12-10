# MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts
[paper link](https://arxiv.org/pdf/2401.04081) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new model called MoE-Mamba that combines a mixture of experts (MoE) with a state space model (SSM) to improve its performance and efficiency.          | Mamba         |

## Methodology

### 1. Abstract
The approach was tested on the Mamba model and it was found that the MoE-Mamba model can achieve the same level of performance in fewer training steps than Mamba and has better inference performance relative to the Transformer-based model.

![image](https://github.com/user-attachments/assets/66f39b76-d6bd-4a68-b9a3-674c395010a2)

### 2. Method Description 
The MoE-Mamba architecture proposed in this paper alternately stacks the Mamba layer with the MoE layer and adds the output of each layer to the residual stream. This approach leaves the task of unconditional processing of each token to the Mamba layer, which efficiently integrates the entire sequence context into the internal representation, while the MoE layer is responsible for applying the most relevant experts (and thus subset parameters) to each token. This idea of alternating conditional and unconditional processing is also used in some designs based on the MoE model, and is usually implemented by alternating the vanilla and MoE fully connected layers.

Another design is to run the MoE layer in parallel while the Mamba layer executes, an approach inspired by Wang (2021) and Chowdhery et al. (2023). Although the results are not as good as MoE-Mamba, they are still positive. In addition, the authors conducted other experiments that modified the original block designs to have conditional MoE computational capabilities. Some of these designs improved over the benchmark architecture and provide promising directions for future research.

![image](https://github.com/user-attachments/assets/1a22ca47-4e0b-478c-9686-cb5f6500f95b)

### 3. Methodological improvements
  1. MoE-Mamba architecture: alternating stacking of Mamba layers with MoE layers for alternating conditional and unconditional processing.
  2. Parallel MoE-Mamba architecture: run the MoE layer in parallel while the Mamba layer executes.
  3. Modified Mamba blocks: modifying the original block design to have conditional MoE computation capability.

### 4. Issues addressed 
The main research goal of this paper is to improve the parametric efficiency of neural network models, especially for large-scale natural language processing tasks. The traditional Mamba architecture is not able to efficiently utilise the whole sequence context information, so the ability of conditional processing needs to be introduced. Both the MoE-Mamba architecture and the parallel MoE-Mamba architecture proposed by the authors successfully achieve this with significant performance gains.

## Experiments
This paper focuses on performance validation experiments of the Mamba model-based MoE (Mixed-effects Model) architecture for natural language processing tasks. Specifically, the authors conducted the following comparison experiments:

**MoE-Mamba versus Mamba, Transformer, and Transformer-MoE:** Using the C4 dataset, these models were trained on the next markup prediction task, and cross-entropy was used as the loss function. The authors use the EMA-smoothed training log perplexity as a comparison metric to measure the effect of the final loss and speedup. The experimental results show that MoE-Mamba shows significant improvements relative to all three other baseline models, and in particular exhibits better performance in small-scale models.

![image](https://github.com/user-attachments/assets/e21255c6-ebfb-4b01-af3c-3d15f3a3a3a4)

**Effect of different number of experts on MoE-Mamba:** The authors explored the performance of MoE-Mamba at different scales by varying the number and size of MoE layers. The results show that increasing the MoE parameter can improve the performance, but when a certain ratio is reached, further increasing the parameter brings the problem of decreasing marginal effect.

![image](https://github.com/user-attachments/assets/39509e91-7740-4ce3-afa6-e4e4350b7e97)

**Design of Parallel MoE-Mamba and Embedded MoE:** The authors tried two different design approaches, parallel MoE-Mamba and embedded MoE, and compared them with MoE-Mamba. The results show that while parallel MoE-Mamba can match or even exceed the performance of MoE-Mamba in some cases, MoE-Mamba is still the superior choice in most cases.

**Effect of different number of experts on MoE-Mamba:** The authors explored the performance of MoE-Mamba at different ratios by varying the number and size of MoE layers. The results show that increasing the MoE parameter improves the performance. 

![image](https://github.com/user-attachments/assets/4d9d7afe-342b-42d2-9a56-905ef2a727a7)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new neural network architecture, MoE-Mamba, and experimentally demonstrate its advantages in terms of training time and performance.
  
  2. The architecture combines Mamba and MoE to improve model efficiency by exploiting the sparsity of MoE and the efficiency of Mamba.
  
  3. In addition, the authors explore different types of MoEs and how MoEs are integrated with Mamba, providing directions for future research.

### 2. Innovative points
The main contribution of this paper is to propose MoE-Mamba as a novel neural network architecture and demonstrate its advantages in terms of training time and performance. The authors also explored different types of MoEs and the way of integration between MoE and Mamba, which are important for further optimisation of neural network architectures. 

### 3. Future Works
The authors mention some possible limitations and future issues that need to be addressed, such as how to achieve MoE compression and how to better utilise long sequence information. The answers to these questions will further advance the development of neural network technology.  
