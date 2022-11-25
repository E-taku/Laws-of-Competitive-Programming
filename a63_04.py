from collections import defaultdict
from collections import deque

N,M = map(int,input().split())

G = defaultdict(list)

for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N+1)
dist[1] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while Q:
    pos = Q.popleft()
    for next in G[pos]:
        if dist[next] == -1:
            dist[next] = dist[pos] + 1
            Q.append(next)

for i in range(1,N+1):
    print(dist[i])
