# GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
[paper link](https://arxiv.org/pdf/2006.16668) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper introduces a new module called GShard, which consists of a set of lightweight annotated APIs and XLA compiler extensions that can provide an elegant way to express various parallel computation patterns and enable efficient implementations without changing the existing model code.           | Deep Learning           |

## Methodology

### 1. Abstract
  The authors successfully scaled the multilingual neural machine translation Transformer model to over 600 billion parameters using GShard and achieved efficient training on 2048 TPU v3 gas pedals through automatic partitioning. The results show that this giant model can be efficiently trained in 4 days with higher quality than previous techniques in translating from 100 languages to English.

![image](https://github.com/user-attachments/assets/90acf2ed-a05a-4f87-9e36-1789075e93f6)

### 2. Method Description 
  The paper proposes a method for efficiently training large-scale models, focusing on how to achieve effective parallel computing when using a large number of devices. They address this problem by designing a Transformer architecture based on a Position-wise Mixture-of-Experts mechanism, and use the GShard module to achieve efficient distributed training

  ![image](https://github.com/user-attachments/assets/b8760084-38f1-47b6-acbe-33fa6dff32be)

### 3. Methodological improvements
  1. **Use of a hierarchical hybrid attention mechanism**: the inputs at each location are assigned to be processed by multiple expert networks to reduce the computational cost.
  
  2. **Use of the GShard module**: this module automatically divides the model into multiple parts and assigns different devices to each part, thus enabling the realization of efficient distributed training.

### 4. Issues addressed 
  1. A low computational cost model structure is realized, allowing large-scale models to be trained in a reasonable amount of time.
  
  2. Efficient distributed training is realized, enabling large-scale models to be trained on multiple devices simultaneously, greatly reducing training time.

## Experiments
  This paper mainly introduces the Moe Transformer model implemented using GShard in large-scale multilingual machine translation tasks, and analyzes and compares experiments on its performance and memory consumption. Specifically, this paper first introduces the basic structure and training process of the Moe Transformer model, and then explores the impact of key factors in model design on model performance through a series of comparative experiments.

**The relationship between model depth and capacity bottleneck**: the model quality is improved by increasing the model depth, and it is found that as the model depth increases, the model needs more parameters to achieve the best results. In addition, when the number of model parameters exceeds a certain threshold, a capacity bottleneck occurs, leading to a decrease in model quality.

**Benefits from more experts**: the quality of the model is improved by increasing the number of experts in the model, especially on tasks dealing with low-resource languages. However, as the number of experts increases, the training time and sample efficiency of the model suffer.

**Advantages of deep-dense models**: by comparing the models with different depths and densities, it is found that the deep-dense models perform better on the task of processing low-resource languages and can better utilize the capability of the shared sub-network to improve the overall performance.

**Analysis of training efficiency and time**: by comparing the training loss and training time of different models, it is found that deeper models require less training data to achieve the same training effect and can be trained in less time.

![image](https://github.com/user-attachments/assets/e2454de4-0b27-431e-9d38-30efb0e64aad)

## Conclusion

### 1. Advantages of the Thesis
 1. This paper presents a deep learning module called GShard that automatically partitions computational tasks in large-scale computations.
 
 2. GShard is easy to use by simply adding lightweight partitioning annotations to the user model code and provides an easy-to-use flexible API to scale large neural networks.
 
 3. The authors apply GShard to a sparse gated hybrid expert layer (MoE Transformer) in the Transformer architecture and show that training a multilingual neural machine translation model with 600B parameters can be done efficiently in 4 days with better quality than a single model translating 100 languages.
 
 4. GShard can significantly improve model quality while reducing training costs compared to traditional data-parallelism-based approaches.
 
 5. With the experimental results, the authors demonstrate the feasibility of using conditional computation to achieve model scale-up, and that this design decision can reduce the model training time to just a few days.
    
### 2. Innovative points
  1. A new DL module, GShard, is proposed to automatically partition computational tasks in large-scale computations.
  
  2. GShard employs the SPMD partitioning technique, which allows any tensor dimension to be partitioned, thus improving compilation efficiency.
  
  3. The authors also propose various compiler improvements based on SPMD partitioning to further improve the performance and scalability of the model.
  
  4. By combining conditional computation with an easy-to-use interface, the authors demonstrate that algorithmic improvements can efficiently utilize a large amount of computational power.

### 3. Future Works
  1. With the development of computer hardware, the application of large-scale neural networks will become more and more widespread.
  
  2. The authors believe that as the field of DL continues to evolve, more efficient and scalable tools and techniques are needed to support larger-scale NNs.
  
  3. Future research directions include how to better handle large-scale datasets, how to optimize the model training process, and how to build more efficient distributed computing systems.
