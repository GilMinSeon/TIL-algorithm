'''
문제
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

입력
첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

출력
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.
'''
# 1) 너무 느림 -> 2632ms
'''
n = int(input())

def sieve(n):
    isprime = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i, n+1, i):
                isprime[j] = False
    return isprime

isprime = sieve(1000000)

for i in range(n):
    num = int(input())
    res = 0
    for i in range(2, num//2 + 1):
        if isprime[i] and isprime[num-i]:
            res += 1
    print(res)
'''
#######
#2 -> 764ms
import sys

MAX = 1000000
p_arr = [False, False] + [True] * (MAX - 1)
for i in range(2, int(MAX ** 0.5) + 1):
    if p_arr[i]:
        for j in range(i * i, MAX + 1, i):
            #if p_arr[j]:
            p_arr[j] = False
prime = [x for x in range(len(p_arr)) if p_arr[x]]
#print(prime) -> 소수만 쭉 있는 리스트! 
for i in range(int(sys.stdin.readline())):
    cnt = 0
    num = int(sys.stdin.readline())
    for j in prime:
        if j > num // 2:
            break
        if p_arr[num - j]: # p_arr에서 인덱스로 찾기!!!
            cnt += 1
    print(cnt)

'''
import sys

r = 1000000
p = [False, False] + [True] * (r - 1)
for i in range(2, int(r ** 0.5) + 1):
    if p[i]:
        for j in range(i * 2, r + 1, i):
            if p[j]:
                p[j] = False
prime = [x for x in range(len(p)) if p[x]]

for i in range(int(sys.stdin.readline())):
    cnt = 0
    n = int(sys.stdin.readline())
    for j in prime:
        if j > n // 2:
            break
        if p[n - j]:
            cnt += 1
    print(cnt)
'''