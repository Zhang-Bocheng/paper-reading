# Efficient Tool Use with Chain-of-Abstraction Reasoning
[paper link](https://arxiv.org/pdf/2401.17464) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a new method called Chain-of-Abstraction (CoA) for training large language models (LLMs) to better utilise tools for multi-step reasoning.         | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method first decodes inference chains by abstracting placeholders and then invokes domain tools to concretise each inference chain. This approach allows LLMs to learn more general reasoning strategies and avoid reasoning delays caused by waiting for tools to respond. In the domains of mathematical reasoning and wiki Q&A, the method outperforms previous chainthinking and augmented tool baselines, improving QA accuracy by an average of about 6% on both in-distribution and out-of-distribution test sets. In addition, LLMs trained with the CoA method also show more efficient tool use, with inference speeds averaging about 1.4 times faster than the base augmented LLM.

### 2. Method Description
The Chain-of-Abstraction (CoA) approach proposed in this paper is a novel question-and-answer system based on pre-trained models. The approach decouples generic reasoning from domain-specific knowledge, thus enabling the pre-trained model to focus on learning general and holistic reasoning strategies without the need to generate instance-specific knowledge for the model parameters. Furthermore, by decoupling generic reasoning from domain-specific knowledge, it is possible to process multiple samples in parallel and start generating the next abstract chain while the tool populates the current chain, thus speeding up the entire inference process.

![image](https://github.com/user-attachments/assets/6cee8ba0-dc1c-40ca-8d69-943b78099880)

### 3. Methodological improvements
The method employs two main steps: firstly, by fine-tuning the pre-trained model to enable it to generate abstract inference chains, such as y1, y2 and y3, etc.; secondly, in a second stage, each inference chain is concretised by replacing the placeholders, e.g., by using a calculator to compute the results or by retrieving the relevant articles from a web search engine. Finally, the question is answered based on the specific chain of reasoning.

### 4. Issues addressed 
This approach addresses the problem of traditional pre-trained models that require a large amount of domain-specific knowledge when faced with complex problems. By decoupling generic reasoning and domain-specific knowledge, the method enables pre-trained models to focus more on learning general and holistic reasoning strategies, thus improving their generalisation ability and adaptability. At the same time, the method implements parallel processing of multiple samples, which further improves the speed of inference.

## Experiments
This paper focuses on experimental results of model training using the Chained Abstraction (CoA) approach in two representative domains (mathematical reasoning and Wikipedia quizzing). Specifically, the paper conducts the following comparison experiments:
  
  Experiments in the domain of mathematical reasoning:

**COMPARISON METHODOLOGY:** Comparison with zero/few sample cues, raw chainthink data, and baseline methods such as Toolformer;
**EXPERIMENTAL RESULTS:** The CoA method performs well on the GSM8K and ASDiv datasets, outperforming all the baseline methods, and also shows good generalisation on extrapolated datasets such as SVAMP and MAWPS;

![image](https://github.com/user-attachments/assets/9b05778a-58ae-48b9-b82e-69a1f9fa77c2)

**CONCLUSION:** The CoA approach improves adaptation to multi-step inference tasks by planning abstract variables and combining them with tool augmentation, while improving the distributional robustness of the model.

![image](https://github.com/user-attachments/assets/9c7c091c-3507-41b8-a2e1-6c1f0dcb13d7)

  Experiments in the Wikipedia Q&A domain:
  
**COMPARISON METHODOLOGY:** Comparison with zero/few sample prompts, raw chained reflection data, and baseline methods such as FireAct;
**EXPERIMENTAL RESULTS:** The CoA method outperforms all baseline methods on the HotpotQA dataset, and outperforms all baseline methods on other Wikipedia Q&A datasets with zero inference;

![image](https://github.com/user-attachments/assets/c7f51bee-d059-4786-8280-8799ffefe11a)

**CONCLUSION**: The CoA approach improves adaptability to multi-step Wikipedia Q&A tasks by planning abstract variables and incorporating tool augmentation, while improving the model's knowledge manipulation accuracy and inference accuracy.

![image](https://github.com/user-attachments/assets/bdfa912f-6f28-487e-80a1-81feb85e95f9)

In addition, human evaluation experiments are conducted in this paper to demonstrate that the CoA method not only eliminates arithmetic errors, but also reduces non-arithmetic related reasoning errors. At the same time, the reasoning efficiency of the CoA method is no less than that of the baseline method and has better scalability.

## Conclusion

### 1. Advantages of the Thesis
  1. The method enables LLMs to be more robust to changes in knowledge distribution by encouraging them to learn to abstract multi-step inference planning, and enables a more efficient pipeline when using tools for inference.
  2. In addition, the method has a simple and effective implementation that was tested on two different tasks and achieved significant performance gains.

### 2. Innovative points
The main innovation of the CoA approach is that it separates the reasoning process of the LLM from the invocation of the tool, enabling the LLM to plan its reasoning without relying on domain-specific knowledge and to generate the final answer by populating the tool with specific knowledge. This approach not only improves the accuracy of reasoning, but also enables more efficient reasoning as CoA can share the reasoning process across multiple examples, thus reducing the waiting time.

### 3. Future Works
  1. It is possible to further explore how CoA can be combined with other techniques, such as self-consistent decoding, to further improve the accuracy and efficiency of reasoning.
  2. In addition, it is also possible to consider how CoA can be applied to other types of reasoning tasks, such as natural language reasoning, visual reasoning, and other areas.    
