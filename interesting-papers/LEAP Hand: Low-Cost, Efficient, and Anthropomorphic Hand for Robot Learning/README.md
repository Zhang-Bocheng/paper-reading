# LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning
[paper link](https://arxiv.org/pdf/2309.06440) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |This paper describes a hand robot called LEAP Hand, which is low-cost, efficient and human-like, and can be used for machine learning research.           | Machine Learning         |

## Methodology

### 1. Abstract
Unlike previous hand robots, LEAP Hand employs a novel kinematic structure that allows for maximum dexterity in any finger position. In addition, LEAP Hand is capable of generating high torque for extended periods of time and can be used to perform a wide range of practical manipulation tasks, including visual teleoperation and learning from passive video data. Experimental results show that the LEAP Hand significantly outperforms its closest competitor, the Allegro Hand, in all tests and at 1/8th the cost.

### 2. Method Description 
The paper proposes a new finger abduction-adduction mechanism called LEAP hand. Conventional direct-drive hands must have motors mounted inside the fingers, so their kinematic structure is limited and they cannot accurately mimic the movements of the human hand. PIP and DIP joints, on the other hand, are hinge joints and are easy to model, requiring only one actuator per joint. 

But the spherical joint cannot be modelled in this way, and it is usually necessary to use two motors (MCP-1, MCP-2) in close proximity to simulate it approximately. However, previous studies have proposed two designs (Allegro and LEAP-C hand), but both suffer from a problem: one degree of freedom is lost when the finger is either extended or closed, resulting in reduced dexterity.

![image](https://github.com/user-attachments/assets/399b951b-0c6d-402d-b3d0-c89092c9edf2)

The solution proposed by the LEAP hand is to move the abduction-adduction axis into the reference system of the first finger joint and arrange it so that it is always perpendicular to it. This allows abduction-adduction movements of the fingers in all positions. As a result, the LEAP hand has an abduction-adduction action in extension, similar to the LEAP-C hand, and a rotation action in flexion, similar to the Allegro.

### 3. Methodological improvements
In the traditional design, the abduction-adduction axis is fixed to the palm of the hand, which leads to a loss of dexterity, which the LEAP Hand solves by moving the axis into the reference system of the first finger joint and making it always perpendicular to that joint. This design solution allows the fingers to maintain all degrees of freedom in all positions, thus improving dexterity.

### 4. Issues addressed 
The main contribution of this thesis is the proposal of a new finger abduction-adduction mechanism that solves the problem of the limited motion structure of a conventional direct-drive hand due to the motor being mounted inside the finger. At the same time, the mechanism enables the finger to retain all degrees of freedom in all positions, improving dexterity.

## Experiments
This paper describes the design principles and applications of the LEAP Hand across multiple tasks. The authors first compare the cost and repairability of LEAP Hand with other common hand robots (e.g., ShadowHand and AllegroHand), and highlight the low cost and ease of maintenance of LEAP Hand. The authors then conducted several experiments to evaluate the performance of LEAP Hand, including a comparison with the human hand, the application of a machine learning task, and the use of a simulator.

In the comparison with the human hand, the authors used the Manus Meta VR glove for telecontrol and tested the grasping ability of different hand sizes. The results show that the LEAP Hand is able to perform many types of grasps and is highly resistant to interference. In addition, the authors conducted experiments on gesture control learnt from videos, which showed that the LEAP Hand was easier to control than the Allegro Hand.

![image](https://github.com/user-attachments/assets/0890dc08-7d6e-4dba-9947-771a6fa41e8f)

In terms of machine learning tasks, the authors performed behavioural cloning and simulation-to-reality tasks. By collecting Epic-Kitchens videos as pre-training data, the authors applied behavioural cloning to LEAP Hand and compared it to other robot hands. The results show that LEAP Hand performs better in these tasks. In addition, the authors performed a simulation-to-reality task that demonstrated that LEAP Hand was faster at rotating a cube.

![image](https://github.com/user-attachments/assets/17418a36-5481-4178-8ed5-e88d1aa3a5c3)
  
## Conclusion

### 1. Advantages of the Thesis
  1. In this paper, an arm design scheme called LEAP Hand is proposed and its superior performance in terms of strength, gripping ability and durability is experimentally verified. The scheme employs the design of multiple mechanical fingers, each controlled by a spindle actuator, with a high degree of flexibility and adjustability.
  2. In addition, the authors have opened the related source code and hardware design files for other researchers. 

### 2. Innovative points
  1. The main innovation of this paper is the proposed arm design scheme for the LEAP Hand, which is described in detail and experimentally validated. The scheme employs the design of multiple mechanical fingers, each of which is controlled by a spindle actuator and is highly flexible and adjustable.
  2.  In addition, the authors developed an open-source platform including URDF models, 3D CAD files and API interfaces for easy use and extension by other researchers. 

### 3. Future Works
Future research directions may include improving the arm design to enhance its performance and flexibility, exploring more application scenarios and optimising the corresponding algorithms and control systems. It is also possible to consider integrating the LEAP Hand with other robotic components to build more complex and powerful robotic systems. 
