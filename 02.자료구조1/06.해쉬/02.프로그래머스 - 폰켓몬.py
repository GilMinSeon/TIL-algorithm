def solution(nums):

    n = len(nums)
    d = dict()
    for x in nums:
        d[x] = 1
    
    if len(d) > n//2:
        return n//2
    else:
        return len(d)
