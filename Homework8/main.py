"""
Задача 38: Дополнить телефонный справочник возможностью изменения 
и удаления данных. Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных
"""
file_path = "file.txt"
import os

def show_all_records():
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(*line.strip().split(";"))

def search_record(val):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if val in line:
                print(line, end="")

def add_contact(new_contact_fio, new_contact_number):
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(new_contact_fio.replace(" ",";"))
        f.write(';')
        f.write(new_contact_number)

def change_contact(val, new_contact_fio, new_contact_number):
    with open(file_path, "r", encoding="utf-8") as input:
        with open("temp.txt", "w", encoding="utf-8") as output:
            for line in input:
                if val not in line.strip("\n"):
                    output.write(line)
                else:
                    print(line)
                    output.write(new_contact_fio.replace(" ",";"))
                    output.write(';')
                    output.write(new_contact_number)    
                    output.write("\n")
    os.replace('temp.txt', file_path)

def delete_contact(val):
    with open(file_path, "r", encoding="utf-8") as input:
        with open("temp.txt", "w", encoding="utf-8") as output:
            for line in input:
                if val not in line.strip("\n"):
                    output.write(line)
    os.replace('temp.txt', file_path)

def main():
    print(
        "Выберите действие: 1 - Показать справочник"
        " 2 - найти контакт, "
        " 3 - добавить контакт"
        " 4 - изменить контакт"
        " 5 - удалить контакт"
    )
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input("Введите фамилию для поиска: ")
        search_record(name)
    elif select == 3:
        fio = input("Введите ФИО через пробел: ")
        number = input("Введите номер: ")
        add_contact(fio, number)
    elif select == 4:
        name = input("Введите фамилию которую нужно изменить: ")
        fio = input("Введите новые ФИО через пробел: ")
        number = input("Введите новый номер: ")
        change_contact(name, fio, number)
    elif select == 5:
        name = input("Введите фамилию: ")
        delete_contact(name)

main()
