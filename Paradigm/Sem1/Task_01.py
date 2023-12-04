# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится ли target в array.
# Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.

def targetInArrayImperative(array, target):
    for i in array:
        if i == target:
            return True
    return False


array1 = [1, 2, 3, 4, 5]
target1 = 3
print(targetInArrayImperative(array1, target1))

def targetInArrayDeclarative(array, target):
    return target in array

array1 = [1, 2, 3, 4, 5]
target1 = 7
print(targetInArrayDeclarative(array1, target1))
