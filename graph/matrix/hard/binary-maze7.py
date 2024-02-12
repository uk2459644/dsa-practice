"""
Shortest path from source to destination such that edge weights along
path are alternatively increasing and decreasing

Given a connected graph with N vertices and M edges. The task is to find
the shortest path from source to the destination vertex such that the difference
between adjacent edge weights in the shortest path change from positive to 
negative and vice versa.

If no such path exists then print -1.

"""
"""
Approach: Here, we need to keep two copies of adjacent lists one for positive
difference and other for negative difference.

"""

