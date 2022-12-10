# 외판원순회2 - 백트래킹
def DFS(L, sum, tmp, yn):
    global min_val
    if sum > min_val:
        return

    if L == n:
        #print(res, sum)
        a = res[-1]-1
        b = res[0]-1
        #sum += board[a][b]
        #print(sum)
        temp = sum + board[a][b]
        if board[a][b] == 0:
            yn = False
        #print(temp, "temp")
        if yn == True:
            min_val = min(temp, min_val)

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i

                if L > 0:
                    a = res[L-1]-1
                    b = res[L]-1
                    #print("L: ", L, " a에서b로", a+1, "->", b+1)
                    tmp = board[a][b]
                    
                    # 도시 i에서 도시 j로 갈 수 없는 경우
                    if tmp == 0:
                        yn = False

                    sum += tmp
                #print(L, sum, tmp)
                DFS(L+1, sum, tmp, yn)
                ch[i] = 0
                if L > 0:
                    sum -= tmp
                


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = [0]*n
    ch = [0]*(n+1)
    min_val = 2147000000
    DFS(0, 0, 0, True)
    print(min_val)


# 다른사람 제출 코드 -> 매우 깔끔
'''
import sys

n = int(sys.stdin.readline().rstrip())
w = [[0 for __ in range(n)] for _ in range(n)]
for i in range(n):
    w[i] = list(map(int, sys.stdin.readline().split()))

visited = [0 for _ in range(n)]

min_sum = 9876543210
def solution(depth, sum, start):
    global min_sum
    global visited

    if sum > min_sum:
        return

    if depth == n-1:
        if w[start][0] != 0:
            min_sum = min(min_sum, sum + w[start][0])
        return
    
    for i in range(1, n):
        if visited[i] == 0 and w[start][i] != 0:
            visited[i] = 1
            solution(depth+1, sum + w[start][i], i)
            visited[i] = 0


solution(0, 0, 0)
sys.stdout.write(f'{min_sum}')

'''

# 나보다 시간은 오래걸림
'''
import sys

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize #출력할 최소값 정의

def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
            min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
	    
        return
    for i in range(N): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i) #그 도시를 방문목록에 추가
            dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제


#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)
'''

# 거의 뭐 다 이코드인것 같음
'''
import sys
input = sys.stdin.readline
N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
INF = float('inf')

dp = [[INF for i in range(1<<N)] for j in range(N)] 

def TSP(n,s,v): # {v} 에서 도시 n에서 출발도시(s)로 돌아오는 최소비용경로
    if dp[n][v] != INF:
        return dp[n][v] # 찾아놓은 DP 값 활용
    
    if v == (1<<N)-1: # 모든 도시를 방문 했는데, 
        if W[n][s] > 0: # 거기서 다시 최초 위치로 돌아올수 있다면,
            dp[n][v] = W[n][s]
            return dp[n][v] # 그 때 비용 반환
        dp[n][v] = INF
        return dp[n][v] # 아니면 있을 수 없는 값 반환

    min_cost = 10000000
    # 이 값을 dp 의 초깃값과 다르게 설정해줘야 한다.
    # 그렇지 않으면 min_cost 값과 for문을 돌고 난 뒤 min_cost 값이 같을 경우
    # dp[n][v]를 저장 하지 않은것과 마찬가지 여서 나중에 DP 효과를 못받는다.
    for i in range(N): # 위 두 경우에 해당이 없다면 찾는다.
        if W[n][i] == 0:
            continue
        if (1<<i) & v :
            continue
        # 갈수 없거나, 이미 방문한 지역을 제외하고
        min_cost = min(min_cost,W[n][i] + TSP(i,s,v|(1<<i)))
        # 현재 도시에서 다음 도시로 간 뒤 출발 도시로 돌아가는 최소비용들 중 최소비용을
        # 현재 도시에서 출발 도시로 돌아가는 최소비용으로 저장한다.
    dp[n][v] = min_cost
    return dp[n][v]

print(TSP(N//2,N//2,1<<N//2)) # 아무곳에서 출발해도 되므로 가운데쯤에서 출발해보자
'''