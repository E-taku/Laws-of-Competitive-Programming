import bisect

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

# 半分全列挙
P = []
Q = []

for i in range(N):
    for j in range(N):
        P.append(A[i] + B[j])
        Q.append(C[i] + D[j])

Q = sorted(Q)
# 二分探索

for i in range(len(P)):
    pos1 = bisect.bisect_left(Q,K-P[i])
    if pos1<N*N and Q[pos1] == K-P[i]:
        print("Yes")
        exit()
print("No")