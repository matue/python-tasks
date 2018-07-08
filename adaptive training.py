''' адаптивный тренажер умножения '''
import random


class Level:
    def __init__(self):
        self.level = 20

    def changeLevel(self, value):
        self.level += value


class Example:
    def genExample(self):
        self.m1 = random.randint(10, 99)
        self.m2 = random.randint(10, 99)
        return self.m1, self.m2

    def calcComplexity(self):  # здесь определяем сложность вычисления
        comp = 0
        for i in (self.m1, self.m2):
            if i % 10 == 0:
                comp += 1
            elif i % 10 in (1, 9):
                comp += 2
            elif i % 10 in (2, 8):
                comp += 3
            elif i in range(93, 97):
                comp += 3
            elif i % 5 == 0:
                comp += 4
            else:
                comp += 5
        return comp

    def checkAnswer(self, Level):
        try:
            a = int(input())
        except ValueError:
            return 'Введено не число'

        if self.m1 * self.m2 == a:
            Level.changeLevel(1*self.calcComplexity())  # увеличиваем уровеь в зависимости от сложности вычисления
            return 'Верно, текущий уровень: ' + str(Level.level)
        else:
            Level.changeLevel(-1*(11-self.calcComplexity()))  # понижаем уровеь в зависимости от сложности вычисления
            return 'Неверно, верный ответ: ' + str(self.m1 * self.m2) + '\nУровень понижен на ' +  str(11-self.calcComplexity()) + '\nТекущий уровень: ' + str(Level.level)


L = Level()
print('Начальный уровень: ' + str(L.level))
while L.level >= 1:
    E = Example()
    print('Множители:', E.genExample())
    print('Сложность:', E.calcComplexity())
    print(E.checkAnswer(L))


