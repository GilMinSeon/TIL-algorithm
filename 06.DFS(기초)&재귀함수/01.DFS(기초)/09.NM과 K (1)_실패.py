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