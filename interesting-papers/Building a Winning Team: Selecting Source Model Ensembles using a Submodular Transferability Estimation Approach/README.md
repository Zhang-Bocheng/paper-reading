# Building a Winning Team: Selecting Source Model Ensembles using a Submodular Transferability Estimation Approach
[paper link](https://arxiv.org/pdf/2309.02429) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | The aim of this paper is to address the problem of multiple source model selection.          | Transfer Learning         |

## Methodology

With the growth in the number of pre-trained models and the popularity of model integration, it is necessary to study the transferability of multiple source models on a given target task. However, existing approaches study transferability in the case of multi-source integration using only classification layer outputs and ignore possible domain or task mismatches. In addition, they ignore one of the most important factors in the selection of source models - the coherence between models, which can affect the performance and predictive confidence of the integration. 

To address these issues, the authors propose a novel OSBORN method for estimating the transferability of a set of models to a downstream task. OSBORN integrates differences in image domains, task differences, and coherence between models to provide reliable transferability estimates. The authors evaluated OSBORN on 28 source datasets, 11 target datasets, 5 model architectures, and 2 pre-training methods. They compare the method with the current state-of-the-art metrics MS-LEEP and E-LEEP and consistently outperform them with the proposed method.

![image](https://github.com/user-attachments/assets/1bdc1307-0376-4a2b-96d8-827ac9e2db2d)

## Experiments
This paper focuses on how to select source models in transfer learning, and compares and validates them experimentally. Specifically, the authors adopt the method OSBORN to estimate the transferability of source models and compare it with two existing baseline methods (MS-LEEP and E-LEEP). The experiments are divided into two parts, a dataset for the classification task and a dataset for the semantic segmentation task.

For the dataset for the classification task, the authors chose 11 widely used datasets as the target dataset, including CIFAR-10, CIFAR-100, Caltech-101, etc., and selected two source model architectures, ResNet-101 and DenseNet-201, from the PyTorch library for training. Also, the authors used two different pre-training strategies (BYOL and MoCoV2) to initialise ResNet-50 and add it to the source model pool. 

Finally, the authors used three evaluation metrics (Pearson Correlation Coefficient, Kendall τ and Weighted Kendall τ) to assess the performance of the selected models and compared the results with the baseline approach. The experimental results show that the OSBORN method outperforms the baseline method on all three metrics, especially on the WKT metric, which is the most significant.
![image](https://github.com/user-attachments/assets/8ecb02e7-f510-4b13-9ee1-c145d2017924)

For the dataset of the semantic segmentation task, the authors also chose 11 commonly used datasets as the target dataset and selected two source model architectures, ResNet-101 and DenseNet-201, from the PyTorch library for training. In addition, the authors used Frobenius paradigm regularisation to solve the OT problem and compared them. 

Finally, the authors used three evaluation metrics (Pearson Correlation Coefficient, Kendall τ and Weighted Kendall τ) to assess the performance of the selected models and compared the results with the baseline approach. The results show that the OSBROWN method outperforms the baseline method on all three metrics, especially on the WKT metric, which is the most significant.  
![image](https://github.com/user-attachments/assets/a57acd2d-e448-480b-937e-9918b6f5508b)

## Conclusion

### 1. Advantages of the Thesis
The method considers several factors such as domain differences, task differences and the degree of model cooperation with each other, and uses a sub-model optimisation strategy to select the best set of source models. Experimental results show that OSBORN exhibits higher accuracy and reliability on a variety of downstream tasks and model pools compared to existing methods.
  
### 2. Innovative points
  1. OSBORN is a novel transfer learning method that provides a comprehensive approach for selecting the optimal combination of source models by combining three key factors (domain differences, task differences, and the degree to which models cooperate with each other).
  
  2. In addition, the authors propose a selection algorithm based on a sub-model optimisation strategy that can efficiently find the best set of source models. These innovations make OSBORN a powerful transfer learning tool for a variety of different tasks and model pools.
 
### 3. Future Works
The method only considers three factors, namely domain differences, task differences, and the degree of model cooperation with each other, while ignoring other factors that may affect migration performance. 

Therefore, in future studies, it can further explore how to incorporate more factors into OSBORN to improve its applicability and accuracy. In addition, it can also investigate how to combine OSBORN with other machine learning techniques to achieve higher-level migration learning tasks.
