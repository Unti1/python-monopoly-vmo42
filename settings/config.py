import configparser
import screeninfo
import os,random,pygame
from typing import NoReturn
from pygame import *
import pyautogui


config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings/settings.ini")  # читаем конфиг

def config_update( ) -> NoReturn:
    with open('settings/settings.ini', 'w') as f:
        config.write(f)

def set_display_maxsize() -> NoReturn:
    config.set("Display", "WIDTH", str(
        screeninfo.screeninfo.get_monitors()[0].width))
    config.set("Display", "HEIGHT", str(
        screeninfo.screeninfo.get_monitors()[0].height))
    config_update()


set_display_maxsize()
