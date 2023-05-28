# "Задача 38: Дополнить телефонный справочник возможностью изменения и удаления
# данных. Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных"

import os

def export(data):
    name = input('Введите Имя, Фамилию и телефон: ').title()
    with open('tel.txt', 'a', encoding='utf-8') as f:
        f.write(name)
        f.write('\n')
    reset_data()

def serch_data(data):
    flag = 1
    name = input('Введите данные абонента: ').title()
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag:
        print('Нет таких данных ')
    reset_data()

def del_memb(data):
    name = input('Введите данные: ').title()
    with open('tel.txt', 'r', encoding='utf-8') as input_file, open("temp.txt", "w", encoding='utf-8') as output_file:
        for line in input_file:
            if name not in line:
                output_file.write(line)
    os.remove("tel.txt")
    os.rename("temp.txt", "tel.txt")
    reset_data()

def readfile(filename):
    data = [i for i in open(filename, 'r', encoding='utf-8')]
    return data


def printinfo(data):
    reset_data()
    if len(data) == 0:
        print('Справочник пуст')
    else:
        for i in data:
            print(i)

def reset_data():
    global data
    data = readfile('tel.txt')

def main():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экпорт данных')
        print('3 - поиск данных')
        print('4 - удаление данных')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: export, 3: serch_data, 4: del_memb}
        operations[my_choice](data)
    print('До свидания')

if __name__ == '__main__':
    main()
