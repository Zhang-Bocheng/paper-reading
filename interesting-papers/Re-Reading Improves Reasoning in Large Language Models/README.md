# Re-Reading Improves Reasoning in Large Language Models
[paper link](https://arxiv.org/pdf/2309.06275) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method called RE2 that aims to improve the reasoning of large language models (LLMs).           |  large language models (LLMs)        |

## Methodology

### 1. Abstract
Unlike most heuristic prompting methods, RE2 focuses on the input and enhances the comprehension process by processing the question twice. This approach is highly general and compatible, and can be effectively integrated into different LLMs, heuristic prompts, and integration strategies. The authors validate the effectiveness and generality of RE2 in extensive inference benchmarking on 14 datasets and find that it can consistently improve the inference performance of LLMs through a simple re-reading strategy. Further analyses show that RE2 is adaptable and can be effectively integrated into different LLMs, heuristic hints and integration strategies.

### 2. Method Description 
This paper proposes a Chain-of-Thought-based reasoning model and combine it with hinting techniques for solving various types of reasoning tasks. The basic idea of the model is to decompose a complex problem into a series of smaller manageable reasoning steps, each of which acts as a part of the overall solution. By using chain thinking and hinting techniques, the model can progressively make sense of the inputs and generate plausible answers.

### 3. Methodological improvements
This paper also introduce a ‘re-reading’ (RE2) strategy to improve the model's comprehension. This strategy draws on the idea of human reading strategies, i.e., reading again after the first reading to better understand the text. By applying RE2 to the prompting process, the model can understand the input more deeply and produce more accurate answers.

### 4. Issues addressed 
The models and strategies proposed in this paper can be used to solve various types of reasoning tasks, including but not limited to natural language reasoning, mathematical reasoning, and scientific reasoning. In addition, due to its simplicity and generality, the model can be seamlessly integrated with other cueing techniques and algorithms, such as sample less settings, self-consistency, and so on. Therefore, the model has a wide range of applications.

## Experiments
This paper focuses on the performance of a model-adaptive guided reasoning (RE2) based strategy on different types of natural language processing tasks and compares it with two base cueing methods. Specifically, the authors use the following three categories of reasoning benchmark tests:

**Mathematical Reasoning Benchmark Tests:** seven mathematical reasoning benchmark tests including GSM8K, SVAMP, AS-DIV, AQuA, AddSub, MultiArith and SingelEQ were included.
![image](https://github.com/user-attachments/assets/04687046-2b89-4b8f-951f-7ea230948827)

**Common Sense and Symbolic Reasoning Benchmarks:** Three Common Sense and Symbolic Reasoning Benchmarks including CSQA, StrategyQA and ARC-t/ARC-c.
**Target Recognition Benchmark Tests:** The Date Understanding task of Suzgun et al. (2023a) and the Coinflip task of Wei et al. (2022b) were included.

![image](https://github.com/user-attachments/assets/aac67212-d0fa-45a8-923c-a3541b2db928)

The authors used two powerful backbones: ChatGPT (gpt-3.5-turbo-0613) and davinci-003 (text-davinci-003), and two basic cueing methods: Vanilla and CoT. They then applied the RE2 strategy to these two basic cueing methods to get two new cueing methods, Vanilla+RE2 and CoT+RE2. To avoid the interference of randomness, the authors evaluated their methods mainly in a zero-sample setting.

For each task, the authors designed answer formatting instructions to standardise the structure of the final answer to facilitate accurate answer extraction. Detailed information on baseline hints, RE2 hints, and answer formatting instructions can be found in Appendix B of the paper.

![image](https://github.com/user-attachments/assets/e4b3dc08-231c-4b64-ac31-eb020867daf8)

The authors present the results in Tables 1 and 2. In almost all cases, the LLM with RE2 achieved consistent improvements on both LLMs (davinci-003 and ChatGPT) and both baseline hinting methods (Vanilla and CoT). Specifically, davinci-003 in combination with Vanilla+RE2 showed average improvement rates of 3.81, 2.51, and 1.85 in arithmetic, general knowledge, and symbolic tasks, respectively. By applying RE2, davinci-003 in combination with CoT+RE2 showed further improvement with mean rates of 2.22, 1.23 and 5.25 in the same categories, respectively. These results suggest that RE2 can help LLMs generate answers directly and improve the CoT's ability to elicit correct answers to questions from LLMs.

When applied to ChatGPT, RE2 shows consistent improvements on most datasets, except for a slight decrease on some datasets, such as AQUA and MultiArith, when using Vanilla+RE2. This exception may be due to the fact that ChatGPT has CoT outputs for these datasets that have been exposed during training. In this case, additional explicit instructions, such as CoT or RE2, may disrupt the patterns learnt by ChatGPT, possibly leading to performance degradation. 

Nevertheless, on some datasets such as SVAMP, CSQA, and Date, RE2 is still able to improve the basic cue Vanilla; moreover, on datasets where CoT indication is usually superior to Vanilla indication (e.g., GSM, StrategyQA, and Coin), RE2 significantly enhances Vanilla indication (4.63% rise on StrategyQA and 4.63% rise on Coin). on StrategyQA and 5.20 on the Coin dataset). Overall, our RE2 approach still achieves a 71% experimental improvement on ChatGPT. More examples from the experimental results can be found in Appendix E of the paper.

![image](https://github.com/user-attachments/assets/de609958-d669-4a45-99e9-6c9e37e5ba13)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a simple and effective cueing method, RE2, for enhancing the reasoning capabilities of LLM.
  2. By repetitively reading questions, RE2 can help the model to better understand the input and improve performance in a variety of task settings.
  3. The authors conducted extensive and in-depth experiments to validate the effectiveness and generalisability of RE2 and compared it with other prompting methods.
  4. The results show that RE2 can be used independently of other methods of stimulating thought and on many types of pre-trained models, including non-IFT models.
 
### 2. Innovative points
  1. RE2 is a simple but effective method for enhancing model comprehension through repeated reading of questions.
  2. RE2 differs from existing methods for stimulating thinking by emphasising a focus on input rather than generating answers.
  3. RE2 has broad applicability and can be used on different task settings and pre-trained model types. 

### 3. Future Works
  1. The authors plan to further explore the application of RE2 in other domains such as multi-round dialogue and multimodal reasoning.
  2. Future research will involve more theoretical analyses to provide a more solid foundation.
  3. Further research and improvements are needed to address issues such as the reduced efficiency that may be caused by RE2. 
