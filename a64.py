import heapq

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 隣接リストの作成（重み付きグラフなので、各辺について (隣接頂点, 重み) のタプルを記録する）
G = [ list() for i in range(N + 1) ]
for a, b, c in edges:
	G[a].append((b, c))
	G[b].append((a, c))

Inf = 10**10
cur = [Inf] * (N+1)
kakutei = [ False ] * (N + 1)
pos = 1
cur[pos] = 0

Q = []
heapq.heapify(Q)

heapq.heappush(Q, (cur[pos],pos) )
while Q:
    pos = heapq.heappop(Q)[1]

    # Qの最小要素が既に確定した頂点の場合
    if kakutei[pos] == True:
        continue

    # cur[x] の値を更新する
    # 優先度付きキューを用いてるから最小のものになってる
    kakutei[pos] = True

    for next in G[pos]:
        next_p = next[0]
        cost = next[1]
        if cur[next_p] > cur[pos] + cost:
            cur[next_p] = cur[pos] + cost
            heapq.heappush(Q, (cur[next_p],next_p))

for i in range(1,N+1):
    if cur[i] == Inf:
        print(-1)
    else:
        print(cur[i])
