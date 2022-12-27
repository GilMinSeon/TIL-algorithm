'''
import sys
input = sys.stdin.readline

n = int(input())
stk = list(map(int, input().split()))
remain = []
res = [0] * (n+1)

for i in range(n-1):
    target = stk.pop()

    if stk[-1] > target:
        res[i] = len(stk)
    else:
        remain.append((target, i))

    if len(remain) != 0:
        while (remain != []) and (remain[-1][0] < stk[-1]):
            x, y = remain.pop()
            res[y] = len(stk)
            

res.pop()
res.reverse()

for i in res:
    print(i, end = ' ')
'''

#============== 다른 사람의 빠른 풀이 =============
import sys

N = int(input())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        #현재 타워보다 큰 타워가 있을 때까지 stack을 탐색
        if top_list[stack[-1]] < top_list[i]:
            stack.pop()
        #현재 타워보다 큰 타워가 있다면 해당 위치를 answer에 push
        else:
            answer.append(stack[-1] + 1)
            break

    #stack을 다 탐색해도 현재 타워보다 큰 타워가 없다는 것을 의미
    if not stack:
        answer.append(0)
    stack.append(i)
    
    print(i, '번째 턴')
    print('답 :   ', answer)
    print('스택:   ', stack)
    print()
    

#print(answer) -> [0, 0, 2, 2, 4]
print(*answer) #-> 0 0 2 2 4


''''''''''''''''''''''''''''''''''''
'''
아이디어
1. 앞에서부터 탑을 체크한다.
2. 동시에 stack을 쌓는데, stack에 쌓인 탑은 비교군이다.
stack을 쌓으면서 i번째 탑의 앞에 있는 탑을 '역순'으로 관찰할 수 있으며, --> 핵심 1
i의 높이(height)가 더 높다면, stack에 있는 탑은 무의미해 진다. i번쨰 뒤에서는 '가려지기 때문'이다. --> 핵심 2
따라서 stack.pop()을 하고, 그 앞에거를 보는데, 만약 stack에 있는 탑이 더 높다면 레이저 수신하는 탑이
해당 탑이므로, result list에 저장한다.
'''

import sys

input = sys.stdin.readline

N = int(input())

tops = list(map(int, input().split()))
stack = []
result = [0 for _ in range(N)]

for i, height in enumerate(tops):
    while stack:
        if stack[-1][1] > height:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, height))
    
print(*result)
