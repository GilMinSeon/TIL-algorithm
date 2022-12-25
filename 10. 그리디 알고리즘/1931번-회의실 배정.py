import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1], x[0]))

last = 0
cnt = 0

for s, e in meeting:
    if s >= last:
        cnt += 1
        last = e
    
print(cnt)
