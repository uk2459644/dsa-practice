for _ in range(int(input())):
    n=int(input())
    nli=input().replace(" ","")
    ans=0
    for a in nli:
        count=nli.count(a)
        count_next = 0
        count_prev = 0
        nli.replace(a,"")
        num=int(a)

        if num%2==0:
            next_num = num+1 
            if str(next_num) in nli:
                count_next=(nli.count(str(next_num)))
                nli.replace(str(next_num),"")
            count+=count_next 
            ans=max(ans,count)
        else:
            prev_num=num-1
            if str(prev_num) in nli:
                count_prev = (nli.count(str(prev_num)))
                nli.replace(str(prev_num),"")
            count+=count_prev 
            ans=max(ans,count)
    
    print(n-ans)