# Требуется вычислить, сколько раз встречается некоторое число
# X в массиве A[1...N].
# Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве.
# В последующих  строках записаны N целых чисел A[i].
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

number = int(input('Введите количество элементов: '))
our_list = []
# for i in range(0, number):
#     our_list.append(int(input('Введите элемент: ')))
# print(*our_list) # для наглядности

digit = int(input('Введите число для проверки: '))
count = 0
for i in our_list:
    if digit == i:
        count += 1
print(count)
