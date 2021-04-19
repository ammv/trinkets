import random
import time
text = 'Артём'
alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba123456789'
alpha = list(alpha)
key =''
for i in range(len(alpha)):
    char = random.choice(alpha)
    key += ''.join(alpha.pop(alpha.index(char)))
text = list(text)
key = list(key)
for k, i in enumerate(text, start=0):
    text[k]=key[key.index(i)]
    print(key[key.index(i)])
    print(text)
print(''.join(i for i in text))
