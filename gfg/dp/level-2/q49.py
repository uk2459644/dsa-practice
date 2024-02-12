# A Dynamic programming based implementation to count
# decodings 

# A Dynamic programming based function to count decodings

def countDecodingDP(digits,n):
    # A table to store results of subproblems
    count=[0]*(n+1)

    count[0]=1
    count[1]=1

    for i in range(2,n+1):
        count[i]=0

    # If the last digit is not 0, then last
    # digit must add to the number of words
    if (digits[i-1]>'0'):
        count[i]=count[i-1]
    
    # IF second last digit is smaller than 2 and last digit is smaller
    # than 7, than last tow digits form a valid characters

    if (digits[i-2]=='1' or (digits[i-2]=='2' and digits[i-1]<'7')):
        count[i]+=count[i-2]

    return count[n]

   


