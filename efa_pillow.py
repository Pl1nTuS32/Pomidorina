from PIL import Image, ImageFilter
import os

class Filter:
    def __init__(self, image, output):
        self.image = image
        self.output = output

class ContourFilter(Filter):
    def __init__(self, image, output):
        super().__init__(image, output)

    def ContourFil(self):
        self.image = image.filter(ImageFilter.CONTOUR)
        self.image.save(self.output)




class EmbossFilter(Filter):
    def __init__(self, image, output):
        super().__init__(image, output)

    def EmbossFil(self):
        self.image = image.filter(ImageFilter.EMBOSS)
        self.image.save(self.output)

class BlurFilter(Filter):
    def __init__(self, image, output):
        super().__init__(image, output)

    def BlurFil(self):
        self.image = image.filter(ImageFilter.BoxBlur(radius=100))
        self.image.save(self.output)

filters = ['Contour filter', 'Emboss filter', 'Blur filter']

print('Приветсвуем в консольном фоторедакторе!!!')
while True:
    print(f" 1: {filters[0]}\n 2: {filters[1]}\n 3: {filters[2]}\n")
    choice = int(input('Введите фильтр или 0 для выхода: '))
    print()
    if choice != 0:
        if choice in [1, 2, 3]:
            if choice == 1:
                print(f'{filters[0]}\n'
                      'Оставляет только контур картинки')
            elif choice == 2:
                print(f'{filters[1]}\n'
                      'Совершает тиснение')
            elif choice == 3:
                print(f'{filters[2]}\n'
                      'Заблюривает всю картинку')
            print()
            ans = input('Применить фильтр к тексту (Да/Нет)? ')
            if ans.lower() == 'да':
                path = input("Введите путь к файлу: ")
                image = Image.open(path).convert('RGB')
                output = input('Введите путь сохранения: ')
                while not os.path.exists(path):
                    path = input("Файл не найден. Попробуйте ещё раз: ")
                if choice == 1:
                    b = ContourFilter(image, output)
                    b.ContourFil()
                elif choice == 2:
                    a = EmbossFilter(image, output)
                    a.EmbossFil()
                elif choice == 3:
                    c = BlurFilter(image, output)
                    c.BlurFil()
                print('Результат сохранен по пути, который вы прописали')
            elif ans.lower() != 'нет':
                print('Неверный ввод, попробуйте ещё раз')
            print()
        else:
            print('Такой цифры нет!!!')
            print()
    else:
        print('До свидания!')
        break








