# 1) while문

def next_permutation(arr):
    i, j = len(arr)-1, len(arr)-1

    while i>0 and arr[i-1]>=arr[i]:
        i -= 1
    
    if i == 0:
        return False

    while arr[i-1]>=arr[j]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    k = len(arr)-1

    while i<k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1
    
    return arr
'''
1.arr[i-1] >= arr[i]가 되는 i 중 제일 큰 값을 찾는다
  i가 0이 되면 [3 2 1]같이 역으로 정렬되어 있는 값이라 순열의 끝 False 반환
2. arr[i-1] >= arr[j] 가 되는 j 중 가장 큰 값 찾는다
  이때 1번에서 arr[i-1] >= arr[i]를 찾았기때문에 무조건 i<j이다
3. arr[i], arr[j] 바꿔준다
4. arr[i]번째부터 끝까지의 원소를 뒤집는다
'''
