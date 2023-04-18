# python program to find the element occuring
# odd number of time

def getOddOccureence(arr):
    res=0
    for element in arr:
        res=res^element
    return res