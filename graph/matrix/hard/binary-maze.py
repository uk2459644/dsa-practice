"""
Shortest path in a Binary Maze

Given an MxN matrix where each element can either be 0 or 1. We need to 
find the shortest path between a given source cell to destination cell.
The path can only be created out of a cell if its value is 1.

"""
"""
Method 1: Using Backtracking

1. Start from the given source cell in the matrix and explore all four possible
   paths.
2. Check if the destination is reached or not.
3. Explore all paths and backtrack if the destination is not reached.
4. And also keep track of visited cells using an array.

Valid moves are:
left: (i,j)----> (i,j-1)
right: (i,j)---->(i,j+1)
top: (i,j)---->(i-1,j)
bottom:(i,j)---->(i+1,j)

"""

import sys 

class Pair:
    def __init__(self,x,y) -> None:
        self.first=x
        self.second=y

# Check if it is possible to go to (x,y) from the current position.
# The function returns false if the cell has value 0 or already visited

def isSafe(mat,visited,x,y):
    return (x>=0 and x<len(mat) and y>=0 and y<len(mat[0]) and mat[x][y]==1 and (not visited[x][y]))

def findShortestPath(mat,visited,i,j,x,y,min_dist,dist):
    if (i==x and j==y):
        min_dist=min(dist,min_dist)
        return min_dist
    
    # set i,j cell as visited
    visited[i][j]=True
    # go to the bottom cell
    if (isSafe(mat,visited,i+1,j)):
        min_dist=findShortestPath(mat,visited,i+1,j,x,y,min_dist,dist+1)
    # go to the right cell
    if (isSafe(mat, visited, i, j + 1)):
        min_dist = findShortestPath(
            mat, visited, i, j + 1, x, y, min_dist, dist + 1)
 
    # go to the top cell
    if (isSafe(mat, visited, i - 1, j)):
        min_dist = findShortestPath(
            mat, visited, i - 1, j, x, y, min_dist, dist + 1)
 
    # go to the left cell
    if (isSafe(mat, visited, i, j - 1)):
        min_dist = findShortestPath(
            mat, visited, i, j - 1, x, y, min_dist, dist + 1)
 
    # backtrack: remove (i, j) from the visited matrix
    visited[i][j] = False
    return min_dist


