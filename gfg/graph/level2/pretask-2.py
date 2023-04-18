# a bfs solution to check if we can finish
# all tasks or not. 

# class to store dependencies as a pair

class pair:
    def __init__(self,first,second) -> None:
        self.first = first
        self.second = second

# Returns adjacency list representation from a list
# of pairs

def make_graph(numTasks, prerequisites):
    graph=[]
    for i in range(numTasks):
        graph.append([])

    for pre in prerequisites:
        graph[pre.second].append(pre.first)
    
    return graph

# find in-degree of every vertex
def compute_indegree(graph):
    degrees = [0]*len(graph)

    for neighbors in graph:
        for neigh in neighbors:
            degrees[neigh]+=1
    return degrees

# main finish to check whether possible to finish
# all tasks or not

def canFinish(numTasks, prerequisites):
    graph= make_graph(numTasks, prerequisites)
    degrees = compute_indegree(graph)

    for i in range(numTasks):
        j=0
        while(j<numTasks):
            if (degrees[j]==0):
                break
            j+=1
        if (j==numTasks):
            return False
        
        degrees[j]=-1
        for neigh in graph[j]:
            degrees[neigh]-=1
    return True