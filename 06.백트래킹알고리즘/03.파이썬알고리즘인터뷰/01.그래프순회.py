# DFS - 재귀구조로 구현
# 그래프를 표현하는 방식에는 크게 1)인접행렬과 2)인접리스트 두가지 방법이 존재

# 아래 방법은 그래프를 인접리스트로 표현한 방식(딕셔너리 활용) -> 출발노드를 "key"로 도착노드를 value"로 표현
# 도착노드는 여러 개가 될 수 있으므로 리스트 형태로 표현
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

# 1.딕셔너리를 입력값으로 해서 DFS 구현
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:# 정점 v의 모든 인접유향간선들을 반복해라
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

print(recursive_dfs(1))

# 2. BFS 구현 - 모든 인접 간선을 추출하고 도착점인 정점을 큐에 삽입한다
# 인접노드를 우선으로 방문하는 너비우선탐색
def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
    return discoverd

print(iterative_bfs(1))
