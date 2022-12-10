'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

# 반례!
'''
4
1000
0000
0000
0000
'''


n = int(input())
board = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 정답 출력할 변수
res = []
#cnt = 0

# DFS 함수
def DFS(x,y):
    global cnt

    cnt += 1                ##들어왔을때부터 1 증가시키기!!!
    board[x][y] = 0         ##체크!!!

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<n and 0<=b<n and board[a][b]==1:
            #board[a][b] = 0
            DFS(a, b)
    
    #if cnt == 0: cnt = 1
    return cnt


# DFS 호출
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            res.append(DFS(i,j))
            # 아니면 이 밑 라인에서 res.append(cnt)
            
# 출력
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])


###########<강의풀의>
'''
1. 일단 DFS하기전에 board 방문했다고 체크하는거 또!!! 놓침!!!
  -> 그래서 board 찍었을때 내꺼는 한 단지 체크의 가장 마지막에 시작 좌표를 방문하는 오류 발생, 돌아는 갔지만 틀림거임
  !!! 꼭 DFS하기전에 board판 체크할것!!!
2. return을 안해도 됨 => DFS호출하는 구문 밑에 res.append(cnt) 해주는 방법도 있음!! 지금부터는 이렇게 쓰기
'''

