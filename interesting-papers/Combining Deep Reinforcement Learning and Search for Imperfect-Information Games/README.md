# Combining Deep Reinforcement Learning and Search for Imperfect-Information Games
[paper link](https://arxiv.org/pdf/2007.13544) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a reinforcement learning (RL) and search framework called ReBeL that can be used for deep RL and search in single-player games and perfect information games.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
  In incomplete information games, previous algorithms cannot cope with this situation. Therefore, the authors propose the ReBeL framework, which can converge to a Nash equilibrium in any two-player zero-sum game and achieves an approximate Nash equilibrium in two different incomplete information games. In addition, ReBeL achieves beyond human-level performance, excelling in incomplete information games such as Texas Hold'em, while using much less domain knowledge than any previous poker AI.
  
### 2. Method Description 
  The ReBeL algorithm proposed in this paper is a combination of RL and search for finding Nash equilibrium strategies in depth-constrained imperfect information games. The core idea of the algorithm is to transform an imperfect information game into a perfect information game with a continuous state and action space, and use the iterative equilibrium solution method (CFR) to find Nash equilibrium strategies in subgames. Then, the value network and the strategy network are trained by self-play RL to improve the quality of the strategies. Finally, the same algorithm is used to perform a secure search for Nash equilibrium strategies based on the known value and strategy networks and a randomly chosen number of iterations at the time of testing.
  
### 3. Key concepts
  _Nash equilibrium_: A concept in game theory where no player can benefit by unilaterally changing their strategy, given the strategies of the other players. In other words, it is a stable state of a game where each player's strategy is optimal considering the strategies of the other players.
  
### 4. Methodological improvements
  Compared with traditional RL methods, the ReBeL algorithm has the following advantages in dealing with imperfect information games:

  1. Converting imperfect information games into perfect information games makes the search process more efficient.

  2. Using the iterative equilibrium solution (CFR) to find the Nash equilibrium strategy in the subgame ensures a higher quality of the strategy.

  3. Using the same secure search algorithm during testing avoids the problem of strategy attacks that may occur in traditional search methods.

### 5. Issues addressed 
  The ReBeL algorithm solves the problem of finding Nash equilibrium strategies in depth-constrained games with imperfect information. The algorithm is applicable to various types of 2p0s imperfect information games, including some complex games such as Poker and Chess. Experimental results show that the ReBeL algorithm can achieve high winning rates in different games and performs well in comparison with other related algorithms. Therefore, ReBeL algorithm provides new ideas and solutions for solving imperfect information games.
  
## Experiments
This paper describes the application of the ReBeL algorithm to poker games and conducts several comparative experiments to verify its effectiveness.

First, the authors used two games, Heads-up no-limit Texas hold'em poker (HUNL) and Liar's Dice, for their experiments. In HUNL, the authors used less domain knowledge to train the agents, while in Liar's Dice, more search iterations were used to improve performance.

Second, in the HUNL game, the authors compared the ReBeL algorithm with other algorithms such as BabyTartanian8, Slumbot and Local Best Response (LBR). The results show that ReBeL outperforms these algorithms in HUNL games and is able to achieve performance levels comparable to other top human players.

Finally, the ReBeL algorithm was further tested by the authors in the Liar's Dice game and compared to other algorithms. The results show that the ReBeL algorithm is able to converge to an approximate Nash equilibrium in a shorter time and has better performance than other algorithms.

Overall, this paper verifies the superiority of the ReBeL algorithm in poker games through several experiments and demonstrates its potential for other game-like problems. 

## Conclusion
### 1. Advantages of the Thesis
   1. Different from the traditional RL+Search algorithm, ReBeL takes into account the effect of probability distributions and uses the concept of extended states in the training process.
     
   2. ReBeL can work efficiently in large-scale games and beat top human professionals in the benchmark game heads-up no-limit Texas hold'em, while requiring less domain expertise than any previous poker AI.
  
   3. In addition, the paper demonstrates the use of ReBeL in other benchmark incomplete information games such as Liar's Dice and open-sources its implementation code. This provides more opportunities for researchers to explore the problem of multi-intelligent body interaction in incomplete information games.
      
### 2. Innovative points
  1. ReBeL defines states by extending them to include probabilistic belief distributions for all agents, based on public observations and agent strategies.
  
  2. ReBeL trains value and policy networks through self-play RL and uses these value and policy networks for search during self-play.
  
  3.  The combination of search and reinforcement learning allows ReBeL to better handle state dependencies and probability distribution effects in incomplete information games.
     
### 3. Future Works
  1. The success of ReBeL demonstrates the feasibility of combining search and reinforcement learning for the Nash equilibrium solving problem in incomplete information games. However, ReBeL still suffers from some limitations, such as the amount of information input into its value and strategy functions grows linearly with the number of information states in the common state, which is not feasible for games with strategic depth but little common knowledge (e.g., Recon Chess).
    
  2. Future research focuses on how to further optimize the ReBeL algorithm to better fit different types of game scenarios. In addition, ReBeL can also be applied to other types of multi-intelligence body interaction problems, such as in the areas of auctions, negotiation, cybersecurity, and self-driving vehicle navigation.
