# python program to check whether we can finish all
# tasks or not from given dependencies

# class to store dependencies as a pair

class pair:
    def __init__(self,first,second) -> None:
        self.first = first
        self.second = second

# Returns adjacency list representation from a list
# of pairs

def make_graph(numTasks, prerequisites):
    graph = []
    for i in range(numTasks):
        graph.append([])
    
    for pre in prerequisites:
        graph[pre.second].append(pre.first)
    
    return graph

def dfs_cycle(graph, node, onpath, visited):
    if visited[node]:
        return False
    
    onpath[node]=visited[node]=True
    for neigh in graph[node]:
        if (onpath[neigh] or dfs_cycle(graph,neigh,onpath,visited)):
            return True
    return False


