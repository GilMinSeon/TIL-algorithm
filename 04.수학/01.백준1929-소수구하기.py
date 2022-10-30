# 1) 1456ms => 매우 느림
# m,n = map(int, input().split())

# ch = [0] * (n+1)

# for i in range(2, int(n**0.5)+1):
#     if ch[i] == 0:
#         print(i)
#     for j in range(i*2, n+1, i):
#         ch[j] = 1

''''''''''''''''''''''''''''''''''''''''''''''''
# 참고) 인터넷에서 가져온 풀이
# m, n = map(int, input().split())

# case = [True] * (n+1)
# case[0] = case[1] = False
# for i in range(2,int(n**0.5)+1):
#     if case[i]:
#         for j in range(2*i,n+1,i):
#             case[j] = False
# for i in range(m,n+1):
#     if case[i]:
#         print(i)

''''''''''''''''''''''''''''''''''''''''''''''''
# 확장방법 => 352ms
import math
m,n = map(int, input().split())

flags = [0,0] + [1]*(n-1)
#sqrtn = math.floor(math.sqrt(n))
sqrtn = int(n ** 0.5)
for i in range(2, sqrtn+1):
    if flags[i] == 1:
        for j in range(2*i, n+1, i):
            flags[j] = 0

for i in range(m, n+1):
    if flags[i] == 1:
        print(i)

'''
# 이해하기!
def prime_list(a, n: int):
    # 에라토스테네스의 체
    # 0, 1 + 2 ~ n - 1
    seive = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)
    for k in range(2, m + 1):
        if seive[k]:
            seive[k * 2::k] = [False] * ((n - k) // k)
    for x in range(a, n + 1):
        if seive[x]:
            print(x)

a, b = map(int, input().split())

prime_list(a, b)
'''