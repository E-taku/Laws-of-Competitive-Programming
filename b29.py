a,b = map(int,input().split())

MOD = 1000000007

ans = 1

b_bin = bin(b)[2:]
A = [None] * (len(b_bin))

A[0] = a
for i in range(1,len(b_bin)):
    A[i] = (A[i-1] *  A[i-1]) % MOD

i = 0
for c in reversed(b_bin):
    if c == '1':
        ans = (ans * A[i]) % MOD
    i += 1 
print(ans)