import bisect

N = int(input())
A = list(map(int,input().split()))

sort_A = sorted(set((A)))
B = []

for i in range(N):
    pos = bisect.bisect(sort_A,A[i])
    B.append(pos)

print(*B)
