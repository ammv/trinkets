text = input()

def text_to_hex(text):
    hex_text = [str(hex(ord(i)))[2:] for i in text]
    return ''.join(hex_text)

print(text, len(text))


tth = text_to_hex(text)
print(tth, len(tth))
