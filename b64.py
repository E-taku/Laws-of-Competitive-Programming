# import heapq

# N,M = map(int,input().split())

# edges = [list(map(int,input().split())) for _ in range(M)]

# G = [list() for _ in range(N+1)]
# # 隣接リストの作成 (重み付きグラフなので、確変について（隣接焦点、重み）のタプルを記録する)
# for a,b,c in edges:
#     G[a].append((b,c))
#     G[b].append((a,c))

# Inf = 10**10
# cur = [Inf] * (N+1)
# kakutei = [False] * (N+1)
# pos = 1
# cur[pos] = 0

# Q = []
# heapq.heapify(Q)

# heapq.heappush(Q,(cur[pos],pos))

# while Q:
#     pos = heapq.heappop(Q)[1]
    
    
