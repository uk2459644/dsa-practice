for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur = []
    ans = 0
    for x in a:
        if len(cur) == 0 or x == cur[-1]: cur.append(x)
        else:
            ans += 1
            cur.pop()
    if len(cur) > 0 and cur[0] == 1:
        ans += len(cur)//3
    print(ans)