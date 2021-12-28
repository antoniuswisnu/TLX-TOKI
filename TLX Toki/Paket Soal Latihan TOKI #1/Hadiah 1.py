n,m = list(map(int,input().split()))
x = list(map(int,input().split()))
data = []

for i in range(n):
    a = sum(x[i:i+m])
    data.append(a)

print(max(data))