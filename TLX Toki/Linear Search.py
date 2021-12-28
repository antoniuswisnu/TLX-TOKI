n,d = list(map(int,input().split()))
data = []

for i in range(n):
    a = int(input())
    data.append(a)

for j in range(n):
    if data[j] == d:
        print(j)
        break
    elif d not in data:
        print(-1)
        break
    