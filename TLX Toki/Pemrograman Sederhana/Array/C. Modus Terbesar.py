n = int(input())
data = list(map(int,input().split()))

for i in range(n):
    awal = data[0]
    if awal > data[i]:
        awal = data[i]