N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


dp = [0] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3,N+1):
    dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])

now = N
ans = []

while True:
    ans.append(now)
    if now == 1:
        break
    if dp[now-1] + A[now-2] == dp[now]:
        now = now-1
    else:
        now = now-2
ans = list(reversed(ans))
print(len(ans))
print(*ans)
