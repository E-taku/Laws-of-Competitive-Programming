from collections import deque

R, C = map(int,input().split())

sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1

maze = [list(map(str,input())) for _ in range(R)]
maze[sy][sx] = 0

# ←↓↑→
direc = [(0,-1),(1,0),(-1,0),(0,1)]

start_pos = (sy,sx)
Q = deque()
Q.append(start_pos)

while Q:
    pos = Q.popleft()
    pos_y = pos[0]
    pos_x = pos[1]
    for y, x in direc:
        to_y = pos_y + y
        to_x = pos_x + x
        if 0 <= to_y <= R-1 and 0 <= to_x <= C-1 and maze[to_y][to_x] == ".":
            maze[to_y][to_x] = maze[pos_y][pos_x] + 1
            Q.append((to_y,to_x))
print(maze[gy][gx])
