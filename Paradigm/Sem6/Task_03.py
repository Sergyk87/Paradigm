"""Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке возрастания. Пример сортировки слиянием."""


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    merged = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
    i += 1

    while j < len(right_half):
        merged.append(right_half[j])
    j += 1

    return merged


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = merge_sort(numbers)
print("Отсортированный массив:", sorted_numbers)
