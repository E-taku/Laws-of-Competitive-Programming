import bisect
N = int(input())
A = map(int,input().split())
Q = int(input())

A = sorted(A)

for i in range(Q):
    x = int(input())
    print(bisect.bisect_left(A,x))