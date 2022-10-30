'''
문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

1 ≤ n ≤ 123,456
'''
# 1) 시간초과
# def is_prime(x):
#     for i in range(2, int(x ** 0.5)+1):
#         if x % i == 0:
#             return False
#     return True


# def get_prime_cnt(x):
#     cnt = 0
#     for i in range(x+1, 2*x+1):
#         if is_prime(i):
#             cnt += 1
#     return cnt

# while True:
#     x = int(input())
#     if x == 0: break

#     print(get_prime_cnt(x))

# 2) 에라토스테네스 => 1440ms (내가 푼 방식)
'''
def get_prime_cnt(m, n):
    cnt = 0
    flags = [0,0] + [1]*(n-1)
    for i in range(2, int(n ** 0.5)+1):
        if flags[i] == 1:
            for j in range(2*i, n+1, i):
                flags[j] = 0

    for i in range(m, n+1):
        if flags[i] == 1:
            cnt += 1
    return cnt

while True:
    x = int(input())
    if x == 0: break

    print(get_prime_cnt(x+1, 2*x))
'''
#2) ==> 통과는 했는데 시간 오래걸림 -> 일단 최대숫자까지 소수 다 만들어놓고 거기서 해당하는 구간만 빼내오는 방식으로 작성

# 3) 소수 전체 나열하고 구간으로 빼오기 ==> 800ms
def sieve(n):
    flags = [0,0] + [1]*(n-1)
    for i in range(2, int(n ** 0.5)+1):
        if flags[i] == 1:
            for j in range(2*i, n+1, i):
                flags[j] = 0
    
    primes = []
    for i in range(len(flags)):
        if flags[i] == 1:
            primes.append(i)

    return primes

prime_arr = sieve(123456 * 2)

while True:
    x = int(input())
    if x == 0: break
    cnt = 0
    for i in prime_arr:
        if x < i <= 2*x:
            cnt += 1
    print(cnt)

####################################다른 맞힌 풀이#################################
'''
def get_prime_array(N: int):
    # N보다 작은 소수를 모두 출력
    
    if N < 2:
        return []
    N = N+1
    Sieve = [1] * (N // 2) #홀수에 대해서만 Sieve를 구성해서 탐색 범위 감소
    for i in range(3, int(N ** 0.5)+1, 2): #3부터 시작되는 홀수에 대해서만 대응 N의 소수는 Root(N+1)보다 클 수 없음
        if Sieve[i // 2] == 1:
            k = i * i
            #Sieve[k//2 : : i] = [0] * ((N-k-1) // (2*i) +1)
            for j in range(k//2, N//2 , i):
                Sieve[j] = 0
    return Sieve
    
def get_prime_number(A):
    # get_prime_array 필요
    # 정수를 입력 받으면 해당 정수 보다 작은 소수를 출력

    if (type(A) == int):
        A = get_prime_array(A)
    
    ans = [2]
    for i in range(1, len(A)):
        if A[i] == 1:
            ans.append(2*i+1)
    return ans

    # return [2] + [(2 * i + 1) for i in range(1, n // 2) if save[i]]

def Search(prime, n):
    l,r = 0, len(prime)-1
    while l<=r:
        m=(l+r)//2

        if prime[m] > n:
            r = m-1
        else:
            l = m+1
    return l

import sys
S = get_prime_number(123456*2)
while(1):
    N = int(sys.stdin.readline())
    if N ==0:
        break
    print(Search(S,2*N) - Search(S,N))
'''
# 엥 이진탐색???
'''
import sys

MAX_N = 123456*2

eratos = [True] * (MAX_N+1)
eratos[0], eratos[1] = False, False
for i in range(2, int(MAX_N**0.5)+1):
    if eratos[i]:
        for j in range(2*i, MAX_N+1, i):
            eratos[j] = False

primes = [num for num, is_prime in enumerate(eratos) if is_prime]

def bin_search(x):
    start = 0
    end = len(primes)-1
    while start <= end:
        mid = (start+end)//2
        if primes[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return start

for n in map(int, sys.stdin.readlines()[:-1]):
    print(bin_search(2*n) - bin_search(n))
'''