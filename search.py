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
from util import Stack
from util import Queue

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    
    status = util.Stack()                # We plan to use status to manage which states will expand next
    status.push(problem.getStartState())  # then store the initiate state to this stack
    currNode = status.pop()        # Keep the end node of the status stack out and then as the current state(node)
    
    isVisited = []                    # This is a List where state has already been visited
    goalPath=[]                         # Final direction list
    currentPath = util.Stack()           # This stack is for storing current path which is already visited
    
    while not problem.isGoalState(currNode):
        if currNode not in isVisited:
            isVisited.append(currNode)
            successors = problem.getSuccessors(currNode)
            for child,direction,cost in successors:

                tempPath = goalPath + [direction]
                currentPath.push(tempPath)
                status.push(child)              #This is a really important step between bfs and dfs
                
        currNode = status.pop()
        goalPath = currentPath.pop()
    return goalPath
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    expand = util.Queue()                 #We plan to use exapnd to manage which states will expand next and correspond path
    action = []
    startNode = problem.getStartState()
    expand.push((startNode, action))
    isVisited = []
    while not expand.isEmpty():
        currNode, action = expand.pop()
        if not currNode in isVisited:
            isVisited.append(currNode)
            if problem.isGoalState(currNode):
                return action
            for child, direction, cost in problem.getSuccessors(currNode):
                newAction = action + [direction]
                expand.push((child, newAction))

    return []
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
    priority for each item : actionCost + heuristic
    """
    "*** YOUR CODE HERE ***"
    "list of states that visited"
    visited = []

    priorityQ = util.PriorityQueue()
    path = []
    priorityQ.push( [path, problem.getStartState()], 0 )

    while not priorityQ.isEmpty():
        currentNode = priorityQ.pop()
        currentPath = currentNode[0]
        currentState = currentNode[1]

        """
        return path if we reach the goal
        check at current state instead of inside the loop
        because A* chose lowest cost path which may skip the goal successor
        """
        if problem.isGoalState(currentState):
            return currentPath

        "push all valid successors into priorityQ"
        if currentState not in visited:
            for successorState, successorAction, successorCost in problem.getSuccessors(currentState):
                if successorState not in visited:
                    successorPath = currentPath[:]
                    successorPath.append(successorAction)
                    successorCost = problem.getCostOfActions(successorPath) + heuristic(successorState, problem)
                    priorityQ.push([successorPath, successorState], successorCost)
            visited.append(currentState)

    "return [] if no solution"    
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
