import time

import requests
import configparser
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Задача №3. Дополнительная (не обязательная)

def selenuim_test():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг

    email = config["Токены"]["email"]
    pwd = config["Токены"]["pwd"]


    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    input_text = driver.find_element(By.ID, 'passp-field-login')
    input_text.clear()
    time.sleep(5)
    input_text.send_keys(email)
    time.sleep(5)
    input_text.send_keys(Keys.RETURN)
    time.sleep(10)
    input_text = driver.find_element(By.ID, 'passp-field-passwd')
    input_text.clear()
    time.sleep(5)
    input_text.send_keys(pwd)
    time.sleep(5)
    input_text.send_keys(Keys.RETURN)
    time.sleep(10)
    #input_text.send_keys(Keys.RETURN)
    #time.sleep(10)

    assert 'Авторизация' in driver.title
    driver.close()
    if 'Авторизация' in driver.title:
        return True
    else:
        return False


#Задача №2 Автотест API Яндекса

def ya_test():
    tokenYA =''

    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг

    tokenYA = config["Токены"]["tokenYA"]

    uploader = YaUploader(tokenYA)
    data = uploader.get_files_list()
    return data


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_files_list(self):
        headers = {
            'Content-Type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
        }


        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        file_path = 'test_homework'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.put(files_url, headers=headers, params=params)
        return response.status_code

#Задача №1 unit-tests
def channel_stat():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    num_max = max(stats.values())
    for i in stats.keys():
        if stats[i] == num_max:
            return i

#Задача №1 unit-tests
def uniq_geo():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    res = set()
    for i in ids.keys():
        for i1 in ids[i]:
            res.add(i1)

    for i in res:
        print(i, end=' ')
        return True


documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;


#Задача №1 unit-tests
def command_p(id_number):
    #id_number = input('Введите номер документа для поиска человека: ')
    exist = False
    for man in documents:
        if man['number'] == id_number:
            exist = True
            #print('Документ с номером ', id_number, ' принадлежит ', man['name'])
            return ('Документ с номером ', id_number, ' принадлежит ', man['name'])

    if exist == False:
        #print('Такого документа не существует')
        return('Такого документа не существует')


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;


def command_s():
    id_number = input('Введите номер документа для поиска полки: ')
    exist = False
    for key, values in directories.items():
        if id_number in values:
            exist = True
            #print('Документ с номером ', id_number, ' находится на полке ',key)
            return ('Документ с номером ', id_number, ' находится на полке ', key)

    if exist == False:
        #print('Такого документа не существует')
        return ('Такого документа не существует')


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";


def command_l():
    for man in documents:
        #print(man['type'], '  ', man['number'], ' ', man['name'])
        return (man['type'], '  ', man['number'], ' ', man['name'])


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.


def command_a():
    id_number = input('Введите номер документа для добавления: ')
    id_type = input('Введите тип документа для добавления: ')
    id_name = input('Введите имя владельца для добавления: ')
    id_polka = input('Введите номер полки для добавления: ')

    if id_polka in directories.keys():
        directories[id_polka].append(id_number)
    else:
        directories[id_polka] = [id_number]

    if id_number in directories.values():
        print('Такой номер документа уже существует. Добавлять не будем')
    else:
        new_person = {
            "type": id_type,
            "number": id_number,
            "name": id_name
        }
        documents.append(new_person)


def main():
    while True:
        command = input("Введите команду - p, s, l, a или q для выхода: ").lower()
        if command == "p":
            id_number = input('Введите номер документа для поиска человека: ')
            print(command_p(id_number))
        elif command == "s":
            command_s()
        elif command == "a":
            command_a()
        elif command == "l":
            command_l()
        elif command == "q":
            print('Goodbye')
            break
        else:
            print("Неверно введена команда. Попробуйте еще раз!")



if __name__ == '__main__':
    selenuim_test()
    ya_test()
    channel_stat()
    uniq_geo()
    main()

