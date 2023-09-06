""" Написать скрипт, который принимает на вход два списка и находит
общие элементы, а затем создает новый список, содержащий только
уникальные элементы. """

list_1 = ["a", "b", "c", "1"]
list_2 = ["1", "2", "3", "a", "b"]

same_elements = set(list_1) & set(list_2)
print( "Повторяющиеся элементы: ", same_elements)

uniq_elements = []
for i in list_1:
    if i not in same_elements:
        if i not in uniq_elements:
            uniq_elements.append(i)
for j in list_2:
    if j not in same_elements:
        if j not in uniq_elements:
            uniq_elements.append(j)
print( "Уникальные элементы: ", uniq_elements)