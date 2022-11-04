import heapq

Q = int(input())

p = []
heapq.heapify(p)
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        heapq.heappush(p,q[1])
    elif q[0] == 2:
        # ↓ソートされてるわけではないがp[0]とするとO(1)で最小値を取得できる
        print(p[0])
    else:
        heapq.heappop(p)
