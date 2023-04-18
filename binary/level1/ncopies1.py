for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    c_1=s.count('1')
    c=0
    if c_1==0:
        print(n*m)
    elif (c_1*m)%2==1:
        print(0)
    elif m%2 ==0:
        for i in range(n):
            if s[i]=='0':
                c+=1 
            else:
                break
        for i in reversed(range(n)):
            if s[i]=='0':
                c+=1 
            else:
                break
        print(c+1)
    else:
        summ=0
        for i in range(n):
            if s[i]=='1':
                summ+=1 
            if summ == int(c_1/2):
                c+=1 
        print(c)
            