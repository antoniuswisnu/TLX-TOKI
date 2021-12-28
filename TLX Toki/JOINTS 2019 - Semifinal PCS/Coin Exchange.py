t = int(input())
x = int(input())
y = int(input())

data1 = []
for i in range(2,x+1):
    data1.append(i)

data2 = []
for i in range(3,y+1):
    data2.append(i)

hasil1 = (x-1) - min(data1)
hasil2 = (y-1) - min(data2)

print(hasil1)
print(hasil2)