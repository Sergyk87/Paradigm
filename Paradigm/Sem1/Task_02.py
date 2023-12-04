# На вход подается: список целых чисел arr
#
# Задача
# Реализовать императивную функцию, которая возвращает три числа в процентах:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел

def plusMinusInArrayImperative(array):
    positiveNumbers = 0
    zeroNumbers = 0
    negativeNambers = 0

    for i in array:
        if i > 0:
            positiveNumbers += 1
        elif i == 0:
            zeroNumbers += 1
        else:
            negativeNambers += 1
    return positiveNumbers / len(array) * 100, zeroNumbers / len(array) * 100, negativeNambers / len(array) * 100


array = [1, 10, -6, 0, 0, 65, -11, -65, 0, 111]
print(plusMinusInArrayImperative(array))


def plusMinusInArrayDeclarative(array):
    positiveCount = len(list(filter(lambda x: x > 0, array)))
    negativeCount = len(list(filter(lambda x: x < 0, array)))
    zeroCount = len(list(filter(lambda x: x == 0, array)))
    counts = [positiveCount, negativeCount, zeroCount]
    return list(map(lambda count: count / len(array), counts))

array = [1, 10, 6, 5, 0, 65, -11, -65, 0, 111]
print(plusMinusInArrayDeclarative(array))
