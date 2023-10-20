import collections

pets = {
    1: {
        'Том': {
            'pet_type': 'кот',
            'pet_age': 11,
            'pet_owner' : 'Джон'
        }
    },
    2: {
        'Джерри': {
            'pet_type': 'мышь',
            'pet_age': 1,
            'pet_owner' : 'Майк'
        }
    }
}

def get_suffix(age):
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
       
def get_pet(id):
    if id.isnumeric():
        id = int(id)
        if id in pets.keys():
            pet_name = list(pets[id].keys())[0]
            return(f"Это {pets[id][pet_name]['pet_type']} по кличке \"{pet_name}\". Возраст питомца: {get_suffix(pets[id][pet_name]['pet_age'])}. Имя владельца: {pets[id][pet_name]['pet_owner']}")
        else:
            return False
    else:
        return False  
      
def pets_list():
    for id in pets:
        pet_name = list(pets[id].keys())[0]
        print(f"ID: {id}. Кличка: \"{pet_name}\". Тип питомца: {pets[id][pet_name]['pet_type']}. Возраст питомца: {get_suffix(pets[id][pet_name]['pet_age'])}. Имя владельца: {pets[id][pet_name]['pet_owner']}")     

def create():
    if len(pets) == 0:
        last = 1
    else:
        last = collections.deque(pets, maxlen=1)[0] +1

    print('Введите имя питомца:')
    pet_name = input()
    pets_tmp = {pet_name: {'pet_type': 'none', 'pet_age': int(0), 'pet_owner': 'none'}}
    ind_tmp = {'ind':pets_tmp} 
    pets[last] = ind_tmp['ind'] 

    print('Введите вид питомца:')
    pet_type = input()
    pets[last][pet_name]['pet_type'] = pet_type

    check_num = True
    while check_num:
        print('Введите возраст питомца:')
        pet_age = input()
        check_num = False
        if not pet_age.isnumeric():
            check_num = True
            print('Ошибка, введено не число. Повторите ввод.')
        else:
            pets[last][pet_name]['pet_age'] = int(pet_age)

    print('Введите владельца питомца:')
    pet_owner = input()
    pets[last][pet_name]['pet_owner'] = pet_owner

def read():
    print("Введите id питомца:")
    id = input()
    if not get_pet(id):
        print('ID не существует') 
    else:
        print(get_pet(id))  

def update():
    pets_list()
    print('Введите ID для редактирования:')
    id = input()
    if not get_pet(id):
        print('ID не существует') 
    else:
        id = int(id)
        pet_name = list(pets[id].keys())[0]
        print("Укажите новое имя:")
        pet_new_name = input()
        pets_tmp = {pet_new_name: {'pet_type': pets[id][pet_name]['pet_type'], 'pet_age': pets[id][pet_name]['pet_age'], 'pet_owner': pets[id][pet_name]['pet_owner']}}
        ind_tmp = {'ind':pets_tmp} 
        pets[id] = ind_tmp['ind'] 

        print("Укажите новый тип питомца:")
        pet_type_new = input()
        pets[id][pet_new_name]['pet_type'] = pet_type_new

        check_num = True
        while check_num:
            print('Укажите новый возраст питомца:')
            pet_new_age = input()
            check_num = False
            if not pet_new_age.isnumeric():
                check_num = True
                print('Ошибка, введено не число. Повторите ввод.')
            else:
                pets[id][pet_new_name]['pet_age'] = int(pet_new_age)

        print("Укажите нового владельца питомца:")
        pet_new_owner = input()
        pets[id][pet_new_name]['pet_owner'] = pet_new_owner

def delete():
    pets_list()
    print('Введите ID для удаления:')
    id = input()
    if not get_pet(id):
        print('ID не существует') 
    else:
        id = int(id)
        pets.pop(id)
        print('Удалено')


command = ''
while command != 'stop':
    print('Введите команду: create - новая запись, read - показать информацию о питомце, update - обновить информацию, delete - удалить запись, stop - завершить')
    command = input()
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'stop':
        break
    else:
        print('Ошибка. Несуществующая команда.')   


 
