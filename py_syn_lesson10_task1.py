def year_string(age):
    if age % 100 >= 11 and age % 100 <= 19:
       return str(age) + ' лет'  
    elif age % 10 == 1:
        return str(age) + ' год'
    elif age % 10 == 0:
        return str(age) + ' лет'
    elif age % 10 > 1 and age % 10 < 5:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'

pet_features = {'pet_type': 'none', 'pet_age': int(0), 'pet_owner': 'none'}
pets_tmp = {'tmp_dic': pet_features}
next_pet = True
pets = dict()

pets['pet_name'] = pets_tmp['tmp_dic']

print("Введите имя питомца:")
pet_name = input()
pets[pet_name] = pets['pet_name']
del pets['pet_name']

print("Введите вид питомца:")
pet_type = input()
pets[pet_name]['pet_type'] = pet_type

check_num = True
while check_num:
    print("Введите возраст питомца:")
    pet_age = input()
    check_num = False
    if not pet_age.isnumeric():
        check_num = True
        print("Ошибка, введено не число. Повторите ввод.")
    else:
        pets[pet_name]['pet_age'] = int(pet_age)

print("Введите владельца питомца:")
pet_owner = input()
pets[pet_name]['pet_owner'] = pet_owner
print(f"Это {pets[pet_name]['pet_type']} по кличке \"{list(pets.keys())[0]}\". Возраст питомца: {year_string(pets[pet_name]['pet_age'])}. Имя владельца: {pets[pet_name]['pet_owner']}")

