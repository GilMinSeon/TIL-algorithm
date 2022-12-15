# 조합문제

def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)

n, m = map(int, input().split())
res = [0]*m
DFS(0, 1)

# (1) 순열일때 output
# 1 2 
# 1 3 
# 1 4 
# 2 1 
# 2 3 
# 2 4 
# 3 1 
# 3 2 
# 3 4 
# 4 1 
# 4 2 
# 4 3 

# (2) 조합일때 output
# 1 2 
# 1 3 
# 1 4 
# 2 3 
# 2 4 
# 3 4 
