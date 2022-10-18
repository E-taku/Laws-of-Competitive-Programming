N,W = map(int,input().split())
w = [None] * (N+1)
v = [None] * (N+1)

for i in range(1,N+1):
    tmp_w,tmp_v = map(int,input().split())
    w[i] = tmp_w
    v[i] = tmp_v

dp = [[10**15]*(100001) for _ in range(N+1)]

dp[0][0] = 0

for i in range(1,N+1):
    for j in range(0,100001):
        if j < v[i]:
            dp[i][j] = dp[i-1][j]
        
        if j >= v[i]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]]+w[i])
ans = 0
for i in range(100001):
    if dp[N][i] <= W:
        ans = i
print(ans)