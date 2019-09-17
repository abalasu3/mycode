names = ['fluffy', 'spot', 'cujo']
ages = [3, 7, 12]
animal_type = ['cat', 'dog', 'mean dog']

pets ={}

for i in range(len(names)):
    pets.update({names[i]:{'age':ages[i],'animal_type':animal_type[i]}})
print(pets)


