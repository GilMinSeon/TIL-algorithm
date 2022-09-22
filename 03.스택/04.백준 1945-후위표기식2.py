'''
18라인 stk.append(alpha_list[ord(x) - ord('A')])
-> 이 부분을 생각을 도저히 못해서 힌트를 보고 풀었다

!!! 꼭 복습해야 하는 문제 !!!
'''
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

alpha_list = [0] * n
for i in range(n):
    alpha_list[i] = int(input())

stk = []
for x in s:
    if x.isalpha(): # 영문자면!
        # 이해하기!
        stk.append(alpha_list[ord(x) - ord('A')])
    else:
        num1 = stk.pop()
        num2 = stk.pop()
        if x == '*':
            stk.append(num2*num1)
        elif x == '/':
            stk.append(num2/num1)
        elif x == '+':
            stk.append(num2+num1)
        else:
            stk.append(num2-num1)

print('%.2f' %stk[0]) # 소수점 출력!
