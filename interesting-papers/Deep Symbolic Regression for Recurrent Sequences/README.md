# Deep Symbolic Regression for Recurrent Sequences
[paper link](https://arxiv.org/pdf/2201.04600) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a method called "deep symbolic regression" for predicting functions or relationships in recursive sequences.         | Transformer          |

## Methodology

### 1. Abstract
  The method uses the Transformer model and is evaluated on integer and floating-point sequences commonly used in human IQ tests. Experimental results show that the method outperforms Mathematica's built-in functions in a recursive prediction task for OEIS sequences and provides useful approximations
  
### 2. Method Description 
  The paper proposes a DL based model to solve the sequence prediction problem. Given a sequence of n points {u0, ... , un-1}, the task of the model is to find a function f such that for any i ∈ N, ui = f(i, ui-1,... , ui - d), where d is the recurrence degree. Since an infinite number of points cannot be evaluated, the function is considered a solution if, given the first n input terms, the model can predict the next npred terms.
  
### 3. Key concepts
  _Symbolic regression_: A type of regression analysis that searches for mathematical expressions or formulas that best fit a given set of data points. Unlike traditional regression techniques that fit data to a predefined model (e.g., linear regression, polynomial regression), symbolic regression attempts to discover the underlying mathematical relationships in the data without assuming a specific form.
  
### 4. Methodological improvements
  The paper considers two settings: integer sequences and floating-point sequences. In integer sequences, recursive formulas use only operators closed to Z (e.g., +, ×, abs, modulo, and integer division). In floating-point sequences, more operators and functions are allowed, such as real division, exponentiation, and cosine. Both settings have their own characteristics and advantages. Integer sequences are an important area in mathematics, especially related to arithmetic. Floating-point sequences, on the other hand, help to observe how the model handles a wider set of operators, thus providing more challenging problems.

In addition, the paper presents both symbolic and numerical regression tasks. In symbolic regression, the model is asked to predict the recursive relationship used by the sequence. At test time, the performance of the model is evaluated by the degree of approximation of that recurrence relation. In numerical regression, on the other hand, the model directly predicts the next npred values instead of the hidden recurrence relation. At test time, the model's predictions are compared to the true values.

### 5. Issues addressed 
  The main objective of the thesis is to solve the problem of sequence prediction. Specifically, the model aims to find a simple and efficient solution to minimize the complexity of the expression and the number of parameters. Also, the model can be used to explore the connection between recursive relations and mathematical expressions and can be used in areas such as symbolic reasoning and numerical computation.
  
## Experiments
  This article focuses on the symbol math prediction method based on the Transformer model, and verifies its performance and advantages through several comparison experiments. Specifically, the article includes the following comparison experiments:

**In-Domain Accuracy Comparison Experiment**: this experiment compares the accuracy of the model under different settings by testing the model's performance on a training dataset. The results show that although the floating point setting is more challenging than the integer setting, the symbolic model achieves good accuracy in both cases, while the numerical model performs poorly.

**Sensitivity experiment for evaluation metrics for symbolic models**: this experiment investigates the effect of tolerance and number of predictions on symbolic models by varying the parameters of these factors. The results show that the symbolic model performs better at low tolerance and maintains some accuracy at high tolerance. Meanwhile, the accuracy of the symbolic model decreases as the number of predictions increases, but the decrease is small.

**Difficulty analysis experiment**: this experiment investigates the model's ability to handle different types of operators by testing sequences with different difficulty levels. The results show that the symbolic model also handles other types of operators well, except for division and trigonometric functions.

**Out-of-domain generalization experiment**: This experiment uses sequences of integers from the OEIS database as test data to evaluate the model's generalization ability in the out-of-domain case. The results show that the symbolic model is able to successfully find recursive relations for about one-fifth of the sequences, and has some ability to recognize non-recursive relations as well.

## Conclusion

### 1. Advantages of the Thesis
  This paper presents a symbolic regression method based on the Transformer model that is able to successfully infer recurrence relationships for a given sequence and performs well in a range of challenging tasks. The method is applicable not only to integer sequences but also to floating-point sequences, and is able to predict the next value more accurately than numerical models. In addition, the method can be used to predict complex functional expressions as well as approximate values of numerical constants. These results show that the method can be applied to a wide range of areas, including practical problems such as time series forecasting.
  
### 2. Innovative points
 The methodological innovation of the paper is the use of the Transformer model to infer recurrence relations. Unlike traditional non-recursive functions, the recurrence relation provides a more general setting which better describes the dynamical processes of the system. This method introduces numerical labeling to deal with the problem of complex prefactors, which provides directions for future research.
 
### 3. Future Works
  The method may not be directly applicable when dealing with real-world time-series data, which usually cannot be simply represented as mathematical formulas. Therefore, further research is needed to address these issues. And the method can be extended to areas such as multidimensional series and differential equations, which will be an important future research direction.

