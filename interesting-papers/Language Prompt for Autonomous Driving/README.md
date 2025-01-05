# Language Prompt for Autonomous Driving
[paper link](https://arxiv.org/pdf/2309.04379) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper describes a new approach that uses natural language cues to capture objects of interest in driving scenarios.         | 3D target detection         |

## Methodology

### 1. Abstract
The application of this approach to driving scenes is limited by the lack of paired cue-instance data. To address this problem, the authors propose an object-centred language-based cue set, called NuPrompt, and extend it to 3D, multi-view and multi-frame spaces. By constructing a dataset of a total of 35,367 linguistic descriptions, each referring to an average of 5.3 object trajectories, they also provide a simple end-to-end benchmark model called PromptTrack.

![image](https://github.com/user-attachments/assets/7bef1fe4-75a9-4fac-8deb-eb8ac6fb2c99)

### 2. Method Description 
The paper proposes a new multi-view 3D target detection task, NuPrompt, and constructs a large dataset based on the Nuscenes dataset. The dataset contains a variety of environments, weather conditions and time of day with rich semantic information. The paper proposes an end-to-end framework called PromptTrack to address this problem. The framework augments visual features using the product of visual and linguistic features and captures information from different perspectives over time and space. In addition, the framework introduces a past inference branch, a future inference branch, and a new cue inference branch to predict the trajectory of cue references. 

![image](https://github.com/user-attachments/assets/d11e4143-f756-4e8e-b2ab-c8e8552af55a)

### 3. Methodological improvements
The main improvement of the method is the introduction of the cue inference branch, which allows the model to better capture the relationship between visual and linguistic elements. The method also employs a cross-frame attention mechanism to improve the integration of historical information, which further improves the model performance.

### 4. Issues addressed 
The method solves the problem of semantic inconsistency in multi-view 3D target detection, enabling more accurate identification of targets mentioned in cues and efficient tracking in complex environments. At the same time, the method also extends the traditional multi-view 3D target detection task, making it more in line with the needs of real-world scenarios.

## Experiments
This paper focuses on the performance of the PromptTrack model on the NuScenes dataset and compares it with some heuristics-based trackers. Specifically, the authors used VoVNetV2 and RoBERTa to extract visual features and verbal cues, fused the two together through a multi-head attention mechanism, and used MLP for regression and classification tasks. The authors also performed Ablation Study on different parts of the model and visualised the results.

In their experiments, the authors first used the PromptTrack model trained on the NuScenes dataset and compared it with other trackers based on heuristics. The experimental results show that the PromptTrack model achieves better performance on metrics such as AMOTA and AMOTP, proving its effectiveness.

![image](https://github.com/user-attachments/assets/1e695c3a-5b8a-4a03-9bcd-9322642c5761)

Next, the authors conducted Ablation Study to test the effect of removing different branches separately. The results showed that removing any of the branches resulted in performance degradation, further confirming the effectiveness of each branch. In addition, the authors tested different cue threshold settings and found that the AMOTA score decreased slightly when the cue threshold was increased.

![image](https://github.com/user-attachments/assets/9363968e-0730-4a5a-bb50-9f33fca8ae9a)

Finally, the authors show some typical results of the PromptTrack model and compare it with all the predicted and linguistic cued objects. The results show that PromptTrack is able to accurately detect and track targets in a variety of challenging situations, including changes across different viewpoints and numbers of objects.

## Conclusion

### 1. Advantages of the Thesis
  1. NuPrompt, a new large set of linguistic cues, is proposed to provide fine-grained text pairwise annotation of 3D objects for perception tasks in autonomous driving scenarios.
  2. A new cue-based driving perception task is designed that uses given linguistic cues to predict and track multiple 3D objects in a driving environment and addresses challenges such as cross-frame temporal association and cross-modal semantic understanding.
  3. A simple end-to-end baseline model, PromptTrack, is proposed for cross-modal feature fusion and understanding by adding a cued inference branch to PF-Track, achieving impressive performance.

### 2. Innovative points
  1. NuPrompt is the first linguistic cue set dedicated to multiple 3D objects of interest in the video domain, with enhanced utility and generalisability.
  2. The design of the cueing inference branch allows PromptTrack to efficiently deal with cross-modal feature fusion and understanding, improving model accuracy and robustness. 

### 3. Future Works
  1. More complex spatio-temporal modelling and inference algorithms can be further explored to improve the generalisation ability of PromptTrack in different scenarios.
  2. Trajectory prediction and driving planning can be integrated into the same framework for a more comprehensive autonomous driving solution.
  3. The data scale and diversity of NuPrompt can continue to be expanded to meet the needs of more application scenarios. 
