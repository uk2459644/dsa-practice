class Pair:
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second

# Returns adjacency list representation from a list
# of pairs

def make_graph(numTasks,prerequisites):
    graph=[]
    for i in range(numTasks):
        graph.append([])
    for pre in prerequisites:
        graph[pre.second].append(pre.first)
    
    return graph

# a dfs function to check if there is a cycle in the
# directed graph

def dfs_cycle(graph,node,onpath,visited):
    if visited[node]:
        return False
    onpath[node]=visited[node]=True
    for neigh in graph[node]:
        if (onpath[neigh] or dfs_cycle(graph,neigh,onpath,visited)):
            return True
    return False

# main function to check whether possible to finish
# all tasks or not

def canFinish(numTasks,prerequisites):
    graph=make_graph(numTasks,prerequisites)
    onpath=[False]*numTasks
    visited=[False]*numTasks
    for i in range(numTasks):
        if (not visited[i] and dfs_cycle(graph,i,onpath,visited)):
            return False
    return True

# a bfs based solution to check if we can finish
# all tasks or not . This solution is mainly based
# on kahn's algorithm

# class to store dependencies as a pair

class pair:
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second

# Returns adjacency list representation from a 
# list of pairs

def make_graph(numTasks,prerequisites):
    graph=[]
    for i in range(numTasks):
        graph.append([])
    
    for pre in prerequisites:
        graph[pre.second].append(pre.first)
    
    return graph

# first in-degree of every vertex
def compute_indegree(graph):
    degrees=[0]*len(graph)
    for neighbors in graph:
        for neigh in neighbors:
            degrees[neigh]+=1
    return degrees

# main function to check whether possible to finish all tasks
# or not
def canFinish(numTasks,prerequisites):
    graph=make_graph(numTasks,prerequisites)
    degrees=compute_indegree(graph)

    for i in range(numTasks):
        j=0
        while (j<numTasks):
            if (degrees[j]==0):
                break
            j+=1
        if (j==numTasks):
            return False
        degrees[j]=-1
        for neigh in graph[j]:
            degrees[neigh]-=1 
    
    return True
    