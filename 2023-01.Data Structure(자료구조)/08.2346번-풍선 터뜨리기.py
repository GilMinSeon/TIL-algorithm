from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
arr = []
for idx, val in enumerate(tmp):
    arr.append((idx+1, val))

cur = 0
res = []
for _ in range(n):
    i, j = arr.pop(cur)
    res.append(i)

    if j > 0:
        pass
    else:
        pass


print(*res)

'''
5
3 2 1 -3 -1

정답 : 1 4 5 3 2
'''


'''
4
2 2 2 2
    
정답: 1 3 2 4
출력: 1 4 3 2 
'''