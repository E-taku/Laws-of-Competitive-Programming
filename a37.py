N,M,B = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

sum_C = sum(C)
ans = 0

for i in range(N):
    ans += A[i] * M + sum_C

ans += B * N * M
print(ans)