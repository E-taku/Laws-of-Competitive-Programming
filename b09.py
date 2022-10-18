N = int(input())

Z = [[0]*(1500+2) for _ in range(1500+2)]

for i in range(N):
    a,b,c,d = map(int,input().split())
    Z[b+1][a+1] += 1
    Z[d+1][c+1] += 1
    Z[b+1][c+1] -= 1
    Z[d+1][a+1] -= 1

for i in range(1,1500+2):
    for j in range(1,1500+2):
        Z[i][j] += Z[i][j-1]

for i in range(1,1500+2):
    for j in range(1,1500+2):
        Z[i][j] += Z[i-1][j]

ans = 0

for i in range(1502):
    for j in range(1502):
        if Z[i][j] > 0 :
            ans += 1
print(ans)