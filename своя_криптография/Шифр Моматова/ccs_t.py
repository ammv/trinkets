from ccs import CCS as cs

#ТАБЛИЦА ПОКА ТОЛЬКО ДЛЯ РУССКОГО ЯЗЫКА
#ВПРОЧЕМ РЕАЛИЗАЦИЯ ЭТОГО ШИФРА ПРОСТО ПРАКТИКА В КРИПТОГРАФИИ(нет)) )

#Ыьу цтуах эруьх абяосьэ юэыэсчбу!ЫЬУ ЬВХЬО РОСО ЮЭЫЭТХ!

while True:
    text = input()
    #columns, class, shift, symbols = False, debug=False, multi=False
    key = cs.key(16, 'S', 3, debug=False)
    #text, key
    encoded_text= cs.encode(text, key)
    print(encoded_text)
    text2 = input()
    decoded_text= cs.decode(text2, key)
    def f():
        b = 0
        l = len(text)
        for i in range(len(text)):
            if text[i] == text2[i]:
                b += 1
        return round(l / 100 * b, 2)
    print(decoded_text)
    print(str(f()) + "%")


