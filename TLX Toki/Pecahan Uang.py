uang = int(input())
uang_pecahan = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
jumlah_pecahan = []

for pecahan in uang_pecahan:
    if uang < pecahan:
        continue
    banyak_pecahan = uang // pecahan
    jumlah_pecahan.append(banyak_pecahan)
    uang -= pecahan * banyak_pecahan 
    print(pecahan ,banyak_pecahan)