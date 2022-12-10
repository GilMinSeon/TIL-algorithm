'''
def check(i):
    if ch[i] == 1:
        return True
    else:
        return False


def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        
        print('끝!!!!', cnt)

    else:
        for i in range(n):
            #ch[i] = 1
            if check(i):
                DFS(L+1)
                ch[i] = 0




n = int(input())
arr = [[0 for col in range(n)] for row in range(n)]
cnt = 0
# for i in range(n):
#     print(arr[i])
ch = [0]*n
DFS(0)
'''


'''
def dfs(L):
    global answer
    if L==n:
        answer += 1
        return
 
    for x in range(n):
        #print(x, L)
        if x in col or (L-x) in diag1 or (L+x) in diag2:
            continue
        col.add(x)
        diag1.add(L-x)  #오른쪽
        diag2.add(L+x)  #왼쪽
        dfs(L+1)
        col.remove(x)
        diag1.remove(L-x)
        diag2.remove(L+x)
 
n = int(input())
col, diag1, diag2 = set(), set(), set()
answer = 0
dfs(0)
print(answer)
'''




'''
import sys
input = sys.stdin.readline

def DFS(L, x, y, sum):
    global res 
    if L == k:
        if res < sum:
            res = sum
        return
    
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            # 방문 확인
            if [i,j] not in ch:
                if ([i + 1, j] not in ch) and ([i - 1, j] not in ch) and ([i, j + 1] not in ch) and ([i, j - 1] not in ch):
                    ch.append([i,j])
                    DFS(L+1, i, j, sum + arr[i][j])
                    ch.pop()

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ch = []

res = -10000
DFS(0, 0, 0, 0)
print(res)
'''


# 언니 코드
def DFS(L,x,y,sum):
    global res

    if L == k:
        if res<sum:
            res = sum
        return
    else:
        for i in range(x,n):
            for j in range(y if i==x else 0,m):
                if ch[i][j] == 0:             
                    for z in range(4):
                        a = i + dx[z]
                        b = j + dy[z]
                        if 0<=a<n and 0<=b<m:
                            if ch[a][b] == 1:  
                                break
                    else: 
                        ch[i][j] = 1
                        DFS(L+1,i,j,sum+g[i][j])
                        ch[i][j] = 0

                        

#dx = [0, 0, 1, -1]
#dy = [1, -1, 0, 0]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m,k = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*m for _ in range(n)]
res = -10000

DFS(0,0,0,0)
print(res)

