"""
If the sum of the array is already even, the answer is obviously
0. Now what if the sum is odd?
It can be observed that any power of an odd integer is always going to be
odd, and any positive power of an even integer is even - however,
an even integer to the power 0 is 1, which is odd.
So, if we are to change the parity of our sum from odd to even, our only 
hope is to turn some even integer into 1 - operating on odd integer is useless
because its parity will never change.

If the array has a 2, in one operation we can make it to 1, and this is
enough to change the parity of the sum.

What if every even integer in A is >= 4. Then none of them can be brought
down to 1.

"""
for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))

    if sum(nli)%2==0:
        print(0)
        continue
    if sum(nli)%2==1:
        if 2 in nli:
            print(1)
            continue
        else:
            print(-1)