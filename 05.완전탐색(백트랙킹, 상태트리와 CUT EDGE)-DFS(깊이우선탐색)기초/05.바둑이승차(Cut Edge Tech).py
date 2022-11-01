
import sys

def DFS(L, sum, tsum):
    global result

    # cut edge
    if sum + (total-tsum) < result:
        return

    # c를 넘지 않는 경우만!
    if sum > c:
        return

    # 재귀 if-else
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum     , tsum+a[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)