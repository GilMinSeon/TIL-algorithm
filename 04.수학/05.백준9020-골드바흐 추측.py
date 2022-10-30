# 1) 내 풀이 -> 460
# import sys

# MAX = 10000
# p_arr = [False, False] + [True] * (MAX - 1)
# for i in range(2, int(MAX ** 0.5) + 1):
#     if p_arr[i]:
#         for j in range(i * i, MAX + 1, i):
#             p_arr[j] = False
# prime = [x for x in range(len(p_arr)) if p_arr[x]]

# for i in range(int(sys.stdin.readline())):
#     num = int(sys.stdin.readline())
#     arr = []
#     for j in prime:
#         if j > num // 2:
#             print(arr)
#             #print(arr[-2], arr[-1])
#             break
#         if p_arr[num - j]: # p_arr에서 인덱스로 찾기!!!
#             arr.append((j, num-j))
#             # arr.append(j)
#             # arr.append(num - j)

# 2) 맞힌 사람 풀이 보고 변형 -> 96ms
import sys
input = sys.stdin.readline

MAX_NUM = 10000

prime = [True for _ in range(MAX_NUM + 1)]
prime[0] = prime[1] = False

for i in range(2, int(MAX_NUM ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX_NUM + 1, i):
            prime[j] = False

n = int(input())
# 문제 : 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
for _ in range(n):
    num = int(input())
    for i in range(num//2, MAX_NUM + 1):  # ---> 시작 위치를 아예 num//2로 줘버림 ==> 머리를 이렇게 써야지!!!
        if prime[i] and prime[num-i]:
            print(num-i, i)
            break

## 고민!!! 1번풀이와 2번풀이 시간 차이가 엄청 남 => ***시작 위치를 아예 num//2로 줘버림*** 이 부분 때문