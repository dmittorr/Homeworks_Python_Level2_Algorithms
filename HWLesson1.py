# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.
# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
#
#
# Доп
#
# 1. Дан файл  с логинами и паролями. Найдите топ10 самых популярных паролей.
#
# # 2. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки компьютер
# сообщает меньше или больше загаданное число. В конце игры текст с результатом
# (или “Вы угадали”, или “Попытки закончились”).

# 1.

num = input("Input 3-digit number: ")
summa = 0
multiplication = 1
for i in num:
    summa += int(i)
    multiplication = multiplication * int(i)
print(summa, multiplication)
