def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(s, n):
            res[L] = a[i]
            DFS(L+1, i)

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

res = [0]*m 

DFS(0, 0)

''' qjawns318
n,m = map(int, input().split())

s = list(sorted(list(map(int, input().split()))))
em_list = []

def dfs(tmp):
    if len(em_list) == m:
        return print(' '.join(map(str, em_list)))
    for i in range(len(s)): # 맨 앞자리
        if s[i] >= tmp:
            em_list.append(s[i])
            dfs(s[i])
            em_list.pop()
        
dfs(0)
'''