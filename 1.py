number = int(input("Введите число: "))
border = int(input("Введите пограничное число: "))

if number < border:
    print("Первое число меньше пограничного")
elif number > border:
    print("Первое число больше пограничного")
if number > border * 3:
    print("Первое число больше пограничного более, чем в 3 раза")
if number == border:
    print("Числа равны")