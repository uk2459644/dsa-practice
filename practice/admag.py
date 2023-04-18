f = [1, 2]
for i in range(2, 90):
    f.append(f[i - 1] + f[i - 2])
for i in range(int(input())):
    x, ind = int(input()), 0
    for j in range(len(f)):
        if f[j] > x:
            ind = j
            break
    print(ind)