import sys
input = sys.stdin.readline

MAX_NUM = 1000000

prime = [True for _ in range(MAX_NUM + 1)]
prime[0] = prime[1] = False

for i in range(2, int(MAX_NUM ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX_NUM + 1, i):
            prime[j] = False

only_prime = [x for x in range(len(prime)) if prime[x]]

while True:
    num = int(input())
    if num == 0: break

    for i in only_prime:
        if prime[num - i]:
            print(f'{num} = {i} + {num - i}')
            break


#  만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 
#  또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

# 첫번째 풀이
'''
import sys
input = sys.stdin.readline

MAX_NUM = 1000000

prime = [True for _ in range(MAX_NUM + 1)]
prime[0] = prime[1] = False

for i in range(2, int(MAX_NUM ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX_NUM + 1, i):
            prime[j] = False

while True:
    num = int(input())
    if num == 0: break
    for i in range(2, MAX_NUM+1):
        if prime[i] and prime[num - i]:
            print(f'{num} = {i} + {num - i}')
            break
'''
