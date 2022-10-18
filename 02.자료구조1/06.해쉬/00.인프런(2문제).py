# 08.단어찾기(해쉬)

import sys
input = sys.stdin.readline
n = int(input())
d = dict()

for i in range(n):
    word = input().rstrip()
    d[word] = 1

for i in range(n-1):
    word = input().rstrip()
    d[word] = 0

for key, val in d.items():
    if val == 1:
        print(key)
        break


##================================

# 09.아나그램(해쉬)
import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH[x] != 0:
        print('NO')
        break
else:
    print('YES')

'''
def are_anagrams(a, b):
    counter = {}

    for c in a:
        counter[c] = counter.get(c, 0) + 1

    for c in b:
        counter[c] = counter.get(c, 0) - 1

    return all(n == 0 for n in counter.values())
'''
