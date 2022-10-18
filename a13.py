N,K = map(int,input().split())
A = list(map(int,input().split()))

R = [None] * N

# しゃくとり法
for i in range(N-1):
    # スタート地点を決める
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i-1]
    
    # ギリギリまで増やしていく
    while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
        R[i] += 1

ans = 0
for i in range(N-1):
    ans += (R[i] - i)
print(ans)