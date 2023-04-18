for _ in range(int(input())):
    s,t,d=sorted(list(map(int,input().split())))
    print(max(0,d-t-s))