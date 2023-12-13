'''Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
● Ваша задача
Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
'''

from functools import reduce


def pearson_correlation(array_x, array_y):
    avgX = sum(array_x) / len(array_y)
    avgY = sum(array_x) / len(array_y)
    xi_avgX = [x - avgX for x in array_x]
    yi_avgY = [y - avgY for y in array_y]
    r_1 = reduce(lambda a, b: a + b, [x * y for x, y in zip(xi_avgX, yi_avgY)])
    print(xi_avgX, yi_avgY)
    print(r_1)
    r_2x = reduce(lambda a, b: a + b, [x ** 2 for x in xi_avgX]) ** 0.5
    r_2y = reduce(lambda a, b: a + b, [y ** 2 for y in yi_avgY]) ** 0.5
    print(r_2x, r_2y)
    r_2 = r_2x * r_2y
    r_xy = r_1 / r_2
    return r_xy


array_x = [1, 2, 3]
array_y = [4, 5, 6]
print(pearson_correlation(array_x, array_y))
