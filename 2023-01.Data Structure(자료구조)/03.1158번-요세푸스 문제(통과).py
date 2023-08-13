# 시간초과 떠서 deque 사용
'''
from collections import deque
n, k = map(int, input().split())

# idea -> 1~n까지의 배열을 만들어서 k가 아니면 pop해서 append, k면 pop

q = deque([i for i in range(1, n+1)])
answer = []

idx = 1
while q:
    if (idx % k) == 0:
        answer.append(q.popleft())
    else:
        q.append(q.popleft())
    idx += 1

print('<', end='')
print(*answer, sep=', ', end='')
print('>')
'''
# 2) 
'''
N,K = map(int, input().split())
M = list(range(1,N+1))
X = []
a = 0
while len(M):
	a+=K-1
	a%=len(M)
	X.append(M[a])
	del M[a]
print('<', end='')
print(*X, sep=', ', end = '')
print('>')
'''

# 3)
''''''
N, K = map(int, input().split())

queue = []
ans = []

for i in range(1,N+1):
    queue.append(i)

cur = 0
while(queue):
    
    cur += K - 1

    print(cur)

    if cur >= len(queue):
        cur = cur % len(queue)
        print(cur)
    ans.append(queue.pop(cur))

    print(ans)

print("<" + ", ".join(str(x) for x in ans) + ">")
''''''

#print(str(result).replace('[', '<').replace(']', '>'))