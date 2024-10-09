# GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection
[paper link](https://arxiv.org/pdf/2403.03507) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a training strategy called ‘Gradient Low-Rank Projection (GaLore)’, which aims to address the memory challenge in the training of large language models.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Traditional low-rank adaptation methods have limitations in parameter search and training dynamics, and may require full-rank warm-ups, and therefore do not perform as well as methods that use full-parameter learning. GaLore, on the other hand, allows for full-parameter learning while being more memory-efficient than common low-rank adaptation methods. 

Experimental results show that GaLore can reduce optimiser state memory usage by up to 65.5% in pre-training on the LLAMA 1B and 7B architectures and the C4 dataset and fine-tuning of RoBERTa on the GLUE task and, for the first time, demonstrates that it is possible to use GaLore on consumer consumer GPUs with only 24 GB of memory, without the use of model-parallelism, checkpointing, or offline strategies. GPU (e.g., NVIDIA RTX 4090) to pre-train a 7B model. Additionally, by using 8-bit GaLore, it is also possible to reduce optimiser memory usage by up to 82.5% and total training memory by 63.3% compared to the BF16 benchmark.

### 2. Method Description 
The algorithm presented in this paper is a memory optimisation method based on the Adam optimizer called GaLore (Gradient Low-Rank Optimization with Reduced Memory). The algorithm reduces memory cost by projecting the gradient matrix to a low-rank form and merges the weight updates during training to reduce the need to store the low-rank factorisation BA.GaLore can also be applied to other optimizers that have similar update rules and require a large amount of memory for storing gradient statistics, such as Adafactor.

![image](https://github.com/user-attachments/assets/fc66a2fb-715b-4cf0-aa47-068e03863907)
 
### 3. Methodological improvements
The main improvement of GaLore over previous methods is the use of a new gradient normalisation method that computes the low-rank normalised gradient Nt. In addition, GaLore employs more efficient parameterisation and quantisation techniques to further reduce the cost of the projection matrix, but these have not yet been fully implemented.

### 4. Issues addressed 
This research aims to address the problem of high memory requirements in deep learning, especially for optimisers that rely on component-level statistical information about the gradient, such as Adam.By using low-rank optimisation techniques and optimal memory management strategies, GaLore can significantly reduce memory consumption while maintaining optimised performance. This allows deep learning models to run efficiently on resource-constrained devices, such as mobile devices or embedded systems.

## Experiments
This paper focuses on the application of GaLore algorithm in pre-training and fine-tuning of large-scale language models. The authors compare GaLore through several experiments and draw some conclusions.

First, the authors compare GaLore with other low-rank algorithms, including methods such as Adam, 8-Bit Adam, and Adafactor. They conducted experiments on the C4 dataset using the LLaMA infrastructure. The results show that GaLore achieves comparable performance to full-rank training for a variety of model sizes and reduces the memory required to store parameters and optimiser state.

![image](https://github.com/user-attachments/assets/d3c54496-d008-4115-9db8-896bb9be0166)

Secondly, the authors show that GaLore can be applied to different learning algorithms, in particular memory-efficient optimisers such as 8-bit Adam and Adafactor.They conduct experiments on the LLaMA 1B architecture and find that GaLore is able to further reduce the memory footprint. In addition, the authors show how GaLore performs on large-scale models. They performed experiments on the LLaMA 7B architecture and found that GaLore was able to achieve the same level of perplexity as 8-bit Adam in the same number of steps.

![image](https://github.com/user-attachments/assets/3c16fa27-04ff-4126-b428-8868d687e809)

Finally, the authors conducted fine-tuning experiments, applying GaLore to the task of fine-tuning the RoBERTa model and comparing it to other low-rank algorithms. The results show that GaLore achieves better performance on most tasks and saves more memory space. 

![image](https://github.com/user-attachments/assets/c11d4bf9-7f46-4db8-b9f2-d137d7875fdf)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a memory-efficient pre-training and fine-tuning strategy called GaLore, which reduces memory usage by exploiting the slow-varying low-rank structure of the weight matrix.

  2. The paper details theoretical proofs as well as experimental results demonstrating the superior performance of GaLore in pre-training and fine-tuning of large language models (LLMs).

  3. GaLore is a general method that can be easily integrated with existing optimisers and has a wide range of applications for various types of models.
 
### 2. Innovative points
  1. The core idea of GaLore is to reduce memory usage by exploiting the slow-varying low-rank structure of the weight matrix, rather than directly approximating the weight matrix itself as a low-rank matrix, as in traditional low-rank reparameterisation methods.

  2. GaLore is able to achieve more efficient memory usage while maintaining full parametric learning, which makes it possible to train large models with reduced environmental impact.

  3. GaLore also offers important improvements such as optimiser state updates based on memory efficiency and resilient distributed training for different hardware platforms.

### 3. Future Works
  1. GaLore is a very promising research direction that can be applied in many fields, such as natural language processing and computer vision.

  2. Future research can further explore how to improve the computational efficiency and generalisation ability of GaLore to better meet practical needs.

  3. In addition, researchers can also consider combining GaLore with other techniques, such as adaptive learning rate adjustment, dynamic weight pruning, etc., to obtain better results.   
