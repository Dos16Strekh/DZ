""" Написать скрипт, который принимает на вход две строки и выводит на
экран все символы, которые встречаются в обеих строках.
 """
text1 = input( "Введите первый текст: " )
text2 = input( "Введите второй текст: " )

elements = []
for i in text1:
    if i not in elements:
        elements.append(i)
for j in text2:
    if j not in elements:
        elements.append(j)
print( "В текстах встречаются элементы: ", elements)