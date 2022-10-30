import math
a, b = map(int, input().split())
#print(math.gcd(a, b))
#print(math.lcm(a, b))

def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y%x, x
    return y

g = gcd(a, b)
print(g)
print(a*b // g)