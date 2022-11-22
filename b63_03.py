from collections import deque

R,C = map(int,input().split())

s_x, s_y = map(int,input().split())
g_x, g_y = map(int,input().split())

c = [list(input()) for _ in range(R) ]


c[s_y-1][s_x-1] = 0

Q = deque()
Q.append([s_y,s_x])

direct = [[-1,0],[0,-1],[1,0],[0,1]] # ←　↑　→ ↓

while Q:
    pos = Q.popleft()
    
    for y,x in direct:
        y = pos[0] + y
        x = pos[1] + x
        to = [y,x]
        if c[to[0]][to[1]] == '#':
                continue
        if c[to[0]][to[1]] == '.':
            c[to[0]][to[1]] = c[pos[0]][pos[1]] + 1
            Q.append(to)
for i in range(R):
    print(c[i])
print(c[g_y-1][g_x-1])