""" Написать скрипт, который принимает на вход кортеж и проверяет, все
ли его элементы являются уникальными. """

tuple = ('a', 'A', 'Apple', 'Samsung', '5')
uniq_elements = []
for i in tuple:
    if i not in uniq_elements:
        uniq_elements.append(i)
if len(tuple) == len(uniq_elements):
    print("Uniq")
else:
    print("NOT uniq")