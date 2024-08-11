# Regularizing Trajectory Optimization with Denoising Autoencoders
[paper link](https://arxiv.org/pdf/1903.11981.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper presents a trajectory optimization method for use in model reinforcement learning that aims to improve planning efficiency and sample efficiency by regularizing the environment model using a denoising self-encoder.          | Reinforcement Learning          |

## Methodology

The method can be applied in both gradient-based and gradient-free optimizers and has achieved fast initial learning in several popular motion control tasks. This work has important implications for improving the performance of model RL.

![image](https://github.com/user-attachments/assets/60f2a252-dc25-4a19-8f76-346e0d9a0a34)

## Experiments
This paper focuses on four comparative experiments conducted by the authors on five standard Mujoco environments (Cart-pole, Reacher, Pusher, Half-cheetah and Ant):

  1. The Probabilistic Ensembles with Trajectory Sampling (PETS) model was used as a benchmark in these environments and was compared with it to compare the effectiveness of the authors' proposed normalized trajectory optimization method;
  
  2. For the normalized trajectory optimization method, in the Cartpole environment, the normalization did not significantly improve the results because the model was already good, while in the Half-cheetah environment, the normalization was effective in preventing problems caused by utilizing dynamic models with inaccurate models;
  
  3. In closed-loop control, normalization improves the results of trajectory optimization;
  
  4. Applying normalization to end-to-end training reveals that normalization can significantly improve learning speed and performance, but has problems with exploration.

![image](https://github.com/user-attachments/assets/ae95ff41-3c40-4b99-baa6-b6d7f1052f80)

<br>&emsp;for the first experiment, the authors compared the PETS model to a normalized trajectory optimization approach and showed that normalization was effective in improving performance in the Half-cheetah environment. 
<br>&emsp;For the second experiment, the authors take a closer look at the normalized trajectory optimization approach and find that normalization can further improve performance in closed-loop control. 
<br>&emsp;In the third experiment, a visual analysis was performed in a Cartpole environment to show how normalization affects the trajectory optimization process. 
<br>&emsp;The last experiment applies normalization to end-to-end training and finds that normalization can significantly improve learning speed and performance in the initial phase, but lack of exploration may impair performance in complex environments. 

![image](https://github.com/user-attachments/assets/3c20256a-678b-4ee2-81dd-f2f27726d61c)

## Conclusion

### 1. Advantages of the Thesis
  1. **Broad research area**: the authors study the problem of model predictive control in RL, which is an important problem faced by robot control, autonomous driving, and other fields.
  
  2. **Methodological innovation**: the authors propose the use of Denoising Autoencoder (DAE) to solve the problem caused by model error in the planning process, which is a new approach to improve the quality of planning effectively.
  
  3. **experimental validation**: The authors validate the effectiveness and feasibility of the methodology in several experiments, including a standard motor control task and a complex industrial process control task, demonstrating the generalizability and practicality of the methodology.
     
### 2. Innovative points
The authors use the denoising self-encoder for estimating the probability distribution of past experience, and then combine it with the objective function of the planning optimization to achieve constraints on the planning results. This approach has the following advantages:

  1. It can effectively reduce the effect of model error in the planning process and improve the quality of planning.
  
  2. It can be applied to the case of high-dimensional input space, such as sensor data.
  
  3. It can be applied to online learning situations, e.g., where constant adaptation to environmental changes is required.
 
### 3. Future Works
  1. **Explore a wider range of system types**: the current research focuses on continuous control systems, and in the future, it can consider extending the method to other types of systems, such as discrete control systems.
  
  2. **Improving the design of denoising self-encoder**: the existing structure of denoising self-encoder may have some limitations, and in the future, it can try to improve its design to better adapt to different application scenarios.
  
  3. **Combining other techniques**: in addition to denoising self-encoders, other techniques, such as deep RL, adversarial training, etc., can be considered to further improve the effectiveness of model predictive control. 

