
from collections import deque

R,C = map(int,input().split())

sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

c = [list(input()) for _ in range(R)]

def dfs():
    c[sy-1][sx-1] = 0
    pos = (sy-1,sx-1)
    t_r_b_l = [[-1,0],[0,1],[1,0],[0,-1]]
    q = deque()
    q.append(pos)

    while q:
        pos = q.popleft()
        for to in t_r_b_l:
            y = pos[0]+ to[0]
            x = pos[1]+ to[1]
            to = (y,x)
            if c[to[0]][to[1]] == '#':
                continue
            elif c[to[0]][to[1]] == '.':
                q.append(to)
                c[to[0]][to[1]] = c[pos[0]][pos[1]] + 1
    return c
c = dfs()

print(c[gy-1][gx-1])