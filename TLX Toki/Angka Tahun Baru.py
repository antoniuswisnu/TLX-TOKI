n = int(input())

if n == 1 or n == 2:
    print("YES")
    
for i in range(2,n):
    if n < 7 and n % i != 0:
        print("YES")
        break
    else:
        print("NO")
        break

    