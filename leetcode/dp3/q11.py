
primes=list(map(int,input().split()))
n=len(primes)
super_ugly=[1]
idx=[0]*n
prod=[p for p in primes]
while len(super_ugly)<n:
    next_ugly=min(prod)
    super_ugly.append(next_ugly)
    for i in range(n):
        if next_ugly == prod[i]:
            idx[i]+=1
            prod[i]=primes[i]*super_ugly[idx[i]]

print(primes)
