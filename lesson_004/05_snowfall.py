# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
# x = 0
# y = 570
# N = 20
#
# n_list_x = []
# factor_b_list = []
#
# length = 15
# step = int(length / 2)
#
#
# for i in range(N):
#     x = i * length * 4
#     n_list_x.append(x)
#
#     factor_b_random = sd.random_number(1, 10)/10
#     factor_b_list.append(factor_b_random)
#
#
# sd.resolution = 1200, 600
#
# for y in range(570, length, - step):
#
#     for i in range(N):
#         point = sd.get_point(n_list_x[i]+sd.random_number(0, 20), y + sd.random_number(0, 25))
#
#         factor_b = factor_b_list[i]
#
#         sd.snowflake(center=point, length=length, factor_b=factor_b)
#
#     sd.sleep(0.1)
#
#     sd.clear_screen()
#
#     if sd.user_want_exit():
#         break


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


x = 0
x1 = 0
y = 0
y1 = 0
N = 20
length = 15
count = 0

n_list_x = []
n_list_x1 = []
n_list_y = []
n_list_y1 = []

factor_b_list = [0]
step_random_x = 0
step_random_y = 0

sd.resolution = 1200, 600


def snow():
    for i in range(int(1200/N)):
        x = length + i * length * 4
        n_list_x.append(x)

        factor_b_random = sd.random_number(1, 20) / 10
        factor_b_list.append(factor_b_random)

        # step_x = sd.random_number(1, 30)
        # step_random_x.append(step_x)

        # step_y = sd.random_number(1, 15)
        # step_random_y.append(step_y)

        y = 650
        n_list_y.append(y)
        n_list_x1.append(0)
        n_list_y1.append(650)

    # print(n_list_x1)
    # print(n_list_y1)
    # print('n_list_y', n_list_y)
    # print('n_list_x', n_list_x)

    count = 0

    while True:
        count += 1
        sd.start_drawing()

        for i, x in enumerate(n_list_x):
            factor_b = factor_b_list[i]
            x = n_list_x1[i]
            y = n_list_y1[i]

            point = sd.get_point(x, y)
            # print(i, 'point_old', point)

            sd.snowflake(center=point, length=length, color=sd.background_color, factor_b=factor_b)
            # TODO С изменениями координат слишком много операций выходит
            # TODO Попробуйте откинуть использование x1, y1 и записать код из 148-155 строк в две строки
            x1 = n_list_x[i] + sd.random_number(1, 15)

            step_random_y = sd.random_number(1, 50)
            y1 = n_list_y[i] - step_random_y
            n_list_y[i] = y1

            n_list_y1[i] = y1
            n_list_x1[i] = x1

            point = sd.get_point(x1, y1)
            # print(i, 'point_new', point)

            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_b=factor_b)

            if y1 <= length:
                # print(y1)
                if n_list_y1[i] <= length:  # TODO Тут и ниже у вас дублируется один код многократно
                    # TODO Делать этого не стоит. Лучше используйте отдельную переменную, для обозначения нижнего порога
                    # TODO И увеличивайте эту переменную раз в N-итераций цикла
                    n_list_y1[i] = 650
                    n_list_y[i] = 650
                    n_list_x1[i] = 0
                    n_list_x[i] = sd.random_number(length, 1200)
                # print(count)
            if count >= 150:
                if y1 <= 3 * length:
                    # print(y1, 3 * length)
                    # if n_list_y1[i] <= int(2*length):
                    n_list_y1[i] = 650
                    n_list_y[i] = 650
                    n_list_x1[i] = 0
                    n_list_x[i] = sd.random_number(length, 1200)

                if count >= 200:
                    if y1 <= int(4 * length):
                        # print(y1)
                        # if n_list_y1[i] <= int(3 * length):
                        n_list_y1[i] = 650
                        n_list_y[i] = 650
                        n_list_x1[i] = 0
                        n_list_x[i] = sd.random_number(length, 1200)
                    if count >= 250:
                        if y1 <= int(5 * length):
                            # print(y1)
                            # if n_list_y1[i] <= int(3 * length):
                            n_list_y1[i] = 650
                            n_list_y[i] = 650
                            n_list_x1[i] = 0
                            n_list_x[i] = sd.random_number(length, 1200)




        sd.finish_drawing()
        # sd.sleep(0.1)

        if sd.user_want_exit():
            break


snow()
sd.pause()