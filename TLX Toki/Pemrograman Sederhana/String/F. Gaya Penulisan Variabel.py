s = input().split("_")
data = []


for i in range(len(s)):
    if i == 0:
        a = s[i].lower()
        data.append(a)
    else:
        a = s[i].capitalize()
        data.append(a)

hasil = "".join(data)
print(hasil)


