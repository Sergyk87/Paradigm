'''Дан список целых чисел numbers. Необходимо написать в императивном и декларативном стиле процедуру для сортировки
числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.'''


def sortNumbersImperative(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def sortNumbersDeclarative(numbers):
    return sorted(numbers, reverse=True)


numbers = [1, 2, 3, 4, 5]
print(sortNumbersImperative(numbers))
print(sortNumbersDeclarative(numbers))
