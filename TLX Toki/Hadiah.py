a,b,c,n = list(map(int,input().split()))

hasil = (a ** b ** c) % n + 1
print(hasil)