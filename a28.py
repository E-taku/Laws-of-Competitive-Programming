N = int(input())

MOD = 10000
ans = 0 

T = [None] * N
A = [None] * N

for i in range(N):
    T[i] , A[i] = input().split()
    A[i] = int(A[i])

    if T[i] == '+':
        ans += (A[i] % MOD)
    elif T[i] == '-':
        ans -= (A[i] % MOD)
    else:
        ans *= (A[i] % MOD)
    ans = ans % MOD
    print(ans)

