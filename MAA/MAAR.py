def rf(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print("Ошибка во время чтения:", e)
        
def get_dict(text):
    ts = text.split('\n')
    values_dict = {}
    for i in range(len(ts)):
        if '=' in ts[i]:
            x = ts[i].split('=')
            values_dict[x[0]] = x[1]
        else:
            break
    
    return values_dict
    
def start_text(text):
    x = text.find('!')
    return x+1
    
def recomp(text):
    skip = False
    recomp_text = ''
    j = -1
    for i in range(len(text)):
        if i > j:
            if skip == True:
                if text[i] == '>':
                    skip = False
                recomp_text += text[i]
                
            elif skip == False:
                if text[i] == '<':
                    skip = True
                    recomp_text += text[i]
                else:
                    if i< len(text):
                        if text[i].isdigit():
                            recomp_text += text[i+1] * int(text[i])
                            j = i + int(text[i])-1
                        else:
                            recomp_text += text[i]
                    else:
                        recomp_text += text[i]
                        
    return recomp_text
    
def text_to_values(value_dict, recomp_text):
    text_list = []
    skip = False
    not_value = ''
    k = 0
    for i in recomp_text:
        if skip == True:
            if i == '>':
                skip = False
                text_list.append(not_value)
                not_value = ''
            else:
                not_value += i
                
        elif skip == False:
            if i == '<':
                skip = True
            else:
                text_list.append(value_dict[i])
                
        k += 1
        
    return text_list
                
def values_to_str(text_list):
    text = ''
    for i in text_list:
        i = '0x' + i
        text += chr(int(i, 16))
    
    return text
            
        
    
file = 'kto.maa'
text = rf(file)
values_dict = get_dict(text)
recomp_text = recomp(text[start_text(text):])
text_list = text_to_values(values_dict, recomp_text)
text = values_to_str(text_list)

with open('kto.txt', encoding='utf-8') as f:
    x = f.read()

with open('kto_maar.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(len(text), len(x), text==x)

        
