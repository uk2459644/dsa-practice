
def is_subsequence(sub,main):
    # Lengths of stings
    m,n=len(main),len(sub)
    # Pointers for main and sub string
    i,j=0,0
    # Traverse both strings
    while i<m and j<n:
        # If characters match, move subsequence pointer
        if main[i]==sub[j]:
            j+=1
        # move main string pointer
        i+=1
    return j==n

strs=["aba","cdca","eae"]
# strs.sort(k)
sorted_list=sorted(strs,key=lambda x:len(x),reverse=True)
n=len(sorted_list)
ans=-1
for i in range(n):
    flag=True
    for j in range(n):
        if i!=j:
            if is_subsequence(sorted_list[i],sorted_list[j]):
                flag=False
                break
    if flag:
        ans=len(sorted_list[i])
        break
    
print(sorted_list,ans)


