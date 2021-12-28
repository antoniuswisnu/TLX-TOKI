n = int(input())
data = []

for i in range(n):
    a = int(input())
    data.append(a)

data2 = []
for j in range(n):
    if data[j] in data:
        if data[j] not in data2:
            data2.append(data[j])
        else:
            pass
    
for hasil in data2:
    print(hasil)
        