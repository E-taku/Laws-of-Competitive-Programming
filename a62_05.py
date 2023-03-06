from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
N, M = map(int,input().split())

# -1 : 白色 , 1 : 青色
WHITE = -1
BLUE = 1
visited = [WHITE] * (N+1)

G = defaultdict(list)

for _ in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
def dfs(pos):
    visited[pos] = BLUE
    for next in G[pos]:
        if visited[next] == WHITE:
            dfs(next)
dfs(1)
ans = "The graph is connected."
for i in range(1,N+1):
    if visited[i] == WHITE:
        ans = "The graph is not connected."
print(ans)
