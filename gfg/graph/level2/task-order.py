# Python program to find order to process tasks so that all tasks
# can be finished. This program mainly uses
# kahn's algorithm.

from collections import deque

# returns adjacency list representation of 
# graph from given set of pairs.

def make_graph(numTasks, prerequisites):
    graph = [set() for _ in range(numTasks)]
    for u,v in prerequisites:
        graph[v].add(u)
    
    return graph

# Computes in-degree of every vertex

def compute_indegree(graph):
    indegree=[0]*len(graph)
    for neighbors in graph:
        for neigh in neighbors:
            indegree[neigh]+=1
    
    return indegree

# main function for topological sorting
def findOrder(numTasks, prerequisites):
    graph=make_graph(numTasks,prerequisites)
    indegrees = compute_indegree(graph)
    zeros = deque([i for i,degree in enumerate(indegrees) if degree ==0])

    toposort = []
    while zeros:
        zero = zeros.popleft()
        toposort.append(zero)
        for neigh in graph[zero]:
            indegrees[neigh]-=1
            if indegrees[neigh]==0:
                zeros.append(neigh)
    
    return toposort if len(toposort) == numTasks else []
