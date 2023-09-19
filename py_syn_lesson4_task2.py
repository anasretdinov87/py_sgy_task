x = 34234

tens = (x % 100) // 10
units = (x % 10)
hundreds = (x % 1000) // 100
tens_of_thousands = x  // 10000
thousands = (x % 10000) // 1000

if tens_of_thousands - thousands != 0:
    print(((tens ** units)*hundreds)/(tens_of_thousands - thousands))
else:
    print("Division by zero")
