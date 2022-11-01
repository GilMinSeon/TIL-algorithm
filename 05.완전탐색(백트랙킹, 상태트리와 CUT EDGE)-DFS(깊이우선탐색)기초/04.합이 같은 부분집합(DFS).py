
import sys

def DFS(L, sum):
    global cnt

    # 시간복잡도 줄이기
    if sum > total//2:
        return

    # 재귀 if-else
    if L == n:
        #cnt += 1
        #print(cnt) => 원소의 개수 총 6개, 2**6 = 64가지 경우
        
        if sum == (total - sum):
            print('YES')
            sys.exit(0)
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    total = sum(a)
    DFS(0, 0)
    print('NO')