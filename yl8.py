a = int(input("Sisestage aasta arv: "))

if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print("Tegu on liigaastaga")
else:
    print("Tegu on lihtaastaga")