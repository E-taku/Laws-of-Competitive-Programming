N,K = map(int,input().split())

A = list(map(int,input().split()))
A = sorted(A)
dp = [None] * (N+1)

for i in range(N+1):
    for a in A:
        if dp[i] == True:
            continue
        if i >= a and dp[i-a] == False:
            dp[i] = True
        else:
            dp[i] = False
    # print('i',i,'dp=',dp)
# 出力
if dp[N] == True:
	print("First")
else:
	print("Second")