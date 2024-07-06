# Deep Landscape Forecasting for Real-time Bidding Advertising
[paper link](https://arxiv.org/pdf/1905.03028) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper focuses on the problem of real-time auction market competition in online advertising, i.e., bid price prediction         | Deep Learning          |

## Methodology

### 1. Abstract
  Since the use of a second-price auction mechanism leads to missing data, a censorhip approach to the problem needs to be considered. Most of the current solutions are only based on counting statistics of discretized sample clusters or learning parameterized models based on some assumed distributional form. To address these issues, the authors propose a model called Deep Landscape Forecasting (DLF) that combines deep learning and survival analysis techniques. Specifically, they use a RNN to flexibly model the probability of winning at each bid price and perform bid price prediction via probabilistic chain rules. Finally, they optimize the whole model by minimizing two negative log-likelihood loss functions. 

 ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/80b1592f-2062-4e18-9ba5-381f757c6396)
 
### 2. Method Description 
  The paper proposes a deep learning-based bid landscape forecasting model -- Deep Landscape Forecasting (DLF) in real-time bidding advertisement scenarios. The model first discretizes the bid space and defines win probability and failure probability functions. Then a recurrent neural network (RNN) is used to capture the variation of conditional probabilities in each price interval. Finally, the model is trained by maximizing the negative log-likelihood of the data distribution.
  
### 3. Key concepts
  _Bid Landscape Forecasting_: A technique used primarily in digital advertising to predict the future bidding environment for advertising space or keywords. This forecasting is crucial for advertisers and marketers to strategize their bidding approach, optimize their budgets, and achieve better return on investment (ROI). The "bid landscape" refers to the range and distribution of bids that are placed for a particular ad placement, keyword, or action over time.
  
### 4. Methodological improvements
  Compared with traditional survival analysis methods, the model not only considers P.D.F., but also introduces the concept of C.D.F. to better handle missing values. In addition, the model employs an integrated loss function, which includes the learning of the probability of winning and the probability of losing, thus improving the model efficiency.
  
### 5. Issues addressed 
  The model solves the problem of bid landscape prediction in real-time bidding advertisements, which can more accurately estimate the probability distribution of market prices and improve advertisers' revenue and competitiveness. Meanwhile, the model is also applicable to large-scale online systems with good online inference efficiency.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/f0828ec0-ce76-4bb0-8cf8-f87af8cea441)

## Experiments
  This paper describes an experimental study conducted by the authors on the application of deep survival modeling to online advertising bidding scenarios. The experiments use two real-time bidding datasets in the real world, and a variety of evaluation metrics are evaluated and tested for significance. The experimental results show that the DLF model proposed by the authors exhibits better performance in both market price distribution prediction and win probability estimation, and achieves significant improvements in metrics such as Average Negative Log Likelihood (ANLP) and C-Index, relative to the other nine benchmark models. And, by further analyzing the experimental results, the authors demonstrate the superiority of the DLF model in accurately predicting the market price distribution, flexibly handling the distribution form, and effectively handling distorted data.
  
## Conclusion

### 1. Advantages of the Thesis
  This paper proposes a fine-grained prediction model based on deep RNN and survival analysis modeling for bid landscape prediction in real-time bidding advertisements. The model not only captures the complex price distribution patterns in each bid request, but also considers the prediction of win probabilities, including win logs and fail (blocked) logs. Experimental results show that the model has significant advantages over strong benchmarks and can be applied to optimize advertisement profit maximization strategies in future practical applications.
  
### 2. Innovative points
 1. **Fine-grained prediction**: The model not only predicts the market price distribution for a sample segment, but also predicts a personalized market price distribution and the corresponding winning probability distribution for each specific bid request.
 
 2. **No Assumption of Distribution Form**: The model is based on a novel modeling approach that generates flexible predictions without pre-assuming the market price distribution.
 
 3. **Novel Distortion Loss Function**: The model employs a composite loss function to deal with the distortion problem and further improves the traditional survival analysis approach to better model the market price distribution.
    
### 3. Future Works
  1. The model is used in combination with other techniques, such as recommender systems or user behavior analysis, to improve advertising effectiveness and revenue.
  
  2. For different types of advertisements, different prediction models need to be designed according to their characteristics to better meet the needs of advertisers.
  
  3. Test on larger datasets to verify the effectiveness of the model in a wider range of application scenarios.
