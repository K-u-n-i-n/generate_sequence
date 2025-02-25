"""
Программа, которая выводит n первых элементов последовательности.
"""


def generate_sequence(n):
    return ''.join(str(i) * i for i in range(1, n + 1))


def main():
    while True:
        try:
            n = int(input('Введите любое положительное число: '))
            if n > 0:
                print(generate_sequence(n))
                break
            else:
                print('Ошибка: Число должно быть положительным.')
        except ValueError:
            print('Ошибка: Введите целое число.')


if __name__ == '__main__':
    main()
