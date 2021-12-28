n = int(input())
data1 = []
data2 = []
data3 = []

for i in range(n):
    i = int(input())
    if i < 0:
        data1.append(i)
    elif i == 0:
        data2.append(i)
    else:
        data3.append(i)
        
data4 = data1 + data2 + data3
for i in data4:
    print(i)