n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = arr[0]

for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j]+arr[i])
    else:
      dp[i] = max(dp[i], arr[i])

print(max(dp))

'''
import sys
n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

dp = [0] * n # 각 인덱스 위치에 가장 큰 증가 부분 수열의 합
dp[0] = m[0]

# 반복문을 통해 각 인덱스 위치에 가장 큰 증가 부분 수열의 합을 구한다.
for i in range(1, n):
    # 현재 인덱스 값과 이전 인덱스의 값을 비교
    for j in range(i):
        # 현재 수가 이전 수보다 크다면
        # 현재 인덱스 위치에 가장 큰 부분 수열의 합과 이전 인덱스 위치에 가장 큰 부분 수열의 합 + 현재 수를 비교한다.
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j] + m[i])

        # 이전 수가 더 크다면 현재 인덱스 위치에 가장 큰 부분 수열의 합과 현재 수를 비교한다.
        else:
            dp[i] = max(dp[i], m[i])

print(max(dp))
'''