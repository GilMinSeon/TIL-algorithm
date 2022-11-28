from collections import deque

n = 7
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1)
board = [list(map(int, input().split())) for _ in range(n)]
dis = [[0 for _ in range(n)] for _ in range(n)]

# 2)
dq = deque()
dq.append((0,0))

# 3)
board[0][0] = 1 # input배열이면서 동시에 visited 배열!
#dis[0][0] = 0 --> 이미 0이니까 할 필요 없다!

while dq:
    now = dq.popleft()

    for i in range(4):
        x, y = now[0]+dx[i], now[1]+dy[i]

        if 0<=x<n and 0<=y<n:
            if board[x][y] != 1:
                dq.append((x,y))
                dis[x][y] = dis[now[0]][now[1]] + 1
                board[x][y] = 1

# for i in range(n):
#     print(dis[i])

#print(dis[6][6]) --> 이렇게만 하면 안됨!!

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])


'''
0 0 0 0 0 0 0 
0 1 1 1 1 1 0 
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0 
1 0 0 0 1 0 0 
1 0 1 0 0 0 0
'''

# 위 : 내가 짠 코드
#######################################################
# 아래 : 강의코드
'''
내가 놓친 점 
: 도착할 수 없으면 -1 출력! => 맨 아래 프린트문 바꾸기
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])

: 그리고 for문 돌면서 체크하는 if문 두개로 나눈거 한개로 합칠 수 있다!
if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
'''

