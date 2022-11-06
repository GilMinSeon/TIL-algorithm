n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)] # 모두 0으로 초기화!!!
# n이 6이라면 만드는건 7행 7열을 만든다
# -> 하지만 밑에서 print할때 인덱스1부터 프린트함으로서 6행 6열 2차원 리스트처럼 사용하는 것!

# 간선정보를 읽어서 가중치 방향 인접행렬 조작
# 간선의 개수(m개의 간선정보) => m
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end= ' ')
    print()

'''
# 무방향 인접행렬일 경우
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1
'''

# input
# 6 9 
# 1 2 7 
# 1 3 4 
# 2 1 2 
# 2 3 5 
# 2 5 5 
# 3 4 5 
# 4 2 2 
# 4 5 5 
# 6 4 5