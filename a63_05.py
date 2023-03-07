from collections import defaultdict
from collections import deque

N,M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


INF = -1
dist = [INF] * (N)
d = deque()
d.append(0)
dist[0] = 0
def bfs():
    while d:
        pos = d.popleft()
        for to in G[pos]:
            if dist[to] == INF: #未確認頂点
                dist[to] = dist[pos] + 1
                d.append(to)
    return dist
dist = bfs()

for i in dist:
    print(i)
