import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt_ = Counter(arr)  # 해당 점수에 해당하는 학생 수 얻기 

#[-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]

res = 0

for i in range(n-2):
    now = i
    left = i+1
    right = n-1

    while left < right:
        calc = arr[now] + arr[left] + arr[right]
        if calc == 0:
             #  left값과 right 갑이 같은 경우 해당 범위 저장. -4 -4 2 2 2 
            if arr[left] == arr[right]:
                res += right - left
                        # 다른 경우 right 값에 대한 개수 합
            else: 
                res += cnt_[arr[right]]
            left += 1
        elif calc > 0:
            right -= 1
        else:
            left += 1

print(res)

'''
(2, -5, 3), (2, 2, -4), (2, 2, -4), (-5, 2, 3), (3, -4, 1), (3, -4, 1)
'''