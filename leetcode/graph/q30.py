from collections import defaultdict

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]

graph = defaultdict(list)

for i,j in allowedSwaps:
    graph[source[i]].append(source[j])
    graph[source[j]].append(source[i])

count=0
for i in range(len(target)):
    if target[i]!=source[i]:
        if target[i] not in graph.keys():
            count+=1
          


print(count)


