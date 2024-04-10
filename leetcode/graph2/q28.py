
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

folder.sort()

ans=[]

pfx=""
n=len(folder)

for i in range(n):
    if pfx=="" and folder[i].startswith("/"):
        pfx=folder[i]
        ans.append(pfx)
        continue
    if folder[i].startswith(pfx+"/"):
        # ans.append(folder[i])
        continue
    # else:
    if folder[i].startswith("/"):
        pfx=folder[i]
        ans.append(pfx)

print(ans)






