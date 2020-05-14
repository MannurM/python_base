# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
count = 1
material_assistance = 0
expenses_procent = 0

while count < 10:
    expenses_procent += (12000 + expenses_procent) * 0.03
    expenses += 12000
    educational_grant += 10000

    count += 1

material_assistance = round(expenses + expenses_procent - educational_grant, 2)
print("Студенту надо попросить", material_assistance, "рублей")


