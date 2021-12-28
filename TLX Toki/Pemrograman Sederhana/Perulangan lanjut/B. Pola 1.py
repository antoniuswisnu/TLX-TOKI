maks = int(input())
limit=maks

for bintang in range (maks):
    for pola in range (limit+1):
        print(" ",end="")

    for bentuk in range (bintang+1):
        print("*",end="")
        
    limit-=1
    print(" ")