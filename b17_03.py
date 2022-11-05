N = int(input())
h = [0] + list(map(int,input().split()))

dp = [0] * (N+1)

dp[1] = 0
dp[2] = abs(h[2] - h[1])
for i in range(3,N+1):
    dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]) ,dp[i-1] + abs(h[i] - h[i-1]) )

now = N
ans = []
while True:
    ans.append(now)
    if now == 1:
        break

    if dp[now] == (dp[now-2] + abs(h[now] - h[now-2])):
        now -= 2
    else:
        now -= 1
print(len(ans))
print(*list(reversed(ans)))