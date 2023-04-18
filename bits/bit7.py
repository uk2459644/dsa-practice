# python program to find the even
# occuring elements in given array

def printRepeatingEven(arr,n):
    axor=0
    for i in range(0,n):
        pos=1<<arr[i]
        axor^=pos
    for i in range(0,n-1):
        pos=1<<arr[i]
        if (not(pos&axor)):
            axor^=pos
            