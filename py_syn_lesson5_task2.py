print("Введите слово из строчных латинских символов")
str = input()
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
consonants_count = 0

for ch in str:
    if ch == 'a':
        a_count += 1
    elif ch == 'e':
        e_count += 1
    elif ch == 'i':
        i_count += 1
    elif ch == 'o':
        o_count += 1
    elif ch == 'u':
        u_count += 1
    else:
        consonants_count += 1

vowels_count = a_count + e_count + i_count + o_count + u_count

print("Количество гласных: " + vowels_count.__str__() + ", количество согласных: " + consonants_count.__str__() + ".")
print("Список гласных:")
print('\'a\': ' + a_count.__str__() if a_count > 0 else '\'a\': false' )
print('\'e\': ' + e_count.__str__() if e_count > 0 else '\'e\': false' )
print('\'i\': ' + i_count.__str__() if i_count > 0 else '\'i\': false' )
print('\'o\': ' + o_count.__str__() if o_count > 0 else '\'o\': false' )
print('\'u\': ' + u_count.__str__() if u_count > 0 else '\'u\': false' )

