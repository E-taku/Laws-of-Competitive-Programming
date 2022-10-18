N = int(input())
A = list(map(int,input().split()))

dp = [ [None] * (i) for i in range(N+1)]

for i in range(N):
    dp[N][i] = A[i]

for i in reversed(range(1,N)):
    for j in range(i):
        if i % 2 == 1:
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])

print(dp[1][0])