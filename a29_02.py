MOD = 10**9 + 7

a,b = map(int,input().split())

b = bin(b)[2:]

b = list(b[::-1])
A = [None] * (len(b))
A[0] = a
ans = 1

for i in range(1,len(b)):
    A[i] = (A[i-1] * A[i-1]) % MOD
i = 0
for v in b:
    if v == '1':
        ans = (ans * A[i]) % MOD
    i += 1
print(ans%MOD)