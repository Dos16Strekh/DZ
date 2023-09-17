"""  Создайте класс "Студент", который имеет атрибуты имя, возраст и
средний балл. Создайте методы для вычисления среднего балла и
определения статуса студента (отличник, хорошист, троечник).Создайте
несколько объектов этого класса и вызовите его методы для каждого
объекта. """

import statistics
class student:
    def __init__(self, name, age, bal):
        self.name = name
        self.age = age
        self.bal = bal
    def score (self, average):
        if not average:
            print("EROR: enter the student's grades!")
        else:
             average = statistics.mean(average)
             print(f'\nAverage score {self.name}: {average}')
             if average < 3.7:
                 print(f'Student {self.name} studies poorly!')
             else:
                 if 3.7 <= average < 4.7:
                     print(f'Student {self.name} studies well!')
                 else:
                     print(f'Student {self.name} studies perfectly!')
                     
list_ball1 = [5, 3, 4, 5, 5]
student1 = student("Igor", 25, list_ball1)
student1.score(list_ball1)

list_ball2 = [3, 2, 4, 3, 3]
student2 = student("Denis", 25, list_ball2)
student2.score(list_ball2)

list_ball3 = [5, 5, 5, 5, 4]
student3 = student("Zina", 21, list_ball3)
student3.score(list_ball3)