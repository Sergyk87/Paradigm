'''Ваша задача
Реализовать секундомер на любом языке программирования в любой парадигме.
Секундомер должен поддерживать следующий функционал:
○ Запуск
○ Пауза
○ Выход из паузы
○ Остановка'''
import time


def start_stopwatch():

    start_time = 0
    result_time = 0
    while_running = True

    print("Команды: старт - 1, пауза - 2, продолжить - 3, стоп - 4, выход - 5")
    is_start = False
    is_pause = False
    while while_running:
        user_input = input("Введите команду: ")
        if user_input == "1" and not is_start:
            print("Секундомер запущен")
            start_time = time.time()
            is_start = True
        elif user_input == "2" and is_start and not is_pause:
            result_time += time.time() - start_time
            print(f"Секундомер на паузе, {result_time} прошло")
            is_pause = True
        elif user_input == "3" and is_pause and is_start:
            start_time = time.time()
            print("Секундомер запущен")
            is_pause = False
        elif user_input == "4" and is_start:
            result_time += time.time() - start_time
            print(f"Секундомер остановлен, {result_time} прошло")
            start_time = 0
            result_time = 0
            is_start = False
            is_pause = False
        elif user_input == "5":
            break
        else:
            print('Неверная команда')

if __name__ == "__main__":
    start_stopwatch()