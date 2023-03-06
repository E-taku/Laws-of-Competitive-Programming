from collections import defaultdict

N, M = map(int,input().split())

G = defaultdict(list)

for _ in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

f = 0
ans = -1
for i in range(1, N+1):
    if f < len(G[i]):
        ans = i
    f = max(f, len(G[i]))

print(ans)
