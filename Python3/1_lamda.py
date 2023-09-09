"""  Напишите функцию multiply_numbers(), которая принимает два
аргумента и возвращает их произведение. Затем вызовите эту функцию
и выведите результат на экран. """

multiply_numbers = lambda a, b: a * b
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = multiply_numbers(a, b)
print("Произведение равно: ", result)