n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    c=input()
    ones,d,e = c.count('1'),0,0
    if ones == 0:
        print(a*b)
    elif ones*b%2 == 1:
        print(0)
    elif b%2 == 0:
        i=0
        while i<a:
            if c[i]=='1':
                break
            d+=1
            i+=1 
        j=a-1
        while j>=0:
            if c[j]=='1':
                break
            d+=1 
            j-=1
        print(d+1)
    else:
        i=0
        while i<a:
            if c[i]=='1':
                e+=1
            if e==ones/2:
                d+=1
            i+=1 
        print(d)