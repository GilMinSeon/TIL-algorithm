# 인프런 page5. 최대 부분 증가수열
n = int(input())
arr = list(map(int, input().split()))

arr.insert(0, 0)
dy = [0]*(n+1)

dy[1] = 1

for i in range(2, n+1):
    max_val = 0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max_val:
            max_val = dy[j]
        dy[i] = max_val + 1
    
print(max(dy))


############################################ 96ms(더 빠른 풀이)

n = int(input())
array = list(map(int,input().split()))

def LIS(n) : #Longest Increasing Subsequence
    dp = [1] + [0 for _ in range(n-1)]

    for i in range(1,n) :
        max_val = 0
        for j in range(i) :
            if array[i] > array[j] : # 기준 값이 이전 값보다 크다면
                max_val = max(max_val,dp[j]) #최대값 갱신
        dp[i] = max_val + 1
    return max(dp)

print(LIS(n))
#시간 복잡도 N^2