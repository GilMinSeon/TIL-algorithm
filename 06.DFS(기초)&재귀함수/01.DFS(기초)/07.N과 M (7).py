def DFS(L):
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(0, n):
            res[L] = a[i]
            DFS(L+1)

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

res = [0]*m 

DFS(0)


# 다른 사람 풀이 => 이게 확실히 빠름!
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

out = []
def solve(cnt, data):
    # m 번 모두 뽑았으면 결과를 출력
    if cnt == m:
        print(" ".join(map(str, out)))
        return
        
    for num in data:
        out.append(num)
        solve(cnt + 1, data)
        out.pop()        
        
solve(0, data)    
'''