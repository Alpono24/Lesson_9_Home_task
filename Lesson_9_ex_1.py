print("Lesson 9. Home task №1.")

"""
1.Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
• Вывести имя вашей ОС
• Вывести путь до папки, в которой вы находитесь
• Рассортировать файлы по расширениям, например, для текстовых файлов создается папка, в неё перемещаются все файлы с расширением .txt, 
  то же самое для остальных расширений
• После рассортировки выводится сообщение типа «в папке с текстовыми файлами перемещено 5 файлов, их суммарный размер – 50 гигабайт»
• Как минимум один файл в любой из получившихся поддиректорий переименовать. Сделать вывод сообщения типа «Файл data.txt был переименован в some_data.txt»
• Программа должна быть кроссплатформенной – никаких хардкодов с именем диска и слэшами
"""
import os
import platform

# Вывести имя вашей ОС
print("1.")
print("1.1 Имя ОС: ", os.name)
print("1.2 Имя ОС: ", platform.system())
print("1.3 Полное имя и версия ОС: ", platform.platform())
print("1.4 Версия ядра: ", platform.release())
print("1.5 Архитектура процессора: ", platform.architecture()[0])

# Вывести путь до папки, в которой вы находитесь
current_directory = os.getcwd()
print("")
print("2. Полный путь до папки в которой находимся: ", current_directory)
print("")

# Рассортировать файлы по расширениям
print("3. Рассортировать файлы по расширениям")
print("")

if not os.path.exists("HT_Les_9_ex_1"):
    os.mkdir("HT_Les_9_ex_1")
    print("Создана папка: ", "HT_Les_9_ex_1")
else:
    pass
    count_txt = 0
    count_txt_size = 0
    count_docx = 0
    count_docx_size = 0
    count_rar = 0
    count_rar_size = 0

    for file in os.listdir("HT_Les_9_ex_1"):

         if file.endswith(".txt"):
             if not os.path.exists("HT_Les_9_ex_1/Folder_txt"):
                 os.mkdir("HT_Les_9_ex_1/Folder_txt")
             else:
                 pass
             count_txt+=1
             os.replace(f"HT_Les_9_ex_1/{file}", f"HT_Les_9_ex_1/Folder_txt/{file}")
             count_txt_size += os.stat(f"HT_Les_9_ex_1/Folder_txt/{file}").st_size # Определяю размер перемещаемого файла
             print(f"Для .txt: Размер папки после перемещения №{count_txt} : {round(count_txt_size/1024, 3)} Килобайт ")

         if file.endswith(".docx"):
             if not os.path.exists("HT_Les_9_ex_1/Folder_docx"):
                 os.mkdir("HT_Les_9_ex_1/Folder_docx")
             else:
                 pass
             count_docx += 1
             os.replace(f"HT_Les_9_ex_1/{file}", f"HT_Les_9_ex_1/Folder_docx/{file}")
             count_docx_size += os.stat(f"HT_Les_9_ex_1/Folder_docx/{file}").st_size  # Определяю размер перемещаемого файла
             print(f"Для .docx: Размер папки после перемещения №{count_docx} : {round(count_docx_size / 1024, 3)} Килобайт ")

         if file.endswith(".rar"):
             if not os.path.exists("HT_Les_9_ex_1/Folder_rar"):
                 os.mkdir("HT_Les_9_ex_1/Folder_rar")
             else:
                 pass
             count_rar += 1
             os.replace(f"HT_Les_9_ex_1/{file}", f"HT_Les_9_ex_1/Folder_rar/{file}")
             count_rar_size += os.stat(f"HT_Les_9_ex_1/Folder_rar/{file}").st_size  # Определяю размер перемещаемого файла
             print(f"Для .rar: Размер папки после перемещения №{count_rar} : {round(count_rar_size / 1024, 3)} Килобайт ")


    try:
        os.rename("HT_Les_9_ex_1/Folder_txt/file1.txt", "HT_Les_9_ex_1/Folder_txt/some_data.txt")
        print("")
        print("Файл file.txt был переименован в some_data.txt")
    except OSError:
        print("Ошибка. Переименовать файл не получилось!")

    print("")


print(f"В папку с TXT-файлами перемещено {count_txt} файлa(ов), их суммарный размер - {round(count_txt_size/1024, 2)} Килобайт")
print(f"В папку с DOC-файлами перемещено {count_docx} файлa(ов), их суммарный размер - {round(count_docx_size / 1024, 2)} Килобайт")
print(f"В папку с RAR-файлами перемещено {count_rar} файлa(ов), их суммарный размер - {round(count_rar_size / 1024, 2)} Килобайт")
print( f"Итого общий размер перемещаемых файлов {round((count_txt_size + count_docx_size + count_rar_size) / 1024, 3)} Килобайт")

print("Программа завершила работу.")




