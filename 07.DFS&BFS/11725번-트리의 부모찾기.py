#11725_recursion
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

parent = [0 for _ in range(N+1)] #visited

def dfs(child):
    for i in tree[child]:
        if parent[i]==0: #unvisited
            parent[i]=child #parent update 
            dfs(i)

parent[1] = 1   # 방문했다고 체크하고 시작하기 
                # => 해줘야 1번 인덱스에 이상한 값 안들어감
dfs(1)

#print(parent)

for i in range(2, N+1):
    print(parent[i])