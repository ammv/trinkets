class CCS:

    #АЛФАВИТЫ
    _RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _NUMS = '0123456789'
    _SYMBOLS = {' ': 'пробел', ',': 'запятая', '!': 'знаквосклицания', '?': 'знаквопроса', '.': 'точка', '-': 'дефис',
                '=': 'равно', ')': 'праваяскобка', '(': 'леваяскобка', '@': 'собакапочта', '%': 'процент',
                '#': 'решетка', '*': 'звёздочка', '+': 'плюс'}
    #_CLASSES = {'S': _S(), 'IS': CCS._IS(), 'D': CCS._D(), 'OS': CCS._OS(), 'OIS': CCS._OIS()}

    #ИНИЦИАЛИЗАЦИЯ КЛЮЧА КЛАССА СДВИГА
    #ПРОВЕРКА LCS НА ВАЛИДНОСТЬ
    #ПРОВЕРКА КЛАССА НА СУЩЕСТВОВАНИЕ
    @classmethod
    def key(self, column, _class, shift, symbols = False, debug=False, multi=False):
        column, _class, shift = str(column), str(_class), str(shift)
        CCS._check_lcs(column, _class, shift, symbols, debug, multi)
        _class = CCS._find_class(_class)
        return (CCS._table(column, shift, _class, symbols, debug, multi))

    #СОЗДАНИЕ ТАБЛИЦ
    def _table(column, shift, _class, symbols, debug, multi):
        column, shift = int(column), int(shift)
        #СОЗДАНИЕ АЛФАВИТА В ВИДЕ ТАБЛИЦЫ
        language = CCS._RU + '#' * column

        table = []
        for i in range(0, len(language), column):
            table.append(language[i:i+column])

        for i in table.copy():
            if i[0] == '#':
                table.remove(i)
        dictt = dict((('table', table), ('language', CCS._RU), ('shift', shift), ('class', _class), ('symbols', symbols),
                    ('debug', debug), ('multi', multi)))
        return dictt

    #ENCODE
    @classmethod
    def encode(self, text, args):
        if args['class'] == 'S':
            f = CCS._S(text, args)
        elif args['class'] == 'IS':
            f = CCS._IS(text, args)
        elif args['class'] == 'D':
            f = CCS._D(text, args)
        elif args['class'] == 'OS':
            f = CCS._OS(text, args)
        elif args['class'] == 'OIS':
            f = CCS._OIS(text, args)
        elif args['class'] == 'MC':
            f = CCS._MC(text, args)
        return f

    @classmethod
    def decode(self, text, args):
        if args['class'] == 'S':
            f = CCS._deS(text, args)
        elif args['class'] == 'IS':
            f = CCS._deIS(text, args)
        elif args['class'] == 'D':
            f = CCS._deD(text, args)
        elif args['class'] == 'OS':
            f = CCS._deOS(text, args)
        elif args['class'] == 'OIS':
            f = CCS._deOIS(text, args)
        elif args['class'] == 'MC':
            f = CCS._deMC(text, args)
        return f

    #STANDART
    def _S(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']+args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:
            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = row.index(letter)
                        if i_row != max_rows - 1 and i_row + 1 <= max_rows - 1:
                            if table[i_row+1][i_letter] == '#':
                                i_letter = lang.index(table[i_row][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang.index(table[i_row+1][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('ОПУСТИЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                        elif i_row == max_rows - 1:
                            if i_row < 0:
                                i_letter = lang.index(table[i_row][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang.index(table[i_row-1][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = row.index(letter)
                        if i_row != max_rows - 1 and i_row + 1 <= max_rows - 1:
                            if table_low[i_row+1][i_letter] == '#':
                                i_letter = lang_low.index(table_low[i_row][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang_low.index(table_low[i_row+1][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('ОПУСТИЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                        elif i_row == max_rows - 1:
                            if i_row < 0:
                                i_letter = lang_low.index(table_low[i_row][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang_low.index(table_low[i_row-1][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    #INVERSION STANDART
    def _IS(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']+args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:

            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = row.index(letter)
                        if max_rows > 2:
                            if i_row != 0 and i_row != max_rows-1:
                                i_letter = lang.index(table[i_row-1][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang.index(table[i_row][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                        else:
                            i_letter = lang.index(table[i_row][i_letter])
                            new_letter = lang[i_letter+shift]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)

            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = row.index(letter)
                        if max_rows > 2:
                            if i_row != 0 and i_row != max_rows-1:
                                i_letter = lang_low.index(table_low[i_row-1][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang_low.index(table_low[i_row][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                        else:
                            i_letter = lang_low.index(table_low[i_row][i_letter])
                            new_letter = lang_low[i_letter+shift]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    #DOWN
    def _D(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']+args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:

            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = row.index(letter)
                        if max_rows > 1:
                            if i_row != max_rows - 1:
                                if table[i_row+1][i_letter] == '#':
                                    i_letter = lang.index(table[i_row][i_letter])
                                    new_letter = lang[i_letter+shift]
                                    if args['debug'] == True:
                                        print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                                else:
                                    i_letter = lang.index(table[i_row+1][i_letter])
                                    new_letter = lang[i_letter+shift]
                                    if args['debug'] == True:
                                        print('ОПУСТИЛИ БУКВУ(index) ->:', i_letter+1)
                                        print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang.index(table[i_row][i_letter])
                                new_letter = lang[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                        else:
                            i_letter = lang.index(table[i_row][i_letter])
                            new_letter = lang[i_letter+shift]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)

            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = row.index(letter)
                        if max_rows > 1:
                            if i_row != max_rows - 1:
                                i_letter = lang_low.index(table_low[i_row+1][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('ОПУСТИЛИ БУКВУ(index) ->:', i_letter+1)
                                    print('СДЕЛАЛИ СДВИГ ->:', new_letter)
                            else:
                                i_letter = lang_low.index(table_low[i_row][i_letter])
                                new_letter = lang_low[i_letter+shift]
                                if args['debug'] == True:
                                    print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
                        else:
                            i_letter = lang_low.index(table_low[i_row][i_letter])
                            new_letter = lang_low[i_letter+shift]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    #ONLY SHIFT
    def _OS(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']+args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:

            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = row.index(letter)

                        i_letter = lang.index(table[i_row][i_letter])
                        new_letter = lang[i_letter+shift]
                        if args['debug'] == True:
                            print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)

            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = row.index(letter)

                        i_letter = lang_low.index(table_low[i_row][i_letter])
                        new_letter = lang_low[i_letter+shift]
                        if args['debug'] == True:
                            print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)

            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    #ONLY INVERSION SHIFT
    def _OIS(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']+args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:

            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = row.index(letter)

                        i_letter = lang.index(table[i_row][i_letter])
                        new_letter = lang[i_letter-shift]
                        if args['debug'] == True:
                            print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = row.index(letter)

                        i_letter = lang_low.index(table_low[i_row][i_letter])
                        new_letter = lang_low[i_letter-shift]
                        if args['debug'] == True:
                            print('СДЕЛАЛИ ТОЛЬКО СДВИГ ->:', new_letter)
            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    def _MC(text, args):
        try:
            multi = args['multi']
            multi = multi.split('/')
        except:
            print('Error in multi', multi)
            exit()
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        multi = multi * len(text)
        multi = multi[0:len(text)]

        k = 0
        for i in text:
            args['class'] = multi[k]
            try:
                encoded_text += CCS.encode(i, args)
            except:
                print('Error in multi')
                exit()
            else:
                k += 1

        return encoded_text

    def _deS(text, args):
        shift = args['shift']
        table = args['table']
        table_low = [row.lower() for row in table]
        lang = args['language']
        lang_low = lang.lower()

        max_rows = len(table)
        encoded_text = ''

        if args['symbols'] == True:
            for key in CCS._SYMBOLS.keys():
                try:
                    text = text.replace(key, CCS._SYMBOLS[key])
                except:
                    pass

        for letter in text:
            if args['debug'] == True:
                print('БУКВА ИЗ TEXT:', letter)
            #UPPER
            if letter in lang:
                for row in table:
                    if letter in row:
                        i_row = table.index(row)
                        i_letter = lang.index(letter)-shift
                        if max_rows == 1:
                            new_letter = lang[i_letter]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО ОБРАТНЫЙ СДВИГ:', new_letter)

                        elif max_rows > 1:

                            if args['debug'] == True:
                                print('СДЕЛАЛИ ОБРАТНЫЙ СДВИГ:', lang[i_letter])

                            for row in table:
                                if lang[i_letter] in row:
                                    new_row = table.index(row)
                                    i_new_letter = row.index(lang[i_letter])

                            if new_row != max_rows - 1:
                                new_row += 1
                                new_letter = table[new_row][i_new_letter]
                                if args['debug'] == True:
                                    print('ОПУСТИЛИ БУКВУ:', new_letter)

                            elif new_row == max_rows - 1:
                                new_row -= 1
                                new_letter = table[new_row][i_new_letter]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ:', new_letter)
            #LOWER
            elif letter in lang_low:
                for row in table_low:
                    if letter in row:
                        i_row = table_low.index(row)
                        i_letter = lang_low.index(letter)-shift
                        if max_rows == 1:
                            new_letter = lang_low[i_letter]
                            if args['debug'] == True:
                                print('СДЕЛАЛИ ТОЛЬКО ОБРАТНЫЙ СДВИГ:', new_letter)

                        elif max_rows > 1:

                            if args['debug'] == True:
                                print('СДЕЛАЛИ ОБРАТНЫЙ СДВИГ:', lang_low[i_letter])

                            for row in table_low:
                                if lang_low[i_letter] in row:
                                    new_row = table_low.index(row)
                                    i_new_letter = row.index(lang_low[i_letter])

                            if new_row == 0:
                                new_row += 1
                                new_letter = table_low[new_row][i_new_letter]
                                if args['debug'] == True:
                                    print('ОПУСТИЛИ БУКВУ:', new_letter)

                            elif new_row != max_rows - 1:
                                new_row -= 1
                                new_letter = table_low[new_row][i_new_letter]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ:', new_letter)

                            elif new_row == max_rows - 1:
                                new_row -= 1
                                new_letter = table_low[new_row][i_new_letter]
                                if args['debug'] == True:
                                    print('ПОДНЯЛИ БУКВУ:', new_letter)
            else:
                new_letter = letter

            encoded_text += new_letter

        return encoded_text

    #ПОИСК КЛАССА ИЛИ ПРОВЕРКА НА ВАЛИДНОСТЬ
    def _find_class(_class):
        CLASSES = ['S', 'IS', 'D', 'OS', 'OIS', 'MC']

        if _class in CLASSES:
            return _class
        else:
            print('This class not exist')
            exit()

    #ПРОВЕРКА ДАННЫХ НА ВАЛИДНОСТЬ
    def _check_lcs(column, _class, shift, symbols, debug, multi):
        #invalid line
        if column.isdigit():
            if int(column) < 1:
                print('Column must be then more 0')
                exit()
        elif column.isalpha():
            print('Line must be a number')
            exit()

        #invalid class
        if _class.isalpha():
            pass
        elif _class.isdigit():
            print('Class must be alpha')
            exit()

        #invalid shift
        if shift.isdigit():
            pass
        elif column.isalpha():
            print('Shift must be a number')
            exit()

        if symbols not in [True, False]:
            print('Whitespace must be bool')
            exit()

        if debug not in [True, False]:
            print('Debug must be bool')
            exit()

        if multi == False and _class == 'MC':
            print('To use the MC class you must specify special arguments')
            exit()

        if _class == 'MC' and type(multi) != str:
            print('Multi must be string. IS/OS/D...')
            exit()
