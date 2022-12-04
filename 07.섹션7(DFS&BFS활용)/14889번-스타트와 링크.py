import itertools as it

n = int(input())
arr_n = [x for x in range(1, n+1)]
arr = [list(map(int,input().split())) for _ in range(n)]
res = []
for x in it.combinations(arr_n, n//2):
    combi = list(x)
    sum = 0
    for y in it.combinations(combi, 2):
        sum += arr[y[0]-1][y[1]-1]
        sum += arr[y[1]-1][y[0]-1]
    res.append(sum)

min_val = 2147000000

for i in range(len(res)//2):
    min_val = min(abs(res[i] - res[len(res) - i - 1]), min_val)

print(min_val)

