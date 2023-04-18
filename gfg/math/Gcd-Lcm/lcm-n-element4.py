"""
Method 4: Using Euclidean algorithm

The function starts by initializinng the lcm
variable to the first element in the array. It then iterates through the 
rest of the array, and for each element using the Euclidean algorithm. The 
calculated GCD is stored in the gcd variable.

Once the gcd is calculated, the LCM is updated by multiplying the current
lcm with the element and dividing by the GCD.
"""
def lcm_of_array(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        num1 = lcm
        num2 = arr[i]
        gcd=1 
        while num2!=0:
            temp=num2
            num2=num1%num2
            num1 = temp
        gcd=num1

        lcm=(lcm*arr[i])//gcd
    return lcm
