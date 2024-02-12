for _ in range(int(input())):
    n=int(input())
    s=input()
    c0,c1=0,0
    if '0' in s:
        c0=s.count('0')
    if '1' in s:
        c1=s.count('1')
    
    mn=min(c0,c1)
    if mn%2==1:
        print("Zlatan")
    else:
        print("Ramos")
        