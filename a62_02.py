import sys
sys.setrecursionlimit(120000)

N,M = map(int,input().split())


G = [list() for _ in range(N+1)]

for i in range(1,M+1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)

def dfs(pos,G,visited):
    visited[pos] = True
    for nex in G[pos]:
        if visited[nex] == False:
            dfs(nex,G,visited)
    return 0

dfs(1,G,visited)

answer = True
for i in range(1,N+1):
    if visited[i] == False:
        answer = False
        break

# 答えの出力
if answer == True:
	print("The graph is connected.")
else:
	print("The graph is not connected.")
