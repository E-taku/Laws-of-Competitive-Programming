import sys
sys.setrecursionlimit(10**7)


from collections import defaultdict

N,M = map(int,input().split())

G = defaultdict(list)

for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)
def dfs(pos: int):
    visited[pos] = True
    for to in G[pos]:
        if visited[to] == False:
            dfs(to)

dfs(1)
ans = 'The graph is connected.'
for i in range(1,N+1):
    if visited[i] == False:
        ans = ('The graph is not connected.')

print(ans)
