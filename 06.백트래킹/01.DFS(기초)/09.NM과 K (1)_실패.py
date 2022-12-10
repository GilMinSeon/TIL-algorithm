# def DFS(L, s, sum):
#     if L == k:
#         print(sum)
#     else:
#         for i in range(0, n):
#             DFS()

# n, m, k = map(int, input().split())

# # 2차원 리스트 입력받기 => https://minjoos.tistory.com/2
# a = [list(map(int, input().split())) for _ in range(n)]

# res = [0]*k

# DFS(0, 0, 0)


def dfs(x, y, L, sum_value):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if L == k:
        global max_value
        max_value = max(max_value, sum_value)
        print("하나 완성! max_value===>", x, y, L, max_value)
        return
    for i in range(x, n):
        print("i==========================>", i)
        for j in range(y if i == x else 0, m):
        #for j in range(y, m):
            print("j======>", j)
            print("for문===>", i, j)
            if check[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny]:
                    break
            else:
                check[i][j] = True
                print("L : ", L+1, " [ x : ", i, "y : " ,j, " ]sum : ", sum_value + item[i][j])
                dfs(i, j, L + 1, sum_value + item[i][j])
                check[i][j] = False


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    item = []
    for _ in range(n):
        item.append(list(map(int, input().split())))

    max_value = 0
    check = [[False for _ in range(m)] for _ in range(n)]
    dfs(0, 0, 0, 0)
    print(max_value)



''''''''''''''''''''''''''''''''''''''
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = -1000000

def dfs(px, py, index, sum):
    if index == k:
        global answer

        if answer < sum:
            answer = sum
        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue

            ok = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False

            if ok:
                visited[x][y] = True
                dfs(x, y, index + 1, sum + arr[x][y])
                visited[x][y] = False


dfs(0, 0, 0, 0)

print(answer)