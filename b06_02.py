N = int(input())

A =[0] + list(map(int,input().split()))

hit = [0] * (N+1)

for i in range(1,N+1):
    hit[i] = hit[i-1] + A[i]

Q = int(input())


for i in range(1,Q+1):
    l,r = map(int,input().split())
    day = r - l + 1

    hit_n = hit[r] - hit[l-1]
    no_hit_n = day - hit_n

    if hit_n > no_hit_n:
        print('win')
    elif  hit_n < no_hit_n:
        print('lose')
    else:
        print('draw')

