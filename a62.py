# PyPyだとTLEしたから注意

import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数(pos:現在位置,visited[x]は頂点xを訪れたかどうか)
def dfs(pos,G,visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i,G,visited)

N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

G = [list() for _ in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

# 深さ優先探索
visited = [ False ] * (N + 1)
dfs(1,G,visited)

# 連結かどうかの判定（answer = True のとき連結）
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


