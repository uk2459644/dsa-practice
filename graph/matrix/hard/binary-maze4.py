"""
Steps were taken to solve the problem:

1. Run three nested loops for i=0,j=0,k=0 to i<n,j<n,k<n respectively, and follow below 
mentioned steps under the scope of loop:
- Calculate time[i][j] as the minimum of mat[i][j] and (mat[i][k]+mat[k][j])

2. Run a loop from i=0 to M and do the following:
- Create three variables S, IN and D and initialize them equal to S[i],
I[i] and D[i] respectively.

- Output the value of mat[S][IN]+mat[IN][D] and mat[S][IN]+mat[IN][D]-mat[S][D]

"""
import sys 
import math

n=4

# matrix holding time such that time[i][j]
# denotes time taken to reach from i to j city

time=[[0,2,1,4],
      [1,0,4,1],
      [3,1,0,3],[1,1,1,0]]
# number of queries 
m=2

# array containing number of city as source, destination, and intermediate
source=[1,0]
intermediate=[2,2]
destination=[3,1]

# nested loop for all pair shortest paths from i city to j city having shortest
# intermediate city k

for k in range(n):
    for i in range(n):
        for j in range(n):
            time[i][j]=min(time[i][j],time[i][k]+time[k][j])

# loop for number of queries
for i in range(m):
    # variables containing source, intermediate and destination cities for per
    # query
    s=source[i]
    in_=intermediate[i]
    d=destination[i]

    # time taken if source to destination reached with intermediate city
    with_intermediate =  time[s][in_]+time[in_][d]
    # time taken if source to destination reached without intermediate city
    without_intermediate=with_intermediate-time[s][d]
    # printing the output
    print(with_intermediate,without_intermediate)
    

