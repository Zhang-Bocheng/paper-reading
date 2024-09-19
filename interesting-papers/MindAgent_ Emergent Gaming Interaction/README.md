# MindAgent: Emergent Gaming Interaction
[paper link](https://arxiv.org/pdf/2309.09971) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a new infrastructure called MindAgent for evaluating the planning and coordination capabilities of Large Language Models (LLMs) in game interactions.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The infrastructure utilises existing game frameworks that require coordinators who understand multi-intelligent body systems and cooperate with human players via unfine-tuned appropriate commands with contextual learning and feedback on a small number of prompts. In addition, the authors introduce a new game scenario, CUISINEWORLD, and its associated benchmark tests to assess the efficiency of multi-intelligent body collaboration and the ability to supervise multiple agents playing the game simultaneously. A comprehensive evaluation was performed by computing the collaboration efficiency using a new automated evaluation metric, CoS. Finally, the infrastructure can be customised as a VR version of CUISINEWORLD and applied to the wider ‘Minecraft’ game. It is hoped that these findings will help to understand how such skills can be learnt from large-scale language corpora.

### 2. Method Description 
This paper presents ‘CUISINEWORLD’, a multi-intelligent scheduling and coordination game in a virtual kitchen environment. In this game, a multi-intelligent system needs to manage multiple agents and coordinate their work in order to fulfil as many dish orders as possible. The approach employs a textual interface as the interaction method and separates the tasks from the game engine through a modular design, which allows for the easy addition of additional task types and domains (e.g. text-based game engines, Unity or Minecraft, etc.).

The game's task definition follows previous research work by treating it as a Markov Decision Process (MDP) consisting of a state space S, an action space A, a transfer dynamics T, a reward function R, and a task instruction space G. Although there are multiple agents to coordinate in CUISINEWORLD, the authors adopt a centralised planning scheme and formalise the game as a single fully observable decision problem.

The state space S consists of two entities, locations and agents. For each entity, the game provides a set of descriptive information, and the set of descriptive information of all entities is the return value of the state space S. A location can be a storage area for getting ingredients and discharging waste, a serving counter for finished dishes, or a cooking tool such as a pan, blender, etc. For each location, the game provides up to two descriptions: inside (location, items), which indicates which items are now contained in the location (some ingredients, completed dishes, etc.); and occupy(location), which indicates that the location is in use and cannot be touched, e.g., an activated blender. An agent is an entity that can be dispatched to complete a task, and for each agent the game provides up to three descriptions: at(location, agent), which indicates which location the agent is currently located in; hold(agent, items), which indicates that the agent is holding items in its hands; and occupy(agent), which indicates that the agent is manipulating some tool. for example, cutting fruit, and will not respond to any dispatch commands.

An action in the action space A is a list that contains all dispatch commands. Given N agent entities, a total of N commands need to be generated. The game provides the following five commands:

&emsp;goto(agent, location) to get the agent to move to the specified location;
&emsp;get(agent, location, item), to have the agent get a specific item from the specified location;
&emsp;put(agent, location), put the item in the agent's hand into the specified location;
&emsp;activate(agent, location), if the specified location is a cooking tool, let the agent open it; 
&emsp;noop(agent), let the agent not perform any operation in this round of scheduling.
The scheduler also needs to sequence the scheduling commands correctly in order to avoid confusion that might be caused by multiple agents operating on the same location at the same time.

Tasks and Rewards.Tasks in CUISINEWORLD are orders for a single dish, ranging from the simplest tuna sashimi to the more complex spaghetti with pork, all requiring different cooking tools. Every τint steps (which we call the task interval) during a game round, a new task or dish order is added to the active task list. When a matching dish is placed on the serving table, the task is considered completed and removed from the active task list. Conversely, when a task reaches its lifetime τlft , the task is considered failed and removed from the list. 

![image](https://github.com/user-attachments/assets/aac48860-6b91-4641-8d80-eef366ca04db)

### 3. Methodological improvements
In contrast to the famous video game Overcooked! the implementation of CUISINEWORLD borrows mainly from its spirit, but modifies it while simplifying some of the mechanisms. For example, the authors assume that all agents are entitled to access all locations without having to perform low-level controls. In addition, the authors crawled the rules and recipes on the community-contributed wiki pages, streamlining them and modifying them as necessary to end up with a basic version of CUISINEWORLD, which includes 10 different types of locations (serving counters, storage areas, and 8 different cooking tools), 27 different ingredients, and 33 unique dishes. The dishes are divided into four categories based on difficulty: introductory, easy, intermediate and advanced, with three levels in each category. It's important to note that these recipes, dishes and levels can be easily expanded to allow for more challenging tasks.

## Experiments
This article describes the authors' research on game collaboration, focusing on the efficiency of multi-intelligence cooperation and the ability to collaborate between humans and AI. There are five experiments conducted in the article, which are:

**Experiment 1**: Testing the efficiency of multi-intelligence body collaboration under different task difficulties. The results show that the efficiency of multi-intelligence body collaboration gradually increases with the increase of task difficulty.
**Experiment 2**: Test the effect of multi-intelligent body collaboration on individual intelligences. The results show that multi-intelligent body collaboration can significantly improve the task completion rate of a single intelligent body.
**Experiment 3**: Test the effect of human players collaborating with multiple intelligences. The results show that human players collaborating with multiple intelligences can significantly improve the task completion rate, and that human players find this type of collaboration more interesting.
**Experiment 4**: Test the performance of other language models in multi-intelligent body collaboration. The results show that GPT-4 has better multi-intelligence collaboration ability compared to other language models.
**Experiment 5**: Apply the multi-intelligent body collaboration infrastructure to the Minecraft game and implement human-machine collaboration through voice interaction. The results show that the infrastructure is highly scalable and that voice interaction can further enhance the human-computer collaboration experience.

![image](https://github.com/user-attachments/assets/d760c437-7f2f-4cf2-8ca1-9c026a491ab4)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new infrastructure, MINDAGENT, for interactive multi-intelligent body planning with Large Language Models (LLMs) in a multi-intelligent body virtual kitchen environment. The authors evaluate the multi-intelligent body planning capabilities of LLMs by establishing a new CUISINEWORLD benchmark and conduct extensive experiments using recently introduced LLMs such as GPT-4, Claude and LLAMA.
  
  2. The results show that robust pre-trained LLMs are capable of scheduling and collaborating with multiple agents based on simple game instructions and recipes alone, without any additional hints or optimisations. Furthermore, techniques such as adding a small amount of expert demonstration, explaining the rationale for certain actions, and providing real-time feedback to LLMs can significantly improve their multi-intelligent agent planning performance. 

### 2. Innovative points
The authors also further improve the performance of LLMs for multi-intelligent body planning by introducing some cueing techniques such as providing sample less demonstrations, planning rationale and environmental feedback. This zero-sample learning-based approach has great potential for continuous improvement from data without the need for fine-tuning, and can seamlessly adapt to planning problems from different domains and provide more flexible interfaces.
 
### 3. Future Works
While there are still challenges in using LLMs for multi-intelligence planning compared to traditional domain-specific automated planning systems, such as high computational cost, context length constraints, and non-optimal plans, they have the potential to learn from data without the need for fine-tuning, can be adapted seamlessly to planning problems from different domains, and provide more flexible interfaces. We therefore hope that our findings will help to understand how generic scheduling and coordination skills can be obtained from large text corpora and contribute to the development of better LLM planners.   
