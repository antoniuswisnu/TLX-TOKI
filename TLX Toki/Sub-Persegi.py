n = int(input())

def sub(n):
    if n <= 1:
        return 1
    else:
        return n ** 2 + sub(n-1)

print(sub(n))