"""Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество
попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число
попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь. """
import random


def gues(min_numb, max_numb, count):
    numb_1 = random.randint(min_numb, max_numb)
    print(numb_1)
    for i in range(count):
        numb = int(input('enter numb: '))
        if numb == numb_1:
            return True
        elif numb > numb_1:
            print('больше')
        else:
            print('меньше')
    return False


if __name__ == '__main__':
    print(gues(1, 5, 3))
