def DFS(v):
    global cnt

    if v == n:
        for x in path:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                # 1) 재귀함수 호출전에 해줄 일
                ch[i] = 1
                path.append(i)
                # 2) 재귀함수 호출!
                DFS(i)
                # 3) 재귀함수 호출하고 나서!
                # 뒤로 back하는 지점
                path.pop()
                ch[i] = 0


n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
# 방문했는지 체크할 체크리스트
ch = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
cnt = 0
path = []
path.append(1)
ch[1] = 1 # 처음에 1부터 방문할거니까! 체크해놓고 밑에서 호출
DFS(1)
print(cnt)


# input
# 5 9 
# 1 2 
# 1 3 
# 1 4 
# 2 1 
# 2 3 
# 2 5 
# 3 4 
# 4 2 
# 4 5