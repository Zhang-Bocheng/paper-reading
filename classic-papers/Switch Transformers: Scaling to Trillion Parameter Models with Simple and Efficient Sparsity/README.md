# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
[paper link](https://arxiv.org/pdf/2101.03961) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a new model called Switch Transformer, which uses sparse activation to allow each input to be processed by selecting different parameters, resulting in greater efficiency and speed.         | Transformer          |

## Methodology

### 1. Abstract
By simplifying the Mixture of Experts (MoE) routing algorithm, designing a more intuitive and improved model, and training techniques, the authors succeeded in solving the problems of MoE complexity, communication cost, and training instability, and achieved better results by using a lower-precision format in the pre-training process. The experimental results show that this new model can improve the pre-training speed with the same computational resources, and it can also be scaled to multilingual environments and train larger scale language models at an unprecedented level.

### 2. Method Description 
The paper proposes a new transformer architecture called ‘Switch Transformer’, which aims to achieve efficient model scaling by maximising the number of parameters. Compared to the traditional MoE (Mixed Attention) model, Switch Transformer has less computational overhead and achieves better performance in the same amount of time. The model employs a sparse routing strategy that uses a single expert to process each input token instead of multiple experts as in MoE. This strategy reduces communication costs and hardware requirements and improves the quality and speed of the model.

![image](https://github.com/user-attachments/assets/9ae32aa1-4e4e-40af-bf8e-7c219629af6c)

![image](https://github.com/user-attachments/assets/6296a326-5662-4964-8be2-66388c19b96b)

### 3. Methodological improvements
To further improve the stability and training efficiency of the model, the paper proposes several improvements. First, they use a floating-point precision control technique that divides floating-point operations into two parts, low and high precision, to reduce computation and improve stability. Second, they suggest reducing the standard deviation of the weight matrix during initialisation to avoid model instability. Finally, when performing fine-tuning, they used a higher dropout rate to prevent overfitting.

### 4. Issues addressed 
The Switch Transformer model proposed in this paper solves the problems of long training time and high consumption of computational resources of traditional Transformer models on large-scale datasets. It not only makes better use of hardware resources, but also completes the training task faster with the same computational resources. In addition, the model can effectively cope with the overfitting problem in downstream tasks, thus improving the generalisation ability of the model.

## Experiments
This article focuses on the performance of the Switch Transformer model on pre-training and downstream tasks, and compares it with other models. Specifically, the article explores the following aspects through experiments:

**Comparison of pre-training effects:** the Switch Transformer model is compared with the T5 baseline model, and the results show that the Switch Transformer model performs better with the same number of parameters.

**Impact of the number of parameters on model performance:** The number of parameters of the model was increased by increasing the number of experts, and it was found that the performance of the model was improved with the increase in the number of parameters.

![image](https://github.com/user-attachments/assets/2be2d600-673e-4825-9eb5-6da9bf9673be)

**Model compression:** By compressing the Switch Transformer model into a smaller model while keeping its performance unchanged, the storage space and computational cost of the model can be reduced.

![image](https://github.com/user-attachments/assets/b0d6b1da-4a96-4d4e-b30b-f8e3a3a4ab85)

**Multi-language learning ability:** The Switch Transformer model is applied to a multi-language learning task, and the results show that the model has good multi-language learning ability.

In conclusion, this paper demonstrates the excellent performance of the Switch Transformer model in different tasks through several experiments, proving the effectiveness and practicality of the model.
 
## Conclusion

### 1. Advantages of the Thesis
  1. Switch Transformer is a natural language processing model based on a sparse model, which reduces the model complexity by sharing the parameters together and shows good performance in large-scale pre-training and fine-tuning tasks.
  2. The sparse model proposed in this paper has better efficiency and accuracy, can achieve better results with the same computational resources, and can be applied to model compression in small-scale scenarios.
  3. The authors propose some effective techniques to improve the stability and training efficiency of the sparse model, including the use of regularisation techniques and methods such as adaptive gradient trimming.

### 2. Innovative points
  1. Switch Transformer adopts the idea of hybrid expert model, which achieves the effect of parameter sharing by combining different sub-models into an overall model.
  2. The paper proposes training techniques for sparse models, including methods such as using sparse matrices and dynamically adjusting the degree of sparsity, which improves the stability and training efficiency of the model.
  3. The authors also proposed a new sparse model structure that uses a multilayer sparse network instead of the traditional single-layer sparse network, further improving the performance of the model. 

### 3. Future Works
  1. Sparse models have a wide range of applications in future research, and their deeper nature and advantages can be explored through more experiments and research.
  2. Attempts can be made to apply sparse models to other fields, such as computer vision and speech recognition, to achieve more efficient and accurate model design.
  3. The training process and techniques of sparse models are further optimised to improve the stability and generalisation ability of the models so that they can better cope with complex practical application scenarios.
