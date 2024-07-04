# Counting Out Time: Class Agnostic Video Repetition Counting in the Wild
[paper link](https://arxiv.org/pdf/2006.15418.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new method to estimate the time intervals between repeated occurrences of actions in a video.         | Transformer           |

## Methodology

### 1. Abstract
  The method uses self-similarity as an intermediate representation bottleneck, thus allowing the model to generalize to unseen repetitions. The authors achieved category-free cycle prediction and repetition counting tasks by training the model on a synthetic dataset and combining it with a robust but constrained model. 

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/aa44b732-0aa4-4e0d-96b0-bfc435203b42)

### 2. Method Description 
  The paper proposes a video repetition counting model called RepNet. The model consists of three main components: an image encoder, a temporal self-similarity matrix (TSM), and a cycle prediction module. First, the input video V is converted by the image encoder φ into embedding vectors for each frame X. Then, these embedding vectors are used to compute the similarity between each pair of embedding vectors and construct the temporal self-similarity matrix S. Finally, the cycle prediction module accepts the temporal self-similarity matrix as an input and outputs an estimate of the cycle length l and the cycle classification p for each frame.
  
### 3. Key concepts
  _Temporal Self-similarity Matrix (TSM)_: A tool used in various fields, such as computer vision, music information retrieval, and video analysis, to analyze the temporal structure of sequences. It captures the similarity between different time points within a sequence, providing a way to visualize and understand patterns and repetitions over time.
  
### 4. Methodological improvements
  The main improvement of the method is the introduction of the TSM, which provides information bottlenecks and produces normalization effects in the intermediate layers. In addition, the cycle prediction module shares a processing pipeline consisting of 32 2D convolutional filters, a Transformer layer and two fully connected layers.
  
### 5. Issues addressed 
  The method addresses the video repetition counting problem, i.e., given a video, how to accurately estimate the number of repetitive actions in it. The method achieves this goal by learning periodic and spatio-temporal features in the video, and experiments are conducted on several datasets to verify its effectiveness. In addition, the method proposes a training strategy based on synthetic repetitive videos to improve the generalization ability of the model.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/1450dddd-b35f-4376-940f-e496a3dbe5a8)

## Experiments
  This paper presents a multi-group experiment on RepNet, a model for repeat counting and cycle detection, and evaluates its performance. In their experiments, the authors used two benchmark datasets and two commonly used evaluation metrics to compare the performance of different methods.

First, the authors compared existing cycle detection methods with their RepNet. The benchmark dataset they used is the PERTUBE dataset, which assigns a binary label to each video frame to indicate whether the frame is part of a repetitive action. The authors used metrics such as precision, recall, F1 score, and overlap to evaluate the performance of the models. 

Second, the authors compare different training data sources and alternative cycle prediction architectures. The results show that using synthetic data improves the generalization ability of the model. In addition, the authors compare the effects of using alternative architectures such as LSTM, spatio-temporal CNN and 2D CNN. The results show that the Transformer architecture performs better than the other architectures.

Finally, the authors further evaluated the performance of RepNet. They compare the performance of RepNet with other existing methods and find that RepNet outperforms existing methods in all metrics. In addition, the authors also conducted a more in-depth study of RepNet by means of projection analysis and error analysis.

In conclusion, this paper demonstrates the superior performance of RepNet in repeat counting and cycle detection by comparing and analyzing several experiments, and it can be applied to a variety of practical scenarios.

## Conclusion
### 1. Advantages of the Thesis
  1. The paper presents a method for repetitive action recognition in video that successfully detects periodicity and predicts counts, and is tested on a number of different types of actors and sensors.
  
  2. By using a self-similarity based neural network architecture, the method can handle simple repetitions with good generalization capabilities.
  
  3. The paper also provides a new video repeat counting dataset, Countix, which is approximately 90 times larger than the largest previous dataset.
     
### 2. Innovative points
  1. The method combines real and synthetic training data to increase the robustness and generalization of the model.
  
  2. The use of a self-similarity matrix as an intermediate representation enables the model to classify repeated videos of multiple categories, thus achieving the goal of a single model for many periodic video categories.
  
  3. A data enhancement strategy is proposed to solve the problem of easy overfitting of synthetic videos, thus improving the performance of the model.
     
### 3. Future Works
  1. The method can be further extended to more complex repetitive signals and timings, such as dance steps and repetitive parts in music.
  
  2. The method can be applied to other computer vision tasks such as biological event measurement and kinematic analysis.
  
  3. Ways to combine the method with other techniques could be explored to improve its accuracy and efficiency.
