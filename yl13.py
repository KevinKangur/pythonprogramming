pet = input("Mis lemmikloom teil on? - ")

if pet.lower() == "koer":
    print("What the dog doin?")
    print(pet[0])
else:
    print(pet[0])

petlist = ["Hamster", "Kuldkala", "Hiir"]

petlist.append(pet)

print(petlist)
print(petlist[-1][-1])