for _ in range(int(input())):
    n,m=map(int,input().split())
    a_str=input()
    count0=a_str.count('0')
    count1=a_str.count('1')
    if count0==0:
        print(1)
        continue

    if count1==0:
        print(n*m)
        continue
    # a_str=a_str*m 
    num=n 
    if m%2==0:
        num*=2 
    else:
        num*=3
    if (a_str.count('1')*m)%2!=0:
        print(0)
        continue
    a_str=a_str*num
    mid=int((num)//2)
    if (num)%2!=0:
        mid+=1
    i,j=mid-1,mid
    iTrue=True
    jTrue=True
    ans=0
    while True:
        if i>=0 and iTrue:
            if a_str[i]=='1':
                iTrue=False
            else:
                ans+=1 
                i-=1
        else:
            iTrue=False
        if j<(n*m) and jTrue:
            if a_str[j]=='1':
                jTrue=False
            else:
                ans+=1 
                j+=1
        else:
            jTrue=False
        if iTrue==False and jTrue==False:
            break
    print(ans+1)
 
