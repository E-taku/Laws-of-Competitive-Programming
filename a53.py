import heapq
Q = int(input())

d = []
for i in range(Q):
    s = list(input().split())
    if s[0] == '1':
        heapq.heappush(d,int(s[1]))
    elif s[0] == '2':
        print(d[0])
    else:
        heapq.heappop(d)


