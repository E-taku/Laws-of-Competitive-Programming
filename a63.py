from collections import deque

N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

G = [list() for _ in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

q = deque()
q.append(1)

dist = [-1] * (N+1)
dist[1] = 0

while q:
    pos = q.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)

for i in dist[1:]:
    print(i)

