# Stabilizing RLHF through Advantage Model and Selective Rehearsal
[paper link](https://arxiv.org/pdf/2309.10202) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | The aim of this paper is to address the stability issues faced when using reinforcement learning for human feedback (RLHF) training.           | Reinforcement Learning         |

## Methodology

### 1. Abstract
The authors propose two innovative approaches: dominance modelling and selective repertoire to increase training stability and reward scores. Experimental results show that these methods not only increase training stability, but also improve reward scores and win rates. This research has important implications for the field of artificial intelligence using large-scale language models for natural language processing.

### 2. Method Description 
The paper proposes two methods to improve reward modelling for pre-trained models: the Advantage Model (AM) and Selective Rehearsal.

The Advantage Model (AM) is a new approach to reward modelling that quantifies the additional benefit gained by the response y relative to the expected gain e for cue x. It is based on the use of a weighting term in a pre-trained model. It offsets the bias introduced due to shifts in the strategy distribution by introducing a significant weighting term, and uses two loss functions to ensure that the AM score is well calibrated.

Selective Rehearsal is a method used to maintain learned skills and prevent forgetting. It consists of two main steps: representative example discovery and repeated training. Representative example discovery divides the PPO training cues and policy outputs into c clusters by a clustering algorithm and selects representative (x, y) pairs. Repeat training then uses the (x, y) pairs from all clusters to form the reenactment dataset DR and computes the NLL loss on it as a complement to the standard PPO loss.

![image](https://github.com/user-attachments/assets/6e4572d0-edc8-458c-9d5d-299c4df9df9a)

### 3. Methodological improvements
  1. The Advantage Model (AM) method can more accurately determine the difference between a human's preferred response and alternative options by evaluating the differences between responses. In addition, it avoids the interpretation difficulties that may arise from the use of scalar values themselves.
  
  2. The Selective Rehearsal approach not only maintains learned skills but also prevents forgetting and captures multidimensionally important aspects such as diversity.

### 4. Issues addressed 
  1. The Advantage Model (AM) approach addresses the problem in reward modelling of how to distinguish between human preferred responses and alternative options and how to better account for the interpretive difficulties that may be posed by the scalar values themselves.

  2. The Selective Rehearsal approach addresses the problem of forgetting that can occur in pre-trained models and can improve the generalisation of the model.

## Experiments
This paper presents four experiments including datasets and models, training setup, evaluation, and analysis.

The first experiment is about the **comparison of datasets and models**. The authors used two datasets, English and Chinese, and utilised the HH-RLFH and SFT models to train the models. In the Chinese dataset, the authors used a dataset similar to LLAMA 2 and ranked the models by five scoring criteria. Also, the authors compared the performance of the two models, OpenAssistant and BLOOMZ, and found that AM (Advantage Model) has higher accuracy and lower ECE (Expected Calibration Error) than RM (Reward Model), which suggests that AM is able to provide reliable and accurate scores.

![image](https://github.com/user-attachments/assets/fcc738a0-f169-4a4a-9a62-8008be99bd54)

The second experiment was about the comparison of training settings. The authors used the same hyperparameters and learning rate to initialise the model and used different batch sizes and learning rates to train the model. The authors observed overfitting problems after one epoch and therefore fixed the training epoch to 1. In addition, the authors compared the performance of the different scoring models in PPO training and found that PPO training performed more consistently when using AM as the scoring model.

The third experiment is about the comparison of ratings. The authors used metrics such as accuracy and ECE to evaluate the performance of the models and found that AM had better performance relative to RM. In addition, the authors show the distribution of AM on different tasks and calculate the mean and variance for each task to verify the stability of AM.

![image](https://github.com/user-attachments/assets/2fb71027-867d-477b-92db-1e562346ce4f)

The fourth experiment was about the comparison of analyses. The authors used a random forgetting test to examine whether the model tends to forget previously learnt knowledge and compared performance in the case of using AM and RM as scoring models. The results show that using AM as a scoring model is effective in avoiding the forgetting problem and improving the effectiveness of the model.

![image](https://github.com/user-attachments/assets/2331dd2b-6200-4611-af02-e437f175dafb)

## Conclusion

### 1. Advantages of the Thesis
The authors experimentally validate the effectiveness and stability of these methods, which can significantly improve reward scores and win rates while avoiding reward hacking and the catastrophic forgetting problems.

### 2. Innovative points
  1. Firstly, Advantage Model is able to balance the distribution of reward scores across different categories, preventing significant discrepancies that can lead to reward hacking problems.
  
  2. Second, Selective Rehearsal is able to select the most suitable data for PPO training and retain the knowledge accumulated in the SFT phase, thus avoiding the forgetting problem.

### 3. Future Works
  1. Future research can further explore how these methods can be used in practical applications to optimise model performance, and how they can be combined with other technical tools to improve model effectiveness and stability.
  
  2. In addition, the application of these methods to other types of natural language processing tasks can be considered for a wider range of applications.    
