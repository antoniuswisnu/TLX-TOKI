angka = input().split()
a = int(angka[0])
b = int(angka[1])
k = int(angka[2])
x = int(angka[3])
def f(x,k):
    if k == 0:
        return x
    else:
        return abs(a*f(x,k-1)+b)
print(f(x,k))