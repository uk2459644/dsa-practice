
def kthdigit(a,b,k):
    p=a**b
    count=0

    while (p>0 and count<k):
        rem=p%10 
        count+=1

        if count==k:
            return rem
        
        p=p/10 

