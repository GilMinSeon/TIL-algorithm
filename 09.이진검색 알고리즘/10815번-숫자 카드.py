import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card.sort()

for i in range(m):
    target = nums[i]

    left = 0
    right = n-1
    flag = True
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            print('1', end = ' ')
            flag = False
            break
        elif card[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    if flag : print('0', end = ' ')

'''
1 0 0 1 1 0 0 1
'''
