
ans='abcdefghijklmnopqrstuvwxyz';

for _ in range(int(input())):
    string = input().replace(" ","")
    string=string.lower()
    for a in ans:
        if a not in string:
            print(a)
            break
    else:print('~')
