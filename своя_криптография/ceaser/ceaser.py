alphabet_en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
al_up_ru = alphabet_ru.upper()
al_up_en = alphabet_en.upper()
# numbers = '12345678901234567890'
#СИМВОЛЫ ДЛЯ РАСШИФРОВКИ

s = int(input('Введите сдвиг не больше 9: '))

input_file = 'input2.txt'
output_file = 'output2.txt'
#ВХОДНОЙ И ВЫХОДНОЙ ФАЙЛЫ

texts = []
#СТРОКИ ИЗ ФАЙЛА

with open(input_file, encoding='utf-8') as f:
    for line in f.readlines():
        texts.append(line)
#ЧТЕНИЕ СТРОК В ФАЙЛЕ, И ДОБАВЛЕНИЕ ИХ В СПИСОК

def ceaser(text, shift=s):
    text = list(text)
    encrypt_text = ''
    for element in text:
        if element in alphabet_en:
            new_el = alphabet_en[alphabet_en.index(element)+shift]
            encrypt_text += new_el

        elif element in alphabet_ru:
            new_el = alphabet_ru[alphabet_ru.index(element)+shift]
            encrypt_text += new_el

        elif element in al_up_en:
            new_el = al_up_en[al_up_en.index(element)+shift]
            encrypt_text += new_el

        elif element in al_up_ru:
            new_el = al_up_ru[al_up_ru.index(element)+shift]
            encrypt_text += new_el

        # elif element in numbers:
        #     new_el = numbers[numbers.index(element)+shift]
        #     encrypt_text += new_el
        else:
            encrypt_text += element

    return encrypt_text

with open(output_file, 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(ceaser(text))
