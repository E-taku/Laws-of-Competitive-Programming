N = int(input())
A = list(map(int,input().split()))
Q = int(input())

win_n = [0]

for i in range(N):
    win_n.append(win_n[i] + A[i])

for i in range(Q):
    l,r = map(int,input().split())
    diff_n = r - l + 1
    diff_v = win_n[r] - win_n[l-1]
    if diff_v > (diff_n / 2) :
        print("win")
    elif diff_v == (diff_n / 2) :
        print("draw")
    else:
        print("lose")

