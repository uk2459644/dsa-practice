for _ in range(int(input())):
    k,a,b=map(int,input().split())
    nm=int(abs(b-a))
    if k%2==0 and nm==(k//2):
        a=nm-1
        b=k-(a+2)
        print(min(a,b))