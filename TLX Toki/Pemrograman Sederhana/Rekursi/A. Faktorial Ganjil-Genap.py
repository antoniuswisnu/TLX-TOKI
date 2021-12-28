n = int(input())

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n/2 * f(n-1)
    else:
        return n * f(n-1)

print(round(f(n)))    