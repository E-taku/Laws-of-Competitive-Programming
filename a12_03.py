N,K = map(int,input().split())

A = list(map(int,input().split()))

A = sorted(A)

# 答えが x 以下か判定し Yes であれば True No であれば False を返す
def check(x: int) -> bool:
    sum = 0
    for i in range(N):
        sum += x // A[i]

    if sum >= K:
        return True
    return False

L = 0
R = 10**9 + 1

while L < R:
    Mid = (L + R) // 2
    ans = check(Mid)
    if ans:
        R = Mid
    else:
        L = Mid + 1

print(L)
