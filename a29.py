a,b = map(int,input().split())

MOD = 1000000007

ans = 1

b_bin = bin(b)[2:]
A = [None] * (len(b_bin))

A[0] = a
for i in range(1,len(b_bin)):
    A[i] = (A[i-1] *  A[i-1]) % MOD

i = 0
for c in reversed(b_bin):
    if c == '1':
        ans = (ans * A[i]) % MOD
    i += 1 
print(ans)


# # a の b 乗を m で割った余りを返す関数
# def Power(a, b, m):
# 	p = a
# 	Answer = 1
# 	for i in range(30):
# 		wari = 2 ** i
# 		if (b // wari) % 2 == 1:
# 			Answer = (Answer * p) % m # a の 2^i 乗が掛けられるとき
# 		p = (p * p) % m
# 	return Answer

# # 入力
# a, b = map(int, input().split())

# # 出力
# print(Power(a, b, 1000000007))