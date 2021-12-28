n = int(input())
biner = ""
while n > 0:
    sisa = n % 2
    
    if sisa == 1:
        biner = "1" + biner
    else:
        biner = "0" + biner
    
    n = n // 2
print(biner)