for _ in range(int(input())):
    n=int(input())
    string=input().strip()
    if n==1:
        print("YES")
        continue
    if string.count('1')%2==1:
        print("NO")
        continue
    
    if '11' in string:
        string.replace('11','0')
    
    if '1' in string:
        print("NO")
    else:
        print("YES")