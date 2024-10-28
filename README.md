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
A* is an Informed Search algorithm that finds the path with minimum cost to goal by selecting the next state n to be expanded by finding the state whose sum of:
- **G(n):** The cost to reach state n from initial state.
- **H(n):** A heuristic function that estimates how close state n is to the goal state.
is minimum

### Properties 📏
- **Completeness:** A* is a complete algorithm that always finds a path to the goal state, if there exists one.
- **Optimality:** A* is optimal, it always finds the path with minimum cost.
- **Time Complexity:** O(b^d / log n).
- **Space Complexity:** O(O(b^d)).

where b is the branching factor, d is the goal depth, and n is the maximum number of elements placed in the heap.

### Data Structures Used 📂
- Heap Queue (Priority Queue) to implement the Frontier.
- AStarState Data Structure to store the state, its g(n), h(n) and f(n) values, where f(n) = g(n) + h(n)
- Dictionary (parent_dict - To keep track of parent nodes)
- Dictionary (state_costs - To keep track of the minimum cost found for each state)
- Set (explored - To keep track of explored nodes)
- Set (states_in_frontier - To keep track of all the states present in the Frontier, regardless of their order)

### Functions  ⚙️
- `solve` - Function that runs A* Algorithm for the passed initial state
- `manhattan_distance` - Function to compute the Manhattan Distance heuristic of the passed state for all points except 0
- `euclidean_distance` - Function to compute the Euclidean Distance heuristic of the passed state for all points except 0
- `state_heuristic` - Function the heuristic value of the state based on the heuristic chosen by the user (manhattan/ euclidean)
- `Helper.get_children` - Function to get children of a node

### Pseudocode 🧾
```python
func solve():
create empty list named frontier
create empty dictionary named parent_dict
create empty dictionary named state_costs
create empty set named explored
create empty set named states_in_frontier
set nodes_expanded to 0
set state to initial state

parent_dict[state] = -1

if state is equal to goal state:
    return True, parent_dict, nodes_expanded

create initial_state as AStarState with state, 0, state_heuristic(state, self.heuristic)
add initial_state to frontier
heapify frontier
add state to states_in_frontier
set state_costs[state] to initial_state.f

while frontier is not empty:
    current_state = get and remove the lowest f-value state from frontier
    remove current_state.state from states_in_frontier
    
    if current_state.state is equal to goal state:
        return True, parent_dict, nodes_expanded
    
    add current_state.state to explored
    increment nodes_expanded by 1
    
    for each child in get_children(current_state.state):
        if child is not in explored and child is not in states_in_frontier:
            set parent_dict[child] to current_state.state
            create child_state as AStarState with child, current_state.g + 1, state_heuristic(child, self.heuristic)
            push child_state to frontier
            add child to states_in_frontier
            set state_costs[child] to child_state.f
            
        else if child is in states_in_frontier:
            calculate potential_g as current_state.g + 1
            calculate potential_h as state_heuristic(child, self.heuristic)
            
            if state_costs[child] > potential_g + potential_h:
                update frontier by removing all states with child and their g and h values
                set state_costs[child] to potential_g + potential_h
                set parent_dict[child] to current_state.state
                push AStarState with child, potential_g, potential_h to frontier

return False, parent_dict, nodes_expanded
```
```python
func manhattan_distance(state):
s = convert state to string
    if length of s < 9:
        s = "0" + s
    m_distance = 0
    for i from 0 to 8:
        if s[i] is not "0":
            x = i mod 3
            y = i // 3
            x_goal = convert s[i] to integer mod 3
            y_goal = convert s[i] to integer // 3
            m_distance = m_distance + abs(x - x_goal) + abs(y - y_goal)
    return m_distance
```
```python
func euclidean_distance(state):
s = convert state to string
    if length of s < 9:
        s = "0" + s
    e_distance = 0
    for i from 0 to 8:
        if s[i] is not "0":
            x = i mod 3
            y = i // 3
            x_goal = convert s[i] to integer mod 3
            y_goal = convert s[i] to integer // 3
            e_distance = e_distance + sqrt((x - x_goal)**2 + (y - y_goal)**2)
    return e_distance
```
```python
func state_heuristic(state, heuristic):
    if heuristic = 0:
        return manhattan_distance(state)
    else if heuristic = 1:
        return euclidean_distance(state)
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