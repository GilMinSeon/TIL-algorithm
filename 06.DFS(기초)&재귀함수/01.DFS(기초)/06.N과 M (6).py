def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(s, n):
            res[L] = a[i]
            DFS(L+1, i+1)

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

res = [0]*m 

DFS(0, 0)
