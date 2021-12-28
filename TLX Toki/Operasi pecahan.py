import fractions

a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))

e = a*d + b*c
f = b*d


print(fractions(e),fractions(f))