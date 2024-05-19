iLikePesto = []
otherFoods = []

for food in range(8):
    food = input("Whats your favourite food?")
    if food == "pesto":
        iLikePesto.append("pesto")
    else:
        otherFoods.append(food)

print(len(iLikePesto), "people like pesto")
print(" i like pesto" * (len(iLikePesto)))
print("Other foods:", otherFoods)
