fruits = ["Banaan", "Apelsiin", "Õun"]
print(fruits)

print(fruits[0])

fruits.append("Virsik")

print(fruits[-1])

fruits[2] = "Mandariin"
print(fruits)

if "Mandariin" in fruits:
    print("Jah, mandariin on listis")

print(len(fruits))

fruits.remove("Apelsiin")
print(fruits)

fruits.reverse()

fruits.sort(reverse = True)
print(fruits)