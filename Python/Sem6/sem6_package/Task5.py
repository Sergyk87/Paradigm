"""Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
с которой она угадана). Функция формирует словарь с информацией о результатах отгадывания. Для хранения используйте
защищённый словарь уровня модуля. Отдельно напишите функцию, которая выводит результаты угадывания из защищённого
словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение. """

_results = dict()


def secrets(riddle: str, answers: list[str], counter: int) -> int:
    print(riddle)
    for i in range(counter):
        ans = input("Введите ответ: ")
        if ans in answers:
            answer_counter(riddle, i + 1)
            return i + 1
        answer_counter(riddle, 0)
    return 0


def t_storage():
    dict_riddle = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                   'Не лает, не кусает, в дом не пускает': ['замок'],
                   'Сидит дед во сто шуб одет': ['лук', 'луковица']}
    for test_data in dict_riddle.items():
        print(secrets(*test_data, counter=3))


def answer_counter(riddle: str, result: int):
    global _results
    _results.setdefault(riddle, result)


def print_results():
    global _results
    for k, v in _results.items():
        print(f'{k=}, {v=}')

if __name__ == '__main__':
    t_storage()
    print_results()
