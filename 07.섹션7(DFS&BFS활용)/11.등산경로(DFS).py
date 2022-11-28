'''
5
2 23 92 78 93 
59 50 48 90 80 
30 53 70 75 96 
94 91 82 89 93 
97 98 95 96 100 
'''
n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(n)]

# 체크배열 필요
ch = [[0]*n for _ in range(n)]

# 출발지, 도착지 좌표 구하기
min_val = 2147000000
max_val = -2147000000

aa,bb,cc,dd = 0,0,0,0
for i in range(n):
    for j in range(n):
        tmp = board[i][j]
        if tmp < min_val:
            min_val = tmp
            aa,bb = i,j
        if tmp > max_val:
            max_val = tmp
            cc,dd = i,j

# 정답 출력할 변수
cnt = 0

# DFS 함수
def DFS(x,y):
    global cnt
    if (x,y) == (cc,dd):
        cnt += 1

    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<n and 0<=b<n and ch[a][b]==0 and board[x][y]<board[a][b]:
                ch[a][b] = 1
                DFS(a, b)
                ch[a][b] = 0

# DFS 호출
ch[aa][bb] = 1 ##### 제일 중요한 체크!!! 밑에서 DFS뻗는 첫 죄표를 방문체크 필수!!!!
DFS(aa,bb)

# 출력
print(cnt)