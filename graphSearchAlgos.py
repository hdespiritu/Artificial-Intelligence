"""
Implementation of graph search algorithms that return a list of actions that reaches the goal
"""

def depthFirstSearch(problem):
    """
    Searches the deepest nodes in the search tree first.

    """
   
    root = Node(problem.getStartState(), None, None, 0)
    #create a fringe and initialize it with the initial state
    fringe = util.Stack()
    fringe.push(root)
    #create a set of explored states to represent the paths taken from the initial space
    #state to the visited space state.
    explored = set()
    while fringe:
        #choose a leaf node and remove it from the frontier
        node = fringe.pop()
        #add the current node's state to the set of explored states
        explored.add(node.state)
        #check if the node is a goal state, if so return it
        if(problem.isGoalState(node.state)):
          return node.path
        #for each successor of the current node make a child node
        successors = problem.getSuccessors(node.state)
        for spaceState, action, actionCost in successors:
            child = Node(spaceState, node, action, actionCost)
            #if the child node space state is not a key explored, then add it to the fringe
            if(child.state not in explored): 
                fringe.push(child)
    

def breadthFirstSearch(problem):
    "Searches the shallowest nodes in the search tree first."

    #inialize the search tree with the initial state
    root = Node(problem.getStartState(), None, None, 0)
    #create a fringe and initialize it with the initial state
    fringe = util.Queue()
    fringe.push(root)
    #create a set of explored states
    explored = set()
    #if the fringe is empty there is no solution(failure)
    while fringe:
        #choose a leaf node and remove it from the frontier
        node = fringe.pop()
        
        #check if the node is a goal state, if so return it
        if(problem.isGoalState(node.state)):
          return node.path

        #add the node to the set of explored states
        explored.add(node.state)
        
        #for each successor of the current node make a child node
        successors = problem.getSuccessors(node.state)
        for spaceState, action, actionCost in successors:
            child = Node(spaceState, node, action, actionCost)
            #if the child node space state is not explored and the child node is not in the fringe, then add it to the fringe
            if(child.state not in explored):
                if(not any(node.state == child.state for node in fringe.list)):
                    #add it to the fringe
                    fringe.push(child)
    

def uniformCostSearch(problem):
    "Searches the node of least total cost first. "
   
    #initialize the search tree with the initial state
    root = Node(problem.getStartState(), None, None, 0)
    #create a fringe and initialize it with the initial state and its cost,0
    fringe = util.PriorityQueue()
    fringe.push(root, root.pathCost)
    #create a set of explored states
    explored = set()
    #if the fringe is empty there is no solution(failure)
    while fringe:
        #choose a leaf node and remove it from the frontier
        node = fringe.pop()
        if(problem.isGoalState(node.state)):
            return node.path
        #add the current node's state to the list of explored states
        explored.add(node.state)
        #for each successor of the current node, make a child node 
        successors = problem.getSuccessors(node.state)
        for spaceState, action, actionCost in successors:
            child = Node(spaceState, node, action, actionCost)
            #if the child node space state is not explored and the child node is not in the fringe, then add it to the fringe
            if(child.state not in explored):
                if(not any(node.state==child.state for pathCost,entryCount,node in fringe.heap)):  
                    fringe.push(child, child.pathCost)
                #if the node is already in the fringe, then replace the node in the fringe with the node that has a cheaper cost 
                if(any(node.state==child.state for pathCost,entryCount,node in fringe.heap)): 
                    pathCost,entryCount,oldChild = filter(lambda (pCost,eCount,node): node.state == child.state, fringe.heap).pop()
                    if(child.pathCost < oldChild.pathCost):
                      fringe.push(child, child.pathCost)
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    
    #initialize the search tree with the initial state
    root = Node(problem.getStartState(), None, None, 0)
    #create a fringe and initialize it with the priority function
    fringe = util.PriorityQueueWithFunction(lambda (x, heurVal): x.pathCost + heurVal)
    fringe.push((root, heuristic(root.state, problem)))
    #create a set of explored states 
    explored = set()
    #if the fringe is empty there is no solution(failure)
    while fringe:
        #choose a leaf node and remove it from the fringe
        node, h_n = fringe.pop()
        if(problem.isGoalState(node.state)):
            return node.path
        #add the current node's state to the list of explored states
        explored.add(node.state)
        #for each successor of the current node make a child node 
        successors = problem.getSuccessors(node.state)
        for spaceState, action, actionCost in successors:
            child = Node(spaceState, node, action, actionCost)
            #if the child node space state is not explored and the child node is not in the fringe, then add it to the fringe
            if((child.state not in explored)and(not any(node.state == child.state for h_n,entryCount,(node,h_n) in fringe.heap))):
                fringe.push((child, heuristic(child.state, problem)))
            #if the node is already in the fringe, then replace the node in the fringe with the node that has a cheaper cost     
            if(any(node.state == child.state for h_n,entryCount,(node,h_n) in fringe.heap)):
                h_n,entryCount,(oldChild,h_n) = filter(lambda (pCost,eCount,(node,h_n)): node.state == child.state, fringe.heap).pop()
                if(child.pathCost < oldChild.pathCost):
                    fringe.push((child, heuristic(child.state, problem)))


