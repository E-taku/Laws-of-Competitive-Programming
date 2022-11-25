from collections import deque
R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

maze = [list(input()) for _ in range(R)]

# (y,x) ←↓↑→
directions = [(0,-1),(1,0),(-1,0),(0,1)]


maze[sy-1][sx-1] = 0

Q = deque()
Q.append((sy-1,sx-1))

while Q:
    pos = Q.popleft()
    for y,x in directions:
        y = pos[0] + y
        x = pos[1] + x
        to = (y,x)
        if maze[y][x] == '#':
            continue
        if maze[y][x] == '.':
            maze[y][x] = maze[pos[0]][pos[1]] + 1
            Q.append(to)

print(maze[gy-1][gx-1])
