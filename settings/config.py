import configparser
import screeninfo
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings/settings.ini")  # читаем конфиг

def config_update():
    with open('settings/settings.ini', 'w') as f:
        config.write(f)

def set_display_maxsize():
    config.set("Display", "WIDTH", str(
        screeninfo.screeninfo.get_monitors()[0].width))
    config.set("Display", "HEIGHT", str(
        screeninfo.screeninfo.get_monitors()[0].height))
    config_update()
    return (True)


set_display_maxsize()
