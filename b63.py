from collections import deque

R,C = map(int,input().split())

sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

maze = [list(input()) for _ in range(R)]

maze[sy-1][sx-1] = 0

q = deque()
q.append([sy,sx])

u_r_d_l = [[-1,0],[0,1],[1,0],[0,-1]]
while q:
    pos = q.popleft()
    for to in u_r_d_l:
        y = pos[0] + to[0]
        x = pos[1] + to[1]
        if maze[y-1][x-1] == '#':
            continue
        elif maze[y-1][x-1] == '.':
            maze[y-1][x-1] = maze[pos[0]-1][pos[1]-1] + 1
            q.append([y,x])

print(maze[gy-1][gx-1])