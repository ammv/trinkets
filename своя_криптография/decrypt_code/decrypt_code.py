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

def decrypt(text):
    decrypt_text = ''
    for i in text:
        if i in ALPHABET:
            ind = key_ab.find(i)
            decrypt_text += ALPHABET[ind]
        elif i in ALPHABETU:
            ind = key_abu.find(i)
            decrypt_text += ALPHABETU[ind]
        else:
            decrypt_text += i
    return decrypt_text

with open(output_file, 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(decrypt(text))
    f.write('===============\n' + ''.join(i for i in keyf))
