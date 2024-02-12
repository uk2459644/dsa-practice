from collections import defaultdict

edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
n = 7
graph = defaultdict(list)

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = set()


def dfs(node, arr):
    visited.add(node)
    arr+=1
    for v in graph[node]:
        if v not in visited:
            arr=dfs(v, arr)

    return arr


ans_li = list()

for i in range(n):
    if i not in visited:
        a = dfs(i, 0)
        ans_li.append(a)

print(ans_li)

# ans=0
# for num in ans_li:
#     ans+=num*(n-num)

# print(ans//2)
