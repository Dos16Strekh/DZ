# создаем два списка для сравнения
list1 = ['apple', 'orange', 'banana']
list2 = ['banana', 'apple', 'grapes']

# находим одинаковые элементы с помощью метода set()
same_elements = set(list1) & set(list2)

# выводим только одинаковые элементы на экран
if same_elements:
    for elem in same_elements:
        print(elem)
else:
    print('Оба списка не содержат одинаковых элементов.')