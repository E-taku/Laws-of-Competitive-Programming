from collections import deque
from collections import defaultdict

N,M = map(int,input().split())

# 隣接リストの作成
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
    for nxt in G[pos]:
        if dist[nxt] == -1:
            dist[nxt] = dist[pos] + 1
            Q.append(nxt)
# 頂点 1 から各頂点までの最短距離を出力
for i in range(1, N + 1):
	print(dist[i])


