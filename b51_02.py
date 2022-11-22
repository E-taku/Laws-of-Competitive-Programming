from collections import deque

S = list(input())

que = deque()

for i in range(len(S)):
    if S[i] == '(':
        que.append(i+1)
    else:
        print(que.pop(),i+1)

