alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
al_up_ru = alphabet_ru.upper()
al_up_en = alphabet_en.upper()
# numbers = '123456789'
#СИМВОЛЫ ДЛЯ РАСШИФРОВКИ
while True:
    s = int(input('Введите сдвиг: '))
    input_file = 'input3.txt'
    output_file = 'output3.txt'
    #ВХОДНОЙ И ВЫХОДНОЙ ФАЙЛЫ

    texts = []
    #СТРОКИ ИЗ ФАЙЛА

    with open(input_file, encoding='utf-8') as f:
        for line in f.readlines():
            texts.append(line)
    #ЧТЕНИЕ СТРОК В ФАЙЛЕ, И ДОБАВЛЕНИЕ ИХ В СПИСОК

    def decrypt_ceaser(text, shift=s):
        text = list(text)
        decrypt_text = ''
        for element in text:
            if element in alphabet_en:
                new_el = alphabet_en[alphabet_en.index(element)-shift]
                decrypt_text += new_el

            elif element in alphabet_ru:
                new_el = alphabet_ru[alphabet_ru.index(element)-shift]
                decrypt_text += new_el

            elif element in al_up_en:
                new_el = al_up_en[al_up_en.index(element)-shift]
                decrypt_text += new_el

            elif element in al_up_ru:
                new_el = al_up_ru[al_up_ru.index(element)-shift]
                decrypt_text += new_el

            # elif element in numbers:
            #     new_el = numbers[numbers.index(element)-shift]
            #     decrypt_text += new_el
            else:
                decrypt_text += element


        return decrypt_text

    with open(output_file, 'w', encoding='utf-8') as f:
        for text in texts:
            f.write(decrypt_ceaser(text))
        f.write(f'==============\nKEY: {s}')
