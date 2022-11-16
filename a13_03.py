N,K = map(int,input().split())

A = list(map(int,input().split()))

R = [None] * (N)

for i in range(N):
    left = i 
    if i == 0:
        R[0] = 0
    else:
        R[i] = R[i-1]
    while R[i] < N and (A[R[i]] - A[left]) <= K:
        R[i] += 1

ans = 0
for i in range(1,N+1):
    ans += (R[i-1] - i)
print(ans)
