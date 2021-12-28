n = int(input())
m = list(map(int,input().split()))

m.reverse()
a = ",".join(str(m) for m in m)
print(a)