import random


def num1():
    a = [3, 4, 5, 8, 9]
    b = int(input('Введите число'))
    if b in a:
        print("Вы угадали число!")
    else:
        print("Такого числа нет")



def num2():
    a = [3, 5, 6, 7, 4, 6, 8, 4]
    b = {x for x in a if a.count(x)>1}
    print(b)

def num3():
    a = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    b = int(input("Введите количество выходных"))
    if b == 1:
        print("Выходные: ", a[6])
        print("Рабочие", a[0:5])
    elif b == 2:
        print("Выходные: ", a[5:6])
        print(a[0:4])
    elif b == 3:
        print("Выходные: ", a[4:6])
        print("Рабочие", a[0:3])
    elif b == 4:
        print("Выходные: ", a[3:6])
        print("Рабочие", a[0:2])
    elif b == 5:
        print("Выходные: ", a[2:6])
        print("Рабочие", a[0:1])
    elif b == 6:
        print("Выходные: ", a[1:6])
        print("Рабочие", a[0])
    elif b == 7:
        print("Выходные: ", a[0:6])

def num4():
    f1 = ["Иванов", "Сидоров", "Петров", "Водкин", "Карцев", "Беликова", "Ефлютина", "Аузяк", "Обрывалина", "Ившина"]
    f2 = random.choices(f1, k=5)
    f3 = ["Соколов", "Орлов", "Артемьев", "Ли", "Абросимова", "Блохина", "Виноградов", "Рахимов", "Ткачук", "Ким"]
    f4 = random.choices(f3, k=5)
    f5 = (f2 + f4)
    print(f1, f3, f5)
    dlina = len(f5)
    print(dlina)
    tmp = list(f5)
    tmp.sort()
    f5 = tuple(tmp)
    name = "Иванов"
    if name in f5:
        print("есть")
    else:
        print("нет")



