p,q = list(map(int,input().split()))

hasil = (p**2) + (q**2) + 1
hasil2 = hasil % 4
hasil3 = hasil // 4

if hasil2 == 0:
    print(hasil3)
else:
    print(-1)