from collections import defaultdict,deque,Counter

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1

n=len(friends)

graph=defaultdict(list)

for i in range(n):
    graph[i].extend(friends[i])

queue=deque([id])

levels=[1]
i=0
count=0
sm=0
while level>0:
    node=queue.popleft()
    queue.extend(graph[node])
    sm+=len(graph[node])
    count+=1
    if count==levels[i]:
        levels.append(sm)
        sm=0
        i+=1
        count=0
        level-=1
fnd=set(list(queue))
videos=[] 
for f in fnd:
    if f!=id:
        videos.extend(watchedVideos[f])


def sort_characters_by_frequency(input_string):
    # Count frequencies of characters
    char_freq = Counter(input_string)
    
    # Sort characters based on frequencies
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1])
    
    # Extract characters in ascending order of frequencies
    sorted_chars_list = [char for char, freq in sorted_chars]
    
    return sorted_chars_list

# Example usage:
sorted_characters = sort_characters_by_frequency(videos)
print(fnd,videos,sorted_characters)

