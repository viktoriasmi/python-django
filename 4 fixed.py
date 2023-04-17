import math
import random

while True:
    operation = input("Введите символ операции: ")

    if operation == "+":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a + b
        print(result)
    elif operation == "-":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a - b
        print(result)
    elif operation == "/":
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = a / b
        print(result)
    elif operation == "*":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a * b
        print(result)
    elif operation == "^":
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        result = a ** b
        print(result)
    elif operation == "||":
        a = float(input("Введите число: "))
        result = abs(a)
        print(result)
    elif operation == "random":
        a = float(input("Введите минимальное значение: "))
        b = float(input("Введите максимальное значение: "))
        result = int(random.uniform(a, b))
        print(result)
    elif operation == "!":
        n = int(input("Введите число: "))
        result = math.factorial(n)
        print(result)
    elif operation == "arccos":
        degrees = float(input("Введите угол в градусах: "))
        radians = degrees * math.pi / 180
        arccos = math.acos(math.cos(radians))
        print(arccos)
    else:
        print("Неизвестная операция")
    answer = input("Хотите продолжить работу? (да/нет) ")
    if answer.lower() != "да": break

