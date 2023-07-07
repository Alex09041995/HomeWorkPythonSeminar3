print("Данный код вычисляет стоимость введенного пользователем слова. На вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.")

A_eng = 'abcdefghijklmnopqrstuvwxyz'

A_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

d_english = {1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P', 4: 'F, H, V, W, Y', 5: 'K', 8: 'J, X', 10: 'Q, Z'}

d_russian = {1: 'А, В, Е, И, Н, О, Р, С, Т', 2: 'Д, К, Л, М, П, У', 3: 'Б, Г, Ё, Ь, Я', 4: 'Й, Ы', 5: 'Ж, З, Х, Ц, Ч', 8: 'Ш, Э, Ю', 10: 'Ф, Щ, Ъ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in A_eng:
    summa = 0
    for letter in word:
        for key, value in d_english.items():
            if letter.upper() in value:
                summa += key
    print(f'Cтоимость введенного Вами английского слова составляет = {summa}')

else:
    if word[0].lower() in A_rus:
        summa = 0
        for letter in word:
            for key, value in d_russian.items():
                if letter.upper() in value:
                    summa += key
    print(f'Cтоимость введенного Вами русского слова составляет = {summa}')
