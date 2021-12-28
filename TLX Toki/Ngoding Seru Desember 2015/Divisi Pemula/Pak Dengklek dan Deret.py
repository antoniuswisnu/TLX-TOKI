n = int(input())
data = []

for i in range(1,n+1):
    data.append(i)
    
hasil = "+".join(str(i) for i in data)
print(hasil)