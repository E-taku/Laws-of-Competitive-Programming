N,Q = map(int,input().split())
A = [0] + list(map(int,input().split()))

visited_n = [0] * (N+1)

for i in range(1,N+1):
    visited_n[i] = visited_n[i-1] + A[i]

for i in range(Q):
    l,r = map(int,input().split())
    ans = visited_n[r] - visited_n[l-1]
    print(ans)
