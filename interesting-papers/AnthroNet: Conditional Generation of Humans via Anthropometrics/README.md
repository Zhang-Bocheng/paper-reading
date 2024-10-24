# AnthroNet: Conditional Generation of Humans via Anthropometrics
[paper link](https://arxiv.org/pdf/2309.03812) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a new human model that is modelled by a wide range of anthropometric metrics and is capable of generating a wide range of different human shapes and poses.          | Deep Learning         |

## Methodology

### 1. Abstract
The model uses a deep generative architecture to directly model specific human identities and is capable of generating human images in arbitrary poses. This is the first model of its kind to be trained end-to-end using only synthetic data, providing not only a highly accurate mesh representation of the human body, but also allowing for precise anthropometric measurements of the body. 

In addition, using a highly diverse animation library, they artistically manipulate synthetic human bodies and hands to maximise the diversity of learnable priors. The model was trained on a dataset containing 100,000 procedurally generated posed human meshes and their corresponding anthropometric measurements. Their synthetic data generator can be used to generate millions of unique human identities and poses for non-commercial academic research purposes.

### 2. Method Description 
This thesis proposes a synthetic data-based human body modelling method, which enables high-precision, multi-pose and multi-body shape human body modelling by using body models in the Unity game engine. Specifically, they used hand-sculpting to create body models of various morphologies and Houdini software to create character models with different poses. These models were then imported into Unity to achieve high-quality human modelling using the skin-binding functionality it provides.
![image](https://github.com/user-attachments/assets/36e204e1-55df-4406-8c8f-51127dedf4ab)

### 3. Key concepts
_Anthropometry_ : A sub-discipline of anthropology. It mainly studies anthropometric measurements and observation methods, and explores the characteristics, types, variations and development of the human body through overall and local measurements of the human body. Anthropometry consists of two parts: skeletal measurement and in vivo measurement. 

### 4. Methodological improvements
  1. **Data diversity**: the use of synthetic data produces a more diverse and accurate dataset, making the trained model more pervasive.
  
  2. **Model extensibility**: since it uses body models from the Unity game engine, it can be easily extended to other application areas.
  
  3. **Training efficiency**: using synthetic data can significantly reduce training time and cost compared to methods based on scanned data.

### 5. Issues addressed 
The method solves some of the problems faced by traditional scan data-based body modelling methods, such as insufficient data volume and poor quality of scan data. At the same time, the method also provides a general framework that can be applied to different application scenarios, providing new ideas and methods for human modelling research.

## Experiments
This paper focuses on the performance evaluation of the AnthroNet model and the results of comparative experiments. 
<br>&emsp;Firstly, the authors evaluated the generation module and found that random Fourier coding can improve the conditional generation through Ablation Study. <br>&emsp;Secondly, the authors evaluated the registration module and tested it using the SMPL-X mannequin dataset, which showed that the Euclidean distance error between the AnthroNet model and the target model is low. The authors then demonstrate the interpretability and accuracy of the AnthroNet model in controlling the human shape and that the desired human shape can be generated by adjusting specific anthropometric measurements. 
<br>&emsp;Finally, the authors compare the AnthroNet model with other models to evaluate its ability to regress 3D shapes from monocular images. The authors used the Human Bodies in the Wild (HBW) dataset for testing and compared the AnthroNet model to the measurement module in the SHAPY framework. 

The experimental results show that the AnthroNet model can be converted from the SMPL-X model to the AnthroNet local grid system without loss of accuracy and has similar performance to the SHAPY framework in predicting sparse anthropometric measurements.
![image](https://github.com/user-attachments/assets/0c995cc3-59ea-4f54-95e0-586be8f77434)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a deep generative human body model called AnthroNet that is capable of generating high-resolution human body meshes based on a large number of objective anthropometric measurements and is highly capable of describing human morphology.
  
  2. In addition, the authors provide an open synthetic data generator that can be used for non-commercial academic research purposes, avoiding the privacy, security, and ethical issues associated with collecting and annotating large amounts of real human data.

### 2. Innovative points
  1. AnthroNet is a DL-based nonlinear human model that uses a large number of objective anthropometric measurements as input conditions to generate high-resolution human meshes.
  
  2. In addition, the authors provide two efficient registration pipelines that enable the bi-directional conversion of SMPL and SMPL-X meshes to AnthroNet meshes.
  
  3. This approach not only improves the representativeness and diversity of the human body model, but also allows for easy extraction of anthropometric measurements for a better description of the human body morphology.

### 3. Future Works
  1. Its input dataset may not be fully representative of the entire human population, and thus more datasets are needed to increase its diversity and generalisation capabilities.
  
  2. In addition, AnthroNet needs further research to optimise its architecture and parameter selection, as well as the design of the loss function, in order to obtain a more accurate and complete representation of the human body shape. 
