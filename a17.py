N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [None] * (N+1)

dp[1] = 0
dp[2] = A[0]

for i in range(3,N+1):
    dp[i] = min(dp[i-2]+B[i-3],dp[i-1]+A[i-2])

# 答えの復元
# 変数Place は現在位置（ゴールから進んでいく）
# 例えば入力例の場合、Placeは5,4,2,1と変化していく

Answer = []
Place = N

while True:
    Answer.append(Place)
    if Place == 1:
        break

    # どこから部屋Placeに向かうのが最適解か求める
    if dp[Place-1] + A[Place-2] == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2
Answer.reverse()


print(len(Answer))
print(*Answer)
