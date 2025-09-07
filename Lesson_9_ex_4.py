import re

print("Lesson 9. Home task №4.")

"""
4. Напишите программу, которая получает на вход строку с названием текстового файла и выводит на экран содержимое этого
файла, заменяя все запрещённые слова звездочками.
Запрещённые слова, разделённые символом пробела, должны храниться в файле stop_words.txt.
Программа должна находить запрещённые слова в любом месте файла, даже в середине другого слова. 
Замена независима от регистра: если в списке запрещённых есть слово exam, то замениться должны exam, eXam, EXAm и другие вариации.

Пример.
в stop_words.txt записаны слова: hello email python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python IS the
programming language of thE future. My EMAIL is... PYTHON as
AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming language of
*** future. My ***** **... ****** ** awesome!!!!
"""

import re

with (open("for_ex_4_input.txt", 'r', encoding='utf-8') as f,
      open("for_ex_4_stop_words.txt", 'r', encoding='utf-8') as f_stop):

    stop_words = f_stop.read().split()
    text = f.read()


    for word in stop_words:
        word = word.lower()
        pattern = r'\b' + word + r'\b'
        # pattern = r'\b' + re.escape(word.lower()) + r'\b'
        replacement = '*' * len(word)
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)


        # text = text.lower()
        # text = text.replace(word, replacement)

print(text)
