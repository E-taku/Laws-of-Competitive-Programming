from collections import defaultdict

N, M = map(int,input().split())

G = defaultdict(list)

for _ in range(M):
    a, b = map(str,input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N+1):
    ans = "{" + ", ".join(G[str(i)]) + "}"
    print(f"{i}: {ans}")
