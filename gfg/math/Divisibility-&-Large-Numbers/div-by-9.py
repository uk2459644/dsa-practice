# A number is divisible by 9 if sum of its
# digits is divisible by 9

def check(St):
    # compute sum of digits 
    n=len(St)
    digitSum=0

    for i in range(0,n):
        digitSum+=(int)(St[i])
    
    return (digitSum%9==0)
