from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
N, M = map(int,input().split())

# -1 : 白色 , 1 : 青色

WHITE = -1 # 辿ってない
BLUE = 1   # 辿った
visited = [WHITE] * (N+1)

G = defaultdict(list)

for _ in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

path = []

def dfs(pos: int):
    path.append(str(pos))
    # ゴールに辿り着いた
    if pos == N:
        print(" ".join(path))

    visited[pos] = BLUE
    for next in G[pos]:
        if visited[next] == WHITE:
            dfs(next)
    path.pop()

dfs(1)
