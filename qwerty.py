def kebap_filter(text):
    return text.replace(' ', '--')

def reverse_filter(text):
    text = text.split()
    for i in range(1, len(text), 2):
        text[i] = text[i][::-1]
    return ' '.join(text)


def translate_filter(text):
    text = text.split()
    text_1 = []
    angl = "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
    rus = "йцукенгшщзхъфывапролджэячсмитьбю.ё"
    for i in text:
        string = ''
        for j in i:
            if j in angl:
                ind = angl.index(j)
                string += rus[ind]
            if j in rus:
                ind = rus.index(j)
                string += angl[ind]
        text_1.append(string)
    return ' '.join(text_1)


filters = {
    1: {
        "name": "Kebap-filter",
        "description": "Преобразует текст в формат Kebab "
                       "(слова--разделённые--двумя--тире)",
        "function": kebap_filter
    },
    2: {
        "name": "Reverse filter",
        "description": "Преобразует текcт в формат Reverse "
                       "(разворачивает еоджак второе оволс в етсет)",
        "function": reverse_filter
    },
    3: {
        "name": "Translate filter",
        "description": "Преобразует текст в формат Translate "
                       "(Изменяет  английские буквы на русские и наоборот по раскладке клавиатуры)",
        "function": translate_filter
    }



}

while True:
    for i in range(1, 4):
        print(f'{i}: {filters[i]["name"]}')
    choice = int(input('Введите фильтр или 0 для выхода: ' ))
    print()
    if choice != 0:
        if choice in [1, 2, 3]:
            if choice == 1:
                print(f'{filters[1]["name"]}:\n',
                      f'{filters[1]["description"]}')
            elif choice == 2:
                print(f'{filters[2]["name"]}:\n',
                      f'{filters[2]["description"]}')
            elif choice == 3:
                print(f'{filters[3]["name"]}:\n',
                      f'{filters[3]["description"]}')
            print()
            ans = input('Применить фильтр к тексту (Да/Нет)? ')
            if ans.lower() == 'да':
                text = input('Введите текст для фильтрации: ')
                print(f'Резудьтат : {filters[choice]["function"](text)}')
            print()
        else:
            print('Такой цифры нет!!!')
            print()
    else:
        print('До свидания!')
        break



