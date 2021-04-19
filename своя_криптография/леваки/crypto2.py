import numpy as np
import random

input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    input_text = f.read().strip()

lentext = len(input_text)
input_text = list(input_text)

output_texts = []
output_texts.append(''.join(i for i in input_text))
secretkey = random.randint(100, 999)

if ' ' in list(output_texts[-1]):
    elements= []
    for i in range(len(min([i for i in output_texts[0]]))+secretkey):
        texts = output_texts[-1].split()
        if len(elements) == 0:
            for word in texts:
                word = list(word)
                el = word[0]
                word.pop(word.index(el))
                word.append(el)
                elements.append(''.join(i for i in word))
        else:
            for word in elements:
                word2 = list(word)
                el = word[0]
                word2.pop(word2.index(el))
                word2.append(el)
                elements[elements.index(word)] = ''.join(i for i in word2)

        text = ''.join(i + ' ' for i in elements)
        output_texts.append(text)


else:
    for i in range(49):
        text = list(output_texts[-1])
        el = text[0]
        text.pop(text.index(el))
        text.append(el)
        output_texts.append(''.join(i for i in text))

with open(output_file, 'w', encoding='utf-8') as f:
    for i in output_texts: f.write(i[::-1] + '\n')
