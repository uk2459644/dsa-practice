for _ in range(int(input())):
    nstr=input()
    n=len(nstr)
    for i in reversed(range(n)):
        if nstr[i] == '1':
            nstr.pop()
        else:
            break
    n=len(nstr)
    cnt1s=0
    ans=0
    inds=0
    inds=nstr.find('1')
    if (inds==-1) or (inds==(n-1)):
        print(0)
    else:
        cnt1s+=1
        qut=True
        while qut==True:
            temp=nstr.find('1',inds+1,-1)
            if temp==-1:
                diff=n-inds-1
                if diff>0:
                    ans+=((diff+1)*cnt1s)
                qut=False
            elif (temp==(n-1)):
                diff=n-inds-2
                if diff>0:
                    ans+=((diff+1)*cnt1s)
                qut=False
            elif  (inds+1)==temp:
                cnt1s+=1
                inds=temp
                temp=0
            else:
                diff=(temp-inds-1)
                ans+=((diff+1)*cnt1s)
                cnt1s+=1
                inds=temp
                temp=0
        print(ans)
    



