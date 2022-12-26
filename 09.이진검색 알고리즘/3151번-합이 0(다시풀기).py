from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0

for i in range(n-2):
    left = i+1
    right = n-1

    while left < right:
        calc = arr[i] + arr[left] + arr[right]
        
        if calc > 0:
            right -= 1
        else:
            if calc == 0:
                if arr[left] == arr[right]:
                    res += (right-left)
                else:
                    idx = bisect_left(arr, arr[right])
                    res += (right-idx+1)
            left += 1
print(res)

'''
(2, -5, 3), (2, 2, -4), (2, 2, -4), (-5, 2, 3), (3, -4, 1), (3, -4, 1)
'''

############### 시간초과 ###################
"""
 세 팀원 코딩 실력 합 0
 팀을 얼마나 많이 만들 수 있는지 계산
 결과: 합이 0이 되는 3인조 만들
 주의: 같은 값이 연속적으로 나오는 경우 처리
"""
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())  # 학생 수
arr = list(map(int, sys.stdin.readline().split()))  # 학생 코딩 실력
arr.sort()
cnt_ = Counter(arr)  # 해당 점수에 해당하는 학생 수 얻기 
result = 0
# 학생을 한명 씩 돌린다.
for i, a in enumerate(arr):
    left, right = i + 1, n - 1
    while left < right:
        sum_ = arr[left] + arr[right] + arr[i]
        # 1. 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
        if sum_ == 0:
            #  left값과 right 갑이 같은 경우 해당 범위 저장. -4 -4 2 2 2 
            if arr[left] == arr[right]:
                result += right - left
                        # 다른 경우 right 값에 대한 개수 합
            else: 
                result += cnt_[arr[right]]
            left += 1
                # 2. 점수 총합이 0 보다 큰 경우 
        elif sum_ > 0:
            right -= 1
                # 3. 점수 총합이 0 보다 작은 경우
        elif sum_ < 0:
            left += 1

print(result)
'''
############### 시간초과 ###################

'''
from collections import Counter
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
arr.sort()
std_counter = Counter(arr) 
# 리스트나 셋을 인자로 넘기면 각 항목을 키로 해서 개수
res = 0
for i in range(n) : 
    left,right=i+1,n-1 # 나이 후 ~ 끝 전 
    target = -arr[i]
    # print(i,target)
    while left<right : 
        cmp = arr[left] + arr[right]
        if cmp < target : 
            left+=1 # 증가하여야 하므로 시작점 오른쪽으로 

        elif cmp == target : # 중복 수 걸러줘야 하지 
            if arr[left]==arr[right] : # 만약 양쪽 같으면 
                res+= right-left # -4 0 (2) 2 2 (2) 3 => 인덱스 2와 5, 5-2 = 3
            else : 
                res+= std_counter[arr[right]] #arr[left] 
            left+=1 # right-=1

        else : 
            right-=1 # 감소하여야 하므로 끝점 왼쪽으로 

print(res)


''''''''''''''''''''''''''''''''''''
from collections import Counter
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
arr.sort()
std_counter = Counter(arr) 
res = 0
for i in range(n) : 
    left, right = i+1, n-1
    target = -arr[i]
    while left<right : 
        cmp = arr[left] + arr[right]
        if cmp < target : 
            left+=1 

        elif cmp == target : 
            if arr[left]==arr[right] : 
                res+= right-left 
            else : 
                res+= std_counter[arr[right]] 
            left+=1 

        else : 
            right-=1 

print(res)


#===================================
'''