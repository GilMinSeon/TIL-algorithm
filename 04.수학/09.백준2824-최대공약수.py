import sys
input = sys.stdin.readline

def gcd(a,b) :
    x, y = a, b
    while x:
        x, y = y%x, x
    return y

def multiply(arr) :
    mul = 1
    for x in arr:
        mul *= x
    return mul

n = int(input())
arr_n = list(map(int, input().split()))

m = int(input())
arr_m = list(map(int, input().split()))

a = multiply(arr_n)
b = multiply(arr_m)

#print('%s'%str(gcd(a,b))[-9:])
print(str(gcd(a,b))[-9:])

'''
[첫번째 방법] { % 문자열 포매팅 }
print('%s %s' % ('one', 'two'))
%s가 문자열을 대체해주고, %로 둘을 연결하여 뒤에서 string의 값을 넣어준다.
output :
one two
'''