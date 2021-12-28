def biner(n):
    if n == 1:
        return "1"
    elif n % 2 == 1:
        return biner(n/2) + "1"
    else:
        return biner(n/2) + "0"

a = int(input())
print(biner(a))

