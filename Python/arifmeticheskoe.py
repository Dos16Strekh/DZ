""" Напишите программу, которая запрашивает у пользователя два числа и
выводит на экран их среднее арифметическое. """

x = int(input( "Введите первое число: "))
y = int(input( "Введите второе число: "))
z = (x, y)
q = sum(z) / len(z)
print( "Среднее арифметическое равно ", q )
