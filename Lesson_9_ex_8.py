

print("Lesson 9. Home task №8.")
"""
8. JSON и CSV.
Исходные данные:
https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2XnJDv9xN2LxusbE?usp=sharing

Пункты задания:
• 0+. Есть данные в формате JSON – взять с диска с исходными данными.
• 1 Реализовано №1. Реализовать функцию, которая считает данные из исходного JSON-файла и преобразует их в формат CSV
• 2. Реализовано №1. Реализовать функцию, которая сохранит данные в CSV-файл 
    (данные должны сохраняться независимо от их количества – если добавить в исходный JSON-файл ещё одного сотрудника, работа программы не должна нарушаться).
• 3 - Реализовано №3. Реализовать функцию, которая добавит информацию о новом сотруднике в JSON-файл. Пошагово вводятся все необходимые данные о сотруднике, формируются данные для записи.
• 4 - Реализовано №4. Такая же функция для добавления информации о новом сотруднике в CSV-файл.
• 5 -Реализовано №5.Реализовать функцию, которая выведет информацию об одном сотруднике по имени. Имя для поиска вводится с клавиатуры.
• 6. Реализовано №6. Реализовать функцию фильтра по языку: с клавиатуры вводится язык программирования, выводится список всех сотрудников, кто владеет этим языком программирования.
• 7. Реализовано №7. Реализовать функцию фильтра по году: ввести с клавиатуры год рождения, вывести средний рост всех сотрудников, у которых год рождения меньше заданного.
• 9 - Реализовано.Программа должна представлять собой интерактив – пользовательское меню с возможностью выбора определённого действия (действия – функции из предыдущих пунктов + выход из программы). 
• 10 - Реализовано.Пока пользователь не выберет выход из программы, должен предлагаться выбор следующего действия.
"""

import json
import csv
from datetime import datetime

#'1 2. Конвертировать данные из JSON в CSV'
def convert_JSON_to_CSV():
    with open("employees.json", 'r') as json_f, open("for_ex_8_CSV.csv", 'w') as csv_f:
        data = json.load(json_f)
        json.dump(data, csv_f, indent=4, ensure_ascii=False)

# '3. Добавить нового сотрудника в JSON'
def add_new_person_to_JSON_file():
    with open("employees.json", 'r+',encoding='utf-8') as json_f:
        data = json.load(json_f)
    #Просто смотрю
        # print(data)

    #Счетчик до!
        count = 0
        for line in data:
            # print(line)
            count += 1
        print(f"До добавления в JSON-файле находится информация о {count} людях.")
    #Просто смотрю тип данных - это List -
        # print(type(data))

    #Произвожу ввод данных
        name_input = str(input("Введите имя: "))
        birthday_input = str(input("Введите день рождения: "))
        height_input = int(input("Введите рост: "))
        weight_input = float(input("Введите вес: "))
        car_input = bool(input("Есть ли у сотрудника автомобиль (1-да, 0 - нет): "))
        languages_input_1 = input("Введите язык программирования #1: ")
        languages_input_2 = input("Введите язык программирования #2: ")
        languages_input_3 = input("Введите язык программирования #3: ")
    #Создаю словарь с новыми данными
        dict = {'name': name_input, 'birthday': birthday_input, 'height': height_input, 'weight': weight_input, 'car': car_input, 'languages': [languages_input_1, languages_input_2, languages_input_3]}
    #Добавляю словарь с новыми данными в список
        data.append(dict)
    # print(data)

    #Очищу файл перед добавлением нового списка
    with open('employees.json', 'w', encoding='utf-8') as json_f:
        pass
    #Добавляю новый список
        json.dump(data, json_f, indent=4)

    # Счетчик после!
        count = 0
        for line in data:
            # print(line)
            count += 1
        print(f"После добавления в JSON-файле находится информация о {count} людях.")

# '4. Добавить нового сотрудника в CSV'
def add_new_person_to_CSV_file():
    with open("employees.json", 'r+',encoding='utf-8') as json_f, open("for_ex_8_CSV.csv", 'w') as csv_f:
        data = json.load(json_f)
    #Просто смотрю
        # print(data)

    #Счетчик до!
        count = 0
        for line in data:
            # print(line)
            count += 1
        print(f"До добавления в CSV-файле находится информация о {count} людях.")
    #Просто смотрю тип данных - это List -
        # print(type(data))

    #Произвожу ввод данных
        name_input = str(input("Введите свое имя: "))
        birthday_input = str(input("Введите свой день рождения: "))
        height_input = int(input("Введите свой рост: "))
        weight_input = float(input("Введите свой вес: "))
        car_input = bool(input("Есть ли у Вас машина (1-да, 0 - нет): "))
        languages_input_1 = input("Введите язык программирования #1 который вы знаете: ")
        languages_input_2 = input("Введите язык программирования #2 который вы знаете: ")
        languages_input_3 = input("Введите язык программирования #3 который вы знаете: ")
    #Создаю словарь с новыми данными
        dict = {'name': name_input, 'birthday': birthday_input, 'height': height_input, 'weight': weight_input, 'car': car_input, 'languages': [languages_input_1, languages_input_2, languages_input_3]}
    #Добавляю словарь с новыми данными в список
        data.append(dict)
        json.dump(data, csv_f, indent=4, ensure_ascii=False)
    # print(data)

    #Очищу файл перед добавлением нового списка
    with open('employees.json', 'w', encoding='utf-8') as json_f:
        pass
    #Добавляю новый список
        json.dump(data, json_f, indent=4)

    # Счетчик после!
        count = 0
        for line in data:
            # print(line)
            count += 1
        print(f"После добавления в JSON-файле находится информация о {count} людях.")

#'5. Вывод информации о сотруднике по его имени'
def find_person_by_name():
    with open("employees.json", 'r', encoding='utf-8') as json_f:

        data = json.load(json_f)
        count = 0
        print("В файле содержится информация о нижеследующих сотрудниках:")
        for i, person in enumerate(data):
            count += 1
            print(f'{i+1}. {person['name']}')
        print(f'Всего: {count} записи(ей).')
        name = input("Для вывода информации о сотруднике введите его имя: ")

        for person in data:
            if person['name'] == name:
                for key, value in person.items():
                    print(f'{key}: {value}')

#'6. Отфильтровать сотрудников по языку программирования.'
def find_persons_by_languages():
    with open("employees.json", 'r', encoding='utf-8') as json_f:

        data = json.load(json_f)
        languages = input("Для вывода информации введите название языка: ")

        for person in data:
            for i in range(0, len(person['languages'])):
                if person['languages'][i] == languages:
                    for key, value in person.items():
                        print(f'{key}: {value}')

#'7. Посчитать средний рост сотрудников младше указанного года-'
def find_mid_height_before_year():
    with open("employees.json", 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)
        year = input("Для расчета среднего роста сотрудников введите год: ")

        new_data = filter(lambda person: person['height'] < year, data)
        count = 0
        all_heights = 0
        for person in data:
            all_heights += person['height']
            # if person['height'] < year:
            count += 1
        mid_height = all_heights /count

#'7. Посчитать средний рост сотрудников младше указанного года.'
def find_mid_height_before_year():
    with open("employees.json", 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)
        manual_year = input("Для расчета среднего роста сотрудников введите год в формате ДД.ММ.ГГГГ:  ")
        year = datetime.strptime(manual_year, "%d.%m.%Y")

        new_data = list(filter(lambda person: datetime.strptime(person['birthday'],"%d.%m.%Y") < year, data))
        print(new_data)
        count = 0
        all_heights = 0
        for person in new_data:
            all_heights += person['height']
            # if person['height'] < year:
            count += 1
            mid_height = all_heights / count
        print(f'В расчете была учтена информация о {count} сотрудниках. Средняя высота сотрудников с годом рождения до {manual_year} составляет: {mid_height} см')



def menu():
    while True:
        print('               Меню')
        print('1. Считывание данных из исходного JSON-файла и преобразование их в формат CSV')
        print('2. Сохранение данных в формат CSV')
        print('3. Добавить нового сотрудника в JSON')
        print('4. Добавить нового сотрудника в CSV')
        print('5. Вывод информации о сотруднике по его имени')
        print('6. Отфильтровать сотрудников по языку программирования.')
        print('7. Посчитать средний рост сотрудников младше указанного года.')
        print('8. Выйти из программы')
        choice = input('Выберите дейстиве от 1 до 8: ')
        if choice == '1':
            print('Select #1')
            convert_JSON_to_CSV()
            print('Считывание и преобразование выполнено! Смотрите файл: for_ex_8_CSV.csv')
        elif choice == '2':
            print('Select #2')
            convert_JSON_to_CSV()
            print('Сохранение данных в формат CSV выполнено.Смотрите файл: for_ex_8_CSV.csv')
        elif choice == '3':
            print('Select #3')
            add_new_person_to_JSON_file()
            print('Новый сотрудник добавлен! Смотрите файл: employees.json')
        elif choice == '4':
            print('Select #4')
            add_new_person_to_CSV_file()
            print('Новый сотрудник добавлен! Смотрите файл: for_ex_8_CSV.csv')
        elif choice == '5':
            print('Select #5')
            find_person_by_name()
        elif choice == '6':
            print('Select #6')
            find_persons_by_languages()
        elif choice == '7':
            print('Select #7')
            find_mid_height_before_year()
        elif choice == '8':
            break
        else:
            print(' Выбор не соответствует предлагаемому действию. Повторите заново.')
menu()
