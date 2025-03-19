# Parameter-Efficient Transfer Learning for NLP
[paper link](https://arxiv.org/pdf/1902.00751) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 |  This paper explores the parameter efficiency problem that exists when performing migration learning in Natural Language Processing (NLP) and proposes the use of adapter modules as a solution.         |   Transfer Learning       |

## Methodology

### 1. Abstract
Traditional migration learning requires training a new model for each downstream task, leading to parameter waste and inefficiency. In contrast, adapter modules can add a small number of trainable parameters for different tasks without changing the original network parameters, thus realizing a high degree of parameter sharing and flexibility extension. The authors' experimental results by applying the BERT model to 26 text categorization tasks show that the adapter module can achieve close to full fine-tuning, but only increases the number of parameters per task by 3.6%. This greatly improves parameter efficiency and generalization ability compared to traditional full fine-tuning.

![image](https://github.com/user-attachments/assets/324d6850-0859-41d1-9d50-50082aaad6a6)

### 2. Method Description 
This paper presents a strategy called “adapter tuning” for fine-tuning large text models on multiple downstream tasks. The strategy has three key features:** good performance, allowing tasks to be trained sequentially without having to access all datasets simultaneously, and adding only a few additional parameters.** These features are useful for the case where many models in a cloud service need to be trained sequentially on a series of downstream tasks, making a high degree of sharing desirable.

![image](https://github.com/user-attachments/assets/300c0d4f-49ed-4ff4-b655-fe03a06b4388)

To achieve these properties, this paper proposes a new bottleneck adapter module. Compared to standard fine-tuning, adapter tuning requires only a small number of new parameters to be added to the model, and these are trained on the downstream tasks. In adapter tuning, new adapter layers are injected into the original network, while the weights of the original network remain unchanged. In standard fine-tuning, the new top layer and the original weights are trained together, while in adapter tuning, the parameters of the original network are frozen and can be shared by multiple tasks.

The adapter module has two main features: **a small number of parameters and approximate identity initialization**. the adapter module requires much fewer layers than the original network, which means that the total model size grows relatively slowly when more tasks are added. Approximate identity initialization is used to train the adapted model stably. During training, the adapter module may activate to change the distribution of activations across the network.

This paper also provides a specific implementation of the adapter module for the Transformer network. Each Transformer layer contains two main sublayers: **an attention layer and a feedforward layer**. Each sublayer is followed by a projection that maps the feature size back to the size of the input size. There is skip-connection between each sublayer and the output is passed through layer normalization. Two tandem adapters are inserted after each sublayer, which are always applied directly to the output of the sublayer, but before adding the skip connection back. the output of the adapter is passed directly to the next layer normalization.

To limit the number of parameters, this paper proposes the bottle-neck architecture. adapter first projects the original d-dimensional features to a smaller dimension m, applies a nonlinear function, and then projects them back to the d-dimension. The total number of parameters added to each layer including the bias term is 2md+d+m. The number of parameters added to each layer can be limited by setting m<d; in practice, we use about 0.5% to 8% of the original model. the bottle-neck dimension m provides a simple trade-off between performance and parameter efficiency. the adapter module itself has an internal skip -connection. module is initialized to approximate the identity function if the parameters of the projection layer are initialized to be close to zero.

In addition to the layers in the adapter module, the authors train new layer normalization parameters for each task. This technique is similar to techniques such as conditional batch normalization, FiLM, and self-modulation, which also allow for efficient parameter adaptation of the network; this can be done with only 2d parameters. 

### 3. Methodological improvements
The adapter tuning strategy proposed in this paper is an effective method for fine-tuning large text models that can be trained on multiple downstream tasks with only a few additional parameters added. And, the design of the adapter module allows for efficient sharing of parameters, thus reducing the rate of growth of the overall model size. This approach offers greater flexibility and scalability compared to traditional fine-tuning.

### 4. Issues addressed 
The approach proposed in this paper addresses the problem of fine-tuning large text models on multiple downstream tasks. Traditional fine-tuning methods require re-training the entire model or sharing a large number of parameters across different tasks, which leads to larger model sizes and higher computational costs. In contrast, the adapter tuning strategy adapts to different downstream tasks by adding a small number of new parameters, which makes the model more flexible and scalable. What is more, the design of the adapter module makes it possible to share parameters efficiently, which further reduces the growth rate of the overall model size.

## Experiments
This paper focuses on the authors' experiments using the pre-trained model BERT for textual tasks and verifies the parameter efficiency by comparing it with full fine-tuning. Specifically, the authors conducted the following three comparison experiments:

The first experiment is **conducted on the GLUE benchmark**, where the authors transfer the BERT large model to different datasets and compare the effects of full fine-tuning and adaptor tuning. The results show that adaptor tuning scores an average of 80.0 on the GLUE benchmark, which is slightly lower than full fine-tuning by 0.4 points, but only requires 1.3 times the number of parameters.

![image](https://github.com/user-attachments/assets/36b13ab4-9627-4e96-be08-3f7795bda5ba)

The second experiment was **conducted on other publicly available text categorization tasks** that cover a varying number of training examples, categories, and text length ranges. The authors used an extensive hyperparameter search space to select the best full amount of fine-tuning and adaptor tuning methods. The results show that adaptor tuning provides a more compact model, introducing only 1.14% new parameters, relative to 1.19 times the number of parameters for full fine-tuning.

![image](https://github.com/user-attachments/assets/a4abded0-2129-4b09-8d46-86450c468a1f)

The third experiment was **conducted on the SQuAD quiz task**, where the authors compared the effects of full fine-tuning and adaptor tuning. The results show that adaptor tuning can significantly reduce the number of parameters while preserving performance. 

![image](https://github.com/user-attachments/assets/ca1af1e5-8a21-4793-89a9-c1dd31a0af38)

## Conclusion

### 1. Advantages of the Thesis
  1. In this paper, a new NLP task solving strategy, adapter module, is proposed and experimentally validated in a large number of text categorization tasks. The method has higher parameter efficiency than traditional feature extraction and fine-tuning methods, and also guarantees model performance.
  2. The authors also provide a detailed analysis and discussion of the method, including ablation experiments, robustness experiments, etc., to prove its reliability and effectiveness.

### 2. Innovative points
  1. The adapter module proposed in this paper is a lightweight neural network structure that can be quickly adapted to different downstream tasks based on pre-trained models. Compared with traditional fine-tuning methods, the adapter module can better retain the information of the original model, and also be able to utilize the shared parameters more effectively to improve the model generalization ability.
  2. And, the authors propose some extension methods, such as batch/layer normalization, increasing the number of layers, and different activation functions, to further improve the model performance.

### 3. Future Works
Future research can be carried out in the following aspects: 
  (1) further exploring the optimization methods of the adapter module to improve the model performance; 
  (2) applying the adapter module to more NLP tasks, such as machine translation, speech recognition, etc.; 
  (3) combining with other technological tools, such as meta-learning, adaptive learning, etc., to further improve the adaptive and generalization abilities of the model .    
