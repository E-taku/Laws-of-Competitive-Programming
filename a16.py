N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [None] * (N)

dp[0] = 0

for i in range(1,N):
    if i == 1:
        dp[i] = A[i-1]
    else:
        dp[i] = min(dp[i-1]+A[i-1],dp[i-2]+B[i-2])
print(dp[-1])
        