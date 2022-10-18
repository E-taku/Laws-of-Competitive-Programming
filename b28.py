N = int(input())
MOD = 1000000007

A = [None] * (N+1)
A[1] = 1
A[2] = 1

ans = 0 
for i in range(3,N+1):
    A[i] = (A[i-1] % MOD) + (A[i-2] % MOD)
    A[i] = A[i] % MOD

print(A[-1])