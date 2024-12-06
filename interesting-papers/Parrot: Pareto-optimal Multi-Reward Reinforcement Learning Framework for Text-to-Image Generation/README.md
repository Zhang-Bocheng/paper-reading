# Parrot: Pareto-optimal Multi-Reward Reinforcement Learning Framework for Text-to-Image Generation
[paper link](https://arxiv.org/pdf/2401.05675) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a text-to-image generation framework called Parrot that achieves approximation of Pareto optimal solutions through multi-objective optimisation and an efficient multi-reward optimisation strategy.          |  Reinforcement Learning        |

## Methodology

### 1. Abstract
The method uses batch Pareto optimal selection to automatically identify the best trade-off between different rewards and introduces a new cue-centred bootstrap into the inference time to ensure fidelity to user input after cue expansion. Experimental results show that Parrot has significant advantages over multiple baselines in terms of aesthetics, human preference, text-image alignment, and sentiment.

### 2. Method Description 
The Parrot method proposed in this paper is an image generation model based on Multi-Reward Reinforcement Learning (Multi-Reward RL), whose goal is to improve the quality of image generation by expanding the cues and to achieve Pareto optimisation across multiple reward metrics. The method consists of two main components: **the Prompt Expansion Network (PEN) and the Text-to-Image Diffusion Model (pθ).** 

pEN is initialised from the demo cue expansion pair using supervised fine-tuning, and pθ is initialised using a pre-trained diffusion model. During multi-reward RL fine-tuning, for each sample, multiple quality rewards are computed, including text-image alignment, aesthetics, human preference, and image emotion. A non-dominated sorting algorithm is then used to determine the set of Pareto optimal solutions in the batch and these best samples are used to jointly optimise the PEN and T2I model parameters. For inference, Parrot utilises the original cues and their extensions to incorporate more detail for higher quality while maintaining consistency with the original cues.

![image](https://github.com/user-attachments/assets/f90ac5ed-afb5-4490-b541-4e2808a1c797)

![image](https://github.com/user-attachments/assets/548d7d17-6a72-48e2-a93f-bf97d75b1e45)

### 3. Methodological improvements
While traditional image generation models typically only consider a single reward metric, the Parrot method is able to optimise multiple reward metrics simultaneously, resulting in more comprehensive and high-quality image generation. In addition, Parrot introduces reward-specific preference identifiers, enabling the model to automatically determine the importance of each reward metric and adjust its weight as needed. This approach allows the model to find a balance between different reward metrics for better performance.

### 4. Issues addressed 
Traditional image generation models tend to only optimise a single reward metric and are unable to consider the relationships between multiple metrics at the same time. This results in models that may sacrifice quality in some areas for improvement in others, or produce undesirable results.The Parrot approach, by introducing multi-reward RL and Pareto optimisation techniques, can better balance the relationships between different reward metrics to produce more varied and high-quality images.

## Experiments
This paper focuses on the application of the Parrot model to image generation tasks, and several comparative experiments are conducted to verify its effectiveness.

Firstly, the authors used methods such as Promptist and DPOK as a control group, and proved that the Parrot model performs better compared to other methods by comparing the visual results and quantitative evaluations of the different methods. Among other things, the authors used four qualitative signals (aesthetics, human preference, text-image alignment, and emotion) as reward functions and trained the model using a multi-objective reinforcement learning approach. The experimental results show that the Parrot model is able to better meet the user's needs and generate images that are more aligned with the input cues, as well as improve the aesthetics score and the human preference score.

![image](https://github.com/user-attachments/assets/97ba41a1-43e0-4ccb-a82e-8adb4bd87970)

![image](https://github.com/user-attachments/assets/53298cc3-ddbf-44e8-bed4-c9d3b52d9ef7)

Second, the authors conducted two sub-experiments to further validate the effectiveness of the Parrot model. The first sub-experiment addresses the effect of the reward function, where the authors attempt to remove a single reward model and observe changes in the model's performance. The results of the experiment show that using a single reward model leads to a decrease in other reward signals, whereas using multiple reward models balances all aspects of performance. The second sub-experiment was on the role of primitive cue-centred guidance, where the authors found that using only extended cues resulted in the main content of the input being ignored, whereas using primitive cue-centred guidance better captured the content of the input cue.

![image](https://github.com/user-attachments/assets/87c1a4d7-0dc6-4b07-a481-561a74353a7e)

Finally, the authors also conducted a user study to verify the effectiveness of the Parrot model in real-world applications. The experimental results show that the Parrot model outperforms other approaches in all aspects, including aesthetics, human preference, text-image alignment, and emotion. 

## Conclusion

### 1. Advantages of the Thesis
  1. The algorithm achieves a balance between multiple quality rewards through a multi-objective optimisation strategy and significantly improves the quality of generated images when jointly fine-tuning the T2I model and the cue expansion model.
  
  2. In addition, the authors introduced the original cue-centred guidance technique to ensure that the generated images are consistent with the user cues during inference. Experimental results show that Parrot significantly improves on several quality criteria relative to the benchmark method.

### 2. Innovative points
  1. The methodological innovation of this paper is that it proposes a multi-reward optimisation algorithm, Parrot, which effectively optimises multiple T2I rewards by achieving a balance between multiple quality rewards through batch Pareto optimal selection.
  
  2. Also, the algorithm learns reward-specific preference cues that can be used individually or in combination to control the trade-off between different rewards. In addition, the algorithm jointly fine-tunes the T2I model and the cue expansion network to further improve the quality of the generated images. 

### 3. Future Works
  1. Future research can be carried out in the following ways: firstly, Parrot can be considered for applications in other domains, such as natural language generation;
  
  2.  More complex reward function designs can be explored to better reflect user needs; and lastly, ways to improve the generation speed while ensuring high quality can be investigated. 
