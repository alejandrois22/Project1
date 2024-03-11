# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


# Q1 by Alejandro Alberto Isaac Quintanal
def depthFirstSearch(problem: SearchProblem):
    # Stack for LIFO search frontier
    stack = util.Stack()
    
    # Start state
    startState = problem.getStartState()
    
    # Push the start state with an empty path
    stack.push((startState, []))
    
    # Set to keep track of visited nodes
    visited = set()

    while not stack.isEmpty():
        currentState, actions = stack.pop()

        # If this state is the goal, return the actions to get here
        if problem.isGoalState(currentState):
            return actions

        # If not visited, explore successors
        if currentState not in visited:
            visited.add(currentState)  # Mark as visited
            
            # For each successor of the current state
            for nextState, action, _ in problem.getSuccessors(currentState):
                # If not visited, add it to the stack
                if nextState not in visited:
                    # Push the successor state and the path to reach it
                    stack.push((nextState, actions + [action]))
    
    # In case no solution is found
    return []

# Q2 by Alejandro Alberto Isaac Quintanal
def breadthFirstSearch(problem: SearchProblem):
    # Queue for FIFO search frontier
    queue = util.Queue()
    
    # Start state
    startState = problem.getStartState()
    
    # Enqueue the start state with an empty path
    queue.push((startState, []))
    
    # Set to keep track of visited nodes
    visited = set()

    while not queue.isEmpty():
        currentState, actions = queue.pop()

        # If this state is the goal, return the actions to get here
        if problem.isGoalState(currentState):
            return actions

        # If not visited, explore successors
        if currentState not in visited:
            visited.add(currentState)  # Mark as visited
            
            # For each successor of the current state
            for nextState, action, _ in problem.getSuccessors(currentState):
                # If not visited, add it to the queue
                if nextState not in visited:
                    # Enqueue the successor state and the path to reach it
                    queue.push((nextState, actions + [action]))
    
    # In case no solution is found
    return []
# Q3 by Alejandro Alberto Isaac Quintanal
def uniformCostSearch(problem: SearchProblem):
    # Priority queue for UCS
    priorityQueue = util.PriorityQueue()
    
    # Start state
    startState = problem.getStartState()
    
    # Enqueue the start state with an empty path and 0 cost
    priorityQueue.push((startState, [], 0), 0)
    
    # Set to keep track of visited nodes
    visited = set()

    while not priorityQueue.isEmpty():
        currentState, actions, currentCost = priorityQueue.pop()

        # If this state is the goal, return the actions to get here
        if problem.isGoalState(currentState):
            return actions

        # If not visited, explore successors
        if currentState not in visited:
            visited.add(currentState)  # Mark as visited
            
            # For each successor of the current state
            for nextState, action, stepCost in problem.getSuccessors(currentState):
                # Calculate new cumulative cost
                newCost = currentCost + stepCost
                
                # Push the successor state, updated path, and new cost
                priorityQueue.update((nextState, actions + [action], newCost), newCost)
    
    # In case no solution is found
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# Q4 by Alejandro Alberto Isaac Quintanal
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    # Priority Queue for A* search
    priorityQueue = util.PriorityQueue()
    
    # Start state
    startState = problem.getStartState()
    
    # Enqueue the start state with an empty path and 0 cost, priority is heuristic
    priorityQueue.push((startState, [], 0), heuristic(startState, problem))
    
    # Set to keep track of visited nodes
    visited = set()

    while not priorityQueue.isEmpty():
        currentState, actions, currentCost = priorityQueue.pop()

        # If this state is the goal, return the actions to get here
        if problem.isGoalState(currentState):
            return actions

        # If not visited, explore successors
        if currentState not in visited:
            visited.add(currentState)  # Mark as visited
            
            for nextState, action, stepCost in problem.getSuccessors(currentState):
                newCost = currentCost + stepCost
                newPriority = newCost + heuristic(nextState, problem)
                
                if nextState not in visited:
                    priorityQueue.update((nextState, actions + [action], newCost), newPriority)
    
    # In case no solution is found
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
