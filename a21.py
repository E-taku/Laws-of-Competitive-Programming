# N = int(input())
# P = [None] * (N+1)
# A = [None] * (N+1)

# for i in range(1,N+1):
#     P[i],A[i] = map(int,input().split())

# dp = [[None] * (N+1) for _ in range(N+1)]

# dp[1][N] = 0

# for LEN in reversed(range(0,N-1)):
#     for l in range(1,N-LEN+1):
#         r = l + LEN
#         # score1 の値（l-1 番目のブロックを取り除くときの得点）を求める
#         score1 = 0
#         if l >= 2 and l<=P[l-1] and P[l-1]<=r:
#             score1 = A[l-1]
        
#         # score2 の値（r+1 番目のブロックを取り除くときの得点）を求める
#         score2 = 0
#         if r<=N-1 and l<=P[r+1] and P[r+1]<=r:
#             score2 = A[r+1]

# わからないので後で詳しくやる