from collections import defaultdict

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

f=lambda x: "".join("$" if ch in "aeiou" else ch for ch in x)

cap,vow=defaultdict(str),defaultdict(str)

word_Set,ans=set(wordlist),[]

for w in wordlist:
    wLow=w.lower()
    if not cap[wLow]:
        cap[wLow]=w
    wVow=f(wLow)
    if not vow[wVow]:
        vow[wVow]=w

for q in queries:
    qLow,qVow,res=q.lower(),f(q.lower()),""
    if q in word_Set:
        res=q
    elif qLow in cap:
        res=cap[qLow]
    elif qVow in vow:
        res=vow[qVow]
    
    ans.append(res)

print(ans)



