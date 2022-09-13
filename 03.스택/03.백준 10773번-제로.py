'''
한 번에 통과!
쉬운문제
'''
import sys
input=sys.stdin.readline()

k = int(input)

stk = []
for _ in range(k):
    a = int(sys.stdin.readline())

    if a == 0:
        stk.pop()
    else:
        stk.append(a)
    
print(sum(stk))

    
