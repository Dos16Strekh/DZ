""" Создайте файл test.txt и запишите в него строку "Это тестовый файл для
домашнего задания по программированию". Затем откройте этот файл в
режиме чтения, прочитайте его содержимое и выведите на экран. """

from pathlib import Path

# Проверка на наличие файла
file = Path("test.txt")
if not file.exists():
    file.touch()
# Запись в файл нужной фразы
with open("test.txt", "w") as file:
    file.write("Это тестовый файл для домашнего задания по программированию")
   
# Читаем файл
with open("test.txt", "r") as file:
    content = file.read()
    print(content)