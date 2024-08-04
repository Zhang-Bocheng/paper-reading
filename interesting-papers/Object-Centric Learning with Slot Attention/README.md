# Object-Centric Learning with Slot Attention
[paper link](https://arxiv.org/pdf/2006.15055) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new module called Slot Attention for learning object-centered representations in complex scenes.         | Attention           |

## Methodology

### 1. Abstract
Conventional DL methods typically only learn distributed representations and fail to capture the compositional nature of natural scenes. Slot Attention generates a set of task-relevant abstract representations, called slots, by interacting with perceptual representations such as CNNs. These slots are exchangeable and can be bound over multiple rounds through a competitive process, enabling specialization of any object in the input. Experimental results show that Slot Attention can extract object-centered representations, allowing the model to generalize to unseen combinations, for both unsupervised object discovery and supervised attribute prediction tasks.

![image](https://github.com/user-attachments/assets/8c8fa4a5-1d8e-47e3-b754-9a278549f09f)

### 2. Method Description 
The paper proposes a module called "Slot Attention" that maps a set of input feature vectors to a set of output vectors, each of which describes an object or entity in the input. The module uses an iterative attention mechanism to realize the mapping from inputs to outputs, and in each iteration, the output vectors compete to interpret a different part of the input, so that each output vector can represent a different object or entity in the input. The module has two key properties: replacement invariance with respect to the inputs and replacement equivalence with respect to the order of the outputs.

![image](https://github.com/user-attachments/assets/66bc07b5-e022-43f7-8eaa-2f72f1ecf7f2)

### 3. Methodological improvements
The module employs learnable linear transformations k, q, and v to map the inputs and outputs to the same dimension D. The module then computes the attention coefficients by means of a softmax function and aggregates the input values using weighted averaging to assign them to different output vectors. Finally, each output vector undergoes GRU updating and MLP post-processing to better capture the inputs and improve performance.

### 4. Issues addressed 
  1. In the unsupervised object discovery task, the module is used as part of a self-encoder for encoding an image into a set of hidden representations, where each hidden representation can be decoded back into the original image space.
  
  2. In the ordered set prediction task, the module converts the input into a set of output vectors, each of which can be categorized individually without considering the order between the targets.
  
  3. Thus, the module can help solve ensemble prediction problems in multiple data modalities, such as point cloud prediction, multi-object image classification, and molecule generation.

## Experiments
  This paper describes two experiments, which are comparative experiments for object discovery and ensemble prediction tasks.

For the **object discovery task**, the authors used three multi-object datasets (CLEVR, Multi-dSprites, and Tetrominoes) and divided them into a training set and a test set. The authors compared with two recent state-of-the-art methods, IODINE and MONet, and also with a simple MLP baseline. The authors use average precision (AP) as an evaluation metric and report the performance of each model. 

The experimental results show that the authors' method is comparable in quality to previous methods and is more competitive in terms of training speed and memory efficiency. In addition, the authors show how Slot Attention without a decoder can be used to obtain object-centered representations of unseen scenes.

![image](https://github.com/user-attachments/assets/035cb5ce-e2db-46ed-ba51-93aedcf8e54e)

For the **ensemble prediction task**, the authors use a dataset with attribute annotations (CLEVR) and compare it with a deep network (DSPN) specialized for this task. The authors use average precision (AP) as an evaluation metric and report the performance of each model. 

The experimental results show that the authors' method can match or exceed the DSPN benchmark and performs well with a high distance threshold. In addition, the authors show how performance can be improved by varying the number of attentional iterations and that more objects can be processed by changing the number of slots. Finally, the authors also visualize the attention maps for each slot and calculate their Adjusted Random Index (ARI) scores to evaluate their natural segmentation effect on the scene.

![image](https://github.com/user-attachments/assets/d62992b6-df53-43a1-951a-beaf168eb5a0)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper propose a module called "Slot Attention" that learns object-centered abstract representations and applies them to low-level perceptual inputs.
  
  2. The module uses an iterative attention mechanism to decompose input features into a set of slot representations, thus achieving effective memory consumption and computational efficiency.
  
  3. In addition, the module is broadly applicable and scalable, and can be applied to video data or other data modalities such as graph node clustering, point cloud processing undershirt or text/speech data.

![image](https://github.com/user-attachments/assets/372aab52-563b-4983-9959-8a8cc913466e)

### 2. Innovative points
  1. The main contribution of the paper is the introduction of the "Slot Attention" module, a simple and easy-to-implement architectural component that extracts object representations in images on top of CNN encoders and trains them end-to-end with downstream tasks.
  
  2. The module decomposes the input features through an iterative attention mechanism into a set of slot representations, which are not specialized for particular types or classes of objects, but rather resemble object files, where each slot can store and bind any input object.

### 3. Future Works
  1. The module has demonstrated its flexibility on downstream tasks such as image reconstruction and ensemble prediction, but there is potential for applications in many other areas, such as reward prediction, visual reasoning, control or planning.
  
  2. Therefore, the next steps are to apply Slot Attention on video data or other data modalities (e.g., graph node clustering, point cloud processing undershirts, or text/speech data), or to explore applications for other downstream tasks to further improve its performance and interpretability.  
