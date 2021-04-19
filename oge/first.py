class Cdict:

    def __init__(self):
        self.data = None
        self.entext = None
        self.detext = None

    def set_data(self, data):
        #key value
        data = data.split(',')
        data_dict = {}
        for i in data:
            i= i.split()
            data_dict[i[0]] = i[1]
        self.data = data_dict
        print(self.data)

    def decode(self, text):
        print(self.data)
        import time
        self.entext = text.rstrip()
        self.detext = [None]*len(self.entext)
        k = 0
        for i in text:
            if i in self.data.keys():
                self.detext[k] = self.data[i]
            else:
                j = k
                while True:
                    i = text[k:j]
                    if i in self.data.keys():
                        self.detext[k] = self.data[i]
                        break
                    if j+1 < len(text):
                        j += 1
                    else: break
            k += 1
                    

        print(''.join(i for i in self.detext if i!= None))


ci = Cdict()
data = '@+ К, ~- Л, +@ М, @~+ Н, + О, ~ П'
ci.set_data(data)
text = '+~+~+@@~+'
ci.decode(text)
