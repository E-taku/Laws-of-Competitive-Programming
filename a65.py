
N = int(input())
# 社員2から読み込みたいので
A = [0] * 2 + list(map(int,input().split()))

# 隣接リストの作成
G = [list() for _ in range(N+1)]

for i in range(2,N+1):
    G[A[i]].append(i)

dp = [0] * (N+1)

print(G)
print(dp)

for i in range(N,0,-1):
    for j in G[i]:
        dp[i] += dp[j] + 1
print(*dp[1:])