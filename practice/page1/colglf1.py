from sys import stdin

input=stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    fli=list(map(int,input().split()))
    cli=list(map(int,input().split()))
    lst=list()
    lst.append([0,1])
    for a in fli:
        lst.append([a,1])
    for b in cli:
        lst.append([b,2])
    lst.sort()
    cnt=0
    for i in range(1,len(lst)):
        if (lst[i][1]!=lst[i-1][1]):
            cnt+=1
    print(cnt)