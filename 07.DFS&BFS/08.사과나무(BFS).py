from collections import deque

# 방향 써주고
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 문제의 input
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 체크배열과 최종답 두개 만들기
ch = [[0]*n for _ in range(n)] # => visited 배열!!
sum = 0

# 값이 없을때까지 돌릴 큐 하나 만들어서 거기다가 첫번째 값 넣어두기
Q = deque()
Q.append((n//2, n//2))

# 넣어둔 첫번째 값 체크
ch[n//2][n//2] = 1
sum += a[n//2][n//2]

# ★★★★이 문제의 종료조건인 L을 미리 설정해두기!!★★★★ => 7번문제처럼 while dq가 아님! 
L = 0

while True:
    # 종료조건
    if L == n//2:
        break

    # 시작
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()

        # 4방향만큼 돌아주기 (문제의 조건! 4가지로 뻗어나감 => 가지생성)
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            # 방문한 곳인지 아닌지 체크! 하고 sum 더해주기
            if ch[x][y] == 0:
                # 1) sum 더해주기
                sum += a[x][y]
                # 2) 체크배열에 체크
                ch[x][y] = 1
                # 3) 큐에 넣어주기
                Q.append((x,y))

    # print(L, size)
    # for x in ch:
    #     print(x)


    # for i 가 끝나면 하나의 레벨 탐색이 끝났다는 뜻! 레벨 하나 증가
    L += 1

print(sum)

'''
5
10 13 10 12 15 
12 39 30 23 11 
11 25 50 53 15 
19 27 29 37 27 
19 13 30 13 19
'''
