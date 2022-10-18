from collections import deque

S = list(input())
n = len(S)
d = deque()

for i in range(n):
    if S[i] == '(':
        d.append(i+1)
    if S[i] == ')':
        print(d.pop(),i+1)
