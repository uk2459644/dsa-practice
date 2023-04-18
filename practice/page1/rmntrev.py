for _ in range(int(input())):
    n,k=map(int,input().split())
    srt=input()
    kstr=srt[:k]
    lst_str=srt[k:]
    oprn_lst=[' ']*(n+1)
    odd=False
    if k%2==1:
        odd=True
    nm=k//2
    k-=1
    cnt=0
    fin_ind=0
    for i in range(nm):
        oprn_lst[n-cnt]=kstr[i]
        oprn_lst[n-cnt-1]=kstr[k-i]
        cnt+=2 
        fin_ind+=1 
    if odd:
        oprn_lst[0]=kstr[fin_ind]
    print("".join(oprn_lst).replace(" ","")+lst_str)
