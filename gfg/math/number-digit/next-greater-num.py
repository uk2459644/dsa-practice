"""
If all digits sorted in descending order, then output
is always "Not Possible." 

If all digits are sorted in ascending order, then we
need to swap last two digits.

For other cases, we need to process the number
from rightmost side.

"""


def findNext(number,n):

    for i in range(n-1,0,-1):
        if number[i]>number[i-1]:
            break 
    
    if i==1 and number[i]<=number[i-1]:
        print("Next number not possible")
        return
    
    x=number[i-1]
    smallest = i 
    for j in range(i+1,n):
        if number[j]>x and number[j]<number[smallest]:
            smallest=j
    
    number[smallest],number[i-1]=number[i-1],number[smallest]
    