H,W,N = map(int,input().split())

# 累積和（０で初期化）
Z = [[0] * (W+2) for _ in range(H+2)]

for i in range(N):
    a,b,c,d = map(int,input().split())
    Z[a][b] += 1
    Z[a][d+1] -= 1
    Z[c+1][d+1] += 1
    Z[c+1][b] -= 1

for i in range(1,H+2):
    for j in range(1,W+2):
        Z[i][j] += Z[i][j-1]
        
for i in range(1,H+2):
    for j in range(1,W+2):
        Z[i][j] += Z[i-1][j]

for i in range(1,H+1):
    print(*(Z[i][1:-1]))