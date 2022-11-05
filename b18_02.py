N,S = map(int,input().split())

A = [0] + list(map(int,input().split()))

dp = [[False] * (S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(1,N+1):
    for j in range(S+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
            if j + A[i] <= S:
                dp[i][j+A[i]] = True

if dp[N][S] == True:
    place = S
    ans = []
    for i in reversed(range(1,N+1)):
        if dp[i-1][place] == True:
            place = place - 0
        else:
            place = place - A[i]
            ans.append(i)
    print(len(ans))
    print(*list(reversed(ans)))
else:
    print(-1)