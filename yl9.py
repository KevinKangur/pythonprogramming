a = float(input("Sisestage külg a pikkus: "))
b = float(input("Sisestage külg b pikkus: "))
c = float(input("Sisestage külg c pikkus: "))


if (a + b < c) or (b + c < a) or (a + c < b) or a == 0 or b == 0 or c == 0:
    print("Kolmnurk ei saa eksisteerida")
elif a == b == c != 0:
    print("Kolmnurk on võrdkülgne")
elif (a == b != c) or (a == c != b) or (b == c != a):
    print("Kolmnurk on võrdhaarne")
elif a != b != c:
    print("Kolmnurk on erikülgne")