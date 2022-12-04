n, s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0

def dfs(L, sum):
    global cnt
    if L == n:
        return
    else:
        #sum += arr[L]
        if sum == s:
            cnt += 1
        dfs(L+1,sum)
        dfs(L+1,sum+arr[L])

dfs(0,0)
print(cnt)