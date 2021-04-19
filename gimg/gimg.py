import PIL
from PIL import Image
import random
from time import sleep

class ImageError(Exception):
    pass


class Photo:
    
    '''White Black'''
    @classmethod
    def whbl(self, image, value):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_wb' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)

        #порог
        separator = 255 / value / 2 * 3

        for x in range(size[0]):
            for y in range(size[1]):
                r,g,b = image.getpixel((x,y))
                total = r + g + b
                if total > separator:
                    new_image.putpixel((x,y), (255,255,255))
                else:
                    new_image.putpixel((x,y), (0,0,0))

        new_image.save(new_name, 'jpeg')
        print(f'Фотография {name} сохранена, порог - {value}')

    '''Dark'''
    @classmethod
    def dark(self, image, d):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_dark' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)
        try:
            for x in range(size[0]):
                for y in range(size[1]):
                    r,g,b = image.getpixel((x,y))
                    new_image.putpixel((x,y), (r//d,g//d,b//d))
            
                    
        except Exception as e:
            print(e)
                    
        new_image.save(new_name, 'jpeg')
        print(f'Фотография {name} сохранена, затемнение - {d}')

    '''Brightness'''
    @classmethod
    def brightness(self, image, br):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_brightness' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)
        try:
            for x in range(size[0]):
                for y in range(size[1]):
                    r,g,b = image.getpixel((x,y))
                    
                    r = int(r * br)
                    r = min(255, max(0, r))

                    g = int(g * br)
                    g = min(255, max(0, g))

                    b = int(b * br)
                    b = min(255, max(0, b))
                    
                    new_image.putpixel((x,y), (r,g,b))
            
                    
        except Exception as e:
            print(e)
                    
        new_image.save(new_name, 'jpeg')
        print(f'Фотография {name} сохранена, засветление - {br}')

    '''Negative'''
    @classmethod
    def negative(self, image):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_negative' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)
        try:
            for x in range(size[0]):
                for y in range(size[1]):
                    r,g,b = image.getpixel((x,y))
                    new_image.putpixel((x,y), (255-r,255-g,255-b))
                    
        except Exception as e:
            print(e)
                    
        new_image.save(new_name, 'jpeg')
        print(f'Фотография {name} сохранена')

    '''gray'''
    @classmethod
    def gray(self, image):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_gray' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)
        try:
            for x in range(size[0]):
                for y in range(size[1]):
                    r,g,b = image.getpixel((x,y))
                    gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                    new_image.putpixel((x,y), (gray, gray, gray))
                    
        except Exception as e:
            print(e)
                    
        new_image.save(new_name, 'jpeg')
        print(f'Фотография {name} сохранена')


    '''Контраст'''
    @classmethod
    def contrast(self, image, c):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        
        new_name = name.split('.')[0] + '_contrast' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)

        avg = 0
        for x in range(size[0]):
            for y in range(size[1]):
                r, g, b = image.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= size[0] * size[1]

        palette = []
        for i in range(256):
            temp = int(avg + c * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for x in range(size[0]):
            for y in range(size[1]):
                r, g, b = image.getpixel((x, y))
                new_image.putpixel((x, y), (palette[r], palette[g], palette[b]))

        new_image.save(new_name, "JPEG")
        print(f'Фотография {name} сохранена, c% - {c}')

    '''encode'''
    @classmethod
    def encode(self, image, key):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')

        skey = sum([ord(i) for i in key])**2
        new_name = name.split('.')[0] + '_encode' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)

        def f(r,g,b,x,y):
            return r^x^y^skey, g^x^y^skey, b^x^y^skey

        for x in range(size[0]):
            for y in range(size[1]):
                r,g,b = image.getpixel((x,y))
                r,g,b = f(r,g,b,x,y)
                new_image.putpixel((x,y), (r,g,b))

        new_image.save(new_name, "JPEG")
        print(f'Фотография {name} сохранена, key - {key}')

    '''decoce'''
    @classmethod
    def decode(self, image, key):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')

        skey = sum([ord(i) for i in key])**2 % 255
        new_name = name.split('.')[0] + '_decode' + '.' + 'jpeg'
        new_image = Image.new('RGB', size)

        def f(r,g,b,x,y):
            return r^x^y^skey%255, g^x^y^skey%255, b^x^y^skey%255

        for x in range(size[0]):
            for y in range(size[1]):
                r,g,b = image.getpixel((x,y))
                r,g,b = f(r,g,b,x,y)
                new_image.putpixel((x,y), (r,g,b))

        new_image.save(new_name, "JPEG")
        print(f'Фотография {name} сохранена, key - {key}')

    '''other'''
    @classmethod
    def other(self, image, c):
        name = image
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')

        new_name = name.split('.')[0] + '_other' + str(c) + '.' + 'jpeg'
        new_image = Image.new('RGB', size)

        def f(r,g,b,x,y):
            r += (x**2 + y**2) // c
            g += (x**2 + y**2) // c 
            b += (x**2 + y**2) // c
            return r%255, g%255, b%255

        for x in range(size[0]):
            for y in range(size[1]):
                r,g,b = image.getpixel((x,y))
                new_image.putpixel((x,y), f(r,g,b,x,y))

        new_image.save(new_name, "JPEG")
        print(f'Фотография {name} сохранена, c - {c}')

    '''ascii'''
    @classmethod
    def ascii(self, image):
        name = image
        file = name.split('.')[0] + '_ascii' + '.txt'
        array = []
        #f = "@%#*+=-:. "
        #f = '@&*{}¤|^. '
        f = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI><;:,\"^`". '
        try:
            image = Image.open(image)
            size = image.size
        except:
            raise ImageError('Ошибка чтения изображения')
        for x in range(size[0]):
            x2 = []
            for y in range(size[1]):
                r,g,b = image.getpixel((x,y))
                #gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                gray = (r+g+b)//3
                c = int(gray / 255 * len(f))-1
                try:
                    x2.append(f[c])
                except:
                    print(c, gray, gray / 255)
            array.append(x2)

        with open(file, 'w', encoding='utf-8') as f:
            for i in range(len(array)):
                for x in range(len(array)):
                    try:
                        f.write(array[x][i])
                    except:
                        pass
                f.write('\n')
                

        print(f'Фотография ASCII {file} сохранена')

    

        
#Photo.encode('best_Ava.png', 20)
#Photo.whbl('lev.jpg', 1)
#Photo.dark('lev.jpg', 5)
#Photo.negative('lev.jpg')
#Photo.encode('sq.png', 'как дела брат?')
Photo.ascii('dasha3.jpg')
#Photo.decode('sq_encode.jpeg', '2021')
#Photo.decode('lev_encode.jpeg', '2021')
