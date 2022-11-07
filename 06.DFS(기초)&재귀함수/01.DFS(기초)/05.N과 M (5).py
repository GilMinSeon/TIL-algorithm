def DFS(L):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(0, n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = a[i]
                DFS(L+1)
                ch[i] = 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

res = [0]*m
ch = [0]*(n+1)

DFS(0)

# 다른 사람 풀이
'''
n,m = map(int, input().split())

s = list(sorted(list(map(int, input().split()))))
em_list = []

def dfs():
    if len(em_list) == m:
        return print(' '.join(map(str, em_list)))
    for i in range(len(s)): # 맨 앞자리
        if s[i] not in em_list:
            em_list.append(s[i])
            dfs()
            em_list.pop()
        
dfs()
'''
# 위랑 동일
'''
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
s=[]
def dfs():
    if(len(s)==m):
        print(*s)
        return
    for i in arr:
        if(i not in s):
            s.append(i)
            dfs()
            s.pop()
dfs()
'''