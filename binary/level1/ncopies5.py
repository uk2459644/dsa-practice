for _ in range(int(input())):
    N,M=map(int,input().split())
    A=input()
    if all([a == "0" for a in A]):
        print(N*M)
    else:
        L = A.count("1")
        K = L * M
        if K % 2 == 0:
            ok, ng = 0, M + 1
            while abs(ok - ng) > 1:
                x = (ok + ng) >> 1
                if x * L <= K // 2:
                    ok = x
                else:
                    ng = x
            ok -= 1
            cur = ok * L
            res = 1 if ok != 0 and cur == K // 2 else 0
            A += A
            for a in A:
                cur += int(a)
                if cur == K // 2:
                    res += 1
            print(res)
        else:
            print(0)