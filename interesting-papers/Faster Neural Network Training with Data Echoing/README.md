# Faster Neural Network Training with Data Echoing
[paper link](https://arxiv.org/pdf/1907.05550.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper describes a method called "data echo" that aims to reduce the amount of computation in the early stages of neural network training and increase training speed.          | Neural Network          |

## Methodology

### 1. Abstract
   With the development of GPUs and other specialized hardware gas pedals, the amount of computation in these early stages will gradually become a bottleneck. Data Echo reclaims free capacity by reusing intermediate outputs from previous pipeline stages, thereby reducing the amount of upstream computation and increasing training speed when computation time prior to the gas pedal dominates. The authors tested different data echo algorithms and found that at least one data echo algorithm matched benchmark prediction performance while using less upstream computation in a variety of settings. 

### 2. Method Description 
  The "data echoing" proposed in this paper is a technique used to accelerate deep learning training. It is realized by inserting a stage in the training pipeline that repeats the output of the previous stage. Specifically, it can be implemented in TensorFlow's tf.data library with the following code:
``` Python
 dataset.flat_map(
    lambda t.
    tf.data.Dataset.from_tensors(t).repeat(e)
 )
```

where $e$ is the data echo factor, i.e., the number of times each data item is repeated. If the upstream and downstream phases are executed in parallel, the data echo time can be approximated as:

$$
max \{ t_{upstream}, e \times t_{downstream} \} 
$$

where $t_{upstream}$ is the processing time of all upstream stages, $t_{downstream}$ is the processing time of all downstream stages, and $e$ is the echo factor. If the ratio of upstream and downstream processing times $R=t_{upstream}/t_{downstream}$ is greater than or equal to the echo factor $e$, the increased number of downstream stages are free because they utilize free downstream capacity.

### 3. Key Concepts
_Data Echoing_: A technique used in distributed systems and data processing pipelines to replicate or duplicate data across multiple nodes or components for fault tolerance, load balancing, or performance optimization purposes.

### 4. Methodological improvements
 While traditional SGD updates can only use the input data once, data echoing can use multiple downstream SGD updates in a single upstream step. This can significantly reduce the number of required upstream steps and hence the training time. However, since duplicate data may not be as valuable as brand new data, more downstream SGD updates are required to achieve the desired prediction performance, and thus the speed-up factor may be smaller than the echo factor.

In addition, the location of data echoes can affect their behavior. For example, echoing before or after the batch level, or before or after data augmentation, can affect the diversity of duplicates and whether or not examples within a batch are replicated. Adding a random buffer can also increase the likelihood of different data being used for nearby SGD updates.

### 5. Issues addressed 
  The main purpose of Data Echoing is to reduce training time, by reducing the number of upstream steps required to reach the target predictive performance. It can be applied to various types of models and tasks and does not require additional hardware support. However, the effectiveness of data echo depends on many factors such as dataset size, model complexity, and learning rate. Therefore, the echo factor and other parameters need to be adjusted on a case-by-case basis to get the best results.
  
## Experiments
  This paper describes several data reuse (data echoing) experiments conducted by the authors and compares the performance of data reuse in different situations. Specifically, the authors conducted the following experiments:

**Effect of data reuse on training time**: the authors observe the effect of data reuse on training time by adding it to the training process. The results show that data reuse can significantly reduce the training time when the input data transfer speed becomes a bottleneck.

**Impact of data reuse on model performance**: the authors compare the model performance before and after data reuse by conducting data reuse experiments on different tasks and models. The results show that reasonable setting of data reuse parameters can reduce the number of fresh samples required for training without degrading the model performance.

**Relationship between data reuse and batch size**: the authors investigated the impact of batch size on the effect of data reuse. The results show that the effect of data reuse improves as the batch size increases.

**Relationship between data reuse and number of repetitions**: the authors investigated the effect of the number of data reuses on model performance. The results show that the number of data reuse should be within a certain range, and too large a number of repetitions can lead to the number of fresh samples exceeding the baseline, thus affecting the model performance.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/8efdfc80-30c6-4df6-b053-fa3389838379)

## Conclusion

### 1. Advantages of the Thesis
 1. The paper proposes data echoing, a simple but effective data reuse technique, to reduce the waste of hardware resources and increase the speed of neural network training.
 
 2. The technique is applicable to a wide range of deep learning tasks and can achieve speedup results in a variety of hardware configurations.
 
 3. In addition, the authors detail how data echoing works and how it can be applied to different deep learning workflows. These benefits make the paper highly informative for deep learning practitioners.

### 2. Innovative points
  The data echoing technique proposed in this paper is a novel approach to reuse already processed data for model training, thus reducing the total time required for upstream computation. The strengths of the technique are its simplicity and ease of implementation, as well as its ability to achieve acceleration effects across different deep learning tasks and hardware configurations.
  
### 3. Future Works
  Data echoing techniques will play an increasingly important role in future deep learning efforts. Future research can further explore how to better utilize data echoing techniques to optimize the deep learning training process and develop more efficient data reuse algorithms. In addition, it could also be investigated how to combine data echoing techniques with other deep learning techniques to achieve a more efficient training process.


