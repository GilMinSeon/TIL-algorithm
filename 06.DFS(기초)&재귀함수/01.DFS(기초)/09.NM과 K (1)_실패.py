def DFS(L, s, sum):
    if L == k:
        print(sum)
    else:
        for i in range(0, n):
            DFS()

n, m, k = map(int, input().split())

# 2차원 리스트 입력받기 => https://minjoos.tistory.com/2
a = [list(map(int, input().split())) for _ in range(n)]

res = [0]*k

DFS(0, 0, 0)