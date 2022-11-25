from collections import defaultdict
import heapq

N,M = map(int,input().split())

G = defaultdict(list)

for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))

# 配列・キューの初期化（キューには（距離、頂点番号）のタプルを記録する）
INF = 10 ** 10
kakutei = [False] * (N + 1)
cur = [INF] * (N + 1)
cur[1] = 0

Q = []
heapq.heappush(Q,(cur[1],1))

# ダイクストラ法
while (len(Q)) >= 1:
    # 次に確定させる頂点を求める
    # (ここでは、優先度付きキューQの最小要素を取り除き、その要素の２番目の値（頂点番号）をposに代入する）
    pos = heapq.heappop(Q)[1]

    # Qの最小要素が既に確定した頂点jの場合
    if kakutei[pos] == True:
        continue

    # cur[x]の値を更新する
    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q,(cur[e[0]],e[0]))

# 答えを出力
for i in range(1,N+1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print(-1)






