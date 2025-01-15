# AGENTLESS : Demystifying LLM-based Software Engineering Agents
[paper link](https://arxiv.org/pdf/2407.01489) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an automated approach to software development called AGENTLESS, which employs a simple but effective three-phase process: locate, fix, and verify patches, without the need for complex autonomous software agents or letting large language models (LLMs) determine future operations.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method performs well in the popular SWE-bench Lite benchmark, offers higher performance and lower cost than existing open-source software agents, and has been adopted by OpenAI as a way to demonstrate the real-world coding performance of GPT-4 and new OpenAI models. In addition, the authors constructed SWE-bench Lite-S to exclude problematic issues for more rigorous evaluation and comparison.

### 2. Method Description 
The paper proposes a tool called AGENTLESS for automatic repair of software defects. The tool consists of three phases: locate, fix, and verify. In the locate phase, AGENTLESS uses three methods to determine the location of files and code that need to be modified. First, it uses a structure similar to Linux tree commands to build the directory structure of the project's code base and provides it as input to the Language Model (LLM). It then uses an embedded search method to identify additional files relevant to the problem. Finally, AGENTLESS compares these files with the LLM localised locations and ultimately selects the most relevant files. In the remediation phase, AGENTLESS uses LLM to generate multiple possible solutions and selects them based on the differences between them. In the validation phase, AGENTLESS uses automatically generated tests to evaluate whether each solution correctly solves the problem.

![image](https://github.com/user-attachments/assets/67e7131b-2032-4873-9f5e-de55f6d164e5)

### 3. Methodological improvements
AGENTLESS combines existing techniques such as language modelling, embedded retrieval and automatic test generation to achieve the goal of automatically fixing software defects. By using this combined approach, AGENTLESS can more accurately determine where code needs to be modified and generate reliable solutions.

### 4. Issues addressed 
AGENTLESS helps developers find and fix bugs in software faster, thereby improving software quality and reliability. In addition, due to its automated nature, it reduces the time and labour costs required to fix errors manually. Therefore, AGENTLESS is a tool that has the potential to improve the software development process.

## Experiments
This paper presents research on using generative methods based on pre-trained models to solve software engineering problems. The research was experimented on the SWE-bench Lite dataset and compared with 26 other competitors. The experimental results show that this approach can successfully solve a significant number of problems with high performance and low cost.

![image](https://github.com/user-attachments/assets/8ae4361d-9005-4525-adcc-1c3bc239cb54)

Specifically, the authors first convert problem descriptions into input vectors and generate candidate solutions using a pre-trained language model (e.g., GPT-4). The generated candidate solutions are then screened and filtered to finally identify the best solution and submit it to the code base to solve the problem. The authors also used a variety of metrics to evaluate the performance of the algorithm, including repair rate, cost, etc.

The experimental results show that the method outperforms 26 other competitors on the SWE-bench Lite dataset, proving its effectiveness and usefulness. In addition, the authors provide detailed analyses and explanations of the experimental results for a better understanding of how the algorithm works and its limitations. Overall, this article provides a promising approach to solving practical problems in software engineering and provides a valuable reference for research in related fields.

![image](https://github.com/user-attachments/assets/a2ff7473-b2c9-4e81-8274-372fa9f94e57)

## Conclusion

### 1. Advantages of the Thesis
  1. This approach is simple and intuitive, easy to understand, and avoids the limitations of complex tool use and the risk of wrong decisions. The authors conducted an extensive evaluation in the SWE-bench Lite benchmark and demonstrated that AGENTLESS offers higher performance and lower cost than other open source technologies.
  2. In addition, the authors constructed a more rigorous SWE-bench Lite-S benchmark test to rule out the presence of misleading information, thus providing a basis for more accurate comparisons and evaluations.

### 2. Innovative points
  1. It does not require the use of complex autonomous software agents;
  2. It employs a three-phase solution including localisation, fixing and validation, with clear objectives and processes for each phase;
  3. It uses Natural Language Processing techniques and Text Retrieval techniques for problem localisation and fixing.

### 3. Future Works
Future research can further explore the optimisation and improvement of AGENTLESS, such as how to better use existing natural language processing techniques and text retrieval techniques to improve the accuracy of problem location and repair; how to combine AGENTLESS with other software development problem solving approaches to obtain better results. In addition, the extension of AGENTLESS to other types of software development problems, such as code refactoring, test automation, and other areas, can also be considered. 
