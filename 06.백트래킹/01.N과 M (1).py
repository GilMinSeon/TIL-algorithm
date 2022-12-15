# 순열문제

def DFS(L):
    if L == m:
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

n, m = map(int, input().split())
res = [0]*m
ch = [0]*(n+1)
DFS(0)
