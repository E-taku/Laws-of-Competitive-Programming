import bisect
import sys

# 「配列 A にあるカードからいくつか選んだときの合計」として考えられるものを列挙
# ビット全探索を使う
def Enumerate(A):
    SumList = []
    for i in range(1<<len(A)):
        sum = 0
        for j in range(len(A)):
            wari = (2 ** j)
            if (i // wari) % 2 == 1:
                sum += A[j]
        SumList.append(sum)
    return SumList


N,K = map(int,input().split())
A = list(map(int,input().split()))

# カードを半分ずつに分ける
L1 = A[0:(N//2)]
L2 = A[(N//2):N]
Sum1 = Enumerate(L1)
Sum2 = Enumerate(L2)
Sum1.sort()
Sum2.sort()

for i in range(len(Sum1)):
    pos = bisect.bisect_left(Sum2,K-Sum1[i])
    if pos <len(Sum2) and K-Sum1[i] == Sum2[pos]:
        print("Yes")
        exit()
print("No")