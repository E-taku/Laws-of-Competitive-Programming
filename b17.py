N = int(input())
h = list(map(int,input().split()))

dp = [None] * (N+1)

dp[1] = 0
dp[2] = abs(h[1]-h[0])

for i in range(3,N+1):
    dp[i] = min( abs( h[i-1] - h[i-3] ) + dp[i-2] , abs(h[i-1] - h[i-2]) + dp[i-1])


Place = N
ans = []

while True:
    ans.append(Place)

    if Place == 1:
        break
    
    if dp[Place] == abs(h[Place-1] - h[Place-2]) + dp[Place-1]:
        Place = Place - 1
    else:
        Place = Place -2
ans.reverse()

print(len(ans))
print(*ans)