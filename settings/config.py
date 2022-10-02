import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings/settings.ini")  # читаем конфиг
