# Pruning neural networks without any data by iteratively conserving synaptic flow
[paper link](https://arxiv.org/pdf/2006.05467.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores how to prune neural network parameters without using any data to save time, memory, and energy during training and testing.         |  Neural Network         |

## Methodology

### 1. Abstract
The authors propose a theory-driven approach to algorithm design and verify a conservation law through mathematical formulations and experiments that explains the susceptibility of existing gradient-based initialized pruning algorithms to layer collapse. The theory also describes how to avoid layer collapse altogether, motivating a new pruning algorithm that iteratively maintains the total flow of synaptic strength (SynFlow). 

The algorithm requires no reference to training data, is able to compete with or outperform the best existing pruning algorithms during the initialization phase, and performs well under a wide range of models, datasets, and sparse constraints. Thus, this data-independent pruning algorithm challenges the existing notion that data must be used in the initialization phase to quantify which synapses are important.

### 2. Method Description 
The Synaptic Flow Pruning (SynFlow) algorithm proposed in this paper is an iterative pruning algorithm based on a data-independent scoring function designed to avoid layer collapse and achieve maximum critical compression. The algorithm determines which parameters should be pruned by iteratively computing the Synaptic Flow score of the parameters, which takes into account the interactions of each parameter in the neural network and combines it with a global mask to ensure conservatism between layers. In addition, the algorithm uses a new loss function, called Synaptic Flow Loss, to calculate the Synaptic Flow score.

![image](https://github.com/user-attachments/assets/5b3ce6e2-45b2-4763-907b-0ff22afee323)

### 3. Methodological improvements
  1. The main improvement to the SynFlow algorithm is that it uses a data-independent scoring function instead of the traditional gradient-based backpropagation algorithm.
  
  2. This makes the SynFlow algorithm more efficient and can be applied to large-scale deep learning models.
  
  3. In addition, the SynFlow algorithm introduces a new loss function, the Synaptic Flow Loss, which better captures the interactions between the parameters in the neural network and thus improves the effectiveness of pruning.
     
### 4. Issues addressed 
The SynFlow algorithm solves two major problems that exist in traditional pruning algorithms: **layer collapse and inaccurate scoring functions**.:
<br>&emsp;Layer collapse means that when one layer is pruned, the performance of other layers is also affected, resulting in a degradation of the performance of the entire network. 
<br>&emsp;Inaccurate scoring functions can lead to important parameters being incorrectly clipped, which can affect the performance of the network.The SynFlow algorithm avoids these problems by iteratively calculating the Synaptic Flow score and achieves maximum critical compression.

## Experiments
In this paper, seven experiments are conducted to compare the performance of SynFlow algorithm with other weight-based pruning algorithms at different compression ratios and analyze the strengths and weaknesses of SynFlow algorithm.

First, the authors **compare the SynFlow algorithm with random pruning and weight-size pruning as baseline algorithms**. The experimental results show that at high compression ratios, the SynFlow algorithm outperforms the other algorithms and has better stability. And at low compression ratios , although SNIP and GraSP can partially outperform the SynFlow algorithm, they both suffer from layer collapse.

Second, the authors **compare the differences between iterative pruning algorithms and one-time pruning algorithms**. The experimental results show that the iterative pruning algorithm can help avoid the early layer collapse problem, but its computational cost is exponentially higher. In addition, these iterative versions of SNIP still suffer from layer collapse problems before reaching the maximum compression ratio, which is guaranteed to be reached by the SynFlow algorithm.

Third, the authors **performed a data matching ablation study on the SynFlow algorithm**. The experimental results show that the SynFlow algorithm performs well without the use of data matching and sometimes even outperforms data-dependent pruning methods such as SNIP and GraSP.This challenges the validity of existing algorithms that use data in initialization and provides an algorithmic baseline that any future pruning algorithm that uses data for initialization should surpass.

Finally, the authors **compare the SynFlow algorithm with results from a recent related paper**. The paper confirms the competitiveness of the SynFlow algorithm even at low compression ratios and on large-scale datasets (ImageNet) and models (ResNet-50), and provides concrete evidence on the theoretical motivation of the SynFlow algorithm and insights to support further improvements to the algorithm. 

![image](https://github.com/user-attachments/assets/781140f0-8a8c-4d13-a375-96bdb5d4a9b9)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper propose a new theoretical framework that explains why existing pruning algorithms at initialization encounter the problem of layer collapse, and through which the authors illustrate how iterative magnitude pruning overcomes layer collapse to identify winning lotteries at initialization.
  
  2. Based on this, a new data-independent pruning algorithm, SynFlow, is designed that avoids layer collapse and achieves the maximum critical compression ratio. Experimental results show that the SynFlow algorithm outperforms existing algorithms on 12 different models and datasets.
  
  3. In addition, the article explores the potential application of neural network pruning to improve energy efficiency, reduce the impact of the training environment, and facilitate deployment.

### 2. Innovative points
  1. This article introduces the concept of Maximal Critical Compression, which means that a pruning algorithm should avoid layer collapse as much as possible.
  
  2. And, the article proves that iterative magnitude pruning algorithms can avoid layer collapse by observing conservative laws.
  
  3. the authors design a new data-independent pruning algorithm, SynFlow, which can achieve the maximum critical compression rate and achieve excellent experimental results.

### 3. Future Works
  1. exploring more potential pruning algorithms to meet the requirement of maximum critical compression ratio;
  
  2. using the SynFlow algorithm to calculate an appropriate per-layer compression ratio in combination with existing scoring metrics, so as to accomplish the pruning task more efficiently; 
  
  3. using pruning as the initialization of neural network program to further improve the performance of the neural network.
  
  4. In addition, the article mentions the potential applications of neural network pruning in terms of improving energy efficiency, reducing the impact of the training environment, and facilitating deployment, which can be further explored in the future as well. 
