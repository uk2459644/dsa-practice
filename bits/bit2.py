# python program to generate n-bit gray codes
import math as mt

# this function generate all n bit gray codes
# and prints the generated codes
def generateGrayarr(n):
    if (n<=0):
        return
    arr=list()
    # start with one bit pattern
    arr.append("0")
    arr.append("1")
    i=2
    j=0
    while(True):
        if i>=1<<n:
            break
        # enter the previously generated codes
        # again in arr[] in reverse order.
        # now or arr[] has double number of codes
        for j in range(i-1,-1,-1):
            arr.append(arr[j])
        # append 0 to the first half
        for j in range(i):
            arr[j]="0"+arr[j]
        for j in range(i,2*i):
            arr[j]="1"+arr[j]
        i<<=1
    for i in range(len(arr)):
        print(arr[i])

# program to generate n-bit gray code
def generateGray(n):
    if (n<=0):
        return ["0"]
    if (n==1):
        return ["0","1"]
    recAns=generateGray(n-1)
    mainAns=[]
    for i in range(len(recAns)):
        s=recAns[i]
        mainAns.append("0"+s)
    
    for i in range(len(recAns)-1,-1,-1):
        s=recAns[i]
        mainAns.append("1"+s)
    return mainAns

#  bitwise program to generate gray code 
def GreyCode(n):
    for i in range(1<<n):
        # generate the decimal values
        # using of gray code then using bitset
        # to convert them to binary form
        val=(i^(i>>1))
        s=bin(val)[2::]
        print(s.zfill(n),end=" ")
        