for _ in range(int(input())):
    n=int(input())
    bstr=input()
    astr=bstr
    num=1
    count=1
    for b in bstr:
        if b==" ":
            continue
        elif int(b) >n:
            print(-1)
            break
        elif int(b)>0 and int(b)<=n:
            bstr=bstr.replace(b,' ',int(b))
            astr=astr.replace(b,str(num),int(b))
            count+=1
            num=count
    print(astr)


