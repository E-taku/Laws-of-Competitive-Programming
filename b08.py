N = int(input())

xy = [[0 for _ in range(1501)] for _ in range(1501)]
for i in range(N):
    x, y = map(int, input().split())
    xy[x][y] += 1

for i in range(1, 1501):
    for j in range(1, 1501):
        xy[i][j] = xy[i][j-1] + xy[i][j]
for j in range(1, 1501):
    for i in range(1, 1501):
        xy[i][j] = xy[i-1][j] + xy[i][j]

Q = int(input())
for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = xy[a-1][b-1] + xy[c][d] - xy[a-1][d] - xy[c][b-1]
    print(ans)




# 以下RE
# N = int(input())

# # 各座標にある点の数
# S = [[0 for _ in range(1501)] for _ in range(1501) ]
# # 二次元累積和 
# T = [[0]*(1501) for _ in range(1501) ]
# X = []
# Y = []
# for i in range(N):
#     x,y = map(int,input().split())
#     X.append(x)
#     Y.append(y)
#     # X[i] = x
#     # Y[i] = y
# Q = int(input())
# A = [None for _ in range(1501)]
# B = [None for _ in range(1501)] 
# C = [None for _ in range(1501)]
# D = [None for _ in range(1501)]
# for i in range(1,Q+1):
#     A[i],B[i],C[i],D[i] = map(int,input().split())

# # 各座標にある点の数を数える
# for i in range(N):
#     S[X[i]][Y[i]] += 1

# # 累積和をとる
# for i in range(1,1501):
#     for j in range(1,1501):
#         T[i][j] = T[i][j-1] + S[i][j]

# for i in range(1,1501):
#     for j in range(1,1501):
#         T[i][j] = T[i-1][j] + T[i][j]

# for i in range(1,Q+1):
#     ans = T[C[i]][D[i]] + T[A[i]-1][B[i]-1] - T[C[i]][B[i]-1] - T[A[i]-1][D[i]]
#     print(ans)

