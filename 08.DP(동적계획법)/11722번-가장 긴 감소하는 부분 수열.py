# 인프런 page5. 최대 부분 증가수열 - 응용2

n = int(input())
arr = list(map(int, input().split()))

arr.insert(0, 0)
dy = [0]*(n+1)

dy[1] = 1

for i in range(2, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if arr[j]>arr[i] and dy[j]>max_val:
            max_val = dy[j]
        dy[i] = max_val + 1
    
print(max(dy))


########################## 시간은 비슷한데 간단쓰
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i],dp[j]+1)
    
print(max(dp))