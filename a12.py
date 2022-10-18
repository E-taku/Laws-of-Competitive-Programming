N,K = map(int,input().split())

A = list(map(int,input().split()))

# 答えがx以下かを判定し、Yesであればtrue, Noであればfalseを返す関数
def check(x,N,K,A):
    sum = 0
    for i in range(N):
        sum += x // A[i]

    if sum >= K:
        return True
    return False

# 二分探索
Left = 1
Right = 10 ** 9
while Left < Right :
    Mid = (Left + Right) // 2
    Answer = check(Mid,N,K,A)

    if Answer == False:
        Left = Mid + 1
    if Answer == True:
        Right = Mid

print(Left)