from collections import defaultdict
strs=["eat","tea","tan","ate","nat","bat"]
dc=defaultdict(list)
for s in strs:
    key="".join(sorted(s))
    dc[key].append(s)

print(list(dc.values()))
