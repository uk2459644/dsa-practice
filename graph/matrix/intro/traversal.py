
from time import perf_counter

MAX=1000

arr=[[0 for i in range(MAX)] for i in range(MAX)]

def rowMajor():
    global arr
    for i in range(MAX):
        for j in range(MAX):
            arr[i][j]+=1 

def colMajor():
    global arr

    for i in range(MAX):
        for j in range(MAX):
            arr[j][i]+=1 
            

