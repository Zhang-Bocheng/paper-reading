# Active Neural Mapping
[paper link](https://arxiv.org/pdf/2308.16246) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper introduces a new map building method, Active Neural Mapping (ANM). The method enables the process of actively exploring and building maps in unknown environments through the use of continuously learning neural scene representations.          | Deep Learning         |

## Methodology

### 1. Abstract
By analysing the weight space of the neural field, the researchers found that neural variability can be directly used to measure the immediate uncertainty of the neural map and combined with continuous geometric information to guide the robot to find passable paths to gradually understand the environment. Experimental results show that the method is efficient and effective in the visually realistic Gibson and Matterport3D environments.

### 2. Method Description 
Active Neural Mapping (ANM), proposed in this paper, is a deep learning-based method for environmental mapping. The method constructs an accurate and complete geometric model of the scene by continuously exploring unknown regions and fusing newly observed data with existing maps. The core idea of the method is to guide the mobile robot to a new location and collect the corresponding data by identifying the next target viewpoint, which results in significant distributional differences in the local space. This data is then used to optimise the map parameters and enable the update of the local equilibrium points.
![image](https://github.com/user-attachments/assets/08f0e342-4853-4529-9460-0fa895094fca)

### 3. Methodological improvements
  1. Direct use of NN as scene geometry models, eliminating the need to manually design features or rules.
  
  2. Automatically discovering the high variance region of the scene based on the data-driven approach, avoiding the problem of needing to set the threshold manually in traditional frontier-based methods.
  
  3. Capable of handling inaccurate representations near sparse structures or boundaries.

### 4. Issues addressed 
  1. How to find the next target viewpoint quickly and accurately for continuous exploration of the scene?
  
  2. How to effectively fuse the newly collected data to improve the overall map quality while ensuring the accuracy of the original map?
  
  3. How to cope with inaccurate representation problems such as sparse structures or near boundaries to improve the completeness and accuracy of the map?

## Experiments
This paper focuses on an active mapping system based on implicit neural representations, and evaluates and compares its performance through experiments. Specifically, this paper conducts comparison experiments in the following four areas:

**Comparison of methods**: this paper compares the proposed method with three related methods (FBE, OccAnt and UPEN). These methods all employ a 2D grid map representation and use a completeness metric to evaluate their exploration capabilities in 3D space.
![image](https://github.com/user-attachments/assets/048e1e5e-cd43-4f1d-ae0d-e6c531eb91b4)

**Target Location Recognition Strategies**: this paper compares two different target location recognition strategies, namely the Dropout and Bald Score based methods and the proposed weighted perturbation method. The results show that the proposed weight perturbation method can better quantify the map uncertainty and achieve better performance.

**Best Candidate Selection**: This paper compares three different best candidate selection criteria, including average distance, maximum variance and minimum distance. The results show that selecting the highest variance region gives the best performance.
![image](https://github.com/user-attachments/assets/833afd61-06b4-46d0-b5c9-3f4286687d21)

**System Performance**: This paper also evaluates the performance of the system in terms of reconstruction accuracy, completeness and computational cost. The results show that the system is able to achieve satisfactory reconstruction accuracy and completeness in a finite number of steps, as well as real-time capability and acceleratability. 

## Conclusion

### 1. Advantages of the Thesis
  1. The method takes advantage of the powerful representation capability of NNs and combines ML and CV techniques to achieve fast modelling of the environment and path planning.
  
  2. The method also takes uncertainty into account and improves the robot's exploration efficiency and success rate by optimising strategies and selecting action decisions.

### 2. Innovative points
  1. The main innovation of this paper is to apply NNs to the robot exploration problem and combine them with traditional ML and CV techniques. Specifically, the authors used NNs to construct a scene model and used NNs to predict the next best viewpoint.
  
  2. In addition, the authors propose a graph theory-based optimisation algorithm to compute the optimal path for the robot for more efficient exploration.

### 3. Future Works
In future research, it can be further explored how to improve the NN approach to enhance its performance and reliability. Also, it can be investigated how to combine this approach with other robot control techniques to achieve more intelligent and efficient robot operation. 
