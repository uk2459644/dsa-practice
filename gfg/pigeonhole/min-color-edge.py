"""
Given a directed graph with V vertices and E edges without self-loops
and multiple edges, the task is to find the minimum number of colors required
such that edges of the same color do not form cycle and also find the colors
for every edge.

"""
"""
Approach: The idea is to find the cycle in the graph, 
which can be done with the help of DFS for the graph in which, when a node
which is already visited is visited again with a new edge, then that edge is
colored with another color else if there is no cycle then all edges can be colored
with only one color.

Algorithm: 
- Mark every edges with color 1 and vertices as unvisited.
- Traverse the graph using the DFS Traversal for the graph and mark the 
  nodes visited.

-  when a node which is visited already, then the edge connecting the vertex
  is marked to be colored with color 2. 

- Print the colors of the edges when all the vertices are visited.

"""

