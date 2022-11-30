
n, m, v = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)] # 모두 0으로 초기화!!!
# n이 6이라면 만드는건 7행 7열을 만든다
# -> 하지만 밑에서 print할때 인덱스1부터 프린트함으로서 6행 6열 2차원 리스트처럼 사용하는 것!

# 간선정보를 읽어서 가중치 방향 인접행렬 조작
# 간선의 개수(m개의 간선정보) => m
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(g[i][j], end= ' ')
#     print()

# 방문리스트
ch = [0]*(n+1)

ch[v] = 1
path = []
path.append(v)

# DFS함수
def DFS(v):

    if v == n:
        for x in path:
            print(x, end=' ')
        print()
    else:
        cnt = 0
        for i in range(1, n+1):
            if cnt == 1: break
            if g[i][v] == 1 and ch[i] == 0:
                cnt = 1
                # 1) 재귀함수 호출전에 해줄 일
                ch[i] = 1
                path.append(i)
                # 2) 재귀함수 호출!
                DFS(i)
                # 3) 재귀함수 호출하고 나서 뒤로 back하는 지점
                path.pop()
                ch[i] = 0

DFS(v)