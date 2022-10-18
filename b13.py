N,K = map(int,input().split())
A = list(map(int,input().split()))

# 累積和
Z = [0] * (N+1)
for i in range(1,N+1):
    Z[i] = A[i-1] + Z[i-1]

# 尺取法
R = [None] * (N+1)

for i in range(1,N+1):
    if i == 1:
        R[i] = 0
    else:
        R[i] = R[i-1]
    
    while R[i] < N  and (Z[R[i]+1]-Z[i-1]) <= K:
        R[i] += 1

ans = 0

for i in range(1,N+1):
    ans += R[i]-(i-1)
print(ans)