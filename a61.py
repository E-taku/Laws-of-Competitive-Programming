N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

# 隣接リストの作成
G = [list() for _ in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

for i in range(1,N+1):
    ans = str(i) + ': {' + ", ".join(map(str,G[i])) + '}'
    print(ans)