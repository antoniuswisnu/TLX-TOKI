masukan = input().split()
a = int(masukan[0])
op = str(masukan[1])
b = int(masukan[2])

hasil1 = a - b
hasil2 = a + b
hasil3 = a * b
hasil4 = a < b
hasil5 = a > b
hasil6 = a == b

if op == "-":
    print(hasil1)
elif op == "+":
    print(hasil2)
elif op == "*":
    print(hasil3)
elif op == "<" and hasil4 == True:
    print("benar")
elif op == "<" and hasil4 == False:
    print("salah")
elif op == ">" and hasil5 == True:
    print("benar")
elif op == ">" and hasil5 == False:
    print("salah")
elif op == "=" and hasil6 == True:
    print("benar")
elif op == "=" and hasil6 == False:
    print("salah")