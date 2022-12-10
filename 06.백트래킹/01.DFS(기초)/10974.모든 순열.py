def DFS(L):
    if L == n:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

n = int(input())
res = [0]*n
ch = [0]*(n+1)
DFS(0)