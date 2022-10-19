import sys

sys.setrecursionlimit(10**7)

N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

G = [list() for _ in range(N+1)]
visited = [False] * (N+1)
path = []
def dfs(i:int):
    path.append(i)
    if i == N:
        print(*path)
        exit()

    visited[i] = True
    for j in G[i]:
        if visited[j] == False:
            dfs(j)

    path.pop()


for a,b in edges:
    G[a].append(b)
    G[b].append(a)


dfs(1)
