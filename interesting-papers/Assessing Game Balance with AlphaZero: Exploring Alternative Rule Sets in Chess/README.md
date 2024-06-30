# Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess
[paper link](https://arxiv.org/pdf/2009.04374) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |  This paper explores how to assess game balance and creatively explore and design new chess variants using the AlphaZero system.        | Machine Learning          |

## Methodology

### 1. Abstract
  The AlphaZero system is an unsupervised learning system that can learn the best strategy for any rule set from scratch. By using the AlphaZero system in nine different variants, the researchers determined what kind of game patterns these variants would lead to and found some very dynamic variants. In addition, they compared the value of pieces in the different variants and found that certain variants were more decisive than traditional chess. This research demonstrates the possibility of moving beyond the modern rules of chess.
  
### 2. Method Description 
  The board game variants presented in this paper include self-capture, double pawns, no king, free moves, alternating moves for both sides, long pawns, double pawns, and chess without rules. These variants are realized by changing the rules of the game and in some cases require modification of the 50-move rule to avoid potentially infinite games. These variants aim to preserve the aesthetics and symmetry of the original game while revealing new opening, middlegame, or ending patterns as well as new opening theory.

In this paper, we use the AlphaZero algorithm to train these variants and observe new patterns and theories in each one. AlphaZero is an adaptive learning system that improves itself through self-play over multiple iterations. It consists of a deep neural network fθ that computes a valuation v for a given state s. In addition, the network outputs a probability vector p that is used to consider each possible next move. These predictions are used in Monte Carlo Tree Search (MCTS) to evaluate the board position. MCTS improves the statistical estimation of the outcome of the game by repetitively simulating how the game unfolds. In each MCTS simulation, fθ is recursively applied to sequence positions (nodes) until a certain depth is reached. Finally, the most visited root move is selected for play.

### 3. Key concepts
  _Monte Carlo Tree Search (MCTS)_:  A heuristic search algorithm used to make optimal decisions in artificial intelligence (AI) and game theory, especially for games with a vast decision space like Go, Chess, and various video games. MCTS combines the precision of tree search methods with the robustness of random sampling (Monte Carlo methods) to evaluate moves in a game.
  
### 4. Methodological improvements
  The methodological improvement in this paper is the introduction of the AlphaZero algorithm, which automates the testing of various board game variants and observes new patterns and theories in each variant. This allows researchers to quickly assess the impact of various board game variants without the need to involve a large number of human players.
  
### 5. Issues addressed 
  The main goal of this paper is to explore different board game variants and observe if they have new dynamic patterns and open opening theories. By using the AlphaZero algorithm, researchers can quickly assess the impact of various board game variants and observe new patterns and theories in each variant. This approach can help provide a better understanding of the characteristics, strengths, and weaknesses of different board game variants, which can inform future research.
  
## Experiments
  This paper describes experiments that investigate rule variations of board games. The experiments use the AlphaZero model to train and evaluate different board game variants and compare their performance under different conditions. Detailed description of each comparison experiment:

  **Relative Importance of Board Game Variants**: The experiment compared the relative importance of eight board game variants (including Kingless Chess, Knightless Chess, etc.). The conclusion that Kingless Chess is the optimal variant was reached by calculating the value of the pieces played in each variant, as well as by comparing the average expected score and the average decision rate between the variants.

  **Impact of the new rules on the board game**: This experiment compared the differences in performance between seven board game variants (including No Returning Kings, No Chaining, etc.) and the standard board game. By calculating the value of the pieces played in each variant and comparing the average expected score and average decision rate between the variants, it was concluded that the new rules had a significant effect on some of the variants.

  **Human players' responses to board game variants**: the experiment recruited three professional and five amateur chess players to participate in the test. They were asked to evaluate the difficulty and playability of eight board game variants (including double pawns to a square, bishop can't get out of nine squares, etc.). Statistical analysis of their evaluations led to the conclusion that there were significant differences between the different variants.

  **Changes to the board game with the new rules**: This experiment compared the differences in performance between two board game variants (including no rooks and no cannons) and the standard board game. By calculating the value of the pieces played in each variant, and comparing the average expected score and average decision rate between the variants, it was concluded that the new rules had a significant effect on some of the variants.

  **Historical evolution of board game variants**: The experiment reviews the history of board game variants from ancient times to the present day and explores their origins and trends. Through the collection of historical documents and modern research data, conclusions were drawn about the connections and influences between the different variants.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/8287f70b-eb7c-41ca-80cd-c6a2f55be7bc)

In short, these experiments provide an important reference for us to understand the development history of board games and the characteristics of variants. At the same time, they also reveal some new issues and challenges, such as how to balance the fun and skill of the game, and how to cope with the constant emergence of new variants and rules.

## Conclusion
### 1. Advantages of the Thesis
  1. The paper proposes a method for evaluating rule changes in board games using AlphaZero models, and experiments are conducted using chess as an example.

  2. By training the AlphaZero model under different rules, the researchers can effectively simulate the game behavior of human players over several decades and predict the possible game outcomes under different rules.

  3. The researchers also used quantitative and qualitative analysis methods to delve into the changes and trends of the game under different rules.

  4. Finally, the researchers make recommendations for future research directions, including applying this method to other types of games and exploring more complex rule changes.

### 2. Innovative points
  1. The use of the AlphaZero model to evaluate rule changes in board games is a novel attempt to quickly simulate the behavior of games under different rules and predict possible outcomes.

  2. The researchers used both quantitative and qualitative analysis methods to delve into the changes and development trends of the game under different rules, providing new ideas and methods for studying the development of board games.
     
### 3. Future Works
  1. This approach can be applied to other types of games, such as video games, to help balance game mechanics.

  2. Further exploration of more complex rule variations, such as the introduction of a randomization factor or more strategic choices, can be used to increase the fun and challenge of the game.
