# Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search
[paper link](https://arxiv.org/pdf/2502.02508) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | The aim of this thesis is to explore how to enhance the reasoning capabilities of Large Language Models (LLMs) through reinforcement learning and autoregressive search.           |  Reinforcement Learning & LLMs       |

## Methodology

### 1. Abstract
The researchers propose the Chain-of-Action-Thought (COAT) reasoning method and implement it using a two-phase training model: the first phase is a small format tuning phase to internalize the COAT reasoning format, and the second phase is a large-scale self-improvement phase using reinforcement learning techniques. The method is applied to a 7B LLM called Satori, which performs well in mathematical reasoning benchmarks and has strong generalization capabilities.

### 2. Method Description 
The Chain-of-Action-Thought reasoning (COAT) method proposed in this paper is a strategy for solving sequential decision problems based on meta-action markers. COAT consists of three main components: continued reasoning, reflection, and exploration of alternatives. The model generates a sequence of meta-action tokens in an initial state and then constructs the answer incrementally by continuously generating intermediate reasoning steps. The method decomposes the reasoning process into multiple stages and introduces special meta-action tokens to guide the model to correct reasoning.

![image](https://github.com/user-attachments/assets/e7b47767-b396-4e01-9b7f-a7af8ab5135b)

### 3. Methodological improvements
Aiming at the lack of understanding of meta-action markers and the sparse rewards of long temporal sequences in traditional chained reasoning methods, this paper proposes two improvement strategies:

  1. Format Adaptation: by using the Multi-Intelligent Body Data Synthesis framework, the Pre-trained Language Model (PLM) is trained on a small number of demonstration trajectories so that it can mimic expert COAT trajectories.
  2. Self-improvement: self-correcting and optimizing by training the PLM with reinforcement learning using the PPO algorithm, while allowing the model to start and restart reasoning from the wrong inference path.

### 4. Issues addressed 
  1. Pre-trained language models that are unfamiliar with meta-action markers and their roles, resulting in the inability to correctly perform reflection or explore alternatives in the reasoning process.
  2. The problem of long time-series reward sparsity, i.e., the need to reason correctly several times to obtain a single reward, makes it difficult for the model to learn effective reasoning strategies.

By introducing format adjustment and self-improvement strategies, the COAT method proposed in this paper is able to effectively address these issues, thereby improving the model's performance on sequential decision problems.

  
