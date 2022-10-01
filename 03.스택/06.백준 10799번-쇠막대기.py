import sys
input = sys.stdin.readline

s = input()
stk = []
cnt = 0

for i in s:
    if i == '(':
        stk.append(i)
    else:
        if not stk: break
        
        stk.pop()
        if prev == '(':
            cnt += len(stk)
        else:
            cnt += 1

    prev = i
            
print(cnt)

        
