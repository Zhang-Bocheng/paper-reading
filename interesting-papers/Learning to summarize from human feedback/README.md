# Learning to summarize from human feedback
[paper link](https://arxiv.org/pdf/2009.01325) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 |This paper explores how human feedback can be used to improve the quality of text summaries. The authors use a large, high-quality human comparison dataset and train a model to predict which summaries humans prefer.           | Supervised Learning          |

## Methodology

### 1. Abstract
  The authors used the model as a reward function in reinforcement learning to fine-tune a summarization strategy. Experimental results show that this approach is much better than using only supervised learning and metrics such as ROUGE, and even produces summaries that are similar to human reference summaries. In addition, they perform extensive analysis to demonstrate that their reward model can be generalized to new datasets and that optimizing their reward model yields better summary quality. In summary, this paper provides an effective solution that can help ML researchers better understand the impact of their training loss on the actual desired behavior.

![image](https://github.com/user-attachments/assets/283ba8cc-42d5-4abd-b5bf-f1f014a0f959)

### 2. Method Description 
The study used the Reddit TL;DR dataset and employed a different strategy to train the model than the CNN/DM dataset. The goal was to generate high-quality summaries of up to 48 words in length. They first trained an initial policy by means of supervised learning, and then optimized this policy in three iterative steps: **collecting samples** and sending them to human evaluators for feedback; **training a reward model** based on the feedback to predict which summaries are better; and, finally, using **reinforcement learning** to optimize the policy to maximize the reward.

![image](https://github.com/user-attachments/assets/9143ec04-7506-44d9-aad9-759bbb7d1ca7)

### 3. Methodological improvements
1. Completely offline, alternating between sending large amounts of comparison data to evaluators and retraining the model;

2. Maintaining a close relationship with evaluators, providing detailed instructions, answering questions, and providing regular performance feedback.
 
These improvements allowed the researchers to achieve higher evaluator-researcher agreement and improved data quality.

### 4. Issues addressed 
The main problem is how to generate high quality text summaries. The researchers used the Reddit TL;DR dataset and went through several steps to optimize the policy to generate better summaries. Also, they proposed two improvements to improve data quality and ensure consistency in model performance.

## Experiments
  This paper presents research and experimental results on human feedback-based models for text summarization generation. The authors designed a series of experiments to compare the performance of different models on a text summarization task and analyzed the role of reward functions and automatic evaluation metrics.

First, the authors used human feedback to train two models of different sizes (1.3B and 6.7B) and compared them with a supervised learning-based model. The experimental results show that the human feedback-based model significantly outperforms the supervised learning-based model in terms of quality, especially in terms of coverage. Even after controlling for the effect of summary length, the human feedback-based model still showed better quality.

Second, the authors applied the human feedback-based model to the task of generating summaries of CNN/Daily Mail news articles and compared it with a model based on a pre-trained model. The experimental results show that the human feedback-based model can generate high-quality news article summaries without further training and significantly outperforms the pre-trained model-based model in terms of quality.

In addition, the authors conducted a study on reward functions to explore the effect of the degree of optimization on the performance of reward functions. The experimental results show that optimizing the reward function to a certain extent can improve the quality of the model, but over-optimization can cause the reward function to contradict the true preferences, which ultimately leads to the model generating poorer summaries.

Finally, the authors also investigated automatic evaluation metrics, comparing the predictive power between ROUGE, summary length, replication ratio, and probability under a baseline supervised model with the reward function. The experimental results show that the reward function significantly outperforms the other metrics in its ability to predict human preferences, while ROUGE does not track changes in sample quality well.

![image](https://github.com/user-attachments/assets/9f033a02-e844-472a-ad18-712d5dcc12e8)

## Conclusion

### 1. Advantages of the Thesis
  1. The study presents a reinforcement learning-based approach to training models to optimize human feedback.
  
  2. The researchers used the TL;DR dataset on Reddit to demonstrate their approach and showed that this method can significantly improve the performance of models compared to traditional supervised learning.
  
  3. The study also explores how this technique can be applied to other tasks and suggests future research directions.
     
### 2. Innovative points
  1. The study proposes a new method to train machine learning models using human feedback instead of traditional supervised learning methods.
  
  2. The researchers used RL to train the model so that it could adapt its behavior based on human feedback.
  
  3. The study also explores how this approach can be applied in different tasks and suggests some directions for improvement.

### 3. Future Works
  1. The study provides insights for some future research, such as how to use human feedback for more complex tasks and how to avoid malicious attackers using this approach to create harmful content.
  
  2. The study could also contribute to the discussion on the safety and fairness of machine learning algorithms, especially in the context of automation replacing human work.
  
  3. Future research should further explore how human feedback can be combined with other techniques and approaches to better realize the goals of machine learning.

