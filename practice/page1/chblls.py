import sys

print('1')
sys.stdout.flush()
print('3 1 1 3')
sys.stdout.flush()
print('3 2 2 4')
sys.stdout.flush()
k=input().split()
ans=0
if k=='2':
    ans=1
elif k=='-2':
    ans=2
elif k=='1':
    ans=3
elif k=='-1':
    ans=4
elif k=='0':
    ans=5
print(2)
print(ans)
sys.stdout.flush()
