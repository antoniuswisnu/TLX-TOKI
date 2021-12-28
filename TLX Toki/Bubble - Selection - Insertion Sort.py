n = int(input())
data = []


for i in range(n):
    a = int(input())
    data.append(a)
    
data.sort()

for j in data:
    print(j)