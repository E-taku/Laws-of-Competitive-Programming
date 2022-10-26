from collections import deque

def dfs():
    visited = [ False ] * (N+1)
    dist = [-1] * (N+1)
    dist[1] = 0
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        pos = q.popleft()
        for to in G[pos]:
            if visited[to] == False:
                dist[to] = dist[pos] + 1
                visited[to] = True
                q.append(to)
    return dist
N,M = map(int,input().split())

G = [list() for _ in range(N+1)]

for i in range(1,M+1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

ans = dfs()

for i in ans[1:]:
    print(i)