for _ in range(int(input())):
    n,m=map(int,input().split())
    stn_li=list(map(int,input().split()))
    destn_li=list(map(int,input()))
    reach_time=list()
    ans_li=list()
    for i in destn_li:
        list1=stn_li[:i]
        list1.reverse()
        list2=stn_li[i-1:]
        time1=-1
        time2=-1
        if 1 in list1:
            time1=list1.index(1)
        
        if 2 in list2:
            time2=list2.index(2)
        
        if (time1!=-1) and (time2!=-1):
            ans_li.append(min(time2,time1))
            # print(min(time2,time1))
        elif (time1==-1) and (time2==-1):
            ans_li.append(-1)
            # print(-1)
        elif time2==-1:
            ans_li.append(time1)
            # print(time1)
        else:
            ans_li.append(time2)
            # print(time2)
    
    print(*ans_li)
