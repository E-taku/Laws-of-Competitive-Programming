D = int(input())
N = int(input())

attendees = [0] * (D+2)

for i in range(N):
    l,r = map(int,input().split())
    attendees[l] += 1
    attendees[r+1] -= 1

for i in range(D):
    attendees[i+1] += attendees[i]
    print(attendees[i+1])