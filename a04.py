N = int(input())

ans = bin(N)[2:]

n = 10 - len(ans)
ans = '0'*n + ans
print(ans)