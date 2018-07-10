import random

def genExample(comp):
    c = 0
    while not c == comp:
        m1 = random.randint(10, 99)
        m2 = random.randint(10, 99)
        c = 0
        for i in (m1, m2):
            if i % 10 == 0:
                c += 1
            elif i % 10 in (1, 9):
                c += 2
            elif i % 10 in (2, 8):
                c += 3
            elif i in range(93, 97):
                c += 3
            elif i % 5 == 0:
                c += 4
            else:
                c += 5
    return m1, m2



calc = 2
while calc >= 2:
    a, b = genExample(calc)[0:2]
    print (a, b)
    i = int(input())
    if i == a*b:
        print('Верно')
        calc += 1
        print(calc)
    else:
        print('Неверно')
        calc -= 1
        print(calc)
