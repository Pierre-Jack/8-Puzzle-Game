# 8-Puzzle-Game 🧩
## Collaborators 👥
- [Armia Joseph: 21010229](https://github.com/Armaritto)
- [Andrew Ashraf: 21010313](https://github.com/AndrewAchraf)
- [Pierre Jack: 21010394](https://github.com/Pierre-Jack)
## Table of Contents 📜
<!-- TOC -->
* [8-Puzzle-Game 🧩](#8-puzzle-game-)
  * [Collaborators 👥](#collaborators-)
  * [Table of Contents 📜](#table-of-contents-)
* [Introduction 🌟](#introduction-)
  * [Problem Statement ❓](#problem-statement-)
* [Algorithms 🔍](#algorithms-)
  * [Breadth First Search (BFS) 🌿](#breadth-first-search-bfs-)
    * [About 📝](#about-)
    * [Properties 📏](#properties-)
    * [Data Structures Used 📂](#data-structures-used-)
    * [Functions  ⚙️](#functions-)
    * [Pseudocode 🧾](#pseudocode-)
    * [Testcases ✅](#testcases-)
  * [Depth First Search (DFS) 🛠️](#depth-first-search-dfs-)
    * [About 📝](#about--1)
    * [Properties 📏](#properties--1)
    * [Data Structures Used 📂](#data-structures-used--1)
    * [Functions  ⚙️](#functions--1)
    * [Pseudocode 🧾](#pseudocode--1)
    * [Testcases ✅](#testcases--1)
  * [Iterative Deepening Search (IDS) 🔄](#iterative-deepening-search-ids-)
    * [About 📝](#about--2)
    * [Properties 📏](#properties--2)
    * [Data Structures Used 📂](#data-structures-used--2)
    * [Functions  ⚙️](#functions--2)
    * [Pseudocode 🧾](#pseudocode--2)
    * [Testcases ✅](#testcases--2)
  * [A Star Algorithm (A*)](#a-star-algorithm-a)
    * [About 📝](#about--3)
    * [Properties 📏](#properties--3)
    * [Data Structures Used 📂](#data-structures-used--3)
    * [Functions  ⚙️](#functions--3)
    * [Pseudocode 🧾](#pseudocode--3)
    * [Testcases ✅](#testcases--3)
      * [Manhattan Heuristic 🇺🇸](#manhattan-heuristic-)
      * [Euclidean Heuristic 📐](#euclidean-heuristic-)
* [Screenshots 📸](#screenshots-)
<!-- TOC -->
# Introduction 🌟
This repository contains the implementation of the 8-puzzle game as a lab of AI course using various search algorithms like Breadth First Search (BFS), Depth First Search (DFS), Iterative Deepening Search (IDS), and A* Algorithm. The 8-puzzle is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing. The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space. The puzzle is solved when all the tiles have been ordered. The 8-puzzle problem is a classic artificial intelligence problem that can be solved with the A* algorithm. The A* algorithm is a search algorithm that finds the shortest path between the initial and final nodes. The algorithm uses a heuristic function to estimate the cost of the shortest path. The 8-puzzle problem can be solved with the A* algorithm by representing the problem as a graph and using the Manhattan distance as the heuristic function. The Manhattan distance is the sum of the horizontal and vertical distances between the current and goal positions of the tiles. The A* algorithm uses the Manhattan distance to estimate the cost of the shortest path and find the optimal solution to the 8-puzzle problem.

## Problem Statement ❓
An instance of the 8-puzzle game consists of a board holding 8 distinct movable tiles, plus
an empty space. For any such board, the empty space may be legally swapped with any tile
horizontally or vertically adjacent to it. In this assignment, the blank space is going to be
represented with the number 0.

Given an initial state of the board, the search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending

order 0,1,2,3,4,5,6,7,8.
The search space is the set of all possible states reachable from the initial state. The blank
space may be swapped with a component in one of the four directions ’Up’, ’Down’, ’Left’,
’Right’, one move at a time. The cost of moving from one configuration of the board to another
is the same and equal to one. Thus, the total cost of the path is equal to the number of moves
made from the initial state to the goal state.


# Algorithms 🔍

## Breadth First Search (BFS) 🌿
### About 📝
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (initial state in 8 puzzle) and explores all possible next states starting from the nearest and growing evenly in all directions. It uses first in first out strategy and hence it is implemented using a queue.
### Properties 📏
- **Completeness:** BFS is complete if the branching factor is finite, which is true in our case
- **Optimality:** BFS is optimal.
- **Time Complexity:** O(b^d).
- **Space Complexity:** O(b^(d+1)).

    where b is the branching factor and d is the depth of the goal node
### Data Structures Used 📂
- Queue (Frontier Data Structure)
- Dictionary (parent_dict - To keep track of parent nodes)
### Functions  ⚙️
- `solve` - Main function to solve the 8 puzzle using DFS
- `Helper.get_children` - Function to get children of a node
### Pseudocode 🧾
```python
initialize queue, parent_dict
push initial state to queue
parent_dict[root] = -1
while queue is not empty
    node = queue.dequeue()
    if node is goal state
        return path
    for each child of node
        if child is not in dict
            add child to queue, add to dict
            parent_dict[child] = node
```
### Testcases ✅
| Initial State | Is Solvable? | Cost | Nodes Expanded | Search Depth | Running Time (ms) |
|:-------------:|:------------:|:----:|:--------------:|:------------:|:-----------------:|
| **125340678** |     Yes      |  3   |       18       |      3       |         0         |
| **803215476** |     Yes      |  23  |     122475     |      23      |        739        |
| **806547231** |     Yes      |  31  |     181439     |      31      |       1197        |
| **123450768** |      No      |  0   |     181440     |      31      |       1296        |
| **621837450** |     Yes      |  22  |     93042      |      22      |        579        |

## Depth First Search (DFS) 🛠️
### About 📝
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (initial state in 8 puzzle) and explores as far as possible along each branch before backtracking. It uses last in first out strategy and hence it is implemented using a stack.
### Properties 📏
- **Completeness:** DFS is not complete as fails in infinite-depth spaces, spaces with loops
  But in our case (8-puzzle) it is complete as the depth is limited.
- **Optimality:** DFS is not optimal as it may not find the shortest path.
- **Time Complexity:** O(b^m).
- **Space Complexity:** O(bm).

  where b is the branching factor and m is the maximum depth of the search tree
### Data Structures Used 📂
- Stack (Frontier Data Structure)
- Set (stack_set - To keep track of visited nodes)
- Set (explore - To keep track of explored nodes)
- Dictionary (parent_dict - To keep track of parent nodes)
### Functions  ⚙️
- `solve` - Main function to solve the 8 puzzle using DFS
- `Helper.get_children` - Function to get children of a node
### Pseudocode 🧾
```python
initialize stack, stack_set, parent_dict, explore_set
set state to initial state, parent_dict[state] to -1

if state is goal state:
    return True, parent_dict, nodes_expanded, max_depth

push (state, 0) to stack, add state to stack_set

while stack is not empty:
    pop (state, level) from stack & add state to explore_set
    update max_depth
    
    if state is goal state:
        return True, parent_dict, nodes_expanded, max_depth
    
    nodes_expanded++
    
    for each child in children of state:
        if child is not in stack_set and child is not in explore_set:
            set parent_dict[child] to state
            push (child, level + 1) to stack
            add state to stack_set

return False, parent_dict, nodes_expanded, max_depth
```
### Testcases ✅
| Initial State | Is Solvable? | Cost  | Nodes Expanded | Search Depth | Running Time (ms) |
|:-------------:|:------------:|:-----:|:--------------:|:------------:|:-----------------:|
| **125340678** |     Yes      |   3   |       3        |      3       |         0         |
| **803215476** |     Yes      | 53341 |     54089      |    53341     |        401        |
| **806547231** |     Yes      | 57299 |     58242      |    57299     |        476        |
| **123450768** |      No      |   0   |     241921     |    102447    |       1831        |
| **621837450** |     Yes      | 24524 |     24723      |    24524     |        250        |

## Iterative Deepening Search (IDS) 🔄

### About 📝
Iterative deepening search (IDS) is a state space/graph search strategy in which a depth-limited search is run repeatedly with increasing depth limits until the goal is found. It combines the benefits of depth-first search and breadth-first search. It is complete and optimal for a tree with a finite depth.
### Properties 📏
- **Completeness:** IDS is complete if the branching factor is finite, which is true in our case
- **Optimality:** IDS is optimal.
- **Time Complexity:** O(b^d).
- **Space Complexity:** O(b^(d+1)).

  where b is the branching factor and d is the goal depth

### Data Structures Used 📂
- Stack (Frontier Data Structure)
- Set (stack_set - To keep track of visited nodes)
- Set (explore_set - To keep track of explored nodes)
- Dictionary (parent_dict - To keep track of parent nodes)
- Dictionary (level_dict - To keep track of depth of nodes)

### Functions  ⚙️
- `solve` - Function that run DLS for increasing depth limits
- `solve_dls` - Function to run Depth Limited Search
- `Helper.get_children` - Function to get children of a node

### Pseudocode 🧾
```python
func solve():
  initialize depth to 0
  initialize nodes_expanded to 0
  
  while depth is less than 32:
    call solve_dls with depth, and assign the results to solvable, m, n
    increment nodes_expanded by n
    if solvable is True:
      return True, m, nodes_expanded
    increment depth by 1
  
  return False, empty dictionary, nodes_expanded
```
```python
func solve_dls(depth):
initialize structures to track explored nodes, parent relationships, and levels

if starting state is the goal:
    return success

add starting state to exploration stack

while there are states to explore:
remove the next state from the stack

if this state is the goal:
return success

if depth limit not reached:
    for each child in children of state:
    if next state is unexplored or has a shorter path:
        Update tracking information
        Add next state to the stack
    else
      get child_level from level_dict, default to 0
      if level + 1 is less than child_level:
        set parent_dict[child] to state
        set level_dict[child] to level + 1
        push (child, level + 1) to stack
        add child to stack_set

return failure
```
### Testcases ✅
| Initial State | Is Solvable? | Cost | Nodes Expanded | Search Depth | Running Time (ms) |
|:-------------:|:------------:|:----:|:--------------:|:------------:|:-----------------:|
| **125340678** |     Yes      |  3   |       8        |      3       |         0         |
| **803215476** |     Yes      |  23  |     411222     |      23      |       3491        |
| **806547231** |     Yes      |  31  |    3633577     |      31      |       29942       |
| **123450768** |      No      |  0   |    4330581     |      0       |       34658       |
| **621837450** |     Yes      |  22  |     255655     |      22      |       2121        |


## A Star Algorithm (A*)
### About 📝
Iterative deepening search (IDS) is a state space/graph search strategy in which a depth-limited search is run repeatedly with increasing depth limits until the goal is found. It combines the benefits of depth-first search and breadth-first search. It is complete and optimal for a tree with a finite depth.
### Properties 📏
- **Completeness:** BFS is complete if the branching factor is finite, which is true in our case
- **Optimality:** BFS is optimal.
- **Time Complexity:** O(b^d).
- **Space Complexity:** O(b^(d+1)).

where b is the branching factor and d is the goal depth

### Data Structures Used 📂
- Stack (Frontier Data Structure)
- Set (stack_set - To keep track of visited nodes)
- Set (explore_set - To keep track of explored nodes)
- Dictionary (parent_dict - To keep track of parent nodes)
- Dictionary (level_dict - To keep track of depth of nodes)

### Functions  ⚙️
- `solve` - Function that run DLS for increasing depth limits
- `solve_dls` - Function to run Depth Limited Search
- `Helper.get_children` - Function to get children of a node

### Pseudocode 🧾
```python
func solve():
  initialize depth to 0
  initialize nodes_expanded to 0
  
  while depth is less than 32:
    call solve_dls with depth, and assign the results to solvable, m, n
    increment nodes_expanded by n
    if solvable is True:
      return True, m, nodes_expanded
    increment depth by 1
  
  return False, empty dictionary, nodes_expanded
```
```python
func solve_dls(depth):
initialize structures to track explored nodes, parent relationships, and levels

if starting state is the goal:
    return success

add starting state to exploration stack

while there are states to explore:
remove the next state from the stack

if this state is the goal:
return success

if depth limit not reached:
    for each child in children of state:
    if next state is unexplored or has a shorter path:
        Update tracking information
        Add next state to the stack
    else
      get child_level from level_dict, default to 0
      if level + 1 is less than child_level:
        set parent_dict[child] to state
        set level_dict[child] to level + 1
        push (child, level + 1) to stack
        add child to stack_set

return failure
```
### Testcases ✅
#### Manhattan Heuristic 🇺🇸

| Initial State | Is Solvable? | Cost | Nodes Expanded | Search Depth | Running Time (ms) |
|:-------------:|:------------:|:----:|:--------------:|:------------:|:-----------------:|
| **125340678** |     Yes      |  3   |       3        |      3       |         0         |
| **803215476** |     Yes      |  23  |      944       |      23      |        79         |
| **806547231** |     Yes      |  31  |      6767      |      31      |        339        |
| **123450768** |      No      |  0   |     18140      |      0       |      135006       |
| **621837450** |     Yes      |  22  |      744       |      22      |        11         |


#### Euclidean Heuristic 📐

| Initial State | Is Solvable? | Cost | Nodes Expanded | Search Depth | Running Time (ms) |
|:-------------:|:------------:|:----:|:--------------:|:------------:|:-----------------:|
| **125340678** |     Yes      |  3   |       3        |      3       |         0         |
| **803215476** |     Yes      |  23  |      1558      |      23      |        111        |
| **806547231** |     Yes      |  31  |     37351      |      31      |       7450        |
| **123450768** |      No      |  0   |     181440     |      0       |       29491       |
| **621837450** |     Yes      |  22  |      1423      |      22      |        31         |

# Screenshots 📸
![Screenshot from 2024-10-28 23-19-30.png](assets/Screenshot%20from%202024-10-28%2023-19-30.png)
![Screenshot from 2024-10-28 23-19-43.png](assets/Screenshot%20from%202024-10-28%2023-19-43.png)
![Screenshot from 2024-10-28 23-19-46.png](assets/Screenshot%20from%202024-10-28%2023-19-46.png)
![Screenshot from 2024-10-28 23-20-01.png](assets/Screenshot%20from%202024-10-28%2023-20-01.png)
![Screenshot from 2024-10-28 23-20-08.png](assets/Screenshot%20from%202024-10-28%2023-20-08.png)
![Screenshot from 2024-10-28 23-20-19.png](assets/Screenshot%20from%202024-10-28%2023-20-19.png)