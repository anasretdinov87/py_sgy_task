import collections

pets = dict()

def create():
    if len(pets) == 0:
        last = 1
    else:
        last = collections.deque(pets, maxlen=1)[0] +1
    print("Введите имя питомца:")
    pet_name = input()
    pets_tmp = {pet_name: {'pet_type': 'none', 'pet_age': int(0), 'pet_owner': 'none'}}
    ind_tmp = {'ind':pets_tmp} 
    pets[last] = ind_tmp['ind'] 

    print("Введите вид питомца:")
    pet_type = input()
    pets[last][pet_name]['pet_type'] = pet_type

    check_num = True
    while check_num:
        print("Введите возраст питомца:")
        pet_age = input()
        check_num = False
        if not pet_age.isnumeric():
            check_num = True
            print("Ошибка, введено не число. Повторите ввод.")
        else:
            pets[last][pet_name]['pet_age'] = int(pet_age)

    print("Введите владельца питомца:")
    pet_owner = input()
    pets[last][pet_name]['pet_owner'] = pet_owner
def read(id):
    #print(f"Это {pets[id]['pet_type']} по кличке \"{list(pets.keys())[0]}\". Возраст питомца: {year_string(pets[id]['pet_age'])}. Имя владельца: {pets[id]['pet_owner']}")    
    #print(f"Это {pets[id]['pet_type']}")
    if id in pets.keys():
        print(list(pets[id]))

create()
read(1)


