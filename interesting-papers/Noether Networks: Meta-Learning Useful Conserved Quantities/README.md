# Noether Networks: Meta-Learning Useful Conserved Quantities
[paper link](https://arxiv.org/pdf/2112.03321) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the problem of inductive bias in machine learning and proposes a new method, the Noether network, for automatically discovering useful symmetries.         | Machine Learning          |

## Methodology

### 1. Abstract
Inspired by Neumann's theorem, the authors transform the problem of finding inductive biases into meta-learning useful conserved quantities. Experimental results show that the Noether network improves the quality of prediction and provides a generalized framework for solving sequence prediction problems.

![image](https://github.com/user-attachments/assets/0ecc2ee9-4ca9-4288-80cb-dfe3aa96bb1b)

### 2. Method Description 
The paper presents a predictive model called Noether Network for tasks with time series data. The model consists of two parts: **an embedding model g and a prediction model f**. The embedding model maps the input sequences into a low-dimensional space and extracts the time invariants; the prediction model uses these invariants to predict future values. During training, the model parameters are optimized by minimizing the task loss and the Noether loss.

### 3. Methodological improvements
Compared to traditional prediction models, Noether Network introduces the Noether loss function, which enables the model to learn the time invariants. In addition, the model employs an inner and outer learning process for updating the weights of the embedding and prediction models, respectively. This layered learning approach improves the generalization ability of the model.

### 4. Issues addressed 
Noether Network is suitable for tasks that require the processing of time series data, such as stock price prediction and weather forecasting. The model can automatically learn to be time-invariant, which improves the prediction accuracy. Also, the model can be adapted to different prediction tasks by simply adjusting the structure of the embedding and prediction models. Therefore, Noether Network is a generalized time series forecasting model.

## Experiments
This paper describes the authors' four experiments on Noether networks, namely:

Can known conservation laws be recovered from scientific data?
In this experiment, the authors used two scenarios, an ideal spring and an ideal pendulum, to verify whether the Noether network can recover known conservation laws from scientific data. The authors first generate all valid formulas and remove those that are incompatible with physical units and equivalent formulas, yielding about 41,460 and 72,372 candidate conservation formulas. These formulas are then optimized by optimizing the parameters in them to minimize their variance over real data and are considered to be approximately conserved if the degree of conservation is reduced by two orders of magnitude compared to a random sequence. 

Ultimately, for each possible amount of conservation, the authors attempted to treat it as a meta-tailoring loss, fine-tuning it starting from a pre-trained MLP and meta-tailoring it with an in-step and a range of different learning rates (10^-3 to 1). The experimental results show that the Noether network finds the true conserved quantity well and outperforms the hand-coded conservation loss approach as well as the Hamiltonian neural network with full power to achieve energy conservation.

Is it applicable to controlled dynamical environments?
In this experiment, the authors used a controlled pendulum environment to verify the applicability of the Noether network to a controlled dynamics environment. The authors first modified an SVG model-based approach by removing the sampling component, since the environment is deterministic, and by connecting the actions to the corresponding frame encoder outputs and feeding them into the LSTM.

After training the SVG model for 50 epochs, the authors ran Algorithm 1 for 20 epochs to learn the embedding network to preserve useful quantities. The experimental results show that the Noether network performs better than the baseline method because it is directly adapted to the process of embedding LSTM activations against conservation loss.

Is it possible to parameterize useful conservation quantities from raw pixel information?
In this experiment, the authors used 311 training sequences to verify whether the Noether network can parameterize useful conservation quantities from raw pixel information. The small number of samples makes generalization difficult. Therefore, the authors used a baseline SVG model for comparison. 

The experimental results show that the Noether network with single-step metric tailing improves over the baseline model in all four metrics considered (LPIPS, MSE, PSNR, and SSIM). The relatively better performance of the Noether network as the prediction time increases may be due to the fact that the conservatism promotes certain aspects of the input image that the model retains.

How does the degree of conservation affect performance on the prediction task?
In this experiment, the authors investigated how the degree of conservation affects the performance of the prediction task. The authors used a single-step meta-tailored Noether network and performed several iterations on it to optimize the internal conservation loss. 

The experimental results show an improvement in the external task loss over about 150 steps, suggesting that the approximate conserved quantities learned by the Noether network can be generalized to more accurate conserved settings. 

![image](https://github.com/user-attachments/assets/01f66645-0728-4d30-9b60-8efaa8ebee6f)

![image](https://github.com/user-attachments/assets/cf9fbe87-d80f-439e-b9c9-c9ef44aff6f1)

## Conclusion

### 1. Advantages of the Thesis
  1. Conservation laws in physics are utilized as effective regularizers, which can effectively reduce the generalization error.
  
  2. A new meta-learning algorithm is proposed that is able to learn a more generalized generalization bias without relying on the task or data distribution.
  
  3. Good results are achieved in practical applications such as video prediction.
 
### 2. Innovative points
  1. Conservation laws in physics are utilized to construct the meta-learning objective function, allowing the model to better adapt to real-world data distributions.
  
  2. A combination of program synthesis and gradient descent is used to search for useful conserved quantities, thus avoiding the problem of users specifying conserved quantities manually.
  
  3. The meta-learning approach enables more generalized inductive biases to be learned without relying on the task or data distribution.
     
### 3. Future Works
  1. how to deal with noisy data and how to extend the method to other domains need to be further explored.
  
  2. In addition, the method needs more experiments to prove its applicability and effectiveness in different fields. 
