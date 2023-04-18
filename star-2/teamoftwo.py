for _ in range(int(input())):
    n=int(input())
    s_li=list()
    solve=False

    for i in range(n):
        li=list(map(int,input().split()))
        li.pop(0)
        s_li.append(li)
    
    for i in range(len(s_li)):
        frst_li=s_li[i]
        if solve:
            break
        for j in range(i+1,len(s_li)):
            second_li=s_li[j]
            if len(set(frst_li+second_li))==5:
                solve=True
                break
    
    if solve:
        print('YES')
    else:
        print('NO')