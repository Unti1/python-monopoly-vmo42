import configparser
import screeninfo
import os,random,pygame
from typing import NoReturn
from pygame import *
import pyautogui
import os
from typing import List
from items.player import Player


config = configparser.ConfigParser()  # создаём объекта парсера
config.read(r'C:\Users\Asus\Documents\GitHub\python-java-monopoly-vmo42\settings\settings.ini')  # читаем конфиг

def config_update( ) -> NoReturn:
    with open(r'C:\Users\Asus\Documents\GitHub\python-java-monopoly-vmo42\settings\settings.ini', 'w') as f:
        config.write(f)

def set_display_maxsize() -> NoReturn:
    config.set("Display", "WIDTH", str(
        screeninfo.screeninfo.get_monitors()[0].width))
    config.set("Display", "HEIGHT", str(
        screeninfo.screeninfo.get_monitors()[0].height))
    config_update()


