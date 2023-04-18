for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    srtli=list()
    srtli+=nli
    srtli.sort()
    pli=list()
    qli=list()
    ind_srt=0
    for a in nli:
        if srtli[ind_srt]==a:
            pli.append(a)
            ind_srt+=1
        else:
            qli.append(a)
    pq=pli+qli
    if srtli==pq:
        print('YES')
    else:
        print('NO')
   