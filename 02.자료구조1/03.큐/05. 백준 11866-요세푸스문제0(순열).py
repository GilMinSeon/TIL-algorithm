'''
print 부분 더 깔끔히 코드 작성할 수 있는지 다른 풀이법 보기!
'''
from collections import deque

n, k = map(int, input().split())

#print([x for x in range(1, n+1)])
# 리스트화 안해도 바로 리스트 겸 덱 구조로 변신
dq = deque(x for x in range(1, n+1))

print_str = ''
while True:
    for _ in range(k-1):
        dq.append(dq.popleft())
    remove = dq.popleft()
    print_str += str(remove) + ', '

    if not dq:
        break

print_str = print_str[:-2] # 마지막 숫자 뒤 , 제거

print('<', end='')
print(print_str, end='')
print('>', '')
