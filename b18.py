N,S = map(int,input().split())
A = list(map(int,input().split()))

# 動的計画法(i=0)

dp = [[None] * (S+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(1,N+1):
    for j in range(0,S+1):
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
            
        if j >= A[i-1]:
            if dp[i-1][j-A[i-1]] == True or dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

# 選び方が存在しない場合
if dp[N][S] == False:
    print(-1)
    exit()

# 答えの復元
Answer = []
Place = S

for i in reversed(range(1,N+1)):
    if dp[i-1][Place] == True:
        Place = Place - 0 # カードを選ばない
    else:
        Place = Place - A[i-1] # カードiを選ぶ
        Answer.append(i)

Answer.reverse()

print(len(Answer))
print(*Answer)
