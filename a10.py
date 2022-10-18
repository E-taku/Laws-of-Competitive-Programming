N = int(input())

A = list(map(int,input().split()))

D = int(input())

L = []
R = []
for i in range(D):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

P = [None] *  (N)
Q = [None] *  (N)

P[0] = A[0]
Q[N-1] = A[N-1]

for i in range(1,N):
    P[i] = max(P[i-1],A[i])
for i in reversed(range(0,N-1)):
    Q[i] = max(Q[i+1],A[i])

for d in range(D):
    print(max(P[(L[d]-1)-1], Q[(R[d]+1)-1]))