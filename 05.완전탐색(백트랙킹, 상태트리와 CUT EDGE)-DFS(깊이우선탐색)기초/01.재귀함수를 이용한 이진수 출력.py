# output => 1011

# 내 코드
'''
def DFS(x):
    if x > 0:
        DFS(x//2)
        print(x % 2, end ='')
n = int(input())
DFS(n)
'''

# 강의 코드
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x%2, end='')

if __name__ == "__main__":
    n = int(input())
    DFS(n)