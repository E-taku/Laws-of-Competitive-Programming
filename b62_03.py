import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

N,M = map(int,input().split())

G = defaultdict(list)

for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)
path = []
def dfs( i: int,):
    path.append(i)
    if i == N:
        print(*path)
        exit()
    visited[i] = True
    for next in G[i]:
        if visited[next] == False:
            dfs(next)
    path.pop()

dfs(1)

