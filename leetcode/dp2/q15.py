s1=input()
s2=input()
s3=input()

m,n,t=len(s1),len(s2),len(s3)

if (m+n)!=t:
    print(False)

i=0
j=0
ili=[]
jli=[]
for c in s3:
    if i<m and c==s1[i]:
        ili.append(c)
        i+=1
        continue
    if j<n and c==s2[j]:
        j+=1
        jli.append(c)

if i==m and j==n:
    print(True,ili,jli)
else:
    print(False,ili,jli)

