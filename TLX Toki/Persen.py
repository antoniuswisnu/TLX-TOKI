a,b,c,d = list(map(int,input().split()))

hasil = (a ** b ** c ** d) % 101
print(hasil)