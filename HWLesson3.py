# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне
# от 2 до 9.


# a = list(range(2, 100))
# b = list(range(2, 10))
# print(a)
# print(b)
# for x in b:
#     i = 0
#     for y in a:
#         if y % x == 0:
#             i += 1
#     print("Чисел кратных " + str(x) + " : " + str(i))


# ---------------------------------------------------------------------------------------------------
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5
# - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# from random import randint
#
# c = list(range(1, 101))
# print(c)
# d = []
# # Делаем случайный массив с неповторяющимися членами
# for i in range(1, 101):
#     d.append(c.pop(randint(0, len(c) - 1)))
# print(d)
# even = []
# for i in range(0, 100):
#     if d[i] % 2 == 0:
#         even.append(i)
# print(even)

# ---------------------------------------------------------------------------------------------------
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

# d = []
# # Делаем случайный массив с возможно повторяющимися членами
# for i in range(1, 101):
#     d.append(randint(1, 100))
# print(d)
#
# c = sorted(d)
# print(c)
#
# d_max = c[len(c)-1]
# d_min = c[0]
# print(d_max, d_min)
#
# for i in range(0, len(d)-1):
#     if d[i] == d_max:
#         d[i] = d_min
#         print(i)
#     elif d[i] == d_min:
#         d[i] = d_max
#         print(i)
#     else:
#         pass

# ---------------------------------------------------------------------------------------------------
# 4. Определить, какое число в массиве встречается чаще всего.
# from random import randint
#
# d = []
# # Делаем случайный массив с возможно повторяющимися членами
# for i in range(1, 101):
#     d.append(randint(1, 100))
# print(d)
#
# c = sorted(d)
# print(c)
#
# c_max = c[0]
# c_current = c[0]
# icur = 1
# imax = 1
# nmax = 0
# for i in range(1, len(c)-1):
#     if c[i] == c_current:
#         icur += 1
#         if icur > imax:
#             imax += 1
#             nmax = i
#             c_max = c[i]
#     else:
#         c_current = c[i]
#         icur = 1
# print(c_max, imax)


# ---------------------------------------------------------------------------------------------------
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс)
# в массиве.


# from random import randint
#
# d = []
# # Делаем случайный массив с возможно повторяющимися членами
# for i in range(1, 101):
#     d.append(randint(-100, 100))
# print(d)
# c = sorted(d)
# print(c)
# d_max_negative = c[0]
# for x in d:
#     if x == d_max_negative:
#         print(x, d.index(x))

# ---------------------------------------------------------------------------------------------------
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# from random import randint
#
# # Делаем случайный массив с возможно повторяющимися членами
# d = [randint(1, 500) for i in range(100)]
# print(d)
# # c = sorted(d)
# d_min = min(d)
# d_max = max(d)
# sum_d = 0
# if d.index(d_min) < d.index(d_max):
#     sum_d = sum(d[d.index(d_min)+1: d.index(d_max)])
# else:
#     sum_d = sum(d[d.index(d_max)+1: d.index(d_min)])
# # for i in range(0, 100):
# #     if i = d_max or d[i] == d_min:
# #         pass
# #     else:
# #         sum_d += d[i]
# print(sum_d, sum(d))
# print(d_max, d.index(d_max))
# print(d_min, d.index(d_min))


# ---------------------------------------------------------------------------------------------------
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

# # Делаем случайный массив с возможно повторяющимися членами
# d = [randint(1, 500) for i in range(100)]
# print(d)
# print(len(set(d)))
#
# d_min1 = min(d)
# d.pop(d.index(d_min1))
# if d_min1 in d:
#     print("Double min")
# d_min2 = min(d)
#
# print(d_min1, d_min2)


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    row = []
    for j in range(4):
        x = int(input("Введите число " + str((4 * i + j + 1)) + " - "))
        row.append(x)
    row.append((sum(row)))
    # print(row)
    matrix.append(row)
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])


# ---------------------------------------------------------------------------------------------------
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
min_column = []

for i in range(4):
    min_current_column = min(matrix[i])
    min_column.append(min_current_column)
print(max(min_column))

