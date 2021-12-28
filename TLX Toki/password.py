password = input()

for i in range(len(password)):
    for j in range(len(password)[i]):
        if "_" or "!" or "?" == password[i][j]:
            print(kuat)
        






if len(password) >= 8 and  :
    print("Kuat")
elif len(password) >= 12:
    print("AgakKuat")
else:
    print("Lemah")

