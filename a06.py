N,Q = map(int,input().split())
A = list(map(int,input().split()))
visited_n = [0]

for i in range(N):
    visited_n.append(A[i]+ visited_n[i])


for i in range(Q):
    l,r = map(int,input().split())
    print(visited_n[r] - visited_n[l-1])