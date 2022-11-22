import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict


N,M = map(int,input().split())

G = defaultdict(list)

for i in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    G[B].append(A)
visited = [False] * (N+1)
path = []

def dfs(i: int):
    path.append(i)

    # ゴール地点にたどり着いた
    if i == N:
        print(*path)
        exit()

    # その他の場合
    visited[i] = True
    for j in G[i]:
        if visited[j] == False:
            dfs(j)
    path.pop()
dfs(1)



