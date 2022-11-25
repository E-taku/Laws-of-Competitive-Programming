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
def dfs(pos: int):
    visited[pos] = True
    
    for next in G[pos]:
        if visited[next] == False:
            dfs(next)

dfs(1)
for i in range(1,N+1):
    if visited[i] == False:
        print('The graph is not connected.')
        exit()
print('The graph is connected.')
