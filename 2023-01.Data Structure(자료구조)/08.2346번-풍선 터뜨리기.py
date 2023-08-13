from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
arr = []
for idx, val in enumerate(tmp):
    arr.append((idx+1, val))

cur = 0
res = []
for x in range(n):
    i, j = arr.pop(cur)

    #print('i==>', i, 'j===>', j, 'cur===>', cur)

    #i, j = arr[cur]
    res.append(i)
    #print(i, j, cur)

    if len(arr) == 1:
        res.append(arr[0][0])
        break


    if j > 0:
        # j가 양수일때
        if j > len(arr):
            cur = cur % len(arr)
        elif len(arr) == j:
            cur = 0
        else:
            cur += (j-1)

    else:
        # j가 음수일때
        if abs(j) >= len(arr) and cur > abs(j):
            cur = len(arr) + j + cur
            # 2 -1 +2 3
        else:
            #print('x===>', x, 'cur===>', cur, 'j=====>', j)
            cur += j

    if cur < 0:
        cur = len(arr) - 1

    #print('변한 cur--->', cur)
    
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