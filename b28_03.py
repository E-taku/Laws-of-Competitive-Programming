N = int(input())
MOD = 1000000007

A = [0] * (N+1)
A[1] = 1
A[2] = 1

for i in range(3,N+1):
    A[i] = (A[i-1] + A[i-2]) % MOD
print(A[N])
