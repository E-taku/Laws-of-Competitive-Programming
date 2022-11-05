S = [''] + list(input())
T = [''] + list(input())

dp = [ [0] * (len(T)) for _ in range(len(S)) ]
dp[0][0] = 0

for i in range(1,len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])

