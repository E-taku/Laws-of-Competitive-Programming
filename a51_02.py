from collections import deque

Q = int(input())
que = []
for i in range(Q):
    l = list(input().split())
    if l[0] == '1':
        que.append(l[1])
    elif l[0] == '2':
        print(que[-1])
    else:
        que.pop()

