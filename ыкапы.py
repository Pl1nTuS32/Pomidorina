import random


print('''Приветствую тебя, дорогой игрок!
Предлагаю тебе сыграть в игру, в которой от твоих вариантов ответа зависит исход. Ты готов(а)? Введи да/нет
''')
choise = input()
win = False
if choise.lower() == 'да':
    print('''Тогда поехали! Ты очнулся в тёмном помещении, не видишь собственных пальцев. 
    Не долго мешкая, ты начинаешь искать что угодно на полу, водя по нему руками. 
    Вдруг находишь зажигалку (какой-никакой, а источник света). 
    Пройдя немного вперед, ты видишь два пути: 1. Вправо 2. Влево.  Куда пойдешь?
    ''')
    choise_2 = int(input())
    if choise_2 == 1:
        print('''Завернув направо, ты начинаешь ощущать холод...
         Что-то зловщее в этой части лабиринта, в который ты попал. 
         Идя уже минут 10 вперед, ты наталкиваешься на некое существо, которое не реагирует на твою зажигалку.
         Будить? 1. Да 2. Не надо
        ''')
        choise_3 = int(input())
        if choise_3 == 1:
            print("""Существо просыпается, но не проявляет агрессии. А предлагает угадать загаданное 
            им число за 5 попыток, тогда оно пропустит тебя дальше. Кажется, любопытнее согласиться... 
            Существо говорит, что загадало число от 1 до 20. Как думаешь, какое?""")
            number = random.randint(1,20)
            try_cnt = 5
            while try_cnt > 0:
                guess =int(input())
                if guess == number:
                    print('ura ti pobedil')
                    break

    elif choise_2 == 2:
        print('''Да, слева показалось безопаснее.
         Идя вперед, ты неожиданно заметил бумажку на стене. 
         Берешь?
        ''')
        if
else:
    print('Что ж, тогда желаю удачи, пока!')