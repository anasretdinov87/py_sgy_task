space_check = True

while space_check:
    print("Введите строку без пробелов: ")
    str = input()
    space_check = False
    for i in str:
        if i == ' ':
            space_check = True
            break

if len(str) % 2 == 0:
    middle  = int(len(str)/2)
    str1 = str[0: middle]
    str2 = str[:middle-1:-1]    
else:
    middle = int((len(str)-1)/2)
    str1 = str[0: middle]
    str2 = str[:middle:-1] 

if str2 == str1:
    print("Yes")
else:
    print("No")