# A bio-inspired bistable recurrent cell allows for long-lasting memory
[paper link](https://arxiv.org/pdf/2006.05252.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |  This paper describes a new bio-inspired recurrent neural network unit that enables long memory storage at the cellular level and uses only cellular connections        |     LSTM      |

## Methodology

### 1. Abstract
  This paper describes a new bio-inspired recurrent neural network unit that enables long memory storage at the cellular level and uses only cellular connections. This new recurrent neural network unit performs better in time-series tasks requiring very long memories compared to traditional gated recurrent units. Furthermore, by introducing recurrent neuromodulation into this unit, it can be linked to standard gated recurrent units, thus taking a step towards biological realizability.

### 2. Method Description 
  In this paper, two artificial neural network models based on neuronal feedback mechanisms are proposed: the BRC (Bistable Recurrent Cell) and the nBRC (recurrently neuromodulated BRC). Both models achieve neuronal dimorphism by adjusting parameters to realize the memory function. Among them, BRC is realized by controlling the feedback parameter α and updating the gating parameter C; while nBRC adds interactions between interlaminar neurons on the basis of BRC, which further enhances the memory ability.

### 3. Key concepts
  _Bistable Recurrent Cell (BRC)_:  A concept in the realm of recurrent neural networks (RNNs), particularly aimed at addressing some of the limitations and inefficiencies found in traditional RNN architectures, such as the vanishing gradient problem. The Bistable Recurrent Cell is designed to maintain stable states and handle long-term dependencies more effectively than traditional RNNs.
  
### 4. Methodological improvements
  Compared to traditional recurrent neural networks (RNNs), BRC and nBRC have better memory performance and can control the dimorphism and memory capacity of neurons by adjusting parameters. In addition, nBRC increases the interactions between interlayer neurons, which further improves the memory capacity.
  
### 5. Issues addressed 
  The BRC and nBRC models proposed in this paper can effectively solve the problems of training difficulty and long-term dependence in traditional RNNs, and also realize cell-level memory, which provides new ideas and methods for the research of artificial neural networks.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/4c822a01-6a53-4988-a242-0af94ac90281)

## Experiments
  This paper describes three comparative experiments conducted by the authors in their study:

  1. **One-dimensional toy problem:** In this problem, the network is presented with a one-dimensional time series of length T, where x_t obeys a standard normal distribution with mean 0. The task is to output the predicted value of the first element of the sequence after receiving the last element of the sequence. The authors use the mean squared error as an evaluation metric and compare the performance at different values of T. The results are summarized in the following table. The results show that all recurrent units perform similarly when T is small, but when T is large, only the network consisting of the BRC is able to exceed the random guessing threshold.

  2. **Two-dimensional denoising problem:** In this problem, the network is presented with a two-dimensional time sequence of length T, where five of the first five time steps and the second dimension at the moment of T are generated from a stream of data, while the first dimension is used to notify the network when it reaches the end of the sequence and needs to output the predicted values. The authors used the mean squared error as an evaluation metric and compared the performance for different forgetting period lengths N. The authors also used the mean squared error as an evaluation metric and compared the performance for different forgetting period lengths. The results show that when N is 200, GRU and LSTM are unable to exceed the random guessing threshold, while the performance of BRC and nBRC is hardly affected. In addition, when N is 0, GRU and LSTM can learn long-term dependencies well, but perform poorly on datasets containing only short dependencies, while BRC is not subject to this limitation.

  3. **Sequential MNIST (MNIST Sequential Problem):** in this problem, the network is presented with a time sequence of MNIST image pixels, each pixel is presented to the network in order. The authors added nblack black pixels to increase the length of the forgetting period and used accuracy as an evaluation metric. The results show that BRC and nBRC can learn dynamics over several thousand time steps.

In addition, the authors analyzed the dynamic behavior of BRC and found that the proportion of BRC increases with the presence of relevant inputs, allowing the network to store information better, and the average et value increases, making the network more sensitive to new inputs. These observations further confirm the importance of introducing the BRC for long term memory.

## Conclusion
### 1. Advantages of the Thesis
  In this paper, we propose a new bio-inspired recurrent neuron model, Bistable Recurrent Cell (BRC), which realizes the effect of long term memory by introducing the concepts of cellular memory and bistability, and achieves better performance than LSTM and GRU on several datasets Performance. In addition, the authors propose a special neuromodulation approach to transform the BRC into a structure similar to the standard GRU, which provides ideas for combining the traditional gated recycling unit with biological realizability.
  
### 2. Innovative points
  The main contribution of this paper is to propose a **novel recurrent neuron model, BRC**, whose core idea is to use cellular memory and bistability to simulate the information processing process in the biological brain. Specifically, the hidden state of BRC does not directly affect other neurons, but regulates cellular excitability by means of feedback control, thus realizing the state switching of bistability. In addition, the authors also enable the BRC to better approximate the structure of the standard GRU by regulating the neurons, which provides ideas for further research on the combination of gated recurrent units and biological realizability.
  
### 3. Future Works
  The BRC model proposed in this paper has good application prospects and can be widely used in sequence modeling, speech recognition and other fields. Meanwhile, the authors also propose some future research directions, such as exploring more complex neuromodulation schemes as well as further investigating the combination of gated recurrent units and biological realizability. These studies will further promote the development of recurrent neural networks and provide a more reliable foundation for the application of artificial intelligence technology.


