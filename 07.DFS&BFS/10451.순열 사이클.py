import sys
#sys.setrecursionlimit(2000)

T = int(input())

def DFS(x):
    visited[x] = True
    target = arr[x] 
    if not visited[target]: 
        DFS(target)

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n 
    res = 0
    
    for i in range(1, n+1):
        if not visited[i]: 
            DFS(i) 
            res += 1
    print(res)