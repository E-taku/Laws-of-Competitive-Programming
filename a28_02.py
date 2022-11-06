MOD = 10000 
ans = 0

N = int(input())

for i in range(N):
    t,a = input().split()
    a = int(a)
    if t == "+":
        ans = (ans + a) % MOD
    elif t == "-":
        ans = (ans - a) % MOD
    else:
        ans = (ans * a) % MOD
    print(ans)