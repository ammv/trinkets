from string import ascii_lowercase, ascii_uppercase


def rf(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print("Ошибка во время чтения:", e)
        
def count_bytes(bytes):
    bytes_dict = {}
    for byte in bytes:
        if byte not in bytes_dict.keys():
            x = bytes.count(byte)
            bytes_dict[byte] = x
            
    return bytes_dict
    
def apply_value(bytes_dict):
    alphabet = ascii_lowercase[7:] + ascii_uppercase + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    value_dict = {}
    i = 0
    for key in bytes_dict:
        if bytes_dict[key] > 1:
            value_dict[key] = alphabet[i]
            i += 1
             
    return value_dict
    
def add_comp(text):
    skip = False
    new_text = ''
    j = -1
    for i in range(len(text)):
        if i > j:
            if skip == True:
                if text[i] == '>':
                    skip = False
                new_text += text[i]
                    
            elif skip == False:
                if text[i] == '<':
                    skip = True
                    new_text += text[i]     
                else:
                    if i+1< len(text):
                        if text[i] == text[i+1]:
                            k = i
                            while text[i] == text[k] and k <= len(text):
                                k += 1
                            new_text += str(k-i) + text[i]
                            j = k
                        else:
                            new_text += text[i]
                    else:
                        new_text += text[i]
                    
    return new_text
                        
    
def wf(text_bytes, value_dict, fp):
    values = ''
    for key, value in value_dict.items():
        values += f'{value}={key}\n'
            
    text = ''
    for byte in text_bytes:
        if byte in value_dict:
            text += value_dict[byte]
        else:
            text += f'<{byte}>'
    text = values + '!' + add_comp(text)
            
    try:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(text)
            print(f'Файл {fp} записан')
            
    except:
        print('Ошибка при записи')
        
def file_name(name):
    name = name[::-1]
    ex = name.find('.')
    fname = name[ex+1:][::-1]
    return fname
                
        
file = "kto.txt";
text = rf(file)

text_bytes = [str(hex(ord(i)))[2:] for i in text]

bytes_dict = count_bytes(text_bytes)
value_dict = apply_value(bytes_dict)
wf(text_bytes, value_dict, file_name(file) + '.maa')
