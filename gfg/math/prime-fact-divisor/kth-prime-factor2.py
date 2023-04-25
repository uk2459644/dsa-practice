
MAX=10001

def sieveOfEratosthenes(s):
    prime=[False for i in range(MAX+1)]
    # initializing smallest factor equal to 2
    for i in range(2,MAX+1,2):
        s[i]=2
    
    for i in range(3,MAX,2):
        if (prime[i]==False):
            s[i]=i
            for j in range(i,MAX+1,2):
                if j*j > MAX:
                    break
                if prime[i*j]==False:
                    prime[i*j]=True
                    s[i*j]=i