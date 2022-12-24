import sys
input = sys.stdin.readline

T = int(input())

def binary_search(target):
    left = 0
    right = n-1

    while left<=right:
        mid = (left+right)//2

        if arr1[mid]==target:
            return 1
        elif arr1[mid]>target:
            right = mid-1
        elif arr1[mid]<target:
            left = mid+1

    return 0


for _ in range(T):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    arr1.sort()

    for i in range(m):
        print(binary_search(arr2[i]))

