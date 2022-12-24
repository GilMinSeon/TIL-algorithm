# 결정알고리즘
# 강의안보고 먼저 풀어서 맞춤! 테스트 5개 모두 통과!!!
# -> 노노, 반례 틀린거 동일하게 틀림 ㅠㅠ 나중에 꼭 다시 보자!

n, m = map(int, input().split()) #n개의 곡, m개의 dvd
arr = list(map(int, input().split()))

tot = sum(arr)
max_val = max(arr)

left = 1
right = tot

def fn_count(len):
    tmp = 0
    cnt = 1
    for i in range(0, n-1):
        tmp += arr[i]
        if (tmp + arr[i+1]) > len:
            cnt += 1
            tmp = 0
    return cnt

while left <= right:
    mid = (left + right) // 2

    val = fn_count(mid)
    
    # 반례를 고려 못함
    # if val > m:
    #     left = mid + 1
    # else:
    #     right = mid - 1
    #     res = min(res, mid)

    if mid >= max_val and val <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
