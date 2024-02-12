from collections import defaultdict

words = ["i","love","leetcode","i","love","coding"]
words.sort()
k=2
dct=defaultdict(int)
for w in words:
    dct[w]+=1
ans=list(dct.items())
ans.sort(key= lambda x:x[1],reverse=True)
ans=[x[0] for x in ans]
print(ans[:k])

