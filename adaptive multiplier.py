''' адаптивный тренажер умножения '''
import random


class Level:
    def __init__(self):
        self.level = 1

    def incLevel(self, value):
        self.level += value


class Multiplier:
    def __init__(self, lenght = 2):
        if lenght == 2:
           self.value = random.randint(10, 99)
        elif lenght == 3:
            self.value = random.randint(100,999)

    def getValue(self):
        return self.value


class Example:
    def genExample(self, lenght = 2):
        if lenght == 2:
           self.m1 = random.randint(10, 99)
           self.m2 = random.randint(10, 99)
        return self.m1, self.m2

    def checkExample(self, answer):
        if self.m1 * self.m2 == answer:
            return 'Верно'
        else:
            return 'Неверно, верный ответ ', self.m1 * self.m2

E = Example()
print(E.genExample())

A = int(input())
print(E.checkExample(A))