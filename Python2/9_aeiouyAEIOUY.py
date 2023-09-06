""" Написать скрипт, который принимает на вход строку и заменяет в ней
все гласные буквы на символ "-". Язык строки: английский. """

glasnie = 'aeiouyAEIOUY'

user_string = input('Введите текст на английском языке: ')

for char in glasnie:
    user_string = user_string.replace(char, '-')

print(user_string)