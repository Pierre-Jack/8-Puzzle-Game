from collections import deque

def get_children(state):  #missing number is 0
     children = []
     s = str(state)
     if(len(s) < 9): s = "0" + s
     i = s.find("0")

     for j in [-3, -1, 1, 3]:
          ns = list(s)
          
          if(0 <= i+j and i+j < 9):
            if not (j == -1 and i%3 == 0):
               if not (j == 1 and i%3 == 2):
                tmp = ns[i]
                ns[i] = ns[i+j]
                ns[i+j] = tmp
                children.append(int("".join(ns)))
     return children
    
def solve_bfs(initial):   #missing number is 0 #
    q = deque()
    goal = 12345678
    #s = set()
    d = dict()
    state = initial

    d[state] = -1
    if(state == goal):
         return True, d
    q.append(state)
    
    while q:
        for child in get_children(state):
            if not child in d:
                d[child] = state
                if child == goal: return True, d
                q.append(child)
        state = q.popleft()
    return False, d

def get_path(parent_dict):  #gets the path from the dict of states -- (node, parent) is stored as (key, value) in the dict
    path = deque()
    node = 12345678
    while node != -1:
         path.appendleft(node)
         node = parent_dict[node]
    path = list(path)
    return path

def get_direction(state1, state2):
        val = {-3: "UP", -1: "LEFT", 1: "RIGHT", 3: "DOWN",}
        s = str(state1)
        if(len(s) < 9): s = "0" + s
        i = s.find("0")

        for j in [-3, -1, 1, 3]:
            ns = list(s)
            if(0 <= i+j and i+j < 9):
                if not (j == -1 and i%3 == 0):
                    if not (j == 1 and i%3 == 2):
                        tmp = ns[i]
                        ns[i] = ns[i+j]
                        ns[i+j] = tmp
                        if state2 == (int("".join(ns))):
                            return val[j]
             
def get_directions(path):
    directions = []
    for i in range(len(path)-1):
        directions.append(get_direction(path[i], path[i+1]))
    return directions

     
     
     


         

init = 603247851

  

solvable, map = solve_bfs(init)
print (solvable) 
if solvable:
    print(get_directions(get_path(map)))



