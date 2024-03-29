# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import threading
import time
import os

PATH = "test_1"
count = 0


def get_amount_worlds(filename: str) -> None:
    global count
    with open(filename, encoding="utf-8") as f:
        count += len(f.read().split())


if __name__ == "__main__":
    threads = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            thread = threading.Thread(target=get_amount_worlds, args=(file_path,))
            threads.append(thread)
            thread.start()
        print(f"Сейчас значение счетчика: {count}")

        for thread in threads:
            thread.join()

        time.sleep(3)
        print(f"Финальное значение счетчика: {count}")
