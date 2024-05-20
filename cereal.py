cerealList = []

while True:
    cereal = input("Enter Cereal: ")
    if cereal == 'sultana and bran' or cereal == 'weetbix':
        break
    else:
        cerealList.append(cereal)

print(cerealList)
