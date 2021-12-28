a = int(input())
b = int(input())
c = int(input())

x = max(a,b,c)
y = min(a,b,c)
z = [a,b,c]
z.sort()

print(y)
print(x)
print(z[1])