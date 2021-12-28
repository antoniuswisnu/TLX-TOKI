angka = input().split()
a = int(angka[0])
b = int(angka[1])
c = int(angka[2])
k = int(angka[3])
bil = [a,b,c]

if k == 0:
    bil.sort(reverse = True)
    x = " ".join(str(bil) for bil in bil)
    print(x)
elif k == 1:
    bil.sort(reverse = False)
    x = " ".join(str(bil) for bil in bil)
    print(x)
