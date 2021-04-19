import numpy
import cv2
import os

class Values:

    @classmethod
    def names(self):
        dnames = {
            '0': '50rub',
            '1': '100rub',
            '2': '500rub',
            '3': '1000rub',
            '4': '5000rub',
            }
        return dnames

    @classmethod
    def target(self):
        files = self.get_files()
        targets = []
        for file in files:
            if '50r' in file:
                targets.append(0)
            elif '100r' in file:
                targets.append(1)
            elif '500r' in file:
                targets.append(2)
            elif '1000r' in file:
                targets.append(3)
            elif '5000r' in file:
                targets.append(4)
            else:
                print('Некорректный файл - ', file)

        targets_dict = {file: target for file, target in zip(files, targets)}
        return targets_dict, numpy.array(targets)

    @classmethod
    def data(self):
        files = self.get_files()
        ddata = []
        for file in files:
            name = 'img\\' + file
            read = cv2.imread(name)
            gray_image = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
            n_image = numpy.around(numpy.divide(gray_image, 255.0), decimals=1)
            ddata.append(n_image)
        ddata = numpy.array(ddata)
        return ddata.reshape((len(files),-1)), files

    @classmethod
    def get_data(self, img):
        if img.endswith('jpg'):
            name = 'test\\'+img
            read = cv2.imread(name)
            gray_image = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
            n_image = numpy.around(numpy.divide(gray_image, 255.0), decimals=1)
            return n_image.reshape((1,-1))
            
    @classmethod
    def get_files(self):
        return list(filter(lambda x: True == x.endswith('jpg'),
                os.listdir(os.getcwd()+'\\img')))
