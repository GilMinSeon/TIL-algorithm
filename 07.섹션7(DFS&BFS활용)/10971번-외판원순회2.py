# 외판원순회2 - 백트래킹
def DFS(L, sum):
    global min_val
    # if sum > min_val:
    #     return

    if L == n:
        # 비용 계산
        # for j in range(L):
        #     print(res[j], end=' ')
        #print(res, end = ' ')
        # for i in range(len(res)-1):
        #     a = res[i]
        #     b = res[i+1]
        #     sum += board[a-1][b-1]
        print(res, sum)
        a = res[-1]-1
        b = res[0]-1
        #sum += board[a][b]

        temp = sum + board[a][b]
        print(temp, "temp")
        min_val = min(sum, min_val)

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i

                if L > 0:
                    # print(L)
                    # print(res)
                    # print(res[L-1]-1)
                    # print(res[L]-1)
                    # print(board[0][1])
                    a = res[L-1]-1
                    b = res[L]-1
                    tmp = board[a][b]
                    sum += tmp
                print(L, sum)
                DFS(L+1, sum)
                ch[i] = 0


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = [0]*n
    ch = [0]*(n+1)
    min_val = 2147000000
    DFS(0, 0)
    print(min_val)
