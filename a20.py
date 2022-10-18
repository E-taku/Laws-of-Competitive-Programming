S = input()
T = input()

s_n = len(S)
t_n = len(T)

dp = [[0] * (t_n+1) for _ in range(s_n+1)]

dp[0][0] = 0

for i in range(0,s_n+1):
    for j in range(0,t_n+1):
        if i>=1 and j >= 1 and S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
        elif i>=1 and j >= 1:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        elif i>=1:
            dp[i][j] = dp[i-1][j]
        elif j >= 1:
            dp[i][j] = dp[i][j-1]

print(dp[s_n][t_n])