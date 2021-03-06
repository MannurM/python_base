# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import make_number, check_bull_cow


# import mastermind_engine
# print(dir(mastermind_engine))

def check_input():
    global check_number
    check_number = input('Введите ваше число:')
    check_number_set = set(list(check_number))

    while not check_number.isdigit() or check_number[0] == '0' or len(check_number_set) != 4:  #
        check_number = input('Что - то с Вашим числом не так! Введите ваше число:')
        check_number_set = set(list(check_number))

    return check_number


answer = input('Хотите  сыграть партию  y/n? ')

while answer in ('y', 'Y', 'yes', 'Yes'):

    guess_number = make_number()
    print('Число загадано!')
    check_number = '0'
    count = 1

    while not check_number == guess_number:
        print('Ход', count)

        check_input()
        cow, bull = check_bull_cow(check_number)

        if bull == 4:
            print('Число угадано!!!')
            print('Отгадано на', count, 'ходу')
            break

        print('cows -', cow, 'цифры есть в числе')
        print('bulls -', bull, 'цифры на своем месте')

        count += 1

    answer = input('Хотите  еще партию  y/n? ')
    if answer in ('y', 'Y', 'yes', 'Yes'):
        continue
    else:
        break

print('Тогда давай - до свидания!')
#зачёт!