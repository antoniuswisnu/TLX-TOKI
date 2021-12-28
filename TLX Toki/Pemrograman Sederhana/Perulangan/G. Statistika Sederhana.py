n = int(input())
N = list(map(int,input().split()))

A = 0
B = 0
for i in range(n):
    if A < N[i]:
        A = N[i]
    if B > N[i]:
        B = N[i]
print(A,B)
