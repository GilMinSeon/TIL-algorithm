# math.ceil 함수 활용법 배움!!!

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split()) # 학생수, 보석종류

arr = []
for _ in range(m):
    arr.append(int(input()))

arr.sort()

left = 1
right = max(arr)

# 학생수 리턴
def calc(len):
    student_cnt = 0
    for x in arr:
        # if x <= len:
        #     student_cnt += 1
        # else:
        #     if x % len == 0: 
        #         student_cnt += x//len
        #     else:
        #         student_cnt += (x//len + 1)
        student_cnt += math.ceil(x/len)
        
    return student_cnt

'''
ceil() 함수는 소수점 자리의 숫자를 무조건 올리는 함수이다.
ceil의 사전적의미 '<방에> 천장을 만들다'
처럼 무조건 소수점 자리를 올린다.

ceil(99.2) = 100
ceil(0.11111) = 1
ceil(5.9) = 6
ceil(-3.22) = -3

실수(float)을 정수(integer)로 만든다.
'''

res = 0
while left <= right:
    mid = (left + right) // 2
    calc_val = calc(mid)

    # 보석을 받지 못하는 학생은 있어도 됨. 하지만 정해진 학생수보다 더 주는건 안됨!!
    # 하지만 n보다 적은 숫자의 학생한테 보석을 나눠주면 1인당 보석을 가지는 수가 더 커질테니 최대한 n에 맞아야지
    # n보다 크면은 안되는거지... 작거나 같은 경우일때
    if calc_val <= n:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)

#=================매우 빠른 풀이=============
import sys
import math
input = sys.stdin.readline

def count_child(base):
    cnt = 0
    for c in colors:
        cnt += math.ceil(c/base)
    return cnt

N,M = map(int,input().split())
colors = [ int(input()) for _ in range(M)]

start = 1
end = max(colors)
answer = 0
while start<=end:
    mid = (start+end)//2
    res = count_child(mid)
    if res>N:
        start = mid+1
    else:
        end = mid-1
        answer = mid
print(answer)