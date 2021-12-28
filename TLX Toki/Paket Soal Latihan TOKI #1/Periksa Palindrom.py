s = input().split()
data = []
data_rev = []

for i in range(len(s)):
    rev = "".join(reversed(s[i]))
    data_rev.append(rev)

for i in range(len(s)):
    if s[i] == data_rev[i]:
        data.append(s[i])
        
hasil = " ".join(data)
print(hasil)
