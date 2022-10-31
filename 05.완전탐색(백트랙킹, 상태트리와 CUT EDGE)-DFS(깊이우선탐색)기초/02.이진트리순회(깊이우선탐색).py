def DFS(v):
    if v > 7:
        return
    else:
        # print(v, end = ' ') => 1. 전위순회
        DFS(v*2)
        # print(v, end = ' ') => 2. 중위순회
        DFS(v*2 + 1)
        print(v, end = ' ') # => 3.후위순회

if __name__ == "__main__":
    DFS(1)