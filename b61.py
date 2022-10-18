N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

G = [list() for _ in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(1,N+1):
    if ans <= len(G[i]):
        ans = len(G[i])
        n = i
print(n)
