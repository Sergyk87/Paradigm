'''Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную систему счисления.'''


def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return  binary
print(decimal_to_binary())