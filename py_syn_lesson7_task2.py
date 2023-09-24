len_check = True
while len_check:
    print("Введите строку, длиной до 1000 символов:")
    str = input()
    len_check = False
    if len(str) > 1000:
        len_check = True



for i in range(0, int(len(str)-1)):
    if i > int(len(str)-1):
        break
    if str[i] == ' ':
        count = 0
        for j in range(i, len(str)-1):
            if str[j] == ' ':
                count += 1
            else:
                break
        if count > 1:
            str1 = str[0:i]
            str2 = str[i+count:]
            str = str1 + " " + str2
            
print(str)     