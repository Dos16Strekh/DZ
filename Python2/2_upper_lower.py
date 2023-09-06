"""  Написать скрипт, который принимает на вход строку и выводит на
экран количество букв в верхнем регистре, количество букв в нижнем
регистре, количество цифр и количество символов пунктуации. """

import string # необходимый модуль string

text = input("Введите текст: ")

count_big_letters = len([char for char in text if char.isupper()]) # char.isupper() - большие буквы
count_small_letters = len([char for char in text if char.islower()]) # char.islower() - маленькое буквы
count_digits = len([char for char in text if char.isdigit()]) # char.isdigit() - цифры
count_punctuation = len([char for char in text if char in string.punctuation]) # string.punctuation - знаки препинания

print("Количество больших букв:", count_big_letters)
print("Количество маленьких букв:", count_small_letters)
print("Количество цифр:", count_digits)
print("Количество знаков препинания:", count_punctuation)