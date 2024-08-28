# Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos
[paper link](https://arxiv.org/pdf/2206.11795) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a new approach called Video PreTraining (VPT), which allows robots to learn behavioural prior knowledge by watching unlabelled online videos through semi-supervised imitation learning.          |  Semi-supervised  Learning       |

## Methodology

### 1. Abstract
This approach extends techniques for pre-training on large-scale Internet datasets, allowing robots to learn broad and general abilities without labelling. The authors used videos from the Minecraft game as source data and trained an inverse dynamics model with a small amount of labelled data, thus annotating a large amount of unlabelled data, and then trained a generalised behavioural prior model using this labelled data. Experimental results show that this behavioural a priori model has non-trivial zero-sample capabilities and can be further fine-tuned for difficult tasks through imitation learning and reinforcement learning.

### 2. Method Description 
This paper proposes a method called Video Policy Transfer (VPT) for transferring behavioural policies from a video game to a new environment. The method consists of three main steps: training an inverse dynamics model, data filtering, and base model training.

First, **the inverse dynamics model (IDM)** is trained by collecting a small amount of labelled data to minimise the negative log-likelihood of the action prediction probability given a sequence of observations. Unlike imitation learning strategies, the IDM can be non-causal, i.e., its action predictions can be a function of past and future events. Experiments show that IDM is easier to learn and more efficient than an imitation learning objective based only on past frames.

Second, a large number of gameplay videos are obtained by searching the web for relevant keywords and **filtering** them to retain only clean data, i.e., gameplay clips that do not contain visual noise and are from survival mode. For the unclean data, a filter is trained using a small sample of images labelled as clean or unclean to filter out unclean video segments.

Finally, **using standard imitation learning methods**, a base model is trained on the clean data that exhibits non-trivial behaviour in a non-zero sample setting and can be fine-tuned by imitation learning and reinforcement learning to perform more complex skills.

![image](https://github.com/user-attachments/assets/0396cd67-fc5a-4e99-a1d4-d599eb45ba03)

### 3. Methodological improvements
  1. The use of an inverse dynamics model for training can better capture the dynamics of the environment, thus improving the generalisation ability of the model.
  
  2. The data filtering process can effectively remove unnecessary visual noise and game mode differences, making the training data cleaner and more accurate.
  
  3. The base model is trained using standard imitation learning methods with both non-zero sample capability and scalability for complex skills.

### 4. Issues addressed 
The method proposed in this paper addresses the problem of behavioural policy transfer in video games, enabling adaptive behavioural control in different game environments. In addition, the method improves the generalisation ability and data efficiency of the model, making it suitable for larger datasets and more complex tasks.

## Experiments
This paper focuses on the authors' use of artificial intelligence techniques to simulate human behaviour in Minrcraft, and validates the effectiveness of the approach through comparative experiments. Specifically, the authors conducted the following three comparison experiments:

The first experiment verifies that an IDM model trained using contract labour data performs better at collecting and crafting game items than a BC base model trained directly from the same dataset. The authors used a method called ‘VPT’, where the IDM model was used to predict the behaviour of contract workers, and then these behaviours were used to train the BC base model. The results showed that the BC base model trained with the IDM model was better at collecting and producing game items, demonstrating the effectiveness of the IDM approach.

![image](https://github.com/user-attachments/assets/bddac5d8-8706-4af6-9068-f87bcfa49784)

The second experiment builds on the IDM and BC base models and further investigates how the BC algorithm can be used to fine-tune the base model to improve its performance. The authors used two different datasets (‘earlygame_keyword’ and ‘contractor_house’) to fine-tune the base model and compared the effects of different fine-tuning strategies. The results show that the performance of the fine-tuned model is significantly improved, especially in the production of higher-level game items.

![image](https://github.com/user-attachments/assets/d77b0b52-7091-4304-81d4-19f548df829f)

The third experiment verified the effect of IDM quality on BC performance. The authors trained the IDM using varying amounts of data and used it to label a smaller dataset. They then used the BC models trained with each IDM to evaluate game statistics. The results show that it takes at least 10 hours of data to get the IDM to a certain quality level, and that the quality of the IDM has a significant impact on the performance of the BC model.

 ![image](https://github.com/user-attachments/assets/f16083f5-0611-4b8c-a036-ae66cdc5d28e)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new semi-supervised imitation learning method, Video PreTraining (VPT), which trains a behavioural prior model by exploiting the large amount of unlabelled video data available on the Internet and applies it to reinforcement learning to solve hard-to-explore problems.
  
  2. The authors' experimental results in the Minecraft game show that this approach can effectively improve the learning ability of an intelligent body, enabling it to perform some tasks that were previously impossible.
  
  3. In addition, the paper also proposes some improved methods, such as predicting action labels using inverse dynamics models and generating pseudo-labels using a small amount of labelled data, all of which provide researchers with more ideas and tools.

### 2. Innovative points
  1. The main contribution of the paper is to propose a new semi-supervised imitation learning method which can train a behavioural prior model on large-scale unlabelled video data and apply it to reinforcement learning.
  
  2. In addition, the paper proposes some improved methods, such as predicting action labels using an inverse dynamics model and generating pseudo-labels using a small amount of labelled data, which can help to improve the learning effect.

### 3. Future Works
Future research can further explore how to combine VPT with other techniques to improve learning efficiency and generalisation performance. At the same time, consideration could be given to how to cope with the possible negative effects of VPT methods, such as imitation of undesirable behaviours.  


