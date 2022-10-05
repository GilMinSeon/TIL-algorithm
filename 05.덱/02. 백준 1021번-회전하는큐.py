'''
한 번에 통과했다!!
뭐지??
먼저 수도코드 잘 작성하고 푸니까 바로 잘 풀림!! 연습장에 정리해놓은 수도코드 잘 정리해보기
'''
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pick = list(input().split())

card = deque([str(x) for x in range(1, n+1)])
#print(card.index(7))

cnt = 0 # 출력변수

for i in range(m):
    val = pick[i]
    
    if card.index(val) <= ((len(card)-1)//2):
        for _ in range(card.index(val)):
            card.append(card.popleft())
            cnt += 1
    else:
        for _ in range(len(card) - card.index(val)):
            card.appendleft(card.pop())
            cnt += 1
    
    card.popleft()


print(cnt)

