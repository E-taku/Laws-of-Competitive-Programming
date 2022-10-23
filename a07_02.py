D = int(input())
N = int(input())

ans = [0] * (D+2)
for i in range(1,N+1):
    l,r = map(int,input().split())
    ans[l] += 1
    ans[r+1] -= 1


for i in range(1,D+1):
    ans[i] += ans[i-1]
    print(ans[i])