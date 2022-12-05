val = input()
n = 0
if len(val) <= 9:
    n = len(val)
else:
    n = (len(val) - 9)//2 + 9

res = [0]*n
ch = [0]*(n+1)

def DFS(L):
    global cnt

    if L == n:
        tmp = ''
        for j in range(L):
            #print(res[j], end=' ')
            tmp += str(res[j])
        print()
        if tmp == val:
            print(tmp)

    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

DFS(0)