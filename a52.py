from collections import deque

Q = int(input())
d = deque()
for i in range(Q):
    s = list(input().split())
    if s[0] == '1':
        d.append(s[1])
    elif s[0] == '2':
        print(d[0])
    else:
        d.popleft()
