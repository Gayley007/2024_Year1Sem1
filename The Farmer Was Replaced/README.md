# Programming the Farming Drone (Report)

## Introduction
"The Farmer Was Replaced" is a Python coding game that challenges us to automate 
farm management tasks.In this game, we write Python code to replace a fictional 
farmer who has been automated out of his job. Our task is to develop scripts 
to handle typical farming activities such as planting, watering, harvesting, and trading 
crops, all while maximizing profits and managing resources. Each level introduces new 
complexities, requiring us to use programming concepts like loops, conditionals, 
functions, and data handling to solve problems efficiently. The game is designed to be
educational and entertaining, blending programming skills with strategic thinking.

# Table of Contents
- [Code Snippets and Explanation](#code-snippets-and-explanation)
- [Challenges and Learnings](#challenges-and-learnings)
- [References](#references)
# Code-Snippets-and-Explanation
Write and explain your code along with recordings.
## Step 1: Farming on 1 tile
**Code:**
```python
while True:
if can_harvest():
harvest()
```
**Explanation:**
The code runs an infinite number of times and harvest the grass with the if condition.
**Demo:**
Video Demo:
![](./step1_video.mp4)
**Notes**
- Using the code above I was able to get enough hay to unlock the tile
- These features were unlocked too: variables and functions.
## Step 2: Farming on 3x3 tile
**Code:**
```python
while True:
# Code to go around
if can_harvest():
harvest()

```

**Explanation:**
The code makes the drone go one square at a time harvests the grass with the if condition.
**Demo:**
Video Demo:
![](./step2_video.mp4)
**Notes**
- Using the code above I was able to get enough hay to unlock the tile
- These features were unlocked too: variables and functions.
.
.
.
.
.
.
.
.
.
.
# Challenges and Learnings
## Challenges
Discuss any significant challenges you faced while trying to solve the issues in the game.
Discuss any optimization methods you implemented to make the harvesting faster.
## Learnings
Note down what different algorithms and methods of programming you learnt (E.g: Given a number n, I learnt
an algorithm that makes the drone travel each tile one by one efficiently given it’s position)
## References
List any resources, articles, or libraries you used or referenced while working on this project.
1. [Resource 1 Title](URL)
2. [Resource 2 Title](URL)
3. ...