n = int(input())

hasil1 = (n//2) + (n//3) + (n//4)
hasil2 = (n%2) + (n%3) + (n%4)
hasil3 = 0

if hasil2 > 0:
    hasil3 += 1
    

print(hasil1 + hasil3)