def DFS(L):
    global answer
    if L == n:
        total = 0
        for i in range(n-1):
            total += abs(res[i]- res[i+1])
        answer = max(answer, total)
        
    else:
        for i in range(0, n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = a[i]
                DFS(L+1)
                ch[i] = 0


n = int(input())
a = list(map(int, input().split()))

res = [0]*n
ch = [0]*(n+1)
answer = 0
DFS(0)
print(answer)