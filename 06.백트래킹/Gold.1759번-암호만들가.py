L, C = map(int, input().split())
s = list(map(str, input().split()))

aeiou = ['a', 'e', 'i', 'o', 'u']

s.sort()
def DFS(level, start):
    if level == L:
        # 검사
        cnt = 0
        for x in res:
            if x in aeiou:
                cnt += 1

        if 1<=cnt<=L-2:
            print(''.join(res))
    else:
        for i in range(start, C):
            res[level] = s[i]
            DFS(level+1, i+1)

res = [0]*L
DFS(0,0)