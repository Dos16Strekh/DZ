""" Создайте пустую директорию mydir в текущей рабочей директории.
Затем перейдите в эту директорию и создайте в ней три пустых файла:
file1.txt, file2.txt и file3.txt. Наконец, выведите список файлов в
директории на экран. """

import os
import pathlib

# Проверка существования папки
path = ('mydir')
if not os.path.exists(path):
    os.makedirs(path) # создаем директорию
else:
    print( 'Директория с таким именем существует.')

os.chdir(path) # переходим в директорию

# создаем файлы

file_names = [ 'file1.txt','file2.txt', 'file3.txt']

for file_name in file_names:
    if not os.path.exists(file_name): # Сначала проверяем, существует ли файл
        file_name = open(file_name, 'w')
    else:
        print( 'Файл с именем ', file_name, ' существует.')

# выводим список файлов
for ls in os.listdir('.'):
    print(ls)