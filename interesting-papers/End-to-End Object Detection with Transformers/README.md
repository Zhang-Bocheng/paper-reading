# End-to-End Object Detection with Transformers
[paper link](https://arxiv.org/pdf/2005.12872.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new object detection method, DETR (DEtection TRansformer), which treats object detection as a direct ensemble prediction problem         | Transformer           |

## Methodology

### 1. Abstract
  The main ingredients of the new framework, called DEtection TRansformer or DETR, are a set-based global loss that forces unique predictions via bi-partite matching, and a transformer encoder-decoder architecture. Given a ﬁxed small set of learned object queries, DETR reasons about the re-lations of the objects and the global image context to directly output the ﬁnal set of predictions in parallel.  More-over, DETR can be easily generalized to produce panoptic segmentation in a uniﬁed manner. 
  
### 2. Method Description 
  Unlike traditional detection models based on anchor frame or region proposals, DETR uses an encoder-decoder structure based on a transformer architecture to achieve direct prediction of objects. Specifically, the model takes the input image and unfolds it into a one-dimensional vector by CNN feature extraction and adds position coding as input, which is then converted into a high-dimensional representation by a multilayer transformer encoder. Next, the transformer decoder is initialized with a fixed number of learned positional embeddings (i.e., "object queries"), which are processed by the decoder through the self-attention and encoder-decoder The decoder processes these object queries through self-attention and encoder-decoder-attention mechanisms and produces the final N detection results. Each detection result is predicted by a feedforward network with category labels, center coordinates, and information such as height and width.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/fdf246cf-3d8b-4c4a-a9a8-e9ec12a22bcd)

### 3. Methodological improvements
  The main innovation of DETR is the introduction of transformer architecture to deal with the target detection problem. Compared to traditional detection models based on anchor frame or region proposals, DETR can handle multiple targets in an image more efficiently and does not require predefined anchor frame sizes and shapes. In addition, DETR employs a hybrid loss function based on l1 loss and generalized IoU loss to balance the weights between category prediction and bounding box prediction.
 
### 4. Issues addressed 
  Traditional target detection models usually need to be first generated into a series of candidate frames, which are then classified and regression adjusted by a classifier. This approach suffers from two major problems: first, a set of different anchor frame sizes and shapes need to be predefined, which increases computational complexity and limits detection performance; second, since the anchor frames are usually overlapped, additional non-maximum suppression (NMS) operations are required to remove redundant detection results. In contrast, DETR avoids these problems by directly predicting the location and class of objects, making it more efficient and accurate in handling large-scale datasets.
  
## Experiments
  This paper focuses on the experimental results of object detection using the DETR model on the COCO dataset and compares it with the Faster R-CNN. Specifically, the following four aspects of experiments are conducted in this paper:

  1. The performance of DETR and Faster R-CNN on the COCO dataset is compared;
  <br>2. The impact of different components in DETR on the final performance was analyzed;
  <br>3. Conducted some improvement experiments for the DETR model, such as removing certain components;
  <br>4. Attempted to extend DETR to the panoptic segmentation task and compared it with other methods.

**Comparing the performance of DETR and Faster R-CNN on the COCO dataset**:
The main objective of this experiment is to verify the performance of DETR on the object detection task and compare it with Faster R-CNN. The experimental results show that DETR can achieve comparable or even better performance than Faster R-CNN, especially in terms of small targets and targets with relatively large length and width. This indicates that DETR has great potential for object detection tasks.

**Analyzing the effect of different components in DETR on the final performance**:
This experiment aims to analyze the impact of different components in DETR (e.g., encoder, decoder, attention mechanism, etc.) on the final performance. The experimental results show that all these components have a significant impact on the final performance, with the global self-attention mechanism being one of the most important factors.

**Some improvement experiments are conducted for the DETR model**:
This experiment aims to further optimize the performance of the DETR model by removing some components. The experimental results show that removing some components may lead to performance degradation, but better performance can also be obtained in some cases.

**An attempt is made to extend DETR to the panoptic segmentation task and compare it with other methods**:
This experiment aims to explore the possibility of extending DETR to panoptic segmentation tasks and compare it with other methods. The experimental results show that DETR achieves good performance on this task as well and has a higher advantage over other methods.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/1fc38fe2-2bd5-4676-9022-f1f160a1dba4)

## Conclusion

### 1. Advantages of the Thesis
The paper uses a self-attentive mechanism to handle the interactions between all the elements and does not require any customization layer and can be easily implemented in any framework containing standard CNN and transformer classes. DETR has the following advantages over existing detection methods:

  1. Simplifies the detection pipeline by removing multiple manually designed components that require coding prior knowledge, such as spatial anchoring or non-maximal suppression.
  
  2. Uses an end-to-end training approach, by treating object detection as a direct ensemble prediction problem.
  
  3. A self-attention mechanism is used, which enables better handling of global information.
  
  4. Parallel decoding is implemented to avoid the computational burden of recursive decoding.
     
### 2. Innovative points
  1. The main innovations of DETR are its direct prediction approach to the object detection problem, as well as the self-attention mechanism and parallel decoding techniques used.
  
  2. Compared to traditional indirect prediction methods, DETR is simpler and more straightforward, while also being able to achieve better results in terms of performance.
  
  3. In addition, DETR provides ideas for the extension of other complex tasks, such as its use in a pixel-level recognition task, which has shown good results.
     
### 3. Future Works
  1. For the detection of small targets, ways such as introducing more feature extractors or increasing the number of training samples can be considered to improve the performance.
  
  2. One can further explore how to utilize more prior knowledge to improve the detection performance.
  
  3. One can try to combine DETR with other state-of-the-art models, such as YOLOv4, to obtain better performance.


