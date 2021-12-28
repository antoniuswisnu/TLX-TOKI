n = list(map(int,input().split()))
data = []

for i in range(1,n[0]+1):
    if i % n[1] == 0:
        data.append("*")
    else:
        data.append(i)

hasil = " ".join(str(data) for data in data)
print(hasil)
        