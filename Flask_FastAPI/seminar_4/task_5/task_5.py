# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.
import multiprocessing
import multiprocessing
import os

PATH = 'test_1'
counter = multiprocessing.Value('i', 0)


def get_amount_worlds(counter, filename) -> None:
    with open(filename, encoding='utf-8') as f:
        with counter.get_lock():
            temp = f.read().split()
            counter.value += len(temp)
    print(f'Значение счетчика: {counter.value:_}')


if __name__ == '__main__':
    processes = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            process = multiprocessing.Process(target=get_amount_worlds, args=(counter, file_path))
            processes.append(process)
            process.start()


        for process in processes:
            process.join()

    print(f'Финальное значение счетчика: {counter.value}')
