D,N = map(int,input().split())

L = [None] * (N+1)
R = [None] * (N+1)
H = [None] * (N+1)

for i in range(1,N+1):
    L[i],R[i],H[i] = map(int,input().split())

lim = [24] * (D)

for i in range(1,N+1):
    for j in range(L[i],R[i]+1):
        lim[j-1] = min(lim[j-1],H[i])

print(sum(lim))