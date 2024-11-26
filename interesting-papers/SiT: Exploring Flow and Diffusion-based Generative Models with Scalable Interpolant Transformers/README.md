# SiT: Exploring Flow and Diffusion-based Generative Models with Scalable Interpolant Transformers
[paper link](https://arxiv.org/pdf/2401.08740) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a generative model called Scalable Interpolant Transformers (SiT), which is constructed based on Diffusion Transformers (DiT).          |    Diffusion Transformers (DiT)      |

## Methodology

### 1. Abstract
The model uses an interpolation framework to connect two distributions, allowing for more flexible learning than standard diffusion models. By introducing design choices such as learning in discrete or continuous time, objective functions, interpolation, and deterministic or random sampling, SiT outperforms DiT and achieves better performance in ImageNet 256×256 and 512×512 benchmarks. In addition, SiT explores various individually tunable diffusion coefficients, achieving FID-50K scores of 2.06 and 2.62, respectively.

### 2. Method Description 
This paper proposes Scalable Interpolant Transformers (SiT), a generative model based on probabilistic flow ODEs and inverse SDEs. The model improves flexibility by decoupling the time-dependent coefficients in probabilistic flow ODEs and inverse SDEs, and the generative model can be constructed using any differentiable αt and σt. 

  1. **Temporal discretisation: **the learning process allows flexibility in specifying sampling time points.
  2. **Choice of Fractional Mapping:** Re-expresses the fractional mapping through constraints to make it equivalent to the velocity field.
  3. **Select Interpolation Process:** Provides a variety of interpolation processes for users to choose from.
  4. **Selection of diffusion coefficient:** Select the appropriate diffusion coefficient according to the experimental results.

Finally, the authors also designed a scalable architecture, Interpolant Transformer, for training SiT models at different scales.
 
### 3. Methodological improvements
  1. **Decoupling time-dependent coefficients:** improves model flexibility by decoupling time-dependent coefficients in probabilistic flow ODEs and inverse SDEs.
  2. **Addition of selection options:** Several options such as time discretisation, selection of fractional mappings, selection of interpolation processes and selection of diffusion coefficients are provided for better tuning of model parameters and improved performance.
  3. **Scalable Architecture:** The Interpolant Transformer architecture allows SiT models to be trained at different scales to further improve performance.

### 4. Issues addressed 
  1. **Lack of flexibility:** the time-dependent coefficients in traditional diffusion models usually cannot be adjusted independently, which limits the flexibility of the model.
  2. **Difficulty in parameter adjustment:** due to the lack of selection terms, it is difficult to adjust the parameters of traditional diffusion models according to the experimental results, which affects the model performance.
  3. **Low computational efficiency:** traditional diffusion models may have computational problems, resulting in high training time and computational cost.

## Experiments
This paper focuses on three comparative experiments:

The first experiment involves a gradual transition from the DiT model (discrete time, score prediction, VP interpolation) to the SiT model (continuous time, speed prediction, Linear interpolation) and investigates the effect of this transition on performance. The experiments used the SiT-B model trained on ImageNet at a resolution of 256 × 256 with a fixed number of training steps of 400 K. The results show that switching to continuous time improves performance in the transition from discrete time to continuous time and has a more flexible choice of integrators that allows trade-offs between functional evaluation steps and FID scores.

![image](https://github.com/user-attachments/assets/2ea47ff9-87dc-4759-874d-bde8bc289722)

The second experiment compares learning three different parameterisations: learning a score model using (6), learning a weighted score model using (6,λ), and learning a speed model using (7). The results show that better performance is obtained using the weighted score model and the speed model, and that choosing the appropriate weights λ at different time points also plays an important role in performance improvement.

![image](https://github.com/user-attachments/assets/66a036cb-e9f3-4a1b-8a59-5003c1c1cabf)

The third experiment compares the difference between two sampling methods using the probabilistic flow equation (2) and SDE (4). The results show that sampling using SDE outperforms sampling using probabilistic flow equations and that the performance of the two methods varies with different computational budgets. 

![image](https://github.com/user-attachments/assets/667a0a18-47dd-4500-8726-38f3c850f725)

## Conclusion

### 1. Advantages of the Thesis
By comparing different time discretisation, model prediction, interpolator and sampler choices, the authors find that carefully weighing these choices can significantly improve performance. In addition, the paper explores ways to further improve performance without changing the model structure or hyperparameters.

### 2. Innovative points
  1. The authors experimented with the choices of time discretisation, model prediction, interpolator and sampler to arrive at the optimal combination of design choices and applied them to an image generation task, achieving better results than existing methods.
  2. In addition, the authors explored how the diffusion coefficient can be used to control the KL dispersion to further optimise the performance.

### 3. Future Works
  1. The experiments in this paper focus on the ImageNet dataset, so more experiments are needed to prove its performance on other datasets.
  2. Finally, as deep learning techniques evolve, we expect to see more similar interpolator-based image generation frameworks emerge.   
