a = int(input("Sisestage üks number : "))
b = int(input("Sisestage teine number : "))
c = int(input("Sisestage kolmas number : "))

if a > b and a > c:
    print("max:", a)

elif b > c:
    print("max: ", b)

else:
    print("max: ", c)