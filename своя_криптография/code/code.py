ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ALPHABETU = ALPHABET.upper()

key = input('Введите слово: ')
keyf = key
key = sorted(set(key), key=lambda d: key.index(d))

key_ab = ''.join(i for i in key + list(ALPHABET))
key_ab = sorted(set(key_ab), key=lambda d: key_ab.index(d))
key_ab = ''.join(i for i in key_ab)
key_abu = key_ab.upper()

input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, encoding='utf-8') as f:
    texts = f.readlines()

def encrypt(text):
    encrypt_text = ''
    for i in text:
        if i in ALPHABET:
            ind = ALPHABET.find(i)
            encrypt_text += key_ab[ind]
        elif i in ALPHABETU:
            ind = ALPHABETU.find(i)
            encrypt_text += key_abu[ind]
        else:
            encrypt_text += i
    return encrypt_text

with open(output_file, 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(encrypt(text))
    f.write('===============\n' + ''.join(i for i in keyf))
