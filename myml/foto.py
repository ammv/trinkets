from numpy import array
import cv2
import os


class IMG:

    #FROM IMG2 TO IMG!!!

    def __init__(self, img, path='img\\'):
        self.img2 = 'img2\\'+img
        self.img = path+img
        self.name = img

    def iread(self):
        self.img2 = cv2.imread(self.img2)

    def resize(self):
        self.img2 = cv2.resize(self.img2, (800, 600))

    def data(self):
        self.data = array(self.img2)
        print(self.data.shape)

    def save(self):
        cv2.imwrite(self.img, self.img2)
        print('{} сохранена и изменена'.format(self.name))

    def jpg(self):
        return cv2.imwrite(self.name, self.img2,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100])


def get_files():
    return list(filter(lambda x: True == x.endswith('jpg'),
            os.listdir(os.getcwd()+'\\img2')))

path = input('Путь?: ')
if len(path) == 0: path = 'img\\'

try:
    for file in get_files():
        x = IMG(file, path)
        x.iread()
        x.resize()
        x.save()
except:
    print('ошибка в: ' + file)

print('проверяй')



        



