my_dict = dict()

for i in range(10, -6, -1):
    _key = int(i)
    _value = float(i ** i)
    my_dict.update({ _key : _value})
print(my_dict)