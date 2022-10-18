N = int(input())
A = list(map(int,input().split()))

d = {}

for i in range(N):
    if A[i] not in d:
        d.setdefault(A[i],1)
    else:
        d[A[i]] += 1
ans = 0

for k in d.keys():
    if d[k] >= 3:
        v = d[k]
        ans += (v*(v-1)*(v-2))/6

print(int(ans))