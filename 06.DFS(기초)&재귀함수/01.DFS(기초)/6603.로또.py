def DFS(L, s):
    if L == 6:
        for j in range(L):
            print(res[j], end = ' ')
        print()

    else:
        for i in range(s, n):
            res[L] = a[i]
            DFS(L+1, i+1)

while True:
    a = list(map(int, input().split()))
    n = a.pop(0)

    if n == 0:
        break

    res = [0]*n
    DFS(0, 0)
    print()

