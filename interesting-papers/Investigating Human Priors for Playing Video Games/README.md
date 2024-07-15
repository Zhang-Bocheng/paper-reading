# Investigating Human Priors for Playing Video Games
[paper link](https://arxiv.org/pdf/1802.10217.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This paper explores the role of human prior knowledge in solving video games.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
 Through a series of experiments, the authors modify the game environment to systematically mask different types of human a priori knowledge and quantify the effect of this a priori knowledge on human performance. The results show that removing certain a priori knowledge leads to a dramatic decrease in human players' problem-solving speed, e.g., from 2 minutes to over 20 minutes. Furthermore, it was shown that general a priori knowledge, such as the importance of objects and visual consistency, is crucial for efficient game play. The paper's methodology and results have important implications for understanding the role of human intelligence in games.

 ![image](https://github.com/user-attachments/assets/542c5f4a-24e3-436d-af14-549ddeafc5c7)

### 2. Method Description 
The aim of this study was to investigate the aspects involved in efficiently solving visual information in video games for humans. The researchers created different versions of the game to hide various forms of prior knowledge by re-rendering various entities such as ladders, enemies, keys, platforms, etc. using different textures. In addition, they changed various properties of the physical attributes of the game, such as the effects of gravity and the way agents interact with the environment. All games are structured and rewarded in exactly the same way, ensuring that any changes are only caused by a priori shielding.

![image](https://github.com/user-attachments/assets/f982df68-16ee-4ca9-8d62-abadc67ba82c)

### 3. Methodological improvements
  The researchers used a browser-based gaming platform to simulate the exploration problem encountered in the classic ATARI game Montezuma's Revenge, which has proven to be very challenging for deep reinforcement learning techniques. However, because the game was too large to be solved by an RL agent, the researchers chose to create different versions of the game to be able to run a wide range of experiments. They used different textures in each version to mask various forms of prior knowledge and altered physical properties in the game to see how these changes affected human performance.
  
### 4. Issues addressed 
The main goal of the study was to explore the aspects involved in efficiently solving visual information in video games for humans. The researchers shielded various forms of prior knowledge by creating different versions of the game and altered the physical attributes in the game to understand how these changes affected human performance. By recruiting 120 participants for the experiment, the researchers quantified human performance in each version of the game and recorded the amount of time players spent in the game, the number of deaths, and the number of unique game states visited.

## Experiments
  This paper focuses on the comparison between human performance in games and the performance of ML algorithms. The authors conducted several comparative experiments to investigate the effects of different visual concepts on human game performance and to determine whether these concepts affect the performance of the algorithms by comparing them to the performance of RL algorithms.

First, the authors compare the original game version with a version of the game that hides object information and find that hiding object information causes human players to take longer, die more times, and explore more states in order to complete the game. This suggests that knowing about objects is one of the important prior knowledge.

Second, the authors compare a version of the game that hides the appearance of objects but retains their locations to a completely randomized version of the game and find that human players can use the similarity a priori to identify other platforms and ladders, and thus hiding the appearance of objects does not significantly affect game performance. However, when item information is completely removed, human players' game performance decreases significantly.

Next, the authors compare a version of the game that hides item colors and shapes but retains their locations to a version of the game that is completely randomized and find that hiding item colors and shapes does not significantly affect game performance. However, when item information is completely removed, human players' game performance decreases significantly.

Finally, the authors compared a version of the game that changed the ladder to an upward-only form and altered the button controls with a version of the game that flipped the direction of gravity and found that both resulted in the human player taking longer to complete the game. Also, when the direction of gravity is flipped, it becomes more difficult to use keyboard controls.

In summary, the results of this paper show that understanding a priori knowledge of objects, item similarities, and item locations in a game is crucial for human players' game performance. Furthermore, the authors demonstrate that this prior knowledge has no significant effect on the performance of the algorithms by comparing the performance of reinforcement learning algorithms.

![image](https://github.com/user-attachments/assets/686b145e-5146-4f17-baad-a5a00dab2e47)

![image](https://github.com/user-attachments/assets/a1a7504c-2ad2-407c-a660-5afd02308dd4)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper systematically quantifies the importance of different types of prior knowledge in solving video game problems.
  
  2. The study was made more reliable and manageable by designing a special game environment and systematically masking different types of information to test human performance.
  
  3. The results suggest that specific knowledge such as "ladders to climb" and "keys to open doors" are important for fast problem solving, but more general a priori knowledge about objects and visual coherence is more critical.
     
### 2. Innovative points
  1. Through experimental design and data analysis, this paper is the first to systematically explore the relative importance of different types of prior knowledge in solving video game problems.
  
  2. This paper uses a curiosity-driven RL algorithm that specializes in sparse reward settings to better model human behavior.
  
  3. This paper also provides an open source experimental platform for other researchers to further explore the importance of human prior knowledge.
     
### 3. Future Works
  1. The results of this paper provide guidance for future research, especially in developing better RL algorithms that need to consider how to utilize human prior knowledge.
  
  2. The interactions between different types of human a priori knowledge and how they affect task solving efficiency can be further explored.
  
  3. Attempts could also be made to apply human prior knowledge to other domains, such as natural language processing or robot control.




