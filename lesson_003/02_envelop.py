# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
def paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y):
    if envelop_x >= paper_x or envelop_x >= paper_y:
        if envelop_y >= paper_x or envelop_y >= paper_y:
            print('Да')
        else:
            print('Нет')

envelop_x, envelop_y = 10, 7

paper_x, paper_y = 8, 9
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

# проверить для
paper_x, paper_y = 9, 8
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

paper_x, paper_y = 6, 8
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

paper_x, paper_y = 8, 6
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

paper_x, paper_y = 3, 4
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

paper_x, paper_y = 11, 9
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)

paper_x, paper_y = 9, 11
paper_in_envelope(paper_x, paper_y, envelop_x, envelop_y)


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

def brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z):
    hole = 0
    brick_1 = 0
    brick_2 = 0
    brick_3 = 0

    hole = hole_x + hole_y
    brick_1 = brick_x + brick_y
    brick_2 = brick_x + brick_z
    brick_3 = brick_y + brick_z

    if hole >= brick_1 and hole >= brick_2 and hole >= brick_3:
        print('Да', brick_x, brick_y, brick_z)
    else:
        print('Нет', brick_x, brick_y, brick_z)

print('усложненный блок')

hole_x, hole_y = 8, 9

#тест
brick_x, brick_y, brick_z = 8, 8, 9
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 9, 9, 0
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

# данные
brick_x, brick_y, brick_z = 11, 10, 2
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 2, 10
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 10, 11, 2
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 10, 2, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 2, 10, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 2, 11, 10
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 5, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 6, 5
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 3, 5
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 5, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 5, 6, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 5, 3, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 3, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 6, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 11, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 3, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 6, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 11, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)




