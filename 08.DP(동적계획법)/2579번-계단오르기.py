n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
else:
    D = [[[0,0],[0,0]] for _ in range(n+1)]

    D[1][0] = arr[0]
    D[1][1] = 0
    D[2][0] = arr[1]
    D[2][1] = arr[0]+arr[1]

    for i in range(3, n+1):
        D[i][0] = max(D[i-2][0], D[i-2][1]) + arr[i-1]
        D[i][1] = D[i-1][0] + arr[i-1]

    print(max(D[n][0], D[n][1]))

#===============================================================

import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * (N+1)

for i in range(1, N+1):
    arr[i] = int(input())

if N == 1:                          # 계단이 하나일 때는 그 값
    print(arr[1])
elif N == 2:
    print(arr[1] + arr[2])          # 계단이 두개일 때는 둘다 밟은 값
else:                               # 세개 이상부터는, 
    dp = [0] * (N+1)
    dp[0] = [0, 0]                  # dp[n]의 0번 인덱스는 n-1칸에서 n번 칸으로 왔을 때의 최대값, 1번 인덱스는 n-2칸에서 n번 칸으로 점프했으 때의 최대값
    dp[1] = [arr[1], 0]             # dp를 구하기 위한 초기값들을 계산해서 미리 넣어준다
    dp[2] = [arr[2]+arr[1], arr[2]]


    for n in range(3, N+1):
        dp[n] = [dp[n-1][1] + arr[n], max(dp[n-2]) + arr[n]] 
        # 한칸 이동한 경우의 최대값은(0번 인덱스) 이전(n-1)에 한번 이동한 경우는 안되기 때문에, 두번 이동한 경우(1번 인덱스)의 값을 더해주고
	    # 두칸 이동한 경우의 최대값은(1번 인덱스) 이전(n-2)에 한번(0번인덱스)이든 두번(1번인덱스)이든 제약이 없기 때문에, 둘중 큰 경우의 이동을 더함 

    print(max(dp[N]))